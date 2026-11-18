"""Toy-case runner for HO-002.a (variants A and B). Fictional data.
Usage: python -I toy_status.py <A.ttl> <B.ttl>
Implements the variant B status calculation (Author decisions 3, 5-20) and runs CQ queries.
"""
import sys
from datetime import date
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS

HO = Namespace("https://example.org/harm-ontology/v3-test#")
HOA = Namespace("https://example.org/harm-ontology/v3-test/attr#")
TOY = Namespace("https://example.org/harm-ontology/toy#")


def short(x):
    if x is None:
        return "-"
    if isinstance(x, tuple):  # non-exclusive attributes return a tuple of values
        return "{" + ", ".join(short(i) for i in x) + "}"
    s = str(x)
    for p in (str(TOY), str(HOA), str(HO)):
        s = s.replace(p, "")
    return s


def one(g, s, p):
    return next(g.objects(s, p), None)


# ---------------- Variant B ----------------
def assessments(g):
    out = []
    for a in set(g.subjects(HO.aboutAttribute, None)):
        out.append(dict(
            node=a, target=one(g, a, HO.assesses), attr=one(g, a, HO.aboutAttribute),
            value=one(g, a, HO.value), entity=one(g, a, HO.forAffectedEntity),
            persp=one(g, a, HO.takenFrom), org=one(g, a, HO.assessorOrganisation),
            proc=one(g, a, HO.usesProcedure), evidence=one(g, a, HO.hasEvidence),
            repeats=one(g, a, HO.repeats), revised=one(g, a, HO.revisedBecause),
            horizon=(int(one(g, a, HO.assessmentHorizon)) if one(g, a, HO.assessmentHorizon) is not None else None),
            date=one(g, a, HO.assessedAt).toPython()))
    return out


def root_entity(g, e):
    # decision 12: overlapping groups count as the same claim
    while e is not None and one(g, e, HO.subgroupOf) is not None:
        e = one(g, e, HO.subgroupOf)
    return e


def band(g, a):
    v = a["value"]
    if isinstance(v, URIRef) and (v, HO.bandRank, None) in g:
        return v  # given directly as a band (e.g. an opinion)
    if (a["attr"], RDF.type, HO.GradedAttribute) not in g:
        return v  # categorical attribute (cause, agent, year, type): compare values as themselves
    if a["proc"] is None:
        return None  # graded raw value with no procedure: can't be banded
    for m in g.objects(a["proc"], HO.mapsValue):
        if str(one(g, m, HO.fromValue)) == str(v):
            return one(g, m, HO.toBand)
    return None


def basis(g, persp):
    # decision 6: derived
    if persp is None:
        return "Unstandardized"
    if one(g, persp, HO.appliedEvaluativeStandard) is not None:
        return "Stated"
    t = one(g, persp, HO.instantiates)
    if t is not None and one(g, t, HO.defaultEvaluativeStandard) is not None:
        return "Inherited"
    return "Unstandardized"


