import io, re, sys, html
import markdown

SRC = str(__import__("pathlib").Path(__file__).resolve().parent.parent)
OUT = SRC + r"\index.html"

FILES = [
    ("00-README.md", "Index"),
    ("10-mentor-letter.md", "Mentor's Letter"),
    ("01-what-we-have.md", "What We Have"),
    ("02-analysis.md", "Analysis"),
    ("03-business-model-and-phases.md", "Business Model & Phases"),
    ("04-rebranding-strategy.md", "Rebranding Strategy"),
    ("05-marketing-plan.md", "Marketing Plan"),
    ("06-growth-and-business-policy.md", "Growth & Business Policy"),
    ("07-90-day-action-plan.md", "90-Day Action Plan"),
    ("08-open-questions.md", "Open Questions"),
    ("09-sources.md", "Sources"),
    ("99-hamidur-links-whatsapp-2026-10-16.md", "Raw Links (WhatsApp)"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"])

sections = []
nav = []
for i, (fn, label) in enumerate(FILES):
    text = io.open(f"{SRC}\\{fn}", encoding="utf-8").read()
    # convert links to sibling .md files into in-page anchors
    text = re.sub(r"\]\((\d\d-[^)]+\.md)\)", lambda m: f"](#{m.group(1).replace('.md','')})", text)
    # the raw links file has no markdown structure; wrap as a code-like block preserving lines
    if fn.startswith("99-"):
        body = "<pre class='raw'>" + html.escape(text) + "</pre>"
    else:
        md.reset()
        body = md.convert(text)
    sid = fn.replace(".md", "")
    sections.append(f"<section id='{sid}' class='doc'><div class='doc-tag'>{html.escape(fn)}</div>{body}</section>")
    nav.append(f"<a href='#{sid}'><span class='n'>{fn[:2]}</span>{html.escape(label)}</a>")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Business Launch Plan</title>
<meta name="description" content="Accounting training, agency and placement venture: inventory, analysis, model, rebrand, marketing, policy, 90-day plan. Compiled 22 Oct 2026.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#f7f6f2; --panel:#ffffff; --ink:#1b2430; --muted:#5b6673; --line:#e3e0d8;
  --accent:#0f5f6b; --accent-ink:#ffffff; --soft:#e8f1f2; --code:#f1efe9; --warn:#b4541a;
  --th:#eef0f3;
}}
@media (prefers-color-scheme: dark){{ :root:not([data-theme="light"]){{
  --bg:#0f1317; --panel:#161b21; --ink:#e7e9ec; --muted:#9aa4ae; --line:#2a323b;
  --accent:#5fc3cf; --accent-ink:#0f1317; --soft:#1b2a2e; --code:#1d232a; --warn:#f0a06a; --th:#1d242c;
}}}}
:root[data-theme="dark"]{{
  --bg:#0f1317; --panel:#161b21; --ink:#e7e9ec; --muted:#9aa4ae; --line:#2a323b;
  --accent:#5fc3cf; --accent-ink:#0f1317; --soft:#1b2a2e; --code:#1d232a; --warn:#f0a06a; --th:#1d242c;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Inter,"Noto Sans Bengali",system-ui,sans-serif;}}
header.top{{position:sticky;top:0;z-index:5;background:var(--panel);border-bottom:1px solid var(--line);padding:12px 16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
header.top h1{{font-size:17px;margin:0;font-weight:700;letter-spacing:-.01em}}
header.top .sub{{color:var(--muted);font-size:13px}}
header.top a.hbtn{{margin-left:auto;background:var(--accent);color:var(--accent-ink);border-radius:8px;padding:6px 12px;font-size:13px;font-weight:600;text-decoration:none}}
nav.side a.sim,.toc-mobile a.sim{{background:var(--accent);color:var(--accent-ink);font-weight:600;margin-bottom:8px}}
nav.side a.sim .n{{color:var(--accent-ink)}}
header.top button{{background:var(--soft);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font:inherit;font-size:13px;cursor:pointer}}
.layout{{display:grid;grid-template-columns:260px minmax(0,1fr);gap:0;max-width:1280px;margin:0 auto}}
nav.side{{position:sticky;top:57px;align-self:start;height:calc(100vh - 57px);overflow:auto;padding:16px;border-right:1px solid var(--line)}}
nav.side a{{display:flex;gap:10px;align-items:baseline;color:var(--ink);text-decoration:none;padding:7px 10px;border-radius:8px;font-size:14px}}
nav.side a:hover{{background:var(--soft)}}
nav.side a .n{{font:500 12px JetBrains Mono,monospace;color:var(--muted);min-width:22px}}
main{{padding:24px 16px 80px;min-width:0}}
section.doc{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:28px 28px 20px;margin:0 0 28px}}
.doc-tag{{font:500 12px JetBrains Mono,monospace;color:var(--muted);margin-bottom:8px}}
h1{{font-size:28px;line-height:1.25;margin:4px 0 16px;letter-spacing:-.02em}}
h2{{font-size:21px;margin:30px 0 10px;padding-top:10px;border-top:1px solid var(--line);letter-spacing:-.01em}}
h3{{font-size:17px;margin:22px 0 8px}}
h4{{font-size:15px;margin:18px 0 6px}}
p{{margin:0 0 12px}}
a{{color:var(--accent)}}
ul,ol{{padding-left:22px;margin:0 0 12px}}
li{{margin:3px 0}}
blockquote{{margin:12px 0;padding:8px 16px;border-left:4px solid var(--accent);background:var(--soft);border-radius:6px}}
code{{font:13.5px JetBrains Mono,monospace;background:var(--code);padding:1px 5px;border-radius:4px}}
pre{{background:var(--code);padding:14px 16px;border-radius:10px;overflow:auto;font:13px/1.5 JetBrains Mono,monospace;margin:0 0 14px}}
pre code{{background:none;padding:0}}
pre.raw{{white-space:pre-wrap;word-break:break-all}}
.tbl{{overflow:auto;margin:0 0 16px;border:1px solid var(--line);border-radius:10px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}}
th{{background:var(--th);font-weight:600;position:sticky;top:0}}
tr:last-child td{{border-bottom:none}}
strong{{font-weight:650}}
hr{{border:0;border-top:1px solid var(--line);margin:22px 0}}
.toc-mobile{{display:none}}
@media (max-width:900px){{
  .layout{{grid-template-columns:1fr}}
  nav.side{{display:none}}
  .toc-mobile{{display:block;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px;margin:0 0 20px}}
  .toc-mobile a{{display:inline-block;margin:4px 8px 4px 0;font-size:14px}}
  section.doc{{padding:18px 16px 12px}}
  h1{{font-size:24px}}
  main{{padding:16px 16px 60px}}
}}
@media print{{header.top button,nav.side,.toc-mobile{{display:none}} section.doc{{border:none;page-break-after:always}}}}
</style>
</head>
<body>
<header class="top">
  <div><h1>Business Launch Plan</h1><div class="sub">Accounting training · agency · placement — compiled 22 Oct 2026 from <code>01_business-launch/</code></div></div>
  <a class="hbtn" href="12-simulator.html">▶ Simulator</a>
  <button id="theme" type="button">Theme</button>
</header>
<div class="layout">
  <nav class="side"><a class="sim" href="12-simulator.html"><span class="n">▶</span>Open the Simulator (digital twin)</a>{''.join(nav)}</nav>
  <main>
    <div class="toc-mobile"><a class="sim" href="12-simulator.html">▶ Open the Simulator (digital twin)</a><br>{''.join(nav)}</div>
    {''.join(sections)}
  </main>
</div>
<script>
(function(){{
  var root=document.documentElement, b=document.getElementById('theme');
  var saved=null; try{{saved=localStorage.getItem('theme')}}catch(e){{}}
  if(saved) root.setAttribute('data-theme',saved);
  b.addEventListener('click',function(){{
    var dark = root.getAttribute('data-theme')==='dark' || (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
    var next = dark?'light':'dark'; root.setAttribute('data-theme',next);
    try{{localStorage.setItem('theme',next)}}catch(e){{}}
  }});
  document.querySelectorAll('table').forEach(function(t){{var w=document.createElement('div');w.className='tbl';t.parentNode.insertBefore(w,t);w.appendChild(t);}});
}})();
</script>
</body>
</html>
"""
io.open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "chars")
