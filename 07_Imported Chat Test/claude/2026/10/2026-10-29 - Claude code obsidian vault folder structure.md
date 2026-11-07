---
nexus: nexus-ai-chat-importer
plugin_version: "1.8.1"
provider: claude
aliases: Claude code obsidian vault folder structure
conversation_id: 6cd16ecd-56b1-4af7-94a8-b0f7aa03b420
create_time: 2026-10-29T16:12:45.000Z
update_time: 2026-10-29T17:17:00.000Z
---
# Title: Claude code obsidian vault folder structure

Created: 10/29/2026 at 10:12:45 AM
Last Updated: 10/29/2026 at 11:17:00 AM
Chat URL: https://claude.ai/chat/6cd16ecd-56b1-4af7-94a8-b0f7aa03b420


>[!nexus_user] **User** - 10/29/2026 at 10:12:45 AM
> I'm using Claude code terminal integrated into obsidian and I've just completed the setup. Claude recommended since using obsidian vault to create a book a particular structure. Can you imagine or anticipate the folder structure that Claude proposed
<!-- UID: 01a1886f-68c3-7fc5-9cc4-74d7f2ae457a -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:12:52 AM
> Most likely something like this:
>
> ```
> BookVault/
> ├── CLAUDE.md              # project instructions for Claude Code
> ├── 00-Inbox/              # raw notes, clippings, ideas
> ├── 01-Research/
> │   ├── Sources/           # literature notes, one per source
> │   ├── Concepts/          # atomic notes on key ideas
> │   └── People-Orgs/
> ├── 02-Outline/
> │   ├── Book-Outline.md
> │   ├── Themes.md
> │   └── Argument-Map.md
> ├── 03-Manuscript/
> │   ├── 00-Front-Matter/
> │   ├── 01-Chapter-01.md
> │   ├── 02-Chapter-02.md
> │   └── 99-Back-Matter/
> ├── 04-Drafts/             # alternate versions, cut material
> ├── 05-Reference/          # style guide, glossary, citations
> ├── Templates/             # chapter, source-note, and concept templates
> └── Attachments/           # images, PDFs
> ```
>
> The idea is a pipeline: capture in Inbox, process into Research, shape in Outline, write in Manuscript. Chapters are usually separate numbered files (or a folder per chapter with scene or section files) so Claude can edit one without touching the rest.
>
> The most important piece is probably `CLAUDE.md` at the vault root. It typically holds the book's premise, audience, tone and voice rules, the folder conventions, and rules like "never rewrite manuscript text without asking" or "always cite from Sources." Claude Code reads it at the start of every session, so it works as the book's standing brief.
>
> If you paste the structure Claude actually proposed, I can compare it with this and tell you where it differs and why.
<!-- UID: 01a1886f-68e9-7b4d-a870-ebe9c3debe0a -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:21:12 AM
> This is very similar in many ways to what was proposed. And is sufficient. I had also asked Claude to add a root level folder for Claude administrative materials. Within that Claude added a folder for templates which included templates for chapters characters ideas research sources sessions and world building. 
>
> I am curious what the sessions template was intended for? Are these for individual chat or conversation sessions with claude? Or would these be templates for an obsidian document summarizing a session? What was intended here?
<!-- UID: 01a18877-22d5-7434-95e0-f612f6836782 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:21:21 AM
> It's almost certainly a template for an Obsidian note that summarizes a working session, not a container for the chat itself.
>
> Claude Code doesn't remember anything between sessions. Each new session starts cold, apart from what it reads from your vault (like `CLAUDE.md`). A session log is the workaround: at the end of a session, Claude writes a short note recording what was worked on, decisions made, files changed, open questions, and what to pick up next. At the start of the next session, Claude reads the latest log and gets its bearings quickly.
>
> A typical sessions template looks something like:
>
> - Date and focus of the session
> - What was accomplished
> - Decisions made (and why)
> - Files created or edited
> - Open questions or problems
> - Next steps
>
> That's also why it lives in the Claude admin folder rather than with the manuscript: it's working memory for the collaboration, not book content.
>
> If you open the template file, you'll see the headings and can confirm. If you want it to work well, add a line to `CLAUDE.md` telling Claude to read the most recent session note at the start of each session and write a new one at the end.
<!-- UID: 01a18877-22de-7d9f-86f3-72313056c526 -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:26:55 AM
> So I'm trying to explore how best to collaborate with Claude in this writing process. It seems that I would want to have the individual conversations or sessions saved somewhere so that I could reinitiate or pick them up later. But I'm not certain where that would be. I know the inbox is to be used for ongoing idea generation but I was imagining that if something interesting emerged in a conversation I would ask Claude to save it as an idea and it would become an obsidian note in the ideas folder? That still leaves me curious where the chats would persist?
<!-- UID: 01a1887c-6128-7636-8ea2-72699116ca7e -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:27:05 AM
> Your idea workflow is the right one, and the chats themselves persist outside your vault.
>
> **Where the chats live:** Claude Code automatically saves full session transcripts on your computer, in a hidden `.claude` folder in your home directory, organized by project. You don't manage these files. You reopen them with:
>
> - `claude --continue` to resume the most recent session
> - `claude --resume` to pick from a list of past sessions
>
> Resuming brings back the whole conversation, so you can pick up mid-thought.
>
> **What the vault should hold:** curated results rather than raw transcripts. Full chats are long, noisy, and not useful as Obsidian notes. A better split:
>
> - **Ideas folder:** your approach. When something good emerges, tell Claude "save that as an idea note" and it creates a short, titled note you can link and revisit.
> - **Session notes (Claude admin folder):** a brief summary at the end of each session covering what you worked on, decisions, and next steps. This is the bridge between sessions, and Claude can read it at the start of the next one even if you don't resume the old transcript.
> - **Decisions and open questions:** these can live in the session note, or in the relevant chapter or research note if they belong there.
>
> One caveat: the saved transcripts are tied to your machine and project folder, and they can eventually be cleaned up. If a conversation contains something you'd hate to lose, it should be distilled into a note rather than left only in the transcript.
>
> A practical habit is to end each session with "write the session note and save any ideas worth keeping," so nothing important depends on the raw chat surviving.
<!-- UID: 01a1887c-6136-7be0-ba6f-66440338921d -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:30:01 AM
> Got it. So if I wanted to pick up the thread of a previous conversation it sounds like that could get quite complex and cluttered. Do sessions / conversations that are saved in .Claude have names that I can refer to or understand? How do I choose among them if I want to resume or choose?
<!-- UID: 01a1887f-34e9-70a7-b44c-b9dd4acdcb06 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:30:08 AM
> Yes, there's a picker that makes this manageable, though the raw files aren't human-friendly.
>
> **Behind the scenes:** each session is saved as a file named with a long random ID, so browsing the `.claude` folder directly is not useful. You'd never pick sessions from there.
>
> **What you actually use:** running `claude --resume` (or typing `/resume` inside a session) opens an interactive list. Each entry typically shows an auto-generated summary or your first message, how long ago it was last active, and roughly how long the conversation was. You arrow through the list and press Enter. There's also usually a way to search or filter the list by typing.
>
> **Naming sessions:** recent versions let you give a session a name with a `/rename` command, and you can then resume it by that name. I'd confirm the exact commands in your version by typing `/help` or checking Claude Code's docs, since these features have been evolving.
>
> **A habit that keeps this from getting cluttered:**
>
> - Start each session with a clear first message, like "Working on Chapter 3 revisions" or "Brainstorming the antagonist's backstory." That first line often becomes the label you see in the picker.
> - Rename sessions worth returning to.
> - Treat most sessions as disposable. Because you're saving ideas and session notes into the vault, you rarely need to resume the old chat itself. Starting fresh and telling Claude to read the latest session note usually works better than resuming a long, bloated conversation, since long sessions get slower and less focused.
>
> Resuming is best for short gaps on a single task. For anything older or broader, rely on your notes.
<!-- UID: 01a1887f-34ed-74fa-8933-a8f0848be51e -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:33:42 AM
> I'm thinking that the most valuable way to use these would be, for example, in the instance where a summary idea note that Claude might generate when I said let's capture that as an idea note might not have the best wording. In some cases the wording might have been wonderful in the conversation but less desirable in the note that was saved. In that case does it make sense to go back to the original conversation and look for the better wording?
<!-- UID: 01a18882-94d3-7e56-a5d9-3d99f8083e04 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:33:47 AM
> Yes, that's one of the best reasons to go back to the transcript. A summary note compresses, and the phrasing that made an idea sparkle is often the first thing lost.
>
> You can do it in two ways:
>
> - **Resume the session** and ask Claude to find the passage: "Find where we discussed X and quote the best wording verbatim." Claude has the full conversation in view, so this works well if the session isn't too long.
> - **Search the transcript files.** They're plain text (JSONL) in the `.claude` folder, so a text search for a distinctive word or phrase will find the right file. This is clunkier but works when you can't remember which session it was.
>
> Prevention is easier than retrieval, though. Add a rule to `CLAUDE.md` and to the ideas template so the problem mostly goes away:
>
> - When saving an idea note, preserve the best verbatim phrasing from the conversation in a dedicated section, such as "Original wording," rather than only paraphrasing.
> - Include your own words as well as Claude's, since your phrasing in the moment is often the best.
> - Or simply say it in the moment: "Capture that as an idea, and keep the exact wording of that last paragraph."
>
> With that habit, the idea note carries a tidy summary plus the raw language, and going back to the transcript becomes a fallback instead of a routine step.
<!-- UID: 01a18882-94d8-7717-8199-c2cd1c408b6e -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:36:42 AM
> Would it be possible to build a rule or a skill or something that told Claude whenever it creates an idea note to include its own paraphrased summary but then separately and immediately below it it identifies the original wording that was used to generate this summer? What would the workflow for this be? Would it be a rule or a skill or something else? And where would I put such a rule so that it would work for individual notes of various types?
<!-- UID: 01a18885-5374-70df-9862-8f5357cf4123 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:36:51 AM
> Yes, and the simplest version needs no skill at all. Think of it as three layers, from lightest to heaviest:
>
> **1. A rule in `CLAUDE.md` (the best fit for "works for every note type")**
> `CLAUDE.md` at the vault root is read every session, so a rule there applies no matter which note type you're creating. Something like:
>
>> When creating any note from conversation content (ideas, research, characters, world building), include two sections: **Summary** (your paraphrase) and **Original wording** immediately below it, containing the exact words from the conversation that the summary is based on, copied verbatim and attributed to me or to you. Never reconstruct or polish the quotes. If you can't locate the exact wording, say so.
>
> Recent versions of Claude Code also support a `.claude/rules/` folder for splitting instructions into separate files. That's handy if `CLAUDE.md` gets long, but check your version's docs.
>
> **2. The templates (makes it visible and consistent)**
> Add the "Summary" and "Original wording" headings to each template in your Claude admin folder. The rule says why and how; the template gives the structure. Together they're more reliable than either alone.
>
> **3. A skill (only if you want an explicit command)**
> A skill is a packaged workflow, such as a "capture-note" skill that you invoke when you say "capture this as an idea" and that handles the type, filename, template, linking, and the two-section format in one defined procedure. It's worth it if you find yourself repeating the same multi-step instructions. For your stated need, it's more machinery than necessary.
>
> **My recommendation:** start with the `CLAUDE.md` rule plus updated templates. Use it for a few weeks, and if you notice you're giving the same extra instructions each time (filenames, tags, links), promote it into a skill then.
>
> The key phrase is "verbatim, never reconstructed." Without it, Claude may quietly smooth the "original wording" into something cleaner, which defeats the purpose.
<!-- UID: 01a18885-5378-78f7-adff-ea35e2ddfbae -->

