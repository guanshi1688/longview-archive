# file_map.md｜Longview Archive File Structure Map

**Status:** updated from current `mkdocs.yml` snapshot.  
**Purpose:** this file is the canonical path reference for the `docs/` folder and future `mkdocs.yml` updates.

When files are added, deleted, renamed, or moved under `docs/`, update this file first.  
Then update `mkdocs.yml`.

---

## 0. Current MkDocs Snapshot

Current site name in uploaded yml:

```text
Longview Archive 0002
```

Before final public push, remove any temporary test suffix such as `0002`.

Current theme features:

```yaml
features:
  - navigation.path
  - navigation.top
  - search.highlight
```

Current excluded docs:

```yaml
exclude_docs: |
  file_map.md
```

Current extra CSS:

```yaml
extra_css:
  - stylesheets/extra.css
```

Current top-level navigation:

```text
Home
Start Here
Framework
Series
Archive
中文
```

---

## 1. Naming Rules

Use lowercase folder names.

Use stable English file names for English public files.

Use Chinese titles in article content and navigation labels, not in file names, except legacy bundle files that already exist.

Recommended rule:

```text
folder-name/
file-name.md
```

Avoid creating too many `index.md` files unless the file is truly a directory landing page.

---

## 2. Root-Level Docs

Files under:

```text
docs/
```

Keep:

```text
docs/index.md
docs/author.md
docs/copyright.md
docs/robots.txt
docs/sitemap.xml
docs/assets/
docs/stylesheets/
docs/essays/
docs/file_map.md
```

`docs/file_map.md` should remain excluded from MkDocs build:

```yaml
exclude_docs: |
  file_map.md
```

If `docs/core-terms.md` still exists, archive or delete it after confirming no links point to it. The active Core Terms pages are now split:

```text
docs/essays/english/core-terms-eng.md
docs/essays/chinese/core-terms-chinese.md
```

---

## 3. History / Legacy Files

Recommended final location:

```text
history/
```

at repository root, not under `docs/`.

Reason: files under `docs/` may still be built and become publicly accessible unless explicitly excluded.

Suggested legacy files:

```text
history/index-root-chinese-legacy-2026-07.md
history/core-terms-legacy-2026-07.md
history/common-ground-legacy-2026-07.md
```

If you keep legacy files under `docs/history/`, add an explicit exclusion rule.

---

## 4. Private / Local Drafts

Do not put private drafts, final unpublished manifestos, or internal total outlines inside public `docs/`.

Recommended private location outside public docs:

```text
private/
private/western-system/the-war-against-circulation.md
private/western-system/market-scorched-earth.md
```

These files should not appear in `mkdocs.yml`.

---

## 5. Current Navigation Paths

This section mirrors the uploaded `mkdocs.yml`.

### Home

```text
index.md
```

### Start Here

```text
essays/english/reader-map.md
essays/english/common-ground.md
essays/english/core-terms-eng.md
```

### Framework

Current paths:

```text
essays/english/index.md
essays/english/geography-productive-forces-and-civilization.md
essays/english/civilizational-metabolism.md
essays/english/absorptive-capacity.md
essays/english/surplus-absorption-and-reproduction.md
essays/english/western-system.md
```

Current display label for the Western System essay:

```text
Value Capture and the Western System
```

If the file is renamed according to the latest naming decision, update both this file map and `mkdocs.yml`:

```text
essays/english/production-value-capture-western-system.md
```

### Series

The English series remain under:

```text
docs/essays/notes/english/
```

They are public series, not private notes.

### Archive

Current paths:

```text
versions.md
author.md
copyright.md
```

Confirm `docs/versions.md` physically exists.  
If it does not exist, either create it or remove `Version Records` from `mkdocs.yml`.

### 中文

Current Chinese layer paths:

```text
essays/chinese/index.md
essays/chinese/core-terms-chinese.md
essays/chinese/reading-rules.md
essays/chinese/reality/
essays/chinese/future/
essays/notes/chinese/
```

Chinese notes currently remain under:

```text
docs/essays/notes/chinese/
```

Do not change this path unless you also move the files and update `mkdocs.yml`.

---

## 6. Current Full Nav Listing

## Start Here

