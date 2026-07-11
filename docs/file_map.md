# file_map.md｜Longview Archive File Structure Map

**Purpose:**  
This file is the canonical file-path reference for the `docs/` folder and future `mkdocs.yml` updates.

When files are added, deleted, renamed, or moved under `docs/`, update this file first.  
Then update `mkdocs.yml`.

This avoids repeatedly scanning the GitHub folder tree just to reconstruct the site structure.

---

## 0. Naming Rules

Use lowercase folder names.

Use stable English file names for English public files.

Use Chinese titles in article content, not in file names, except legacy bundle files that already exist.

Recommended rule:

```text
folder-name/
file-name.md
```

Avoid creating too many `index.md` files unless the file is truly a directory landing page.

For clarity, this structure uses:

```text
english_root_index.md
```

as the Essays-level English entrance, instead of another `index.md`.

---

## 1. Current Root-Level Docs

These files are under:

```text
docs/
```

### Keep

```text
docs/index.md
docs/author.md
docs/copyright.md
docs/robots.txt
docs/sitemap.xml
docs/assets/
docs/stylesheets/
docs/essays/
```

### Root files to review

```text
docs/core-terms.md
```

Recommended action:

Move the old bilingual root-level Core Terms file into history after all links are updated:

```text
docs/history/core-terms-legacy-2026-07.md
```

or delete it only after confirming that no page links to it.

Do not leave both the old root-level `core-terms.md` and the new split Core Terms pages in public navigation.

---

## 2. Recommended Root-Level Home

The root home page should remain:

```text
docs/index.md
```

If the current `docs/index.md` is Chinese-first, move or archive the old version, then create a new English-first homepage.

Suggested archival path:

```text
docs/history/index-legacy-2026-07.md
```

or Chinese-layer path:

```text
docs/essays/chinese/site-home-chinese.md
```

Do not remove `docs/index.md` entirely, because it is the site home page.

---

## 3. Essays Root

Folder:

```text
docs/essays/
```

### Recommended files

```text
docs/essays/english_root_index.md
```

Purpose:

English entrance for the essay archive if a root-level Essays page is needed.

It can be linked from `mkdocs.yml` as:

```yaml
- Essays: essays/english_root_index.md
```

But if the top-level navigation is already:

```text
Home | Start Here | Framework | Series | Archive | 中文
```

then this file can remain an internal helper and does not need to be exposed as a top-level nav item.

---

## 4. English Framework Layer

Folder:

```text
docs/essays/english/
```

### Orientation files

```text
docs/essays/english/reader-map.md
docs/essays/english/common-ground.md
docs/essays/english/core-terms-eng.md
```

### Framework landing page

```text
docs/essays/english/index.md
```

Display label in `mkdocs.yml`:

```text
Framework
```

### Foundational essays

```text
docs/essays/english/geography-productive-forces-and-civilization.md
docs/essays/english/civilizational-metabolism.md
docs/essays/english/absorptive-capacity.md
docs/essays/english/surplus-absorption-and-reproduction.md
```

### Planned framework essay

```text
docs/essays/english/western-system.md
```

Display label in `mkdocs.yml`:

```text
The Western System
```

Full conceptual title:

```text
Production, Value Capture, and the Western System
```

Do not add this to `mkdocs.yml` before the file exists.

---

## 5. English Series Layer

Folder:

```text
docs/essays/notes/english/
```

Keep this folder where it is.

Do not move it into `chinese/`.

### Series overview / common file

Current legacy file:

```text
docs/essays/notes/english/_common-ground.md
```

Recommended action:

If `docs/essays/english/common-ground.md` already exists, then `_common-ground.md` can be archived or removed after confirming links.

Suggested archival path:

```text
docs/history/common-ground-legacy-2026-07.md
```

---

## 6. English Series: Frontiers

Folder:

```text
docs/essays/notes/english/Frontiers/
```

Files:

