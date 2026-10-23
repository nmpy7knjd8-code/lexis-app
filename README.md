# Lexis
Flashcards for the untranslatable terms of the philosophical canon (Greek, Latin, German, French, and others). Viewer cloned from Glossa.
- `cards/index.html` – viewer (Review only). Palette & fonts: the `LEXIS placeholder theme` block (CSS variables `--lx-*`).
- `content/bN_cards.py` → `python3 content/build.py bN` → `content/bN-cards.json`. Quotes are verified verbatim by `content/verify_quotes.py` against downloaded public sources; unverifiable quotes are dropped.
- `python3 tools_validate.py --strict` – schema, duplicates, images.
- `cards/shot_mobile.py W H` – overflow check (serve repo root on :8767).
