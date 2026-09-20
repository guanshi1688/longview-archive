# The Economics of Productive Organisation｜English Working Manuscript

This directory contains a complete English working manuscript. Chapters are independent Markdown files. Review the book as a whole, then decide how to publish individual web pages. **Nothing in this package automatically changes `mkdocs.yml`, `build_corpus.py`, or any existing Git files.**

## Three Levels

- *Civilizational Structural Algorithm*: the historical, generative framework; Chinese and Western trajectories remain separate.
- *The Economics of Productive Organisation*: one shared manual of economic operation, not divided into China and West volumes.
- Projection essays: specific problems, events, audiences, and evidence arising from a mechanism in the canonical work.

## Human Pressure and Historical Studies

Chapter 01 briefly defines how the requirements of continuous production become sustained obligations for people. Chapter 06 links that effort to conditions for human life and renewal. This manual does **not** add a chapter comparing Chinese and Western human preparation.

Separate projections are (a) a study of work, divine tasks, reciprocal relations with deities, ethics, and responsibility in Chinese cultural history; (b) the existing *The Human Architecture of Industrialization* series, focused on the human preparation for China's fast modern industrialisation; and (c) a future independent study of human preparation for Western industrialisation. These are not one comparative chapter and do not rewrite the historical algorithm.

## Sources and Build Output

`index.md`, `Reading_and_Verification_Rules.md`, `Core_Terms.md`, and `00-*.md` through `10-*.md` are the independent source files. Run:

```powershell
python .\build_organisation_economics_en.py
```

The script generates **one** local review bundle, `_The_Economics_of_Productive_Organisation_EN_Complete.md`, in the **parent directory** of this folder. Its leading underscore marks a generated internal artefact. Do not copy it into MkDocs `docs/` or regard it as a second canonical source. Edit the independent files and rebuild; do not edit the bundle.

The intended future Git path is:

```text
longview-archive/docs/essays/english/organisation_economics/
```

The corresponding Chinese path is:

```text
longview-archive/docs/essays/chinese/organisation_economics/
```

These names use underscores exactly as requested. The earlier `productive-forces-economics` directories can remain in Git as historical archives, but their old navigation should be removed from the **active** `mkdocs.yml` nav when the replacement goes live. A comment alone does not prevent physical Markdown under `docs/` from being built or published by MkDocs. If the old texts must stop being public, also exclude them or remove their published copies as appropriate; keep originals in Git history or another non-published directory.

## Scope

Historical formation belongs to the algorithm; this book explains operational mechanisms in one production circuit. Its treatment of globalisation is conditional feedback analysis, not a deterministic forecast. Numerical claims, specific historical episodes, and current political-economic descriptions need separate verification when adapted for public projection essays.