def status(g, claim_as, scope, as_of):
    """Decision-ordered status per the Variant B design, steps 1-5."""
    rows = [a for a in claim_as if (scope is None or a["persp"] in scope) and a["date"] <= as_of]
    latest = {}
    for a in sorted(rows, key=lambda r: r["date"]):
        latest[a["persp"]] = a
    rows = list(latest.values())
    if not rows:
        return "NotAssessed", None, rows
    vals = {a["node"]: band(g, a) for a in rows}
    comparable = {v for v in vals.values() if v is not None}
    attr = rows[0]["attr"]
    # --- CONFLICT RULES: depend on what kind of attribute this is (toy finding 1 and 6) ---
    # Three kinds:
    #  1. NonExclusiveAttribute (cause, answerable): several values can all be true at once
    #     (HO-003: causes are additive). Different values are NOT a conflict by themselves.
    #     Conflict only if some assessment DENIES a value another names (deniesValue), or claims
    #     a value is the ONLY one (soleValue) while more than one value is in play.
    #  2. IntervalAttribute (occurredDuring): values are "YYYY-YYYY". Compatible if the intervals
    #     overlap; conflict only if some pair is disjoint. Agreed value = the intersection.
    #  3. Everything else: single-valued and mutually exclusive. Two different values conflict,
    #     except ho:Unclassified, which means "no classification", not a competing value.
    is_non_exclusive = (attr, RDF.type, HO.NonExclusiveAttribute) in g
    is_interval = (attr, RDF.type, HO.IntervalAttribute) in g
    if is_interval:
        spans = []
        for v in comparable:
            lo, _, hi = str(v).partition("-")
            spans.append((int(lo), int(hi or lo)))
        lo, hi = max(s[0] for s in spans), min(s[1] for s in spans)
        if lo > hi:  # some pair has no common year -> disjoint
            return "Disputed", None, rows
        if not comparable:
            return "Incommensurable", None, rows
        value = f"{lo}-{hi}"
    elif is_non_exclusive:
        denied = {one(g, a["node"], HO.deniesValue) for a in rows} - {None}
        sole = any(str(one(g, a["node"], HO.soleValue)).lower() == "true" for a in rows)
        if (denied & comparable) or (sole and len(comparable) > 1):
            return "Disputed", None, rows
        if not comparable:
            return "Incommensurable", None, rows
        value = tuple(sorted(comparable, key=short))
    else:
        non_unclass = {v for v in comparable if v != HO.Unclassified}
        # A supertype and its subtype are compatible, not rival values: keep the more specific one.
        # (w is a subtype of v when v is reachable from w by rdfs:subClassOf.)
        def has_subtype(v):
            return any(w != v and isinstance(w, URIRef) and v in set(g.transitive_objects(w, RDFS.subClassOf))
                       for w in non_unclass)
        non_unclass = {v for v in non_unclass if not has_subtype(v)}
        if len(non_unclass) > 1:
            return "Disputed", None, rows
        if not comparable:
            return "Incommensurable", None, rows
        value = next(iter(non_unclass)) if non_unclass else HO.Unclassified
    if any(v is None for v in vals.values()):
        return "Incommensurable", None, rows
    indep_orgs = {a["org"] for a in rows if a["repeats"] is None and a["evidence"] is not None and a["proc"] is not None}
    if len(rows) < 2 or len(indep_orgs) < 2:
        return "SingleSource", value, rows
    procs = {(a["proc"], str(one(g, a["proc"], HO.version)) if a["proc"] else None) for a in rows}
    if len(procs) > 1 or any(a["evidence"] is None for a in rows):
        return "Corroborated", value, rows
    proc = rows[0]["proc"]
    pool = scope if scope is not None else set(g.subjects(RDF.type, HO.PerspectiveSpecification))
    silent = [p for p in pool if (p, HO.usesProcedure, proc) in g and p not in latest]
    if silent:
        return "PartiallyAssessed", value, rows
    return "Settled", value, rows


def revisions(al, target, attr):
    """Where one perspective changed its value on the same target and attribute, return (perspective, old, new).
    CQ4: every change should carry a trigger (`revisedBecause`); a change with none is flagged by the caller."""
    by = {}
    for a in sorted((a for a in al if a["target"] == target and a["attr"] == attr), key=lambda r: r["date"]):
        by.setdefault(a["persp"], []).append(a)
    return [(p, old, new) for p, seq in by.items() for old, new in zip(seq, seq[1:]) if old["value"] != new["value"]]


def display(st):
    return st if st in ("Settled", "Disputed") else "Open"


def claims(g, al):
    groups = {}
    for a in al:
        # HO-006 chain test: horizon joins the claim key only when given, so existing 3-part keys are unchanged
        key = (a["target"], a["attr"], root_entity(g, a["entity"])) + ((a["horizon"],) if a["horizon"] is not None else ())
        groups.setdefault(key, []).append(a)
    return groups


def fmt(rows):
    return "; ".join(f"{short(a['persp'])}@{a['date'].year}={short(a['value'])}" for a in sorted(rows, key=lambda r: r['date']))


