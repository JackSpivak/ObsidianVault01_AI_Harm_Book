# SessionStart hook: report idea notes waiting to be filed by bookmark-index-maintainer.
# Prints one line when notes are marked "bookmark: ready" (or legacy "unfiled"); prints nothing otherwise.
$root = Join-Path $PSScriptRoot "..\..\02_Ideas Topics Concepts"
$ready = @()
$drafts = 0
Get-ChildItem -LiteralPath $root -Recurse -Filter *.md -File | ForEach-Object {
    $head = Get-Content -LiteralPath $_.FullName -TotalCount 15 -Encoding UTF8
    if ($head -match '^bookmark:\s*(ready|unfiled)\s*$') { $ready += $_.BaseName }
    elseif ($head -match '^bookmark:\s*draft\s*$') { $drafts++ }
}
if ($ready.Count -gt 0) {
    "Bookmark inbox: $($ready.Count) note(s) ready to file ($($ready -join '; ')); $drafts draft(s) left alone. Mention this once and offer a sweep (bookmark-index-maintainer); don't file without approval."
}