- `Start Here / Reader Map` → `essays/english/reader-map.md`
- `Start Here / Common Ground` → `essays/english/common-ground.md`
- `Start Here / Core Terms` → `essays/english/core-terms-eng.md`
## Framework

- `Framework / Framework Overview` → `essays/english/index.md`
- `Framework / Productive Forces and Civilization` → `essays/english/geography-productive-forces-and-civilization.md`
- `Framework / Civilizational Metabolism` → `essays/english/civilizational-metabolism.md`
- `Framework / Absorptive Capacity` → `essays/english/absorptive-capacity.md`
- `Framework / Surplus, Absorption, and Reproduction` → `essays/english/surplus-absorption-and-reproduction.md`
- `Framework / Value Capture and the Western System` → `essays/english/western-system.md`
## Series

- `Series / Frontiers / Overview` → `essays/notes/english/Frontiers/index.md`
- `Series / Frontiers / 01. Why Centralized Empires Expand Differently` → `essays/notes/english/Frontiers/01-why-centralized-empires-expand-differently.md`
- `Series / Frontiers / 02. Why the Hexi Corridor Mattered More Than Conquest` → `essays/notes/english/Frontiers/02-why-the-hexi-corridor-mattered-more-than-conquest.md`
- `Series / Frontiers / 03. Why Indian Muslims Became Part of Southeast Asian Culture` → `essays/notes/english/Frontiers/03-why-indian-muslims-became-part-of-southeast-asian-culture.md`
- `Series / Frontiers / 04. Why China Did Not Become the Civilizational Ground of Southeast Asia` → `essays/notes/english/Frontiers/04-why-china-did-not-become-the-civilizational-ground-of-southeast-asia.md`
- `Series / Frontiers / 05. Why Ancient China Rarely Produced European-Style Frontier Warlords and Colonial Groups` → `essays/notes/english/Frontiers/05-why-ancient-china-rarely-produced-european-style-frontier-warlords-and-colonial-groups.md`
- `Series / Frontiers / 06. Why Ancient China Did Not Produce Venetian-Style Maritime Republics` → `essays/notes/english/Frontiers/06-why-ancient-china-did-not-produce-venetian-style-maritime-republics.md`
- `Series / Frontiers / 07. Why Zheng He’s Voyages Did Not Become a Chinese Age of Discovery` → `essays/notes/english/Frontiers/07-why-zheng-hes-voyages-did-not-become-a-chinese-age-of-discovery.md`
- `Series / Frontiers / 08. Why Chinese Merchants Did Not Build an East India Company` → `essays/notes/english/Frontiers/08-why-chinese-merchants-did-not-build-an-east-india-company.md`
- `Series / Frontiers / 09. Why Africa Has Not Become a Complete Copy of Any External Civilization` → `essays/notes/english/Frontiers/09-why-africa-has-not-become-a-complete-copy-of-any-external-civilization.md`
- `Series / Frontiers / 10. Why No Civilization Can Turn the Whole World Into Its Own Replica` → `essays/notes/english/Frontiers/10-why-no-civilization-can-turn-the-whole-world-into-its-own-replica.md`
- `Series / Frontiers / 11. Why a Civilization Cannot Treat Its Own Survival Mode as the World’s Answer` → `essays/notes/english/Frontiers/11-why-a-civilization-cannot-treat-its-own-survival-mode-as-the-worlds-answer.md`
- `Series / Architecture of Production / Overview` → `essays/notes/english/Architecture/index.md`
- `Series / Architecture of Production / 01. Why Infrastructure Alone Does Not Create Industrialization` → `essays/notes/english/Architecture/01-infrastructure-alone-does-not-create-industrialization.md`
- `Series / Architecture of Production / 02. Production Is Not Just Output` → `essays/notes/english/Architecture/02-production-is-not-just-output.md`
- `Series / Architecture of Production / 03. The Problem of Absorptive Capacity` → `essays/notes/english/Architecture/03-the-problem-of-absorptive-capacity.md`
- `Series / Architecture of Production / 04. Why External Capital Cannot Build a Production System` → `essays/notes/english/Architecture/04-why-external-capital-cannot-build-a-production-system.md`
- `Series / Architecture of Production / 05. States Are Not Consumption Machines` → `essays/notes/english/Architecture/05-states-are-not-consumption-machines.md`
- `Series / Architecture of Production / 06. The Boundary of Production` → `essays/notes/english/Architecture/06-the-boundary-of-production.md`
- `Series / Architecture of Production / 07. Why the Global South Is Not the Next China` → `essays/notes/english/Architecture/07-why-the-global-south-is-not-the-next-china.md`
- `Series / Architecture of Production / 08. Industrialization Requires Social Reproduction` → `essays/notes/english/Architecture/08-industrialization-requires-social-reproduction.md`
- `Series / Architecture of Production / 09. Civilization Is Not Just Culture` → `essays/notes/english/Architecture/09-civilization-is-not-just-culture.md`
- `Series / Architecture of Production / 10. Globalization and the Limits of Value Capture` → `essays/notes/english/Architecture/10-globalization-and-the-limits-of-value-capture.md`
- `Series / Architecture of Production / 11. Why Production Systems Cannot Be Imported` → `essays/notes/english/Architecture/11-why-production-systems-cannot-be-imported.md`
- `Series / Boundaries of Development / Overview` → `essays/notes/english/Development/index.md`
- `Series / Boundaries of Development / 01. Why Africa Is Hard to Industrialize` → `essays/notes/english/Development/01-why-africa-is-hard-to-industrialize.md`
- `Series / Boundaries of Development / 02. Why Infrastructure Loans Do Not Create Production Systems` → `essays/notes/english/Development/02-why-infrastructure-loans-do-not-create-production-systems.md`
- `Series / Boundaries of Development / 03. Why Industrial Parks Remain Empty` → `essays/notes/english/Development/03-why-industrial-parks-remain-empty.md`
- `Series / Boundaries of Development / 04. Why Cheap Labor Is Not Enough` → `essays/notes/english/Development/04-why-cheap-labor-is-not-enough.md`
- `Series / Boundaries of Development / 05. Why Foreign Investment Does Not Automatically Create Capability` → `essays/notes/english/Development/05-why-foreign-investment-does-not-automatically-create-capability.md`
- `Series / Boundaries of Development / 06. Why Resource Wealth Does Not Create Industrialization` → `essays/notes/english/Development/06-why-resource-wealth-does-not-create-industrialization.md`
- `Series / Boundaries of Development / 07. Why Global Supply Chains Do Not Create National Production` → `essays/notes/english/Development/07-why-global-supply-chains-do-not-create-national-production.md`
- `Series / Boundaries of Development / 08. The Productive Imperative` → `essays/notes/english/Development/08-the-productive-imperative.md`
- `Series / Boundaries of Development / 09. Why the Global South Cannot Copy China` → `essays/notes/english/Development/09-why-the-global-south-cannot-copy-china.md`
- `Series / Boundaries of Development / 10. Why Aid Cannot Substitute for State Capacity` → `essays/notes/english/Development/10-why-aid-cannot-substitute-for-state-capacity.md`
- `Series / Boundaries of Development / 11. Why Production Is a System, Not a Project` → `essays/notes/english/Development/11-why-production-is-a-system-not-a-project.md`
- `Series / Value Capture / Overview` → `essays/notes/english/Value-Capture/index.md`
- `Series / Value Capture / 01. Why Producing More Does Not Mean Earning More` → `essays/notes/english/Value-Capture/01-why-producing-more-does-not-mean-earning-more.md`
- `Series / Value Capture / 02. Why Value Is Captured at the Interface` → `essays/notes/english/Value-Capture/02-why-value-is-captured-at-the-interface.md`
- `Series / Value Capture / 03. Why Pricing Power Matters More Than Output` → `essays/notes/english/Value-Capture/03-why-pricing-power-matters-more-than-output.md`
- `Series / Value Capture / 04. Why Finance Can Command Production Without Owning It` → `essays/notes/english/Value-Capture/04-why-finance-can-command-production-without-owning-it.md`
- `Series / Value Capture / 05. Why Standards Become Invisible Infrastructure` → `essays/notes/english/Value-Capture/05-why-standards-become-invisible-infrastructure.md`
- `Series / Value Capture / 06. Why Platforms Capture Markets Without Bearing Production` → `essays/notes/english/Value-Capture/06-why-platforms-capture-markets-without-bearing-production.md`
- `Series / Value Capture / 07. Why Brands Turn Production into Hierarchy` → `essays/notes/english/Value-Capture/07-why-brands-turn-production-into-hierarchy.md`
- `Series / Value Capture / 08. Why Legal Systems and Compliance Shape Global Value` → `essays/notes/english/Value-Capture/08-why-legal-systems-and-compliance-shape-global-value.md`
- `Series / Value Capture / 09. Why Reserve Currencies Are Civilizational Interfaces` → `essays/notes/english/Value-Capture/09-why-reserve-currencies-are-civilizational-interfaces.md`
- `Series / Value Capture / 10. Why Mature Markets Defend Value Capture` → `essays/notes/english/Value-Capture/10-why-mature-markets-defend-value-capture.md`
- `Series / Value Capture / 11. Why the Global Rentier System Faces a Production Shock` → `essays/notes/english/Value-Capture/11-why-the-global-rentier-system-faces-a-production-shock.md`
- `Series / China and Production Burden / Overview` → `essays/notes/english/China-Burden-Production/index.md`
- `Series / China and Production Burden / 01. Why China Is Not Just the World’s Factory` → `essays/notes/english/China-Burden-Production/01-why-china-is-not-just-the-worlds-factory.md`
- `Series / China and Production Burden / 02. Why Production Becomes a Social Burden` → `essays/notes/english/China-Burden-Production/02-why-production-becomes-a-social-burden.md`
- `Series / China and Production Burden / 03. Why Infrastructure Is Part of China’s Industrial System` → `essays/notes/english/China-Burden-Production/03-why-infrastructure-is-part-of-chinas-industrial-system.md`
- `Series / China and Production Burden / 04. Why Employment Makes Production Political` → `essays/notes/english/China-Burden-Production/04-why-employment-makes-production-political.md`
- `Series / China and Production Burden / 05. Why Supply Chains Become National Operating Systems` → `essays/notes/english/China-Burden-Production/05-why-supply-chains-become-national-operating-systems.md`
- `Series / China and Production Burden / 06. Why Local Governments Carry Industrial Pressure` → `essays/notes/english/China-Burden-Production/06-why-local-governments-carry-industrial-pressure.md`
- `Series / China and Production Burden / 07. Why Exports Cannot Fully Solve China’s Internal Pressure` → `essays/notes/english/China-Burden-Production/07-why-exports-cannot-fully-solve-chinas-internal-pressure.md`
- `Series / China and Production Burden / 08. Why Domestic Demand Is Harder Than It Looks` → `essays/notes/english/China-Burden-Production/08-why-domestic-demand-is-harder-than-it-looks.md`
- `Series / China and Production Burden / 09. Why China Cannot Simply Abandon Production` → `essays/notes/english/China-Burden-Production/09-why-china-cannot-simply-abandon-production.md`
- `Series / China and Production Burden / 10. Why China’s Industrial Strength Also Creates Constraint` → `essays/notes/english/China-Burden-Production/10-why-chinas-industrial-strength-also-creates-constraint.md`
- `Series / China and Production Burden / 11. Why the Burden of Production Forces Institutional Change` → `essays/notes/english/China-Burden-Production/11-why-the-burden-of-production-forces-institutional-change.md`
- `Series / Technology Amplifier / Overview` → `essays/notes/english/Technology-Amplifier/index.md`
- `Series / Technology Amplifier / 01. Why Technology Does Not Replace Structure` → `essays/notes/english/Technology-Amplifier/01-why-technology-does-not-replace-structure.md`
- `Series / Technology Amplifier / 02. Why AI Amplifies Existing Capacity` → `essays/notes/english/Technology-Amplifier/02-why-ai-amplifies-existing-capacity.md`
- `Series / Technology Amplifier / 03. Why Data Is Not Power Without Organization` → `essays/notes/english/Technology-Amplifier/03-why-data-is-not-power-without-organization.md`
- `Series / Technology Amplifier / 04. Why Automation Rewards Production Systems` → `essays/notes/english/Technology-Amplifier/04-why-automation-rewards-production-systems.md`
- `Series / Technology Amplifier / 05. Why Platforms Gain More From AI Than Isolated Firms` → `essays/notes/english/Technology-Amplifier/05-why-platforms-gain-more-from-ai-than-isolated-firms.md`
- `Series / Technology Amplifier / 06. Why Finance Uses Technology to Price the Future Faster` → `essays/notes/english/Technology-Amplifier/06-why-finance-uses-technology-to-price-the-future-faster.md`
- `Series / Technology Amplifier / 07. Why States With Execution Capacity Benefit More From AI` → `essays/notes/english/Technology-Amplifier/07-why-states-with-execution-capacity-benefit-more-from-ai.md`
- `Series / Technology Amplifier / 08. Why Weak Systems Become More Fragile Under Advanced Technology` → `essays/notes/english/Technology-Amplifier/08-why-weak-systems-become-more-fragile-under-advanced-technology.md`
- `Series / Technology Amplifier / 09. Why AI Changes Labor Without Ending Production` → `essays/notes/english/Technology-Amplifier/09-why-ai-changes-labor-without-ending-production.md`
- `Series / Technology Amplifier / 10. Why Technological Power Depends on Systemic Absorption` → `essays/notes/english/Technology-Amplifier/10-why-technological-power-depends-on-systemic-absorption.md`
- `Series / Technology Amplifier / 11. Why the AI Shock Is Really a Structural Shock` → `essays/notes/english/Technology-Amplifier/11-why-the-ai-shock-is-really-a-structural-shock.md`
## Archive