def run_b(path):
    g = Graph().parse(path)
    al = assessments(g)
    cl = claims(g, al)
    today = date(2026, 11, 18)
    print("=" * 70, "\nVARIANT B\n" + "=" * 70)

    # Snapshot shortcuts for every Effect x attribute, incl. unassessed (mitigation 1)
    print("\n-- Snapshot statuses (scope: all in data; as of 2026-11-18) --")
    effects = sorted(g.subjects(RDF.type, HO.Effect))
    attrs = sorted(at for at in {a["attr"] for a in al} if (at, HO.appliesTo, HO.Effect) in g)
    counts = {}
    for e in effects:
        for at in attrs:
            ks = [k for k in cl if k[0] == e and k[1] == at] or [(e, at, None)]
            for k in ks:
                st, val, rows = status(g, cl.get(k, []), None, today)
                counts[st] = counts.get(st, 0) + 1
                print(f"{short(e):4} {short(at):14} {short(k[2]):13} {display(st):9} [{st}{'(' + short(val) + ')' if val is not None else ''}]  {fmt(rows)}")
    print("Counts:", counts)

    def q(label, key, scope=None, as_of=today):
        st, val, rows = status(g, cl.get(key, []), scope, as_of)
        sc = "all in data" if scope is None else ", ".join(sorted(short(p) for p in scope))
        print(f"{label}\n   -> {display(st)} [{st}{'(' + short(val) + ')' if val is not None else ''}] among: {sc}; as of {as_of}\n   {fmt(rows)}")
        return st

    print("\n-- CQ1 Who caused E1? --")
    q("all perspectives", (TOY.E1, HOA.cause, None))
    print("\n-- CQ2 Which Effects are severe? (naive, via snapshot) --  see snapshot table above")
    print("\n-- CQ3 What do all agree on? Severity of E1 under three scopes --")
    k = (TOY.E1, HOA.severity, TOY.AllOperators)
    q("scope all", k)
    q("scope P2,P3,P6", k, {TOY.P2, TOY.P3, TOY.P6})
    q("scope P2,P6", k, {TOY.P2, TOY.P6})
    print("\n-- CQ4 Cause of E1 over time --")
    for y in (2011, 2013, 2016, 2020, 2022):
        q(f"as of {y}", (TOY.E1, HOA.cause, None), as_of=date(y, 12, 31))
    print("\n-- CQ5 Assessment basis --")
    for a in sorted(al, key=lambda r: str(r["node"])):
        print(f"   {short(a['node']):3} {short(a['persp']):3} {basis(g, a['persp'])}")
    print("\n-- CQ6 What did P1 leave out? --")
    for a, lo in g.subject_objects(HO.leftOut):
        print(f"   {short(a)} ({short(one(g, a, HO.takenFrom))}) left out {short(lo)} as {short(one(g, a, HO.omissionType))}")
    print("\n-- CQ7 Type of AidCircle --")
    q("all", (TOY.AidCircle, HOA.entityType, None))
    print("\n-- CQ9 Who is answerable for E1? (separate from CQ1) --")
    q("all", (TOY.E1, HOA.answerable, None))
    # ---- Expected-result checks. Each states the intent; a mismatch prints FAIL. ----
    results = []

    def expect(label, key, want, val=None, scope=None, as_of=today):
        """want: a status name, or "!Disputed" meaning "any status except Disputed" (used where the point
        is only that a difference must NOT be treated as a conflict). val: expected agreed value, if any."""
        st, v, rows = status(g, cl.get(key, []), scope, as_of)
        ok = (st != "Disputed") if want == "!Disputed" else (st == want)
        if val is not None:
            ok = ok and short(v) == val
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {label}\n        got {st}({short(v)}); expected {want}{'(' + val + ')' if val else ''}\n        {fmt(rows)}")

    print("\n-- Checks 1: non-exclusive attributes (cause, answerable): additive unless denied or sole --")
    expect("E1 cause: F1 and F3 named, no deny/sole -> not a conflict", (TOY.E1, HOA.cause, None), "Corroborated", "{F1, F3}")
    expect("E4 cause: P4 DENIES F1 -> conflict", (TOY.E4, HOA.cause, None), "Disputed")
    expect("E5 cause: P2 says F1 is the ONLY cause, P5 adds F3 -> conflict", (TOY.E5, HOA.cause, None), "Disputed")
    expect("E1 answerable: Manager and CompanyX both -> not a conflict", (TOY.E1, HOA.answerable, None), "Corroborated", "{CompanyX, Manager}")
    expect("E4 answerable: CompanyX claimed SOLE answerable vs Manager -> conflict", (TOY.E4, HOA.answerable, None), "Disputed")
    expect("E5 answerable: CompanyX DENIES Manager -> conflict", (TOY.E5, HOA.answerable, None), "Disputed")
    expect("E11 cause: Grid (Conduit factor) and F1 named together -> not a conflict", (TOY.E11, HOA.cause, None), "Corroborated", "{F1, Grid1}")

    print("\n-- Checks 2: interval attributes: overlap is compatible, disjoint conflicts --")
    expect("E2 occurredDuring: 2009-2014 vs 2012-2014 overlap -> compatible, value narrows", (TOY.E2, HOA.occurredDuring, None), "Corroborated", "2012-2014")
    expect("E5 occurredDuring: 2009-2010 vs 2012-2014 disjoint -> conflict", (TOY.E5, HOA.occurredDuring, None), "Disputed")
    expect("E2 occurredStart (a single point): 2009 vs 2012 -> conflict", (TOY.E2, HOA.occurredStart, None), "Disputed")

    print("\n-- Checks 3: single-valued exclusive attributes (entity type): disjoint conflicts; compatible does not --")
    expect("Tribe1 type: group vs legal entity (disjoint) -> conflict", (TOY.Tribe1, HOA.entityType, None), "Disputed")
    expect("Partnership1 type: two jurisdictions disagree on legal personality -> conflict", (TOY.Partnership1, HOA.entityType, None), "Disputed")
    expect("LLC1 type: both CollectiveArtificialPerson -> agree", (TOY.LLC1, HOA.entityType, None), "!Disputed", "CollectiveArtificialPerson")
    expect("Person1 type: supertype vs subtype -> compatible, keeps the subtype", (TOY.Person1, HOA.entityType, None), "!Disputed", "NaturalPerson")
    expect("Collective2 type: Unclassified vs specific -> compatible, keeps the specific", (TOY.Collective2, HOA.entityType, None), "!Disputed", "CollectiveNaturalGroup")
    expect("AidCircle type: lone Unclassified stays visible", (TOY.AidCircle, HOA.entityType, None), "SingleSource", "Unclassified")
    expect("Herd1 type: a collective, not an individual", (TOY.Herd1, HOA.entityType, None), "!Disputed", "CollectiveNaturalGroup")
    expect("Dog1 type: SentientIndividual", (TOY.Dog1, HOA.entityType, None), "!Disputed", "SentientIndividual")
    expect("Dog1 sentience: two perspectives agree -> not a conflict", (TOY.Dog1, HOA.sentience, None), "!Disputed", "yes")

    print("\n-- Checks 4: independence and settlement paths (all severity, ProcForensic) --")
    expect("E2 severity: P3 repeats P2 (same firm) -> not independent", (TOY.E2, HOA.severity, TOY.AllOperators), "SingleSource")
    expect("E6 severity: same firm, NOT flagged repeats -> still one organisation", (TOY.E6, HOA.severity, TOY.AllOperators), "SingleSource")
    expect("E7 severity: different firms but flagged repeats -> not independent", (TOY.E7, HOA.severity, TOY.AllOperators), "SingleSource")
    expect("E9 severity: agreement but one lacks evidence -> cannot settle", (TOY.E9, HOA.severity, TOY.AllOperators), "Corroborated", "High")
    expect("E8 severity: all forensic perspectives agree, evidence, two firms -> Settled", (TOY.E8, HOA.severity, TOY.AllOperators), "Settled", "High")
    expect("E1 severity among P2,P3,P6: P3 silent -> PartiallyAssessed", (TOY.E1, HOA.severity, TOY.AllOperators), "PartiallyAssessed", "High", scope={TOY.P2, TOY.P3, TOY.P6})
    expect("E1 cause: different procedures agree on F1 -> Corroborated, not Settled", (TOY.E1, HOA.cause, None), "Corroborated")
    expect("E3 severity: raw value with no procedure cannot be banded -> Incommensurable", (TOY.E3, HOA.severity, TOY.AllOperators), "Incommensurable")
    expect("E10 (nothing assessed) -> NotAssessed", (TOY.E3, HOA.cause, None), "NotAssessed")

    print("\n-- Checks 5: CQ4 settled, later reopened, with the trigger (as-of dates) --")
    scope4 = {TOY.P2, TOY.P6, TOY.P1, TOY.P4}
    k = (TOY.E1, HOA.severity, TOY.AllOperators)
    expect("E1 severity as of 2016-12-31, scope P2,P6,P1,P4: only the two forensic opinions exist -> Settled", k, "Settled", "High", scope=scope4, as_of=date(2016, 12, 31))
    expect("E1 severity as of 2020-12-31, same scope: P1 (2018) and P4 (2019) dissent -> reopened as Disputed", k, "Disputed", scope=scope4, as_of=date(2020, 12, 31))
    print("   revision triggers (a changed value must say why):")
    for p, old, new in revisions(al, TOY.E1, HOA.cause):
        why = short(new["revised"]) if new["revised"] is not None else "NO TRIGGER RECORDED"
        print(f"      {short(p)}: {short(old['value'])} ({old['date'].year}) -> {short(new['value'])} ({new['date'].year}); because: {why}")
        want_trigger = (short(p) == "P1")  # P1 gave a trigger (Ev3); P4 deliberately did not
        ok = (new["revised"] is not None) == want_trigger
        results.append(ok)
        print("      ", "PASS" if ok else "FAIL")

    print("\n-- Checks 6: CQ6 omission on a non-causal attribute; CQ7 standing, moral circle, observed core --")
    non_causal_omissions = [a for a in al if one(g, a["node"], HO.leftOut) is not None and a["attr"] != HOA.cause]
    ok = len(non_causal_omissions) >= 1 and all(one(g, a["node"], HO.omissionType) is not None for a in non_causal_omissions)
    results.append(ok)
    print("PASS" if ok else "FAIL", " omission recorded on a severity assessment, with its omission type:",
          ", ".join(f"{short(a['node'])} left out {short(one(g, a['node'], HO.leftOut))} as {short(one(g, a['node'], HO.omissionType))}" for a in non_causal_omissions))
    expect("E11 standing of Grid1: Derivative under both perspectives (and a Conduit factor, see cause above)", (TOY.E11, HOA.affectedStanding, TOY.Grid1), "!Disputed", "Derivative")
    expect("E11 standing of AISys1: Direct vs Derivative -> conflict", (TOY.E11, HOA.affectedStanding, TOY.AISys1), "Disputed")
    expect("E12 standing of Couple1 (therapy): Relationship is primary", (TOY.E12, HOA.affectedStanding, TOY.Couple1), "!Disputed", "Direct")
    expect("E15 standing of Household1 (tax): primary", (TOY.E15, HOA.affectedStanding, TOY.Household1), "!Disputed", "Direct")
    expect("E15 standing of Couple1 (tax): only derivative", (TOY.E15, HOA.affectedStanding, TOY.Couple1), "!Disputed", "Derivative")
    expect("AISys1 moral-circle membership: assessed, and perspectives disagree", (TOY.AISys1, HOA.moralCircleMember, None), "Disputed")
    core_ok = (TOY.E11, HO.affects, TOY.AISys1) in g  # observed core is unchanged by the dispute above
    results.append(core_ok)
    print("PASS" if core_ok else "FAIL", " observed core (E11 affects AISys1) is separate from the disputed assessed reading")
    expect("Tribe1 boundary: returned as assessments by perspective, conflicting", (TOY.Tribe1, HOA.boundary, None), "Disputed")
    sep = [(e, set(g.objects(e, HO.affects))) for e in (TOY.E12, TOY.E13, TOY.E14)]
    sep_ok = sep[0][1] == {TOY.Couple1} and sep[1][1] == {TOY.Partner1} and sep[2][1] == {TOY.Partner2}
    results.append(sep_ok)
    print("PASS" if sep_ok else "FAIL", " couple harm and each partner's harm are separate Effects")

    print("\n-- Checks 7: HO-006 chain test: horizon is part of the claim key --")
    expect("Ch1 netOutcome at horizon 2: P2 and P6 agree -> not a conflict", (TOY.Ch1, HOA.netOutcome, None, 2), "!Disputed", "NetBeneficial")
    expect("Ch1 netOutcome at horizon 20: P2 NetHarmful vs P1 NetBeneficial (same horizon) -> Disputed", (TOY.Ch1, HOA.netOutcome, None, 20), "Disputed")
    ch_keys = sorted(k[3] for k in cl if k[0] == TOY.Ch1 and k[1] == HOA.netOutcome)
    ok = ch_keys == [2, 20]
    results.append(ok)
    print("PASS" if ok else "FAIL", f" two horizons are two separate claims (keys: {ch_keys})")
    naive = [a for a in al if a["target"] == TOY.Ch1 and a["attr"] == HOA.netOutcome]
    st_naive, _, _ = status(g, naive, None, today)
    ok = st_naive == "Disputed"
    results.append(ok)
    print("PASS" if ok else "FAIL", f" control: with horizon IGNORED, one claim -> {st_naive} (this is the false-dispute / lost-verdict risk the key prevents)")
    p2 = [a for a in naive if a["persp"] == TOY.P2]
    st_p2 = {a["horizon"]: short(a["value"]) for a in p2}
    ok = st_p2 == {2: "NetBeneficial", 20: "NetHarmful"}
    results.append(ok)
    print("PASS" if ok else "FAIL", f" P2 holds both verdicts at once, one per horizon (Sai Weng flip stays visible): {st_p2}")
    ok = all((a["horizon"] is not None) for a in naive)
    results.append(ok)
    print("PASS" if ok else "FAIL", " every chain-level assessment declares its horizon (none silent)")

    print(f"\nSUMMARY: {sum(results)} passed, {len(results) - sum(results)} failed, of {len(results)} checks")

    print("\n-- CQ8 When did E2 occur, who was affected? --")
    print(f"   core: {one(g, TOY.E2, HO.occurredStart)}-{one(g, TOY.E2, HO.occurredEnd)}; affected (core): "
          + ", ".join(short(x) for x in g.objects(TOY.E2, HO.affects)))
    q("   assessed start", (TOY.E2, HOA.occurredStart, None))


