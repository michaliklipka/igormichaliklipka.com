#!/usr/bin/env python3
"""Builds work/<slug>/index.html for each SELECTED WORK project. Edit PROJECTS, run: python3 work/build.py"""
from pathlib import Path
import html

HERE = Path(__file__).resolve().parent

PROJECTS = [
    dict(slug="robert-pape", img="dg-robert-pape.jpg", views="1.9M",
         title="DECODED GENIUS × ROBERT PAPE", role="VFX",
         alt="Robert Pape: Is World War 3 About To Begin?",
         yt="https://www.youtube.com/watch?v=e5oIZEmvtUY",
         ask="Decoded Genius wanted their interview with political scientist Robert Pape to feel bigger than two people at a table.",
         idea="I put the story on the studio wall behind the hosts: real footage, data and text composited into the room and timed to every point Pape makes. The episode reached 1.9M views."),
    dict(slug="ai-scientist", img="dg-ai-conscious.jpg", views="3.4M",
         title="DECODED GENIUS × AI SCIENTIST", role="VFX",
         alt="No, AI Isn't Conscious; It's Actually Much Worse",
         yt="https://www.youtube.com/watch?v=FS_hLDTDI1w",
         ask="Decoded Genius needed an hour-long conversation about AI to stay visual from start to finish.",
         idea="I built graphics on the studio wall behind the hosts, timed to the guest's words, so every big claim lands on screen as it's said. The episode reached 3.4M views."),
]

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} · Igor Michalik-Lipka</title>
    <meta name="description" content="{role} · {title}. {ask_attr}">
    <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #ffffff; --fg: #000000; --mute: #6b6b6b; --line: #e6e6e6; --link: #0000EE;
                 --font: "JetBrains Mono", ui-monospace, monospace; --size: 17px; }}
        [data-theme="dark"] {{ --bg: #000000; --fg: #ffffff; --mute: #8a8a8a; --line: #222222; --link: #58a6ff; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        html {{ background: var(--bg); -webkit-text-size-adjust: 100%; }}
        body {{ background: var(--bg); color: var(--fg); font-family: var(--font); font-size: var(--size);
               line-height: 1.45; letter-spacing: -0.02em; text-transform: uppercase;
               -webkit-font-smoothing: antialiased; padding: 64px 24px 48px; }}
        main, footer {{ max-width: 760px; margin: 0 auto; }}
        a {{ color: var(--link); text-decoration: underline; text-underline-offset: 3px; text-decoration-thickness: 1px; }}
        a:hover {{ opacity: .7; }}
        .back {{ display: inline-block; margin-bottom: 32px; }}
        h1 {{ font-size: var(--size); font-weight: 700; }}
        .sub {{ color: var(--mute); margin-top: 6px; }}
        .watch {{ display: block; margin-top: 24px; color: var(--fg); text-decoration: none; }}
        .watch:hover {{ opacity: 1; }}
        .img {{ position: relative; display: block; aspect-ratio: 16 / 9; overflow: hidden; border: 1px solid var(--line); background: #000; }}
        .img img {{ display: block; width: 100%; height: 100%; object-fit: cover; transition: transform .4s ease; }}
        .watch:hover img {{ transform: scale(1.03); }}
        .play {{ position: absolute; left: 12px; bottom: 12px; background: #000; color: #fff; font-size: 16px; font-weight: 700; padding: 7px 11px; line-height: 1; }}
        .watch .cap {{ display: block; margin-top: 10px; font-size: 14px; }}
        .watch:hover .cap {{ text-decoration: underline; text-underline-offset: 3px; }}
        .block {{ border-top: 1px solid var(--line); padding: 20px 0; margin-top: 32px; }}
        .block + .block {{ margin-top: 0; }}
        .label {{ color: var(--mute); margin-bottom: 10px; }}
        .next {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 16px;
                border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 20px 0;
                color: var(--fg); text-decoration: none; }}
        .next:hover {{ opacity: 1; }}
        .next:hover .name {{ text-decoration: underline; text-underline-offset: 3px; }}
        .next .arrow {{ font-size: 28px; line-height: 1; transition: transform .2s ease; }}
        .next:hover .arrow {{ transform: translateX(6px); }}
        footer {{ margin-top: 48px; display: flex; justify-content: space-between; gap: 16px; }}
        #theme-toggle {{ background: none; border: 0; padding: 0; cursor: pointer; font: inherit; color: inherit;
                        text-transform: uppercase; letter-spacing: inherit; text-decoration: underline; text-underline-offset: 3px; }}
        .copy {{ color: var(--mute); }}
        @media (max-width: 640px) {{
            :root {{ --size: 14px; }}
            body {{ padding: 32px 18px 32px; }}
            .watch .cap {{ font-size: 12.5px; }}
            .play {{ font-size: 13px; }}
        }}
    </style>
</head>
<body>
    <main>
        <a class="back" href="../../">← IGOR MICHALIK-LIPKA</a>
        <h1>{title}</h1>
        <p class="sub">{role} · {views} VIEWS</p>

        <a class="watch" href="{yt}" target="_blank" rel="noopener">
            <span class="img"><img src="../../assets/{img}" alt="{alt}" width="960" height="540"><span class="play">▶ WATCH ON YOUTUBE</span></span>
            <span class="cap">{alt_upper} ↗</span>
        </a>

        <section class="block">
            <p class="label">THE ASK</p>
            <p>{ask}</p>
        </section>
        <section class="block">
            <p class="label">THE IDEA</p>
            <p>{idea}</p>
        </section>

        <a class="next" href="../{next_slug}/">
            <span><span class="label" style="display:block;margin-bottom:6px">NEXT PROJECT</span><span class="name">{next_title}</span></span>
            <span class="arrow">→</span>
        </a>
    </main>

    <footer>
        <button id="theme-toggle" type="button">[DARK MODE]</button>
        <span class="copy">© <span id="yr"></span> IGOR MICHALIK-LIPKA</span>
    </footer>

    <script>
        document.getElementById('yr').textContent = new Date().getFullYear();
        (function () {{
            const root = document.documentElement, t = document.getElementById('theme-toggle');
            const label = () => t.textContent = root.getAttribute('data-theme') === 'dark' ? '[LIGHT MODE]' : '[DARK MODE]';
            label();
            t.addEventListener('click', () => {{ root.setAttribute('data-theme', root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'); label(); }});
        }})();
    </script>
</body>
</html>
"""

e = html.escape
for i, p in enumerate(PROJECTS):
    n = PROJECTS[(i + 1) % len(PROJECTS)]
    out = HERE / p["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(PAGE.format(
        title=e(p["title"]), role=e(p["role"]), views=e(p["views"]), yt=e(p["yt"]), img=e(p["img"]),
        alt=e(p["alt"]), alt_upper=e(p["alt"].upper()), ask=e(p["ask"]), idea=e(p["idea"]),
        ask_attr=e(p["ask"]), next_slug=n["slug"], next_title=e(n["title"])))
    print("wrote", out.relative_to(HERE.parent))
