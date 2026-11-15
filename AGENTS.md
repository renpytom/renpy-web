# web-2011 agent guide

This is the source of the renpy.org website: a small Flask app (Python 3, Jinja2 templates). It is **not** the Ren'Py
engine.

Production runs on Python 3.15 (`requires-python = ">=3.15"` in `pyproject.toml`).

## Run

There is no build step, test suite, or linter configuration. Dependencies are declared in `pyproject.toml` and locked in
`uv.lock`. Type checking uses ty, a dev dependency; keep `uv run ty check` passing. It can't see attributes set through
`__dict__.update` (as in `Data` and `Sponsor`), so declare those as class-level annotations.

```sh
uv run ty check                   # type check the project
uv run main.py                    # dev server on :5000, debug + template auto-reload
uv run main.py --public --port N  # bind 0.0.0.0
MONTH=2024-05 uv run main.py      # force a specific sponsors/<MONTH>.tsv
```

reCAPTCHA (for `/email`) is implemented in [recaptcha.py](recaptcha.py), not the Flask-ReCaptcha package, which breaks
with Jinja2 3.1+.

Production uses [renpyweb.service](renpyweb.service): a hardened systemd unit running gunicorn (sync workers;
`sponsors.init` mutates module globals per request, so no threads) on Python 3.15 at `127.0.0.1:38917`, behind nginx.
The sandbox makes the filesystem read-only, so the app must not write files. [deploy.sh](deploy.sh) rsyncs the tree
to the production host, runs `uv sync --frozen --no-dev -p 3.15` there (the `.venv` is built on the server, since
rsync skips dotfiles), installs the unit into `/etc/systemd/system`, reloads systemd, and enables and restarts it.

`deploy.sh` writes to a remote server, so only run it when asked.

## Architecture

- [main.py](main.py): all routes. `/<name>.html` is a catch-all that renders `templates/<name>.html`, so adding a
  template adds a page. `/wiki/<path>` serves pre-rendered HTML from `wiki/page/`. `/feed/` builds the RSS feed from
  `data`. `/channels.json` serves the update channels. `/d/<name>` redirects to the matching docs page using [doc.py](doc.py), which reads
  Sphinx's `objects.inv` from the built Ren'Py docs.
- [data.py](data.py) + [model.py](model.py) + [releases/](releases/): the "database" is code. The `releases/`
  package holds one module per major version (`v8`, `v7_8` for the years 7.x and 8.x were released together, `v7`,
  `v6`, `v5`, `v4`), each a list of `Release(...)` calls (newest first) with changelog/credits text. `data.py` defines
  the `releases` and `aliases` lists, then imports the modules newest first with `from releases import v8, ...`; keep
  that form, since `import releases.v8` would rebind `data.releases` to the package. `model.py` defines `Release`,
  which appends itself to `data.releases` and, in `__init__`, reads file sizes and dates from the release download
  directories on disk. `Release` takes keyword-only, annotated parameters, so an unknown keyword raises `TypeError`
  when the data is imported; a new field needs a parameter there. `Series("x.y", ...)` sets defaults for the fields
  shared by a series (name, world_order, notes, credits, extra_credits, top_html, full_html, deprecations, pygame); a
  `Release` finds its series by version and overrides any field it passes itself. A `Series` must come before its
  releases (it raises `ValueError` otherwise). 8.6 is the first series to use one; older releases pass every field.
  At the bottom of `data.py`, `current_8`/`prerelease_8` (and `_7`), `release_version`, and `final_releases` are
  derived from list order and the `prerelease`/`invisible` flags, so **the order of releases within and across the
  `releases/` modules, and their flags, determine what the site calls "latest"**. Add new releases to
  `releases/v8.py`, which also holds the release/patch checklists in comments at its top; a 9.x series would go in a
  new `releases/v9.py`, imported before `v8`.
- Release text from 8.6 on: `announcement` is the release-specific intro, `notes` the series release notes (e.g.
  `COMMON_8_6`, set on the `Series`), and `changes` this release's release-note-level changes (left unset on an
  x.y.0). Once any release in an x.y series has non-empty `changes`, the series is "new-style"
  (`Release.series_has_changes`): its pages show a history built by `Release.series_history` (the `changes` of every
  public release in the series, plus the page's own prerelease; the x.y.0 is listed as "* Initial release of Ren'Py
  x.y.") instead of `history`, shown only when it lists at least two releases. Pages show `notes` after the
  announcement, and the social formats post `changes` (or `notes` when there are none). Older releases put the series
  notes in `announcement` and keep the free-form `history`.
- [sponsors.py](sponsors.py): loads monthly Patreon exports from `sponsors/YYYY-MM.tsv` plus
  `sponsors/overrides - main.tsv` on every request (`before_request`). `init` walks back month by month until a file
  exists. Files from `2020-07.tsv` on use `load_sponsorfn_new`, which parses by column position and adapts to optional
  columns (Twitter, Discord, free member/trial) by inspecting the header; older files use `load_sponsorfn_old`. When a
  new export changes the column layout, adjust the header detection there. Sponsors are keyed by email in `by_email`.
- `templates/` extend `base.html`. `release.txt` holds the plain-text release announcement and is rendered three ways
  in `main.py`: `/release/<name>.txt` (`release_txt`, BBCode for forum posts), `/release/<name>.md` (`release_md`,
  GitHub release body; the template gets `markdown=True`), and `/release/<name>.update.html` (`release_update_html`,
  rich HTML with a copy button for pasting into sites that take formatting; standalone `release_update.html`, marked
  noindex). All unwrap hard-wrapped lines with `join_lines`, so `announcement`, `notes`, and `changes` should use
  blank lines between paragraphs, `* ` for list items, `**bold**`, and `#1234` for issues (linked on the HTML pages).
- `static/`: `featured/` (each `.jpg`/`.png` needs a same-named `.html` blurb; the index samples 5 of them),
  `artcard/` (per-month art, auto-detected), `sponsors/<W>x<H>/<credit name>.png` banners, `patreon/`.

## Gotchas

- `sponsors/`, `static/sponsors/`, `static/patreon/`, `static/artcard/`, `static/wiki/`, and `wiki/page/` are
  git-ignored (private data or generated); they must exist locally for those pages to work.
- Paths to release downloads and docs are hard-coded to the author's machine (`/home/tom/WWW.update/...`,
  `/home/tom/WWW.renpyorg/...`, with `/home/tom/ab/renpy/dl` as fallback); see `main.py` (`/channels.json`),
  `model.py` (`FILE_PATHS`), and `doc.py` (`PATHS`).
