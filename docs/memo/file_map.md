# file_map.md｜Longview Archive File Structure Map

**Status:** synchronized with `mkdocs.yml` on 2026-07-17.  
**Purpose:** canonical path reference, navigation map, and recovery memo for the entire Longview Archive mother archive.

When files are added, deleted, renamed, or moved under `docs/`, update this file first.  
Then update `mkdocs.yml`, internal links, and `sitemap.xml`.

---

## 0. Recovery Use

This file is designed to restore the project in a new conversation without rereading more than one hundred articles.

A new conversation should read, in this order:

1. **Section 1 — Project identity and publication layers**
2. **Section 2 — Current theoretical architecture**
3. **Section 3 — Current site snapshot**
4. **Section 6 — Current navigation tree**
5. The specific article or series relevant to the next task

The full archive is evidence and expansion. This file is the routing layer.

---

## 1. Project Identity and Publication Layers

```text
Project:
Longview Archive｜观势档案

Public domain:
https://longview-archive.org

Chinese author:
星衡｜Aster Vale

English author:
Evan Vale

Core sentence:
Everything begins with productive forces.
一切从生产力开始。
```

### Publication layers

```text
English public shell
→ international framework
→ search entrance
→ series archive
→ future think-tank and media submissions

Chinese mother-language layer
→ deeper conceptual root
→ Reality / Future Path
→ historical and structural notes

Private/local layer
→ unpublished total outlines
→ sharper strategic deductions
→ sensitive or unfinished system-level manuscripts

History layer
→ old versions and legacy files
→ never used as the current public source of truth
```

The public site is the standard edition, not the complete private theory.

---

## 2. Current Theoretical Architecture

### 2.1 First explanatory coordinate

The framework does not begin with conventional economics, political science, or international relations.

It begins with:

```text
Productive Forces
→ Production System
→ Absorptive Capacity
→ Productive Surplus
→ Value Capture
→ Social Reproduction
```

### 2.2 Three underlying civilizational modes

```text
Work-performing Civilization
Endowment-based Civilization
Global Rentier Civilization
```

These are survival and reproduction structures, not moral rankings.

### 2.3 Core terms

```text
Productive Forces
Production System
Absorptive Capacity
Productive Surplus
External Realization
Interface Power
Value Capture
Civilizational Metabolism
Responsibility Embedding
Disposable Future
```

### 2.4 Productive-Forces Economics

The formal Productive-Forces Economics sequence now exists in both English and Chinese.

Its current execution model is:

```text
Geographic and Survival Pressures
        ↓
Continental Production System
        ↓
Unified Responsibility and Systemic Absorption
        ↓
Responsibility Embedded in Micro-Level Nodes
        ↓
Household as Residual Risk Account
        ↓
Failure Boundary
        ↓
Consumer Formation
        ↓
Productive Surplus and Internal Absorption
        ↓
New Absorptive Loop
```

### 2.5 Horizontal civilizational axis

The current comparison model is not an upper/lower hierarchy.

```text
← Production / Responsibility / Embeddedness / Collective Continuity
                              |
                              |
Individual Settlement / Bounded Contract / Present Life →
```

Its three observable projections are:

```text
Subject:
Responsibility-Bearing Subject ←→ Atomic Individual

Relation:
Continuous Obligation ←→ Bounded Contract

Fiscal Structure:
Production-Node and Local Settlement ←→ Individual and Household Settlement
```

China has historically leaned toward the production-responsibility end.  
Mature Western systems have historically leaned toward the individual-settlement and bounded-contract end.

Neither is a fixed type. Both can move along the same structural axis.

### 2.6 Institutional restoring force

Civilizational position cannot be moved at will.

```text
Subject definition
+ contract boundaries
+ fiscal structure
+ household behavior
+ productive organization
= institutional restoring force
```

When one module moves alone, the others may pull the system back toward its inherited equilibrium.

Moving along the axis therefore means partially incorporating functions historically preserved by the opposite side, not copying the opposite civilization in full.

### 2.7 Reform logic

```text
Parameter Adjustment
→ Interface Rewrite
→ Module Replacement
→ System Reconfiguration
→ System Reset
```

Core boundary:

> When correction can remain modular, reform remains possible.  
> When modules begin reproducing one another’s failure, the system starts searching for a new initialization point.

Do not turn this into deterministic collapse prophecy. It is a failure-boundary model, not a guaranteed terminal forecast.

### 2.8 Current independent research branch

A new branch has emerged:

```text
Interface Network
→ Exit-capable Subject
→ Bounded Contract
→ Predictable Rules
→ Limited Sovereignty
→ Possible co-evolution with liberal and democratic institutions
```

Current boundary:

Do not reduce democracy, liberty, or human rights to a fraudulent cover for capital.

The stronger and more defensible claim is that interface economies and institutions protecting exit, contract, property, and constrained sovereignty may co-evolve and reinforce one another.

This branch remains separate from the main causal-line article until developed as an independent essay.

---

## 3. Current MkDocs Snapshot

```text
site_name: Longview Archive
site_url: https://longview-archive.org
site_author: Aster Vale
theme: material
```

### Theme features

```yaml
features:
  - navigation.path
  - navigation.top
  - search.highlight
```

### Excluded docs

```yaml
exclude_docs: |
  file_map.md
```

### Extra CSS

```yaml
extra_css:
  - stylesheets/extra.css
```

### Current top-level navigation

```text
Home
Start Here
Framework
Productive-Forces Economics
Series
Archive
Chinese
```

### Current public page count

```text
166 navigation entries
166 unique document paths
```

---

## 4. Naming and Path Rules

- Use lowercase folder names for new general-purpose directories.
- Preserve existing public series folder names unless deliberately migrating them.
- Use stable English filenames for English public files.
- Chinese article titles belong in article headings and navigation labels; filenames should remain stable and technical where possible.
- Use `index.md` only for genuine directory landing pages.
- Use `git mv` for path changes.
- Never keep two active public copies merely to avoid updating links.
- Bundles and internal review files should not enter public navigation.

Recommended pattern:

```text
folder-name/
  index.md
  article-name.md
```

---

## 5. Repository Layers and Canonical Locations

### Root-level public docs