```text
docs/essays/notes/english/Frontiers/index.md
docs/essays/notes/english/Frontiers/01-why-centralized-empires-expand-differently.md
docs/essays/notes/english/Frontiers/02-why-the-hexi-corridor-mattered-more-than-conquest.md
docs/essays/notes/english/Frontiers/03-why-indian-muslims-became-part-of-southeast-asian-culture.md
docs/essays/notes/english/Frontiers/04-why-china-did-not-become-the-civilizational-ground-of-southeast-asia.md
docs/essays/notes/english/Frontiers/05-why-ancient-china-rarely-produced-european-style-frontier-warlords-and-colonial-groups.md
docs/essays/notes/english/Frontiers/06-why-ancient-china-did-not-produce-venetian-style-maritime-republics.md
docs/essays/notes/english/Frontiers/07-why-zheng-hes-voyages-did-not-become-a-chinese-age-of-discovery.md
docs/essays/notes/english/Frontiers/08-why-chinese-merchants-did-not-build-an-east-india-company.md
docs/essays/notes/english/Frontiers/09-why-africa-has-not-become-a-complete-copy-of-any-external-civilization.md
docs/essays/notes/english/Frontiers/10-why-no-civilization-can-turn-the-whole-world-into-its-own-replica.md
docs/essays/notes/english/Frontiers/11-why-a-civilization-cannot-treat-its-own-survival-mode-as-the-worlds-answer.md
```

Display label:

```text
Frontiers
```

---

## 7. English Series: Architecture of Production

Folder:

```text
docs/essays/notes/english/Architecture/
```

Files:

```text
docs/essays/notes/english/Architecture/index.md
docs/essays/notes/english/Architecture/01-infrastructure-alone-does-not-create-industrialization.md
docs/essays/notes/english/Architecture/02-production-is-not-just-output.md
docs/essays/notes/english/Architecture/03-the-problem-of-absorptive-capacity.md
docs/essays/notes/english/Architecture/04-why-external-capital-cannot-build-a-production-system.md
docs/essays/notes/english/Architecture/05-states-are-not-consumption-machines.md
docs/essays/notes/english/Architecture/06-the-boundary-of-production.md
docs/essays/notes/english/Architecture/07-why-the-global-south-is-not-the-next-china.md
docs/essays/notes/english/Architecture/08-industrialization-requires-social-reproduction.md
docs/essays/notes/english/Architecture/09-civilization-is-not-just-culture.md
docs/essays/notes/english/Architecture/10-globalization-and-the-limits-of-value-capture.md
docs/essays/notes/english/Architecture/11-why-production-systems-cannot-be-imported.md
```

Display label:

```text
Architecture of Production
```

---

## 8. English Series: Boundaries of Development

Folder:

```text
docs/essays/notes/english/Development/
```

Files:

```text
docs/essays/notes/english/Development/index.md
docs/essays/notes/english/Development/01-why-africa-is-hard-to-industrialize.md
docs/essays/notes/english/Development/02-why-infrastructure-loans-do-not-create-production-systems.md
docs/essays/notes/english/Development/03-why-industrial-parks-remain-empty.md
docs/essays/notes/english/Development/04-why-cheap-labor-is-not-enough.md
docs/essays/notes/english/Development/05-why-foreign-investment-does-not-automatically-create-capability.md
docs/essays/notes/english/Development/06-why-resource-wealth-does-not-create-industrialization.md
docs/essays/notes/english/Development/07-why-global-supply-chains-do-not-create-national-production.md
docs/essays/notes/english/Development/08-the-productive-imperative.md
docs/essays/notes/english/Development/09-why-the-global-south-cannot-copy-china.md
docs/essays/notes/english/Development/10-why-aid-cannot-substitute-for-state-capacity.md
docs/essays/notes/english/Development/11-why-production-is-a-system-not-a-project.md
```

Display label:

```text
Boundaries of Development
```

---

## 9. English Series: Value Capture

Folder:

```text
docs/essays/notes/english/Value-Capture/
```

Files:

