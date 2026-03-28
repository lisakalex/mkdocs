# Initialising UV project

Let's make your project **fully modern with `uv` + lockfile + reproducible builds**.

# 📁 Final Project Structure

```txt
test.com/
│
├── google_parser.py
├── input_pages/
├── pyproject.toml
├── uv.lock
└── .venv/
```

---

# 1. Create `pyproject.toml`

Create:

```bash
touch pyproject.toml
```

Paste:

```toml
[project]
name = "google-html-parser"
version = "0.1.0"
description = "Parse Google Jobs HTML"
requires-python = ">=3.13"
dependencies = [
    "beautifulsoup4",
    "lxml"
]
```

---

# 2. Install dependencies (uv way)

```bash
uv sync
```

This:

✔ Creates `.venv`
✔ Installs dependencies
✔ Creates `uv.lock`
✔ Fully reproducible

---

# 3. Run (no activation needed)

```bash
uv run python google_parser.py
```

---

# 🔥 Now your setup is:

✔ Fast installs
✔ Locked dependencies
✔ No activation needed
✔ Fully reproducible
✔ Modern Python workflow

---

# Optional (recommended)

Add `.gitignore`

```bash
touch .gitignore
```

Add:

```gitignore
.venv/
__pycache__/
*.pyc
input_pages/
```

---

# Your final workflow

```bash
uv sync
uv run python google_parser.py
```

Done.

---

You're now using:

* Python 3.13
* uv
* lockfile
* reproducible builds

That's **senior-level Python setup** 🔥

---

If you'd like next:

* add CLI flags
* add dedupe
* add HTML output
* add multiple job boards