```text
docs/index.md
docs/author.md
docs/copyright.md
docs/versions.md
docs/robots.txt
docs/sitemap.xml
docs/assets/
docs/stylesheets/
docs/essays/
docs/file_map.md
```

`docs/file_map.md` remains excluded from the public build.

### English framework

```text
docs/essays/english/framework/
```

### English Productive-Forces Economics

```text
docs/essays/english/productive-forces-economics/
```

Current public entries: {len(english_pfe)}

### English public series

```text
docs/essays/notes/english/
```

Current series:

```text
Frontiers
Architecture
Development
Value-Capture
China-Burden-Production
Technology-Amplifier
```

### Chinese framework and mother-language layer

```text
docs/essays/chinese/
```

### Chinese Productive-Forces Economics

```text
docs/essays/chinese/productive-forces-economics/
```

Current public entries: {len(chinese_pfe)}

### Chinese notes

```text
docs/essays/notes/chinese/
```

Current groups:

```text
civilizational-expansion/boundary-of-expansion
doudi-civilization
production-boundary
```

### Private/local

```text
private/
```

Do not place unpublished total outlines, final manifestos, sensitive strategic drafts, or internal reasoning bundles under public `docs/`.

### Legacy/history

```text
history/
```

Keep legacy files outside `docs/` whenever possible.

---

## 6. Current Navigation Tree

- Home → `index.md`
- Start Here
  - Reader Map → `essays/english/framework/reader-map.md`
  - Common Ground → `essays/english/framework/common-ground.md`
  - Core Terms → `essays/english/framework/core-terms-eng.md`
- Framework
  - Framework Overview → `essays/english/framework/index.md`
  - Productive Forces and Civilization → `essays/english/framework/geography-productive-forces-and-civilization.md`
  - Civilizational Metabolism → `essays/english/framework/civilizational-metabolism.md`
  - Absorptive Capacity → `essays/english/framework/absorptive-capacity.md`
  - Surplus, Absorption, and Reproduction → `essays/english/framework/surplus-absorption-and-reproduction.md`
  - Value Capture and the Western System → `essays/english/framework/western-system.md`
- Productive-Forces Economics
  - Overview → `essays/english/productive-forces-economics/index.md`
  - Methodological Memorandum → `essays/english/productive-forces-economics/00-methodological-memorandum.md`
  - Causal Line → `essays/english/productive-forces-economics/from-geography-to-consumption.md`
  - 01｜Why Did Modern Western Economics Not Begin with Productive Forces? → `essays/english/productive-forces-economics/01-western-economics.md`
  - 02｜Why Did Long-Term Chinese Governance First Confront the Production System? → `essays/english/productive-forces-economics/02-chinese-governance.md`
  - 03｜How Do Production Systems and Interface Networks Handle Failure? → `essays/english/productive-forces-economics/03-failure.md`
  - 04｜Why Can System Contributions Not Be Fully Reflected in Price? → `essays/english/productive-forces-economics/04-system-contribution.md`
  - 05｜Why Can Productive Capacity Not Automatically Become Effective Consumption? → `essays/english/productive-forces-economics/05-consumption.md`
  - 06｜Why Can Some Productive Capacities Not Wait for the Market? → `essays/english/productive-forces-economics/06-market-generation.md`
  - 07｜Why Can a Production System Also Generate Inefficiency and Reformatting? → `essays/english/productive-forces-economics/07-inefficiency.md`
  - 08｜How Can a System Use Interfaces for Localized Correction? → `essays/english/productive-forces-economics/08-correction.md`
  - 09｜Why Did China’s Modernization Succeed, and Why Must It Enter a New Stage? → `essays/english/productive-forces-economics/09-modernization.md`