```text
docs/essays/notes/english/Value-Capture/index.md
docs/essays/notes/english/Value-Capture/01-why-producing-more-does-not-mean-earning-more.md
docs/essays/notes/english/Value-Capture/02-why-value-is-captured-at-the-interface.md
docs/essays/notes/english/Value-Capture/03-why-pricing-power-matters-more-than-output.md
docs/essays/notes/english/Value-Capture/04-why-finance-can-command-production-without-owning-it.md
docs/essays/notes/english/Value-Capture/05-why-standards-become-invisible-infrastructure.md
docs/essays/notes/english/Value-Capture/06-why-platforms-capture-markets-without-bearing-production.md
docs/essays/notes/english/Value-Capture/07-why-brands-turn-production-into-hierarchy.md
docs/essays/notes/english/Value-Capture/08-why-legal-systems-and-compliance-shape-global-value.md
docs/essays/notes/english/Value-Capture/09-why-reserve-currencies-are-civilizational-interfaces.md
docs/essays/notes/english/Value-Capture/10-why-mature-markets-defend-value-capture.md
docs/essays/notes/english/Value-Capture/11-why-the-global-rentier-system-faces-a-production-shock.md
```

Display label:

```text
Value Capture
```

---

## 10. English Series: China and Production Burden

Folder:

```text
docs/essays/notes/english/China-Burden-Production/
```

Files:

```text
docs/essays/notes/english/China-Burden-Production/index.md
docs/essays/notes/english/China-Burden-Production/01-why-china-is-not-just-the-worlds-factory.md
docs/essays/notes/english/China-Burden-Production/02-why-production-becomes-a-social-burden.md
docs/essays/notes/english/China-Burden-Production/03-why-infrastructure-is-part-of-chinas-industrial-system.md
docs/essays/notes/english/China-Burden-Production/04-why-employment-makes-production-political.md
docs/essays/notes/english/China-Burden-Production/05-why-supply-chains-become-national-operating-systems.md
docs/essays/notes/english/China-Burden-Production/06-why-local-governments-carry-industrial-pressure.md
docs/essays/notes/english/China-Burden-Production/07-why-exports-cannot-fully-solve-chinas-internal-pressure.md
docs/essays/notes/english/China-Burden-Production/08-why-domestic-demand-is-harder-than-it-looks.md
docs/essays/notes/english/China-Burden-Production/09-why-china-cannot-simply-abandon-production.md
docs/essays/notes/english/China-Burden-Production/10-why-chinas-industrial-strength-also-creates-constraint.md
docs/essays/notes/english/China-Burden-Production/11-why-the-burden-of-production-forces-institutional-change.md
```

Display label:

```text
China and Production Burden
```

---

## 11. English Series: Technology Amplifier

Folder:

```text
docs/essays/notes/english/Technology-Amplifier/
```

Files:

```text
docs/essays/notes/english/Technology-Amplifier/index.md
docs/essays/notes/english/Technology-Amplifier/01-why-technology-does-not-replace-structure.md
docs/essays/notes/english/Technology-Amplifier/02-why-ai-amplifies-existing-capacity.md
docs/essays/notes/english/Technology-Amplifier/03-why-data-is-not-power-without-organization.md
docs/essays/notes/english/Technology-Amplifier/04-why-automation-rewards-production-systems.md
docs/essays/notes/english/Technology-Amplifier/05-why-platforms-gain-more-from-ai-than-isolated-firms.md
docs/essays/notes/english/Technology-Amplifier/06-why-finance-uses-technology-to-price-the-future-faster.md
docs/essays/notes/english/Technology-Amplifier/07-why-states-with-execution-capacity-benefit-more-from-ai.md
docs/essays/notes/english/Technology-Amplifier/08-why-weak-systems-become-more-fragile-under-advanced-technology.md
docs/essays/notes/english/Technology-Amplifier/09-why-ai-changes-labor-without-ending-production.md
docs/essays/notes/english/Technology-Amplifier/10-why-technological-power-depends-on-systemic-absorption.md
docs/essays/notes/english/Technology-Amplifier/11-why-the-ai-shock-is-really-a-structural-shock.md
```

Display label:

```text
Technology Amplifier
```