---
>[!nexus_user] **User** - 10/29/2026 at 10:59:13 AM
> Okay. Thank you. I'm using Claude code terminal inside of obsidian as I mentioned. When I open the terminal window the text seems to be wrapping around as if it's too long for the window. Even when I make the window larger it seems to wrap undesirably before reaching the right hand side of the window. What is going on here? The default text in the window is interfering with my cursor
<!-- UID: 01a18899-f403-7096-bd12-d4f78c689489 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 10:59:20 AM
> This is a common problem with terminals embedded in Obsidian. The terminal believes it has a different number of columns than your window actually shows, so text wraps early and Claude Code's interface (which redraws the screen constantly) ends up fighting with your cursor.
>
> **Why it happens:** Obsidian terminal plugins draw the terminal inside a pane and have to report the pane's size to the shell. If that size isn't updated when you resize the pane, or is calculated before the pane finished opening, the shell keeps using the old width.
>
> **Things to try, roughly in order:**
>
> 1. **Close and reopen the terminal after setting your window size.** Resizing later often doesn't update it, but a fresh terminal measures the current width.
> 2. **Nudge the pane:** drag the pane divider or toggle the sidebar open and closed, which can trigger a re-measure. Then quit Claude Code (`/exit`) and restart it.
> 3. **Check the size the shell thinks it has:** at a normal prompt (outside Claude Code), run `stty size`. It prints rows and columns. If the column count is much smaller than what fits in your pane, that confirms the mismatch.
> 4. **Adjust the plugin's font size and line height** in its settings. Odd font metrics are a common cause of the width being miscalculated.
> 5. **Check that the plugin is up to date**, and look at its issue tracker for resize or wrapping bugs.
>
> **If it stays unreliable:** run Claude Code in a regular terminal app (Terminal, iTerm, Windows Terminal) pointed at your vault folder, and keep Obsidian open alongside it. Claude edits the same files either way, and Obsidian updates live. Many people prefer this because full-screen terminal interfaces like Claude Code are the hardest thing for embedded terminals to render well.
>
> Which terminal plugin are you using, and are you on Mac, Windows, or Linux? With that I can give more specific settings to check.
<!-- UID: 01a18899-f41b-7698-880e-ecb3f7d95627 -->

