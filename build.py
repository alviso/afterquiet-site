"""Build index.html from page.html by inlining fig/*.svg at {{fig:name}}.

Figures come from the app repo: uv run python -m sim.site_figures <this>/fig
(and again with the extra argument "sounds").
"""
import re
from pathlib import Path

here = Path(__file__).parent
page = (here / "page.html").read_text()
out = re.sub(r"\{\{fig:(\w+)\}\}", lambda m: (here / "fig" / f"{m[1]}.svg").read_text(), page)
assert "{{" not in out
(here / "index.html").write_text(out)
print("index.html", len(out), "bytes")