- `Archive / Version Records` → `versions.md`
- `Archive / Author` → `author.md`
- `Archive / Copyright` → `copyright.md`
## 中文

- `中文 / 中文总览` → `essays/chinese/index.md`
- `中文 / 核心术语` → `essays/chinese/core-terms-chinese.md`
- `中文 / 阅读规则` → `essays/chinese/reading-rules.md`
- `中文 / Reality｜现实世界 / 阅读前约束` → `essays/chinese/reality/00.md`
- `中文 / Reality｜现实世界 / 01｜人类文明的三种底层模式` → `essays/chinese/reality/01.md`
- `中文 / Reality｜现实世界 / 02｜中国制度不是消费机器，而是做功机器` → `essays/chinese/reality/02.md`
- `中文 / Reality｜现实世界 / 03｜全球南方不是第二个中国` → `essays/chinese/reality/03.md`
- `中文 / Reality｜现实世界 / 04｜中国不能把自己的生存方式当作世界答案` → `essays/chinese/reality/04.md`
- `中文 / Reality｜现实世界 / 05｜成熟市场为什么不愿承接中国工业 2.0` → `essays/chinese/reality/05.md`
- `中文 / Reality｜现实世界 / 06｜不限制生产，只限制变现` → `essays/chinese/reality/06.md`
- `中文 / Reality｜现实世界 / 07｜真正的市场战，不是打工厂，而是打变现` → `essays/chinese/reality/07.md`
- `中文 / Reality｜现实世界 / 08｜旧闭环正在退潮` → `essays/chinese/reality/08s.md`
- `中文 / Reality｜现实世界 / 09｜内部闭环的压力` → `essays/chinese/reality/09.md`
- `中文 / Reality｜现实世界 / 10｜文明战略转型` → `essays/chinese/reality/10.md`
- `中文 / Reality｜现实世界 / 阅读后约束` → `essays/chinese/reality/11.md`
- `中文 / Future Path｜未来之路 / 阅读前约束` → `essays/chinese/future/00.md`
- `中文 / Future Path｜未来之路 / 01｜生产富余不是危机，而是入口` → `essays/chinese/future/01.md`
- `中文 / Future Path｜未来之路 / 02｜组织富余` → `essays/chinese/future/02.md`
- `中文 / Future Path｜未来之路 / 03｜新闭环的必要性` → `essays/chinese/future/03.md`
- `中文 / Future Path｜未来之路 / 04｜从外部变现转向内部承接` → `essays/chinese/future/04.md`
- `中文 / Future Path｜未来之路 / 05｜生产力如何重塑社会关系` → `essays/chinese/future/05.md`
- `中文 / Future Path｜未来之路 / 06｜新的分配与承接结构` → `essays/chinese/future/06.md`
- `中文 / Future Path｜未来之路 / 07｜技术不是终点，而是放大器` → `essays/chinese/future/07.md`
- `中文 / Future Path｜未来之路 / 08｜文明闭环` → `essays/chinese/future/08.md`
- `中文 / Future Path｜未来之路 / 09｜未来之路的边界` → `essays/chinese/future/09.md`
- `中文 / Future Path｜未来之路 / 10｜阅读后约束` → `essays/chinese/future/10.md`
- `中文 / 中文札记 / 扩张的边界 / 01｜为什么印度穆斯林能够成为东南亚文化的一部分？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/01-indian-muslims-in-southeast-asia.md`
- `中文 / 中文札记 / 扩张的边界 / 02｜雄踞东亚两千年的中原王朝，为什么始终没有成为东南亚的文明底色？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/02-southeast-asia-civilization-base.md`
- `中文 / 中文札记 / 扩张的边界 / 03｜中原文明最大规模的结构性扩张，为什么是河西走廊，而不是漠北或越南北部？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/03-hexi-corridor.md`
- `中文 / 中文札记 / 扩张的边界 / 04｜为什么中国古代很少出现欧洲式边境军阀和殖民集团自发扩张？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/04-border-warlords-and-colonial-groups.md`
- `中文 / 中文札记 / 扩张的边界 / 05｜为什么中国古代没有出现威尼斯式海商共和国？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/05-maritime-merchant-republics.md`
- `中文 / 中文札记 / 扩张的边界 / 06｜为什么郑和下西洋没有变成中国版大航海时代？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/06-zheng-he-and-age-of-discovery.md`
- `中文 / 中文札记 / 扩张的边界 / 07｜为什么中国商人遍布东南亚，却没有建立东印度公司式殖民帝国？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/07-chinese-merchants-and-east-india-company.md`
- `中文 / 中文札记 / 扩张的边界 / 08｜为什么非洲至今没有成为任何外来文明的完整复制品？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/08-africa-and-civilization-replication.md`
- `中文 / 中文札记 / 扩张的边界 / 09｜为什么没有一种文明能把整个世界变成自己的复制品？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/09-why-no-civilization-can-copy-the-world.md`
- `中文 / 中文札记 / 扩张的边界 / 10｜文明为什么不能把自己的生存方式当作世界答案？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/10-civilization-boundary-and-working-civilization.md`
- `中文 / 中文札记 / 兜底文明 / 01｜为什么中国文明从一开始就不是城邦文明？` → `essays/notes/chinese/doudi-civilization/01-not-city-state-civilization.md`
- `中文 / 中文札记 / 兜底文明 / 02｜为什么三皇五帝神话的核心，不是神权，而是治世？` → `essays/notes/chinese/doudi-civilization/02-myths-of-governance.md`
- `中文 / 中文札记 / 兜底文明 / 03｜为什么治水是中原文明最早的国家能力原型？` → `essays/notes/chinese/doudi-civilization/03-flood-control-and-state-capacity.md`
- `中文 / 中文札记 / 兜底文明 / 04｜为什么春秋战国五百年血雨，最终没有走向欧洲式封建均势？` → `essays/notes/chinese/doudi-civilization/04-spring-autumn-warring-states-selection.md`
- `中文 / 中文札记 / 兜底文明 / 05｜为什么秦制不是偶然暴政，而是战争时代筛选出的组织机器？` → `essays/notes/chinese/doudi-civilization/05-qin-system-as-organization-machine.md`
- `中文 / 中文札记 / 兜底文明 / 06｜为什么中国世家大族的衰亡具有历史必然性？` → `essays/notes/chinese/doudi-civilization/06-decline-of-aristocratic-clans.md`
- `中文 / 中文札记 / 兜底文明 / 07｜为什么中国王朝必须压制地方军政集团？` → `essays/notes/chinese/doudi-civilization/07-why-central-state-suppresses-local-military-power.md`
- `中文 / 中文札记 / 兜底文明 / 08｜为什么中国王朝是兜底文明，而不是契约文明？` → `essays/notes/chinese/doudi-civilization/08-why-chinese-dynasties-are-fallback-civilizations.md`
- `中文 / 中文札记 / 兜底文明 / 09｜为什么西方可以长期苟住，而中国王朝兜不住就会改朝换代？` → `essays/notes/chinese/doudi-civilization/09-why-the-west-could-muddle-through.md`
- `中文 / 中文札记 / 兜底文明 / 10｜大一统的极限成就：为什么中国文明必须把天下做成秩序？` → `essays/notes/chinese/doudi-civilization/10-great-unification-as-ultimate-order.md`
- `中文 / 中文札记 / 生产的边界 / 01｜为什么修路不等于工业化？` → `essays/notes/chinese/production-boundary/01-roads-do-not-equal-industrialization.md`
- `中文 / 中文札记 / 生产的边界 / 02｜为什么建厂不等于制造业体系？` → `essays/notes/chinese/production-boundary/02-factories-do-not-equal-manufacturing-system.md`
- `中文 / 中文札记 / 生产的边界 / 03｜为什么通电不等于产业能力？` → `essays/notes/chinese/production-boundary/03-electricity-does-not-equal-industrial-capacity.md`
- `中文 / 中文札记 / 生产的边界 / 04｜为什么人口多不等于市场大？` → `essays/notes/chinese/production-boundary/04-population-does-not-equal-market.md`
- `中文 / 中文札记 / 生产的边界 / 05｜为什么资源丰富的国家反而更难工业化？` → `essays/notes/chinese/production-boundary/05-resource-rich-countries-and-industrialization.md`
- `中文 / 中文札记 / 生产的边界 / 06｜为什么工业园常常变成孤岛，而不是产业体系？` → `essays/notes/chinese/production-boundary/06-industrial-parks-as-islands.md`
- `中文 / 中文札记 / 生产的边界 / 07｜为什么廉价劳动力不等于制造业优势？` → `essays/notes/chinese/production-boundary/07-cheap-labor-does-not-equal-manufacturing-advantage.md`
- `中文 / 中文札记 / 生产的边界 / 08｜为什么承接产业转移，比建设工厂更难？` → `essays/notes/chinese/production-boundary/08-industrial-transfer-is-harder-than-building-factories.md`
- `中文 / 中文札记 / 生产的边界 / 09｜为什么中国制造业不是几条产业链就能复制？` → `essays/notes/chinese/production-boundary/09-why-china-manufacturing-cannot-be-copied-by-supply-chains.md`
- `中文 / 中文札记 / 生产的边界 / 10｜生产能力为什么是一种文明能力？` → `essays/notes/chinese/production-boundary/10-production-capacity-as-civilizational-capacity.md`
---