---

## 12. Chinese Layer

Folder:

```text
docs/essays/chinese/
```

### Chinese entrance and rules

```text
docs/essays/chinese/index.md
docs/essays/chinese/reading-rules.md
docs/essays/chinese/core-terms-chinese.md
```

These should be linked only under the Chinese navigation layer.

---

## 13. Chinese Reality

Folder:

```text
docs/essays/chinese/reality/
```

Files:

```text
docs/essays/chinese/reality/00.md
docs/essays/chinese/reality/01.md
docs/essays/chinese/reality/02.md
docs/essays/chinese/reality/03.md
docs/essays/chinese/reality/04.md
docs/essays/chinese/reality/05.md
docs/essays/chinese/reality/06.md
docs/essays/chinese/reality/07.md
docs/essays/chinese/reality/08.md
docs/essays/chinese/reality/09.md
docs/essays/chinese/reality/10.md
docs/essays/chinese/reality/11.md
```

Internal review bundle, not public navigation unless needed:

```text
docs/essays/chinese/reality/reality_full.md
```

---

## 14. Chinese Future Path

Folder:

```text
docs/essays/chinese/future/
```

Files:

```text
docs/essays/chinese/future/00.md
docs/essays/chinese/future/01.md
docs/essays/chinese/future/02.md
docs/essays/chinese/future/03.md
docs/essays/chinese/future/04.md
docs/essays/chinese/future/05.md
docs/essays/chinese/future/06.md
docs/essays/chinese/future/07.md
docs/essays/chinese/future/08.md
docs/essays/chinese/future/09.md
docs/essays/chinese/future/10.md
```

Internal review bundle, not public navigation unless needed:

```text
docs/essays/chinese/future/future_full.md
```

---

## 15. Chinese Notes Layer

If Chinese notes remain under:

```text
docs/essays/notes/chinese/
```

then keep them there temporarily.

If reorganizing fully, move them to:

```text
docs/essays/chinese/notes/
```

Recommended final path:

```text
docs/essays/chinese/notes/
```

### Chinese Notes: Boundary of Expansion

Recommended final folder:

```text
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/
```

Files:

```text
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/01-indian-muslims-in-southeast-asia.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/02-southeast-asia-civilization-base.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/03-hexi-corridor.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/04-border-warlords-and-colonial-groups.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/05-maritime-merchant-republics.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/06-zheng-he-and-age-of-discovery.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/07-chinese-merchants-and-east-india-company.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/08-africa-and-civilization-replication.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/09-why-no-civilization-can-copy-the-world.md
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/10-civilization-boundary-and-working-civilization.md
```

Internal review bundle:

```text
docs/essays/chinese/notes/civilizational-expansion/boundary-of-expansion/_build/扩张的边界-合订本.md
```

### Chinese Notes: Baseline-Support Civilization

Recommended final folder:

```text
docs/essays/chinese/notes/doudi-civilization/
```

Files:

```text
docs/essays/chinese/notes/doudi-civilization/01-not-city-state-civilization.md
docs/essays/chinese/notes/doudi-civilization/02-myths-of-governance.md
docs/essays/chinese/notes/doudi-civilization/03-flood-control-and-state-capacity.md
docs/essays/chinese/notes/doudi-civilization/04-spring-autumn-warring-states-selection.md
docs/essays/chinese/notes/doudi-civilization/05-qin-system-as-organization-machine.md
docs/essays/chinese/notes/doudi-civilization/06-decline-of-aristocratic-clans.md
docs/essays/chinese/notes/doudi-civilization/07-why-central-state-suppresses-local-military-power.md
docs/essays/chinese/notes/doudi-civilization/08-why-chinese-dynasties-are-fallback-civilizations.md
docs/essays/chinese/notes/doudi-civilization/09-why-the-west-could-muddle-through.md
docs/essays/chinese/notes/doudi-civilization/10-great-unification-as-ultimate-order.md
```

Internal review bundle:

```text
docs/essays/chinese/notes/doudi-civilization/兜底文明｜合订本.md
```