- Series
  - Frontiers
    - Overview → `essays/notes/english/Frontiers/index.md`
    - 01. Why Centralized Empires Expand Differently → `essays/notes/english/Frontiers/01-why-centralized-empires-expand-differently.md`
    - 02. Why the Hexi Corridor Mattered More Than Conquest → `essays/notes/english/Frontiers/02-why-the-hexi-corridor-mattered-more-than-conquest.md`
    - 03. Why Indian Muslims Became Part of Southeast Asian Culture → `essays/notes/english/Frontiers/03-why-indian-muslims-became-part-of-southeast-asian-culture.md`
    - 04. Why China Did Not Become the Civilizational Ground of Southeast Asia → `essays/notes/english/Frontiers/04-why-china-did-not-become-the-civilizational-ground-of-southeast-asia.md`
    - 05. Why Ancient China Rarely Produced European-Style Frontier Warlords and Colonial Groups → `essays/notes/english/Frontiers/05-why-ancient-china-rarely-produced-european-style-frontier-warlords-and-colonial-groups.md`
    - 06. Why Ancient China Did Not Produce Venetian-Style Maritime Republics → `essays/notes/english/Frontiers/06-why-ancient-china-did-not-produce-venetian-style-maritime-republics.md`
    - 07. Why Zheng He’s Voyages Did Not Become a Chinese Age of Discovery → `essays/notes/english/Frontiers/07-why-zheng-hes-voyages-did-not-become-a-chinese-age-of-discovery.md`
    - 08. Why Chinese Merchants Did Not Build an East India Company → `essays/notes/english/Frontiers/08-why-chinese-merchants-did-not-build-an-east-india-company.md`
    - 09. Why Africa Has Not Become a Complete Copy of Any External Civilization → `essays/notes/english/Frontiers/09-why-africa-has-not-become-a-complete-copy-of-any-external-civilization.md`
    - 10. Why No Civilization Can Turn the Whole World Into Its Own Replica → `essays/notes/english/Frontiers/10-why-no-civilization-can-turn-the-whole-world-into-its-own-replica.md`
    - 11. Why a Civilization Cannot Treat Its Own Survival Mode as the World’s Answer → `essays/notes/english/Frontiers/11-why-a-civilization-cannot-treat-its-own-survival-mode-as-the-worlds-answer.md`
  - Architecture of Production
    - Overview → `essays/notes/english/Architecture/index.md`
    - 01. Why Infrastructure Alone Does Not Create Industrialization → `essays/notes/english/Architecture/01-infrastructure-alone-does-not-create-industrialization.md`
    - 02. Production Is Not Just Output → `essays/notes/english/Architecture/02-production-is-not-just-output.md`
    - 03. The Problem of Absorptive Capacity → `essays/notes/english/Architecture/03-the-problem-of-absorptive-capacity.md`
    - 04. Why External Capital Cannot Build a Production System → `essays/notes/english/Architecture/04-why-external-capital-cannot-build-a-production-system.md`
    - 05. States Are Not Consumption Machines → `essays/notes/english/Architecture/05-states-are-not-consumption-machines.md`
    - 06. The Boundary of Production → `essays/notes/english/Architecture/06-the-boundary-of-production.md`
    - 07. Why the Global South Is Not the Next China → `essays/notes/english/Architecture/07-why-the-global-south-is-not-the-next-china.md`
    - 08. Industrialization Requires Social Reproduction → `essays/notes/english/Architecture/08-industrialization-requires-social-reproduction.md`
    - 09. Civilization Is Not Just Culture → `essays/notes/english/Architecture/09-civilization-is-not-just-culture.md`
    - 10. Globalization and the Limits of Value Capture → `essays/notes/english/Architecture/10-globalization-and-the-limits-of-value-capture.md`
    - 11. Why Production Systems Cannot Be Imported → `essays/notes/english/Architecture/11-why-production-systems-cannot-be-imported.md`
  - Boundaries of Development
    - Overview → `essays/notes/english/Development/index.md`
    - 01. Why Africa Is Hard to Industrialize → `essays/notes/english/Development/01-why-africa-is-hard-to-industrialize.md`
    - 02. Why Infrastructure Loans Do Not Create Production Systems → `essays/notes/english/Development/02-why-infrastructure-loans-do-not-create-production-systems.md`
    - 03. Why Industrial Parks Remain Empty → `essays/notes/english/Development/03-why-industrial-parks-remain-empty.md`
    - 04. Why Cheap Labor Is Not Enough → `essays/notes/english/Development/04-why-cheap-labor-is-not-enough.md`
    - 05. Why Foreign Investment Does Not Automatically Create Capability → `essays/notes/english/Development/05-why-foreign-investment-does-not-automatically-create-capability.md`
    - 06. Why Resource Wealth Does Not Create Industrialization → `essays/notes/english/Development/06-why-resource-wealth-does-not-create-industrialization.md`
    - 07. Why Global Supply Chains Do Not Create National Production → `essays/notes/english/Development/07-why-global-supply-chains-do-not-create-national-production.md`
    - 08. The Productive Imperative → `essays/notes/english/Development/08-the-productive-imperative.md`
    - 09. Why the Global South Cannot Copy China → `essays/notes/english/Development/09-why-the-global-south-cannot-copy-china.md`
    - 10. Why Aid Cannot Substitute for State Capacity → `essays/notes/english/Development/10-why-aid-cannot-substitute-for-state-capacity.md`
    - 11. Why Production Is a System, Not a Project → `essays/notes/english/Development/11-why-production-is-a-system-not-a-project.md`
  - Value Capture
    - Overview → `essays/notes/english/Value-Capture/index.md`
    - 01. Why Producing More Does Not Mean Earning More → `essays/notes/english/Value-Capture/01-why-producing-more-does-not-mean-earning-more.md`
    - 02. Why Value Is Captured at the Interface → `essays/notes/english/Value-Capture/02-why-value-is-captured-at-the-interface.md`
    - 03. Why Pricing Power Matters More Than Output → `essays/notes/english/Value-Capture/03-why-pricing-power-matters-more-than-output.md`
    - 04. Why Finance Can Command Production Without Owning It → `essays/notes/english/Value-Capture/04-why-finance-can-command-production-without-owning-it.md`
    - 05. Why Standards Become Invisible Infrastructure → `essays/notes/english/Value-Capture/05-why-standards-become-invisible-infrastructure.md`
    - 06. Why Platforms Capture Markets Without Bearing Production → `essays/notes/english/Value-Capture/06-why-platforms-capture-markets-without-bearing-production.md`
    - 07. Why Brands Turn Production into Hierarchy → `essays/notes/english/Value-Capture/07-why-brands-turn-production-into-hierarchy.md`
    - 08. Why Legal Systems and Compliance Shape Global Value → `essays/notes/english/Value-Capture/08-why-legal-systems-and-compliance-shape-global-value.md`
    - 09. Why Reserve Currencies Are Civilizational Interfaces → `essays/notes/english/Value-Capture/09-why-reserve-currencies-are-civilizational-interfaces.md`
    - 10. Why Mature Markets Defend Value Capture → `essays/notes/english/Value-Capture/10-why-mature-markets-defend-value-capture.md`
    - 11. Why the Global Rentier System Faces a Production Shock → `essays/notes/english/Value-Capture/11-why-the-global-rentier-system-faces-a-production-shock.md`
  - China and Production Burden
    - Overview → `essays/notes/english/China-Burden-Production/index.md`
    - 01. Why China Is Not Just the World’s Factory → `essays/notes/english/China-Burden-Production/01-why-china-is-not-just-the-worlds-factory.md`
    - 02. Why Production Becomes a Social Burden → `essays/notes/english/China-Burden-Production/02-why-production-becomes-a-social-burden.md`
    - 03. Why Infrastructure Is Part of China’s Industrial System → `essays/notes/english/China-Burden-Production/03-why-infrastructure-is-part-of-chinas-industrial-system.md`
    - 04. Why Employment Makes Production Political → `essays/notes/english/China-Burden-Production/04-why-employment-makes-production-political.md`
    - 05. Why Supply Chains Become National Operating Systems → `essays/notes/english/China-Burden-Production/05-why-supply-chains-become-national-operating-systems.md`
    - 06. Why Local Governments Carry Industrial Pressure → `essays/notes/english/China-Burden-Production/06-why-local-governments-carry-industrial-pressure.md`
    - 07. Why Exports Cannot Fully Solve China’s Internal Pressure → `essays/notes/english/China-Burden-Production/07-why-exports-cannot-fully-solve-chinas-internal-pressure.md`
    - 08. Why Domestic Demand Is Harder Than It Looks → `essays/notes/english/China-Burden-Production/08-why-domestic-demand-is-harder-than-it-looks.md`
    - 09. Why China Cannot Simply Abandon Production → `essays/notes/english/China-Burden-Production/09-why-china-cannot-simply-abandon-production.md`
    - 10. Why China’s Industrial Strength Also Creates Constraint → `essays/notes/english/China-Burden-Production/10-why-chinas-industrial-strength-also-creates-constraint.md`
    - 11. Why the Burden of Production Forces Institutional Change → `essays/notes/english/China-Burden-Production/11-why-the-burden-of-production-forces-institutional-change.md`
  - Technology Amplifier
    - Overview → `essays/notes/english/Technology-Amplifier/index.md`
    - 01. Why Technology Does Not Replace Structure → `essays/notes/english/Technology-Amplifier/01-why-technology-does-not-replace-structure.md`
    - 02. Why AI Amplifies Existing Capacity → `essays/notes/english/Technology-Amplifier/02-why-ai-amplifies-existing-capacity.md`
    - 03. Why Data Is Not Power Without Organization → `essays/notes/english/Technology-Amplifier/03-why-data-is-not-power-without-organization.md`
    - 04. Why Automation Rewards Production Systems → `essays/notes/english/Technology-Amplifier/04-why-automation-rewards-production-systems.md`
    - 05. Why Platforms Gain More From AI Than Isolated Firms → `essays/notes/english/Technology-Amplifier/05-why-platforms-gain-more-from-ai-than-isolated-firms.md`
    - 06. Why Finance Uses Technology to Price the Future Faster → `essays/notes/english/Technology-Amplifier/06-why-finance-uses-technology-to-price-the-future-faster.md`
    - 07. Why States With Execution Capacity Benefit More From AI → `essays/notes/english/Technology-Amplifier/07-why-states-with-execution-capacity-benefit-more-from-ai.md`
    - 08. Why Weak Systems Become More Fragile Under Advanced Technology → `essays/notes/english/Technology-Amplifier/08-why-weak-systems-become-more-fragile-under-advanced-technology.md`
    - 09. Why AI Changes Labor Without Ending Production → `essays/notes/english/Technology-Amplifier/09-why-ai-changes-labor-without-ending-production.md`
    - 10. Why Technological Power Depends on Systemic Absorption → `essays/notes/english/Technology-Amplifier/10-why-technological-power-depends-on-systemic-absorption.md`
    - 11. Why the AI Shock Is Really a Structural Shock → `essays/notes/english/Technology-Amplifier/11-why-the-ai-shock-is-really-a-structural-shock.md`