## 7. Duplicate Path Check

Duplicate paths found in current yml:

```text
None
```

If duplicate visual labels still appear in the sidebar, that is likely Material's section/index display behavior or CSS handling of nested `.md-nav__title`, not duplicate file paths.

---

## 8. Known Checks Before Commit

### 8.1 Temporary site name

Current uploaded yml uses:

```text
Longview Archive 0002
```

Before final push, change back to:

```text
Longview Archive
```

### 8.2 Reality 08 path

Current yml contains:

```text
essays/chinese/reality/08s.md
```

If the actual file is `08.md`, change it to:

```text
essays/chinese/reality/08.md
```

### 8.3 Western System filename

Current yml uses:

```text
essays/english/western-system.md
```

Recommended final public filename from latest naming decision:

```text
essays/english/production-value-capture-western-system.md
```

Use one of these consistently. Do not keep both unless one is a redirect/legacy copy.

### 8.4 Version Records

Current yml uses:

```text
versions.md
```

Confirm that `docs/versions.md` exists.

---

## 9. Update Procedure

When adding a file:

1. Add the physical file.
2. Update this `file_map.md`.
3. Update links inside related pages.
4. Add to `mkdocs.yml` only if it should appear in public navigation.
5. Run:

```bash
mkdocs build
```

When moving a file:

1. Use `git mv` when possible.
2. Update this `file_map.md`.
3. Search for old paths.
4. Update `mkdocs.yml`.
5. Run:

```bash
mkdocs build
```

---

## 10. Strategic Structure

```text
English public shell:
  docs/index.md
  docs/essays/english/
  docs/essays/notes/english/

Chinese mother-language layer:
  docs/essays/chinese/
  docs/essays/notes/chinese/

Archive:
  docs/author.md
  docs/copyright.md
  docs/versions.md

Private/local:
  private/

Legacy/history:
  history/
```

Core idea:

```text
English = public framework, search entrance, international reference
Chinese = mother-language layer, deeper concepts, original theoretical root
Private = unpublished total outlines and final strategic drafts
History = old versions, not public navigation
```