# ---------------- Variant A ----------------
def run_a(path):
    g = Graph().parse(path)
    print("\n" + "=" * 70, "\nVARIANT A\n" + "=" * 70)
    def sparql(label, text):
        res = list(g.query("PREFIX ho: <%s> PREFIX toy: <%s> %s" % (HO, TOY, text)))
        print(f"{label}\n   -> " + ("; ".join(" | ".join(short(x) for x in r) for r in res) or "(no rows)"))
    sparql("CQ1 naive: ?f ho:causes toy:E1", "SELECT ?f WHERE { ?f ho:causes toy:E1 }")
    sparql("CQ1 expert: causal assessments", "SELECT ?p ?c ?d WHERE { ?a ho:assesses toy:E1 ; ho:attributedCause ?c ; ho:takenFrom ?p ; ho:assessedAt ?d } ORDER BY ?d")
    sparql("CQ2 naive: severe Effects (High/Extreme)", "SELECT ?e ?s WHERE { ?e a ho:Effect ; ho:severity ?s FILTER(?s IN (ho:High, ho:Extreme)) }")
    print("CQ3: no Procedure/Evidence/agreement rule -> query cannot be written")
    sparql("CQ4: dated causal assessments", "SELECT ?d ?p ?c WHERE { ?a ho:attributedCause ?c ; ho:takenFrom ?p ; ho:assessedAt ?d } ORDER BY ?d")
    sparql("CQ7: type of AidCircle", "SELECT ?t WHERE { toy:AidCircle a ?t }")
    print("CQ9: no ResponsibilityAssessment in A -> not answerable separately")
    sparql("CQ8: when/who for E2", "SELECT ?s ?e ?who WHERE { toy:E2 ho:occurredStart ?s ; ho:occurredEnd ?e ; ho:affects ?who }")


if __name__ == "__main__":
    run_b(sys.argv[2])
    run_a(sys.argv[1])