- Archive
  - Version Records → `versions.md`
  - Author → `author.md`
  - Copyright → `copyright.md`
- Chinese
  - 中文总览 → `essays/chinese/index.md`
  - 核心术语 → `essays/chinese/core-terms-chinese.md`
  - 阅读规则 → `essays/chinese/reading-rules.md`
  - 生产力经济学
    - 总览 → `essays/chinese/productive-forces-economics/index.md`
    - 方法论备忘录 → `essays/chinese/productive-forces-economics/00-c-methodological-memorandum.md`
    - 从地理到消费 → `essays/chinese/productive-forces-economics/from-geography-to-consumption-chinese.md`
    - 01｜为什么现代西方经济学没有从生产力出发 → `essays/chinese/productive-forces-economics/01-c-western-economics.md`
    - 02｜为什么中国长期治理首先面对生产系统 → `essays/chinese/productive-forces-economics/02-c-chinese-governance.md`
    - 03｜生产系统与接口网络如何处理失效 → `essays/chinese/productive-forces-economics/03-c-failure.md`
    - 04｜为什么系统贡献无法完全进入价格 → `essays/chinese/productive-forces-economics/04-c-system-contribution.md`
    - 05｜为什么生产能力不能自动转化为有效消费 → `essays/chinese/productive-forces-economics/05-c-consumption.md`
    - 06｜为什么有些生产能力不能等待市场自动生成 → `essays/chinese/productive-forces-economics/06-c-market-generation.md`
    - 07｜生产系统为什么也会制造低效与格式化 → `essays/chinese/productive-forces-economics/07-c-inefficiency.md`
    - 08｜系统怎样使用接口完成局部纠错 → `essays/chinese/productive-forces-economics/08-c-correction.md`
    - 09｜中国现代化为什么成功又为什么必须进入下一阶段 → `essays/chinese/productive-forces-economics/09-c-modernization.md`
  - Reality｜现实世界
    - 阅读前约束 → `essays/chinese/reality/00.md`
    - 01｜人类文明的三种底层模式 → `essays/chinese/reality/01.md`
    - 02｜中国制度不是消费机器，而是做功机器 → `essays/chinese/reality/02.md`
    - 03｜全球南方不是第二个中国 → `essays/chinese/reality/03.md`
    - 04｜中国不能把自己的生存方式当作世界答案 → `essays/chinese/reality/04.md`
    - 05｜成熟市场为什么不愿承接中国工业 2.0 → `essays/chinese/reality/05.md`
    - 06｜不限制生产，只限制变现 → `essays/chinese/reality/06.md`
    - 07｜真正的市场战，不是打工厂，而是打变现 → `essays/chinese/reality/07.md`
    - 08｜旧闭环正在退潮 → `essays/chinese/reality/08s.md`
    - 09｜内部闭环的压力 → `essays/chinese/reality/09.md`
    - 10｜文明战略转型 → `essays/chinese/reality/10.md`
    - 阅读后约束 → `essays/chinese/reality/11.md`
  - Future Path｜未来之路
    - 阅读前约束 → `essays/chinese/future/00.md`
    - 01｜生产富余不是危机，而是入口 → `essays/chinese/future/01.md`
    - 02｜组织富余 → `essays/chinese/future/02.md`
    - 03｜新闭环的必要性 → `essays/chinese/future/03.md`
    - 04｜从外部变现转向内部承接 → `essays/chinese/future/04.md`
    - 05｜生产力如何重塑社会关系 → `essays/chinese/future/05.md`
    - 06｜新的分配与承接结构 → `essays/chinese/future/06.md`
    - 07｜技术不是终点，而是放大器 → `essays/chinese/future/07.md`
    - 08｜文明闭环 → `essays/chinese/future/08.md`
    - 09｜未来之路的边界 → `essays/chinese/future/09.md`
    - 10｜阅读后约束 → `essays/chinese/future/10.md`
  - 中文札记
    - 札记总览 → `essays/notes/chinese/index.md`
    - 扩张的边界
      - 01｜为什么印度穆斯林能够成为东南亚文化的一部分？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/01-indian-muslims-in-southeast-asia.md`
      - 02｜雄踞东亚两千年的中原王朝，为什么始终没有成为东南亚的文明底色？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/02-southeast-asia-civilization-base.md`
      - 03｜中原文明最大规模的结构性扩张，为什么是河西走廊，而不是漠北或越南北部？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/03-hexi-corridor.md`
      - 04｜为什么中国古代很少出现欧洲式边境军阀和殖民集团自发扩张？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/04-border-warlords-and-colonial-groups.md`
      - 05｜为什么中国古代没有出现威尼斯式海商共和国？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/05-maritime-merchant-republics.md`
      - 06｜为什么郑和下西洋没有变成中国版大航海时代？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/06-zheng-he-and-age-of-discovery.md`
      - 07｜为什么中国商人遍布东南亚，却没有建立东印度公司式殖民帝国？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/07-chinese-merchants-and-east-india-company.md`
      - 08｜为什么非洲至今没有成为任何外来文明的完整复制品？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/08-africa-and-civilization-replication.md`
      - 09｜为什么没有一种文明能把整个世界变成自己的复制品？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/09-why-no-civilization-can-copy-the-world.md`
      - 10｜文明为什么不能把自己的生存方式当作世界答案？ → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/10-civilization-boundary-and-working-civilization.md`
    - 兜底文明
      - 01｜为什么中国文明从一开始就不是城邦文明？ → `essays/notes/chinese/doudi-civilization/01-not-city-state-civilization.md`
      - 02｜为什么三皇五帝神话的核心，不是神权，而是治世？ → `essays/notes/chinese/doudi-civilization/02-myths-of-governance.md`
      - 03｜为什么治水是中原文明最早的国家能力原型？ → `essays/notes/chinese/doudi-civilization/03-flood-control-and-state-capacity.md`
      - 04｜为什么春秋战国五百年血雨，最终没有走向欧洲式封建均势？ → `essays/notes/chinese/doudi-civilization/04-spring-autumn-warring-states-selection.md`
      - 05｜为什么秦制不是偶然暴政，而是战争时代筛选出的组织机器？ → `essays/notes/chinese/doudi-civilization/05-qin-system-as-organization-machine.md`
      - 06｜为什么中国世家大族的衰亡具有历史必然性？ → `essays/notes/chinese/doudi-civilization/06-decline-of-aristocratic-clans.md`
      - 07｜为什么中国王朝必须压制地方军政集团？ → `essays/notes/chinese/doudi-civilization/07-why-central-state-suppresses-local-military-power.md`
      - 08｜为什么中国王朝是兜底文明，而不是契约文明？ → `essays/notes/chinese/doudi-civilization/08-why-chinese-dynasties-are-fallback-civilizations.md`
      - 09｜为什么西方可以长期苟住，而中国王朝兜不住就会改朝换代？ → `essays/notes/chinese/doudi-civilization/09-why-the-west-could-muddle-through.md`
      - 10｜大一统的极限成就：为什么中国文明必须把天下做成秩序？ → `essays/notes/chinese/doudi-civilization/10-great-unification-as-ultimate-order.md`
    - 生产的边界
      - 01｜为什么修路不等于工业化？ → `essays/notes/chinese/production-boundary/01-roads-do-not-equal-industrialization.md`
      - 02｜为什么建厂不等于制造业体系？ → `essays/notes/chinese/production-boundary/02-factories-do-not-equal-manufacturing-system.md`
      - 03｜为什么通电不等于产业能力？ → `essays/notes/chinese/production-boundary/03-electricity-does-not-equal-industrial-capacity.md`
      - 04｜为什么人口多不等于市场大？ → `essays/notes/chinese/production-boundary/04-population-does-not-equal-market.md`
      - 05｜为什么资源丰富的国家反而更难工业化？ → `essays/notes/chinese/production-boundary/05-resource-rich-countries-and-industrialization.md`
      - 06｜为什么工业园常常变成孤岛，而不是产业体系？ → `essays/notes/chinese/production-boundary/06-industrial-parks-as-islands.md`
      - 07｜为什么廉价劳动力不等于制造业优势？ → `essays/notes/chinese/production-boundary/07-cheap-labor-does-not-equal-manufacturing-advantage.md`
      - 08｜为什么承接产业转移，比建设工厂更难？ → `essays/notes/chinese/production-boundary/08-industrial-transfer-is-harder-than-building-factories.md`
      - 09｜为什么中国制造业不是几条产业链就能复制？ → `essays/notes/chinese/production-boundary/09-why-china-manufacturing-cannot-be-copied-by-supply-chains.md`
      - 10｜生产能力为什么是一种文明能力？ → `essays/notes/chinese/production-boundary/10-production-capacity-as-civilizational-capacity.md`

