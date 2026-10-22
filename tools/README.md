# tools

`build_report.py` rebuilds `../index.html` from every `.md` file in the folder (order and labels are set in the `FILES` list inside the script).

Run after editing any markdown file:

    python -I tools/build_report.py

Needs Python 3 with the `markdown` package (`pip install markdown`). Then commit and push `index.html` with the changed `.md` files.