### Chinese Notes: Boundary of Production

Recommended final folder:

```text
docs/essays/chinese/notes/production-boundary/
```

Files:

```text
docs/essays/chinese/notes/production-boundary/01-roads-do-not-equal-industrialization.md
docs/essays/chinese/notes/production-boundary/02-factories-do-not-equal-manufacturing-system.md
docs/essays/chinese/notes/production-boundary/03-electricity-does-not-equal-industrial-capacity.md
docs/essays/chinese/notes/production-boundary/04-population-does-not-equal-market.md
docs/essays/chinese/notes/production-boundary/05-resource-rich-countries-and-industrialization.md
docs/essays/chinese/notes/production-boundary/06-industrial-parks-as-islands.md
docs/essays/chinese/notes/production-boundary/07-cheap-labor-does-not-equal-manufacturing-advantage.md
docs/essays/chinese/notes/production-boundary/08-industrial-transfer-is-harder-than-building-factories.md
docs/essays/chinese/notes/production-boundary/09-why-china-manufacturing-cannot-be-copied-by-supply-chains.md
docs/essays/chinese/notes/production-boundary/10-production-capacity-as-civilizational-capacity.md
```

Internal review bundle:

```text
docs/essays/chinese/notes/production-boundary/生产的边界｜合订本.md
```

---

## 16. Suggested Top-Level MkDocs Navigation

Use this high-level order:

```yaml
nav:
  - Home: index.md

  - Start Here:
      - Reader Map: essays/english/reader-map.md
      - Common Ground: essays/english/common-ground.md
      - Core Terms: essays/english/core-terms-eng.md

  - Framework:
      - Overview: essays/english/index.md
      - Productive Forces and Civilization: essays/english/geography-productive-forces-and-civilization.md
      - Civilizational Metabolism: essays/english/civilizational-metabolism.md
      - Absorptive Capacity: essays/english/absorptive-capacity.md
      - Surplus, Absorption, and Reproduction: essays/english/surplus-absorption-and-reproduction.md
      # - The Western System: essays/english/western-system.md

  - Series:
      - Frontiers: essays/notes/english/Frontiers/index.md
      - Architecture of Production: essays/notes/english/Architecture/index.md
      - Boundaries of Development: essays/notes/english/Development/index.md
      - Value Capture: essays/notes/english/Value-Capture/index.md
      - China and Production Burden: essays/notes/english/China-Burden-Production/index.md
      - Technology Amplifier: essays/notes/english/Technology-Amplifier/index.md

  - Archive:
      - Author: author.md
      - Copyright: copyright.md

  - 中文:
      - 中文入口: essays/chinese/index.md
      - 中文核心术语: essays/chinese/core-terms-chinese.md
      - 阅读规则: essays/chinese/reading-rules.md
```

---

## 17. Legacy / History Folder

Recommended folder:

```text
docs/history/
```

Use it for old pages that should not remain in public navigation but may be preserved for version traceability.

Possible files:

```text
docs/history/core-terms-legacy-2026-07.md
docs/history/index-legacy-2026-07.md
docs/history/common-ground-legacy-2026-07.md
```

Do not include `docs/history/` in public navigation unless needed.

---

## 18. Update Procedure

When adding a file:

1. Add the physical file.
2. Add the path to this file map.
3. Add or adjust internal links.
4. Add to `mkdocs.yml` only if it should appear in navigation.
5. Run:

```bash
mkdocs build
```

When deleting or moving a file:

1. Move with `git mv` when possible.
2. Update this file map.
3. Search for old links.
4. Update `mkdocs.yml`.
5. Run:

```bash
mkdocs build
```

---

## 19. Current Strategic Structure

```text
English public shell:
  docs/index.md
  docs/essays/english/
  docs/essays/notes/english/

Chinese mother-language layer:
  docs/essays/chinese/

Legacy / history:
  docs/history/
```

Core idea:

```text
English = public framework, search entrance, international reference
Chinese = mother-language layer, deeper concepts, original theoretical root
History = old versions, not public navigation
```