---

## 7. Full Navigation Listing

### Home

- `Home` → `index.md`

### Start Here

- `Start Here / Reader Map` → `essays/english/framework/reader-map.md`
- `Start Here / Common Ground` → `essays/english/framework/common-ground.md`
- `Start Here / Core Terms` → `essays/english/framework/core-terms-eng.md`

### Framework

- `Framework / Framework Overview` → `essays/english/framework/index.md`
- `Framework / Productive Forces and Civilization` → `essays/english/framework/geography-productive-forces-and-civilization.md`
- `Framework / Civilizational Metabolism` → `essays/english/framework/civilizational-metabolism.md`
- `Framework / Absorptive Capacity` → `essays/english/framework/absorptive-capacity.md`
- `Framework / Surplus, Absorption, and Reproduction` → `essays/english/framework/surplus-absorption-and-reproduction.md`
- `Framework / Value Capture and the Western System` → `essays/english/framework/western-system.md`

### Productive-Forces Economics

- `Productive-Forces Economics / Overview` → `essays/english/productive-forces-economics/index.md`
- `Productive-Forces Economics / Methodological Memorandum` → `essays/english/productive-forces-economics/00-methodological-memorandum.md`
- `Productive-Forces Economics / Causal Line` → `essays/english/productive-forces-economics/from-geography-to-consumption.md`
- `Productive-Forces Economics / 01｜Why Did Modern Western Economics Not Begin with Productive Forces?` → `essays/english/productive-forces-economics/01-western-economics.md`
- `Productive-Forces Economics / 02｜Why Did Long-Term Chinese Governance First Confront the Production System?` → `essays/english/productive-forces-economics/02-chinese-governance.md`
- `Productive-Forces Economics / 03｜How Do Production Systems and Interface Networks Handle Failure?` → `essays/english/productive-forces-economics/03-failure.md`
- `Productive-Forces Economics / 04｜Why Can System Contributions Not Be Fully Reflected in Price?` → `essays/english/productive-forces-economics/04-system-contribution.md`
- `Productive-Forces Economics / 05｜Why Can Productive Capacity Not Automatically Become Effective Consumption?` → `essays/english/productive-forces-economics/05-consumption.md`
- `Productive-Forces Economics / 06｜Why Can Some Productive Capacities Not Wait for the Market?` → `essays/english/productive-forces-economics/06-market-generation.md`
- `Productive-Forces Economics / 07｜Why Can a Production System Also Generate Inefficiency and Reformatting?` → `essays/english/productive-forces-economics/07-inefficiency.md`
- `Productive-Forces Economics / 08｜How Can a System Use Interfaces for Localized Correction?` → `essays/english/productive-forces-economics/08-correction.md`
- `Productive-Forces Economics / 09｜Why Did China’s Modernization Succeed, and Why Must It Enter a New Stage?` → `essays/english/productive-forces-economics/09-modernization.md`

