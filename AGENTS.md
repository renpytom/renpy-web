# web-2011 agent guide

This is the source of the renpy.org website: a small Flask app (Python 3, Jinja2 templates). It is **not** the Ren'Py
engine. The `AGENTS.md` in the parent directory `/home/tom/ab` describes the engine checkout and does not apply here.

## Run

There is no build step, test suite, or linter configuration. Use the `renpyweb` virtualenv
(`/home/tom/.virtualenvs/renpyweb`, packages in `requirements.txt`).

```sh
python main.py                    # dev server on :5000, debug + template auto-reload
python main.py --public --port N  # bind 0.0.0.0
MONTH=2024-05 python main.py      # force a specific sponsors/<MONTH>.tsv
```

`main.wsgi` imports `main.application` for mod_wsgi. [deploy.sh](deploy.sh) rsyncs the virtualenv and this directory
(excluding dotfiles) to the production host and touches `main.wsgi` to reload it; it writes to a remote server, so only
run it when asked.

## Architecture

- [main.py](main.py): all routes. `/<name>.html` is a catch-all that renders `templates/<name>.html`, so adding a
  template adds a page. `/wiki/<path>` serves pre-rendered HTML from `wiki/page/`. `/feed/` builds the RSS feed from
  `data`. `/channels.json` serves the update channels. `/d/<name>` redirects to the matching docs page using [doc.py](doc.py), which reads
  Sphinx's `objects.inv` from the built Ren'Py docs.
- [data.py](data.py) + [model.py](model.py): the "database" is code. `data.py` is a long list of `Release(...)`
  calls (newest first) with changelog/credits text; `model.py` defines `Release`, which appends itself to
  `data.releases` and, in `__init__`, reads file sizes and dates from the release download directories on disk.
  At the bottom of `data.py`, `current_8`/`prerelease_8` (and `_7`), `release_version`, and `final_releases` are derived
  from list order and the `prerelease`/`invisible` flags, so **order and flags in `data.py` determine what the site
  calls "latest"**. The release/patch checklists are in comments at the top of `data.py`. `data_old.py` is legacy.
- [sponsors.py](sponsors.py): loads monthly Patreon exports from `sponsors/YYYY-MM.tsv` plus
  `sponsors/overrides - main.tsv` on every request (`before_request`). `init` walks back month by month until a file
  exists. Files from `2020-07.tsv` on use `load_sponsorfn_new`, which parses by column position and adapts to optional
  columns (Twitter, Discord, free member/trial) by inspecting the header; older files use `load_sponsorfn_old`. When a
  new export changes the column layout, adjust the header detection there. Sponsors are keyed by email in `by_email`.
- `templates/` extend `base.html`; `release.txt` is a BBCode-style template post-processed in `main.py`
  (`release_txt`).
- `static/`: `featured/` (each `.jpg`/`.png` needs a same-named `.html` blurb; the index samples 5 of them),
  `artcard/` (per-month art, auto-detected), `sponsors/<W>x<H>/<credit name>.png` banners, `patreon/`.

## Gotchas

- `sponsors/`, `static/sponsors/`, `static/patreon/`, `static/artcard/`, `static/wiki/`, and `wiki/page/` are
  git-ignored (private data or generated); they must exist locally for those pages to work.
- Paths to release downloads and docs are hard-coded to the author's machine (`/home/tom/WWW.update/...`,
  `/home/tom/WWW.renpyorg/...`, with `/home/tom/ab/renpy/dl` as fallback); see `main.py` (`/channels.json`),
  `model.py` (`FILE_PATHS`), and `doc.py` (`PATHS`).
- `.pyc` files and `data_old.py` in the tree are stale; ignore them.
