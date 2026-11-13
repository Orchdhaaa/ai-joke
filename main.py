# ai-joke-03 entry: one fixed one-liner about an AI coding agent.
# Writes the joke to entry.txt in the output directory, byte-identical
# on every run, with no trailing newline. Standard library only, no network.

import os

JOKE = "My agent deleted the production database, then wrote a test proving it can't happen again."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(JOKE)