### Series

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

### Archive

- `Archive / Version Records` → `versions.md`
- `Archive / Author` → `author.md`
- `Archive / Copyright` → `copyright.md`

### Chinese

- `Chinese / 中文总览` → `essays/chinese/index.md`
- `Chinese / 核心术语` → `essays/chinese/core-terms-chinese.md`
- `Chinese / 阅读规则` → `essays/chinese/reading-rules.md`
- `Chinese / 生产力经济学 / 总览` → `essays/chinese/productive-forces-economics/index.md`
- `Chinese / 生产力经济学 / 方法论备忘录` → `essays/chinese/productive-forces-economics/00-c-methodological-memorandum.md`
- `Chinese / 生产力经济学 / 从地理到消费` → `essays/chinese/productive-forces-economics/from-geography-to-consumption-chinese.md`
- `Chinese / 生产力经济学 / 01｜为什么现代西方经济学没有从生产力出发` → `essays/chinese/productive-forces-economics/01-c-western-economics.md`
- `Chinese / 生产力经济学 / 02｜为什么中国长期治理首先面对生产系统` → `essays/chinese/productive-forces-economics/02-c-chinese-governance.md`
- `Chinese / 生产力经济学 / 03｜生产系统与接口网络如何处理失效` → `essays/chinese/productive-forces-economics/03-c-failure.md`
- `Chinese / 生产力经济学 / 04｜为什么系统贡献无法完全进入价格` → `essays/chinese/productive-forces-economics/04-c-system-contribution.md`
- `Chinese / 生产力经济学 / 05｜为什么生产能力不能自动转化为有效消费` → `essays/chinese/productive-forces-economics/05-c-consumption.md`
- `Chinese / 生产力经济学 / 06｜为什么有些生产能力不能等待市场自动生成` → `essays/chinese/productive-forces-economics/06-c-market-generation.md`
- `Chinese / 生产力经济学 / 07｜生产系统为什么也会制造低效与格式化` → `essays/chinese/productive-forces-economics/07-c-inefficiency.md`
- `Chinese / 生产力经济学 / 08｜系统怎样使用接口完成局部纠错` → `essays/chinese/productive-forces-economics/08-c-correction.md`
- `Chinese / 生产力经济学 / 09｜中国现代化为什么成功又为什么必须进入下一阶段` → `essays/chinese/productive-forces-economics/09-c-modernization.md`
- `Chinese / Reality｜现实世界 / 阅读前约束` → `essays/chinese/reality/00.md`
- `Chinese / Reality｜现实世界 / 01｜人类文明的三种底层模式` → `essays/chinese/reality/01.md`
- `Chinese / Reality｜现实世界 / 02｜中国制度不是消费机器，而是做功机器` → `essays/chinese/reality/02.md`
- `Chinese / Reality｜现实世界 / 03｜全球南方不是第二个中国` → `essays/chinese/reality/03.md`
- `Chinese / Reality｜现实世界 / 04｜中国不能把自己的生存方式当作世界答案` → `essays/chinese/reality/04.md`
- `Chinese / Reality｜现实世界 / 05｜成熟市场为什么不愿承接中国工业 2.0` → `essays/chinese/reality/05.md`
- `Chinese / Reality｜现实世界 / 06｜不限制生产，只限制变现` → `essays/chinese/reality/06.md`
- `Chinese / Reality｜现实世界 / 07｜真正的市场战，不是打工厂，而是打变现` → `essays/chinese/reality/07.md`
- `Chinese / Reality｜现实世界 / 08｜旧闭环正在退潮` → `essays/chinese/reality/08s.md`
- `Chinese / Reality｜现实世界 / 09｜内部闭环的压力` → `essays/chinese/reality/09.md`
- `Chinese / Reality｜现实世界 / 10｜文明战略转型` → `essays/chinese/reality/10.md`
- `Chinese / Reality｜现实世界 / 阅读后约束` → `essays/chinese/reality/11.md`
- `Chinese / Future Path｜未来之路 / 阅读前约束` → `essays/chinese/future/00.md`
- `Chinese / Future Path｜未来之路 / 01｜生产富余不是危机，而是入口` → `essays/chinese/future/01.md`
- `Chinese / Future Path｜未来之路 / 02｜组织富余` → `essays/chinese/future/02.md`
- `Chinese / Future Path｜未来之路 / 03｜新闭环的必要性` → `essays/chinese/future/03.md`
- `Chinese / Future Path｜未来之路 / 04｜从外部变现转向内部承接` → `essays/chinese/future/04.md`
- `Chinese / Future Path｜未来之路 / 05｜生产力如何重塑社会关系` → `essays/chinese/future/05.md`
- `Chinese / Future Path｜未来之路 / 06｜新的分配与承接结构` → `essays/chinese/future/06.md`
- `Chinese / Future Path｜未来之路 / 07｜技术不是终点，而是放大器` → `essays/chinese/future/07.md`
- `Chinese / Future Path｜未来之路 / 08｜文明闭环` → `essays/chinese/future/08.md`
- `Chinese / Future Path｜未来之路 / 09｜未来之路的边界` → `essays/chinese/future/09.md`
- `Chinese / Future Path｜未来之路 / 10｜阅读后约束` → `essays/chinese/future/10.md`
- `Chinese / 中文札记 / 札记总览` → `essays/notes/chinese/index.md`
- `Chinese / 中文札记 / 扩张的边界 / 01｜为什么印度穆斯林能够成为东南亚文化的一部分？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/01-indian-muslims-in-southeast-asia.md`
- `Chinese / 中文札记 / 扩张的边界 / 02｜雄踞东亚两千年的中原王朝，为什么始终没有成为东南亚的文明底色？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/02-southeast-asia-civilization-base.md`
- `Chinese / 中文札记 / 扩张的边界 / 03｜中原文明最大规模的结构性扩张，为什么是河西走廊，而不是漠北或越南北部？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/03-hexi-corridor.md`
- `Chinese / 中文札记 / 扩张的边界 / 04｜为什么中国古代很少出现欧洲式边境军阀和殖民集团自发扩张？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/04-border-warlords-and-colonial-groups.md`
- `Chinese / 中文札记 / 扩张的边界 / 05｜为什么中国古代没有出现威尼斯式海商共和国？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/05-maritime-merchant-republics.md`
- `Chinese / 中文札记 / 扩张的边界 / 06｜为什么郑和下西洋没有变成中国版大航海时代？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/06-zheng-he-and-age-of-discovery.md`
- `Chinese / 中文札记 / 扩张的边界 / 07｜为什么中国商人遍布东南亚，却没有建立东印度公司式殖民帝国？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/07-chinese-merchants-and-east-india-company.md`
- `Chinese / 中文札记 / 扩张的边界 / 08｜为什么非洲至今没有成为任何外来文明的完整复制品？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/08-africa-and-civilization-replication.md`
- `Chinese / 中文札记 / 扩张的边界 / 09｜为什么没有一种文明能把整个世界变成自己的复制品？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/09-why-no-civilization-can-copy-the-world.md`
- `Chinese / 中文札记 / 扩张的边界 / 10｜文明为什么不能把自己的生存方式当作世界答案？` → `essays/notes/chinese/civilizational-expansion/boundary-of-expansion/10-civilization-boundary-and-working-civilization.md`
- `Chinese / 中文札记 / 兜底文明 / 01｜为什么中国文明从一开始就不是城邦文明？` → `essays/notes/chinese/doudi-civilization/01-not-city-state-civilization.md`
- `Chinese / 中文札记 / 兜底文明 / 02｜为什么三皇五帝神话的核心，不是神权，而是治世？` → `essays/notes/chinese/doudi-civilization/02-myths-of-governance.md`
- `Chinese / 中文札记 / 兜底文明 / 03｜为什么治水是中原文明最早的国家能力原型？` → `essays/notes/chinese/doudi-civilization/03-flood-control-and-state-capacity.md`
- `Chinese / 中文札记 / 兜底文明 / 04｜为什么春秋战国五百年血雨，最终没有走向欧洲式封建均势？` → `essays/notes/chinese/doudi-civilization/04-spring-autumn-warring-states-selection.md`
- `Chinese / 中文札记 / 兜底文明 / 05｜为什么秦制不是偶然暴政，而是战争时代筛选出的组织机器？` → `essays/notes/chinese/doudi-civilization/05-qin-system-as-organization-machine.md`
- `Chinese / 中文札记 / 兜底文明 / 06｜为什么中国世家大族的衰亡具有历史必然性？` → `essays/notes/chinese/doudi-civilization/06-decline-of-aristocratic-clans.md`
- `Chinese / 中文札记 / 兜底文明 / 07｜为什么中国王朝必须压制地方军政集团？` → `essays/notes/chinese/doudi-civilization/07-why-central-state-suppresses-local-military-power.md`
- `Chinese / 中文札记 / 兜底文明 / 08｜为什么中国王朝是兜底文明，而不是契约文明？` → `essays/notes/chinese/doudi-civilization/08-why-chinese-dynasties-are-fallback-civilizations.md`
- `Chinese / 中文札记 / 兜底文明 / 09｜为什么西方可以长期苟住，而中国王朝兜不住就会改朝换代？` → `essays/notes/chinese/doudi-civilization/09-why-the-west-could-muddle-through.md`
- `Chinese / 中文札记 / 兜底文明 / 10｜大一统的极限成就：为什么中国文明必须把天下做成秩序？` → `essays/notes/chinese/doudi-civilization/10-great-unification-as-ultimate-order.md`
- `Chinese / 中文札记 / 生产的边界 / 01｜为什么修路不等于工业化？` → `essays/notes/chinese/production-boundary/01-roads-do-not-equal-industrialization.md`
- `Chinese / 中文札记 / 生产的边界 / 02｜为什么建厂不等于制造业体系？` → `essays/notes/chinese/production-boundary/02-factories-do-not-equal-manufacturing-system.md`
- `Chinese / 中文札记 / 生产的边界 / 03｜为什么通电不等于产业能力？` → `essays/notes/chinese/production-boundary/03-electricity-does-not-equal-industrial-capacity.md`
- `Chinese / 中文札记 / 生产的边界 / 04｜为什么人口多不等于市场大？` → `essays/notes/chinese/production-boundary/04-population-does-not-equal-market.md`
- `Chinese / 中文札记 / 生产的边界 / 05｜为什么资源丰富的国家反而更难工业化？` → `essays/notes/chinese/production-boundary/05-resource-rich-countries-and-industrialization.md`
- `Chinese / 中文札记 / 生产的边界 / 06｜为什么工业园常常变成孤岛，而不是产业体系？` → `essays/notes/chinese/production-boundary/06-industrial-parks-as-islands.md`
- `Chinese / 中文札记 / 生产的边界 / 07｜为什么廉价劳动力不等于制造业优势？` → `essays/notes/chinese/production-boundary/07-cheap-labor-does-not-equal-manufacturing-advantage.md`
- `Chinese / 中文札记 / 生产的边界 / 08｜为什么承接产业转移，比建设工厂更难？` → `essays/notes/chinese/production-boundary/08-industrial-transfer-is-harder-than-building-factories.md`
- `Chinese / 中文札记 / 生产的边界 / 09｜为什么中国制造业不是几条产业链就能复制？` → `essays/notes/chinese/production-boundary/09-why-china-manufacturing-cannot-be-copied-by-supply-chains.md`
- `Chinese / 中文札记 / 生产的边界 / 10｜生产能力为什么是一种文明能力？` → `essays/notes/chinese/production-boundary/10-production-capacity-as-civilizational-capacity.md`

