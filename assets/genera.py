"""Banner e copertine del profilo GitHub nello stile di denisbilli.it (Roboto Mono, giallo, terminale Tokyo Night)."""
import pathlib, sys, textwrap
from xml.sax.saxutils import escape as e

OUT = pathlib.Path(sys.argv[1])
FONT = "'Roboto Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
TEMI = {
    "light": dict(bg="#ffffff", card="#ffffff", ink="#111111", soft="#4a4a4a", rule="#111111", bar="#e5ff00", dim="#8a8a8a"),
    "dark": dict(bg="#0d1117", card="#1a1b26", ink="#f2f2f0", soft="#a9b1d6", rule="#f2f2f0", bar="#d8f000", dim="#565f89"),
}
T = dict(bg="#1a1b26", fg="#a9b1d6", dim="#565f89", blue="#7aa2f7", green="#9ece6a", purple="#bb9af7", orange="#e0af68", ink="#f2f2f0")


def header(tema):
    c = TEMI[tema]
    W, H = 1200, 330
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Denis Billi, Senior Software Engineer">
<rect width="{W}" height="{H}" fill="none"/>
<rect x="28" y="28" width="{W-60}" height="{H-60}" fill="{c['rule']}"/>
<rect x="20" y="20" width="{W-60}" height="{H-60}" fill="{c['card']}" stroke="{c['rule']}" stroke-width="3"/>
<rect x="20" y="20" width="{W-60}" height="44" fill="{c['bar']}" stroke="{c['rule']}" stroke-width="3"/>
<circle cx="48" cy="42" r="7" fill="none" stroke="#111111" stroke-width="2.5"/><circle cx="72" cy="42" r="7" fill="none" stroke="#111111" stroke-width="2.5"/><circle cx="96" cy="42" r="7" fill="#111111"/>
<text x="{W/2-20}" y="48" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="#111111">denis@billi: ~</text>
<g font-family="{FONT}">
<text x="56" y="112" font-size="20" fill="{c['dim']}">$ <tspan fill="{c['ink']}">whoami</tspan></text>
<text x="56" y="172" font-size="50" font-weight="700" fill="{c['ink']}">Denis Billi</text>
<rect x="56" y="184" width="340" height="8" fill="{c['bar']}"/>
<text x="56" y="228" font-size="21" fill="{c['soft']}">Senior Software Engineer · Industrial Software · CNC/HMI · Applied AI</text>
<text x="56" y="272" font-size="18" fill="{c['dim']}">$ <tspan fill="{c['ink']}">ls ./work</tspan>  <tspan fill="{c['soft']}">cnc-cam  hmi  legacy-modernization  applied-ai  research</tspan><tspan fill="{c['ink']}"> ▍</tspan></text>
</g>
</svg>
'''


def copertina(nome, riga, tag, colore="blue"):
    W, H = 760, 400
    righe = textwrap.wrap(riga, 40)[:3]
    testo = "".join(f'<text x="44" y="{236 + i*38}" font-size="26" fill="{T["fg"]}">{e(r)}</text>' for i, r in enumerate(righe))
    tags, x = "", 44
    for t in tag:
        w = 18 + len(t) * 12.6
        tags += f'<rect x="{x}" y="334" width="{w}" height="30" fill="none" stroke="{T[colore]}" stroke-width="2"/><text x="{x+8}" y="355" font-size="19" fill="{T[colore]}">{e(t)}</text>'
        x += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(nome)}: {e(riga)}">
<rect width="{W}" height="{H}" fill="{T['bg']}"/>
<rect width="{W}" height="40" fill="#16161e"/>
<circle cx="24" cy="20" r="6" fill="#f7768e"/><circle cx="46" cy="20" r="6" fill="{T['orange']}"/><circle cx="68" cy="20" r="6" fill="{T['green']}"/>
<g font-family="{FONT}">
<text x="{W/2}" y="26" text-anchor="middle" font-size="15" fill="{T['dim']}">~/repos/{e(nome.lower().replace(' ', '-'))}</text>
<text x="44" y="100" font-size="19" fill="{T['dim']}">$ <tspan fill="{T['green']}">cat</tspan> <tspan fill="{T['fg']}">README.md</tspan></text>
<text x="44" y="168" font-size="44" font-weight="700" fill="{T['ink']}">{e(nome)}</text>
<rect x="44" y="182" width="{min(660, 27*len(nome))}" height="7" fill="#d8f000"/>
{testo}
{tags}
</g>
</svg>
'''


COPERTINE = {
    "ground-control": ("Ground Control", "Discrete-time simulation of policy decisions in LEO satellite networks.", ["Python", "simulation", "research"], "blue"),
    "spectral": ("Spectral Generalization", "Frequency-domain detection of AI-generated images across generators.", ["Python", "image forensics", "paper"], "purple"),
    "storyhash": ("StoryHash", "Multi-modal fingerprints for robust video retrieval.", ["video retrieval", "paper"], "purple"),
    "paperdown": ("paperdown", "Markdown to PDF on the command line, with real typography.", ["TypeScript", "CLI", "npm"], "green"),
    "prodkit": ("ProdKit", "Reads a repository and reports what is missing before it can carry real users.", ["TypeScript", "CLI", "open source"], "green"),
    "envlockup": ("envlockup", "An encrypted .env you can commit, unlocked with your own SSH key.", ["TypeScript", "secrets", "CLI"], "green"),
    "quested": ("QuestEd", "Courses, exercises and assessments for teaching programming.", ["Python", "Django", "education"], "orange"),
    "qdbmanager": ("qDBManager", "A lightweight ORM / entity manager for Qt.", ["C++", "Qt", "SQLite"], "blue"),
    "asteroids": ("Asteroids", "The classic arcade game in C++: game loop, rendering, engine basics.", ["C++", "game"], "orange"),
    "pyimgduplicatefinder": ("PyImgDuplicateFinder", "Finds and moves duplicate images with HaarPSI, a perceptual similarity index.", ["Python", "images"], "blue"),
    "snapbiz": ("SnapBiz", "Studio management for wedding photographers: requests, contracts, team, delivery.", ["Django", "SaaS"], "orange"),
    "scribit": ("Scribit.ai", "Transcription and document translation that keeps the original layout.", ["Python", "SaaS", "AI"], "orange"),
}
for tema in TEMI:
    (OUT / f"header-{tema}.svg").write_text(header(tema))
for k, v in COPERTINE.items():
    (OUT / f"{k}.svg").write_text(copertina(*v))
print("ok", len(COPERTINE) + 2)