---
>[!nexus_user] **User** - 10/29/2026 at 11:02:11 AM
> I am using terminal version v3.29.0 by poliipsity, the most popular community terminal plug-in for obsidian
<!-- UID: 01a1889c-aaf8-7034-8c50-f25bea851643 -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 11:02:23 AM
> Your symptoms match a known behavior of Claude Code, which is probably the main cause here.
>
> Claude Code wraps its output with hard line breaks at the terminal width it detects, rather than letting the terminal wrap the text. That has a side effect: text already on screen doesn't reflow when you make the window wider, so it stays cramped at the old width. So if the terminal was narrow when Claude Code started (or when text was printed), widening the pane later won't fix what's already there.
>
> **What to try:**
>
> 1. **Size the pane first, then start fresh.** Get the pane to the width you want, exit Claude Code (`/exit`), and start it again. If you want to keep your conversation, use `claude --continue`. Old text may still look wrapped, but new text should use the full width.
> 2. **Clear the screen** with `/clear` (note that this wipes the conversation context) or Ctrl+L, which only redraws the screen.
> 3. **Check the reported width.** At the normal shell prompt, before launching Claude Code, run `stty size`. The second number is the columns. If it's much smaller than what fits in your pane, the plugin isn't reporting the size correctly.
> 4. **Look at the plugin's font settings.** Font size, line height, and letter spacing affect how many columns fit. Reset these to defaults to see if the wrapping changes.
>
> Your version is recent, and the plugin's 3.25.0 release already included fixes for Claude Code misdetecting the terminal and scrolling to the top during streaming, so you likely already have those. That makes a sizing mismatch more likely than a missing fix.
>
> For the cursor interference, can you describe it a bit more? For example, does the cursor jump to odd positions, does text overwrite itself, or does the input box seem to draw in the wrong place? That would help tell whether it's the same width mismatch or something else, like the shell prompt fighting with Claude Code's redraws.
>
> If it keeps misbehaving after a clean restart at the right size, running Claude Code in a standalone terminal pointed at your vault is the dependable fallback.
>
> ### References
> 1. [https://claudeissues.com/issue/35905-text-output-uses-hard-newlines-instead-of-terminal-soft-wrap](https://claudeissues.com/issue/35905-text-output-uses-hard-newlines-instead-of-terminal-soft-wrap)
> 2. [https://claudeissues.com/issue/8276-bug-text-doesnt-reflow-when-terminal-is-resized-from-narrower-to-wider](https://claudeissues.com/issue/8276-bug-text-doesnt-reflow-when-terminal-is-resized-from-narrower-to-wider)
> 3. [https://github.com/polyipseity/obsidian-terminal/releases/tag/3.25.0](https://github.com/polyipseity/obsidian-terminal/releases/tag/3.25.0)
<!-- UID: 01a1889c-aafc-744f-a5f4-46ca8788776a -->

---
>[!nexus_user] **User** - 10/29/2026 at 11:14:12 AM
> Looks like this terminal plug-in needs to know where python is in order to do the resizing correctly. How do I point this program/plug in to the python which I already have loaded on the computer
<!-- UID: 01a188a7-a985-72fc-9f87-ce02e09e642b -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 11:14:20 AM
> Yes, the plugin has a setting for this. I'm going from memory of how it's laid out, so labels may differ slightly in your version.
>
> **1. Find your Python's full path**
>
> - **Windows:** open Command Prompt or PowerShell and run `where python`
> - **Mac/Linux:** open a terminal and run `which python3`
>
> Copy the full path it prints. On Windows it looks like `C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe`. On Mac it's often something like `/usr/local/bin/python3` or `/opt/homebrew/bin/python3`.
>
> **2. Enter it in the plugin**
>
> Go to Obsidian **Settings → Community plugins → Terminal** (click its gear icon). Look for a field named something like **Python executable**. Paste the full path there. Some versions put this in the individual terminal profile instead, so if you don't see it at the top level, check the profile settings for the shell you're using.
>
> **3. Restart and test**
>
> Fully close the terminal tab, reopen it, and run `stty size` or just resize the pane and see whether wrapping improves.
>
> **Windows tips:**
>
> - Use the full path to the real `python.exe` rather than just `python`. The Microsoft Store "app execution alias" often causes trouble.
> - If it still fails, run `python --version` in a normal terminal to confirm it works at all.
>
> The plugin may also need particular Python packages installed for resizing to work. If the setting is correct and the problem persists, the plugin's documentation or the settings page itself should say what's required.
>
> Which operating system are you on? If it's Windows, I can be more specific about where the setting sits and what to check next.
<!-- UID: 01a188a7-a98f-75f2-938b-1974ffc3ecc1 -->

---
>[!nexus_user] **User** - 10/29/2026 at 11:16:55 AM
> I am on windows. The where 
>  python command executed in powershell simply returns the next command line
<!-- UID: 01a188aa-27e5-78a3-b1fc-d6669b79781c -->
>[!nexus_agent] **Assistant** - 10/29/2026 at 11:17:00 AM
> That's a PowerShell quirk rather than a sign Python is missing. In PowerShell, `where` is a built-in alias for a different command (`Where-Object`), so it silently returns nothing. Use one of these instead:
>
> ```
> where.exe python
> ```
> or
> ```
> Get-Command python
> ```
> or, the most reliable on Windows:
> ```
> py -0p
> ```
>
> `py -0p` uses the Python launcher and lists every installed Python with its full path, even if `python` isn't on your PATH.
>
> **Reading the results:**
>
> - A path like `C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe` is what you want. Copy it into the plugin's Python executable setting.
> - A path containing `WindowsApps` is the Microsoft Store shortcut. It often doesn't work with plugins like this. If that's all you see, use the path from `py -0p` instead, or install Python from python.org.
> - If all three commands say Python isn't found, it isn't installed (or isn't visible to your user account), and you'll need to install it from python.org. During install, check the box that says "Add python.exe to PATH."
>
> Once you've pasted the path into the plugin's settings, close and reopen the terminal tab and test the resizing again.
<!-- UID: 01a188aa-27eb-7028-bad4-d40803804be0 -->

---