---

## 8. Duplicate Path Check

```text
None
```

If duplicate visual labels appear in the sidebar, inspect Material section/index behavior and custom CSS before assuming duplicate document paths.


---

## 9. Known Checks Before Commit

### 9.1 Physical file existence

Confirm that every path in `mkdocs.yml` exists under `docs/`.

Especially verify:

```text
docs/versions.md
docs/essays/chinese/reality/08s.md
docs/essays/english/framework/western-system.md
docs/essays/english/productive-forces-economics/from-geography-to-consumption.md
docs/essays/chinese/productive-forces-economics/from-geography-to-consumption-chinese.md
```

### 9.2 Western System naming

Current active path:

```text
essays/english/framework/western-system.md
```

Do not rename casually. It is the half-exposed strategic blade inside the Framework layer.

If renamed, update:

```text
file_map.md
mkdocs.yml
internal links
sitemap.xml
canonical references
```

### 9.3 Causal Line role

English:

```text
Productive-Forces Economics / Causal Line
→ essays/english/productive-forces-economics/from-geography-to-consumption.md
```

Chinese:

```text
Chinese / 生产力经济学 / 从地理到消费
→ essays/chinese/productive-forces-economics/from-geography-to-consumption-chinese.md
```

This article is the execution diagram of the framework, not an ordinary note.

### 9.4 Sitemap

The sitemap must be regenerated whenever public navigation or public paths change.

### 9.5 Build

Run:

```bash
mkdocs build
```

Resolve all missing-file warnings before deployment.

---

## 10. Update Procedure

### Add a public file

1. Create the physical file.
2. Update `file_map.md`.
3. Update related internal links.
4. Add it to `mkdocs.yml` if it should appear in navigation.
5. Regenerate `sitemap.xml`.
6. Run `mkdocs build`.
7. Commit and deploy.

### Move or rename a file

1. Use `git mv`.
2. Search the repository for the old path.
3. Update `file_map.md`.
4. Update `mkdocs.yml`.
5. Update internal and canonical links.
6. Regenerate `sitemap.xml`.
7. Run `mkdocs build`.

### Add a private manuscript

1. Put it under `private/`.
2. Do not add it to `mkdocs.yml`.
3. Record only its existence and role here when continuity requires it.
4. Do not expose its full argument in the public site map.

---

## 11. Publication and Submission Architecture

The archive contains more than one hundred public pages, but external institutions should not be asked to read the archive first.

Future submission layers:

```text
System-Level Synthesis
→ Series Synthesis
→ Concept / Policy Memo
→ Selected Essays
→ Full Archive
```

Each English series should eventually produce:

```text
Series Synthesis
Policy or Concept Memo
Full 11-essay series
```

The six series will later feed a total synthesis of the Productive-Forces Framework.

The archive proves depth.  
The synthesis delivers the idea.

---

## 12. Strategic Boundaries for Future Conversations

When continuing the project:

- Do not reduce the framework to conventional economics.
- Do not moralize the three civilizational modes.
- Do not convert structural tendencies into deterministic collapse predictions.
- Do not describe China and the West as immutable species.
- Do not equate movement along the axis with complete civilizational imitation.
- Do not collapse democratic and liberal institutions into a single capital conspiracy.
- Do distinguish public framework, Chinese theoretical root, private total outline, and historical legacy.
- Do preserve the algorithmic method: identify modules, interfaces, arrows, failure boundaries, and restoring forces.
- External evidence must enter through a defined node or arrow. It should validate, parameterize, branch, or falsify the model—not interrupt it as an unrelated anecdote.

---

## 13. One-Paragraph Recovery Memo

Longview Archive is a bilingual public mother archive built around Productive-Forces Economics. Its first coordinate is productive forces and absorptive capacity rather than conventional economics or political science. The public English layer contains the framework, the formal Productive-Forces Economics sequence, and six eleven-essay series on production, frontiers, development, value capture, China’s production burden, and technology as a structural amplifier. The Chinese layer preserves the deeper mother-language root through Reality, Future Path, Productive-Forces Economics, and three historical/structural note groups. The current central algorithm runs from geography and survival pressure through continental production, unified responsibility, responsibility embedding, household risk, failure boundaries, consumer formation, productive surplus, and a new absorptive loop. China and mature Western systems are placed on one horizontal structural axis rather than treated as immutable types: responsibility-bearing subject versus atomic individual, continuous obligation versus bounded contract, and production-node settlement versus individual/household settlement. Movement along this axis faces institutional restoring force and means incorporating missing functions historically preserved by the opposite side. Reform should be analyzed as parameter adjustment, interface rewrite, module replacement, or system reconfiguration; system reset is a failure boundary, not a deterministic prophecy. The emerging interface-economy branch may explain the co-evolution of exit, contract, limited sovereignty, and liberal-democratic institutions, but must not be reduced to a claim that democracy and freedom are merely fraudulent covers for capital.
