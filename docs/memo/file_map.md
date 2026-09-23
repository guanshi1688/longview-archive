# file_map.md｜Longview Archive 文件与发布路由图

**状态：** 2026-09-23 更新版；按当日资料库目录及上传的 `mkdocs.yml` 重建。  
**用途：** 文件位置、版本归属、网站活动导航、公开边界、新聊天恢复。  
**理论分工：** 以 `memo/theory-map.md` 为准；正文论证以当前相应正式母版为准。

> **最短规则：文明结构算法＝骨架；组织经济学＝说明书；其他文章＝深入展开历史与现实机制。旧文明结构与旧生产力经济学＝参考材料。**

---

## 0｜路径的三个视角，不要混淆

下列是三个不同的位置体系：

1. **资料库镜像（本次上传）**：`/Longview/Longview母版文件里面不要修改/` 下用 `chinese/`、`English/`、`旧材料/` 保存按阅读功能整理的文件夹。
2. **Git 公共网站仓库**：`longview-archive/` 下的 `docs/`、`mkdocs.yml`、`scripts/build_corpus.py` 等；活动导航由真实 Git `mkdocs.yml` 决定。
3. **本地私有结构母版**：据所上传 `build_corpus.py`，脚本默认在公共仓库同级的 `index/structural-algorithm/` 寻找未公开的52份中文及英文单篇源文件，并将 Corpus 输出至 `index/current/corpus/`。

镜像文件夹重命名或移动，**不代表** Git 中的对应路径已经移动。资料库有当前版本文件，不能单凭资料库列表证明线上网站已经同步、构建成功或隐藏文件已经安全移出 `docs/`。

**权威优先级：** 实际文件和当前 Git 配置 > 本文件对路径的记载；当前母版正文 > 本文件或旧 Memo 的理论摘要。发现不同步，更新本文件，不强迫当前母版回退。

---

## 1｜资料库镜像：已确认的目录层级

```text
/Longview/
├── Longview母版文件里面不要修改/
│   ├── chinese/
│   │   ├── 文明结构/
│   │   │   ├── china/              # 生产型组织 01—11
│   │   │   ├── western/            # 接口型组织 01—11
│   │   │   ├── 00 / 12、规则、术语
│   │   │   └── build_civilization_cn.py
│   │   ├── 组织经济学/              # 00—10、index、规则、术语等
│   │   ├── 中国现实世界/
│   │   ├── 中国未来世界/
│   │   ├── 人力架构/
│   │   ├── 札记/
│   │   │   ├── 扩张的边界/
│   │   │   ├── 兜底文明/
│   │   │   └── 生产的边界/
│   │   └── 规则定义/
│   ├── English/
│   │   ├── structural-algorithm/
│   │   │   ├── china/              # Production-bearing 01—11
│   │   │   ├── western/            # Interface-oriented 01—11
│   │   │   ├── 00 / 12、rules、terms
│   │   │   └── build_civilization_en.py
│   │   ├── organisation_economics/ # 00—10、index、rules、terms等
│   │   ├── framework/
│   │   └── industrial-people/
│   ├── 旧材料/
│   │   ├── 文明结构/
│   │   │   ├── china/              # 旧 Layer 0—9、旧 01a
│   │   │   └── english/            # 旧 Layer 0—9、旧 01a
│   │   └── 生产力经济学/
│   │       ├── chinese/            # 旧 PFE 00—12
│   │       └── english/            # 旧 PFE 00—12
│   ├── memo/
│   │   ├── file_map.md
│   │   └── theory-map.md
│   ├── script/
│   │   └── build_corpus.py         # 资料库镜像的脚本文件
│   └── mkdocs.yml                  # 2026-09-23 上传的配置快照
├── 对外投稿/
│   ├── EHS/
│   ├── Phenomenal_World/
│   ├── reddit/
│   ├── rome cfp/
│   ├── SSRN/
│   ├── substack-medium/
│   └── 投稿备忘录/
├── 工作文件夹/
│   ├── AI/
│   ├── 临时文件夹/
│   └── 母版材料/
└── 投稿与对外联络登记.md
```

`Longview母版文件里面不要修改/` 是用户保护的母版目录；做对照、检索、标记问题均采取只读方式。要修改时由用户明确替换的具体文件和版本。这里的 `旧材料/` 是同级历史参考区，不是最新中英文母版的子目录。

---

## 2｜当前正式源文本与历史材料

| 职能 | 资料库镜像位置 | Git / Corpus 位置或映射 | 公开边界 |
|---|---|---|---|
| 骨架：新版文明结构算法 | `chinese/文明结构/`；`English/structural-algorithm/` | 据构建脚本：仓库同级 `index/structural-algorithm/{chinese,english}/` | 未公开正式母版；不要自行发布总结构 |
| 说明书：组织经济学 | `chinese/组织经济学/`；`English/organisation_economics/` | `docs/essays/{chinese,english}/organisation_economics/` | 活动 MkDocs 导航；各14个页面 |
| 其他深入展开 | `chinese/中国现实世界/`、`中国未来世界/`、`人力架构/`、`札记/`、`English/framework/`、`English/industrial-people/` 等 | 按下文完整活动导航逐条确认 | 具体文章按当前公开状态分别判断 |
| 旧版文明结构 | `旧材料/文明结构/{china,english}/` | 不作为当前 Corpus 正文或新版骨架路径 | 旧 01a、Layer 0—9 仅供历史研究 |
| 旧版生产力经济学 | `旧材料/生产力经济学/{chinese,english}/` | 旧 `productive-forces-economics/` 不在当前活动导航 | 退休参考，不再当作正式说明书 |

**新版骨架每种语言26篇独立材料：** 校验规则、核心术语、共同00、中国线01—11、西方线01—11、共同12。  
**新版说明书每种语言14篇活动页面：** index、校验规则、核心术语、00—10。  
构建脚本、README、内部合订本不计入上述数量。

### 被替换的旧路径，不要恢复成当前正式入口

```text
# 历史性路径／仅旧版引用
index/structural-algorithm/...旧 Layer 0—9 / 01a 的旧稿命名
# 不要因为旧版名称含“最终版”就覆盖新版组织形态骨架

docs/essays/english/productive-forces-economics/
docs/essays/chinese/productive-forces-economics/
# 旧经济学不再是活动目录；若 Git 物理文件仍在 docs/，须另查构建结果
```

不要把旧 PFE 10 称为当前骨架必需的结构桥；旧 01a 不是新版缺失章节。

---

## 3｜实际网站 MkDocs 快照

以下字段来自本次上传的 `mkdocs.yml`，并非从记忆推断：

```yaml
site_name: Longview Archive
site_url: https://longview-archive.org
site_author: Aster Vale
theme:
  name: material
  language: en
exclude_docs: |
  memo/file_map.md
  memo/theory-map.md
extra_css:
  - stylesheets/extra.css
```

**当前九个网站顶层导航区：** Home；Start Here；Framework；The Economics of Productive Organisation；The Human Architecture of Industrialization；Standalone Essays；Series；Archive；Chinese。

**活动导航 Markdown 路径：189 个、189 个不同路径**（按本次上传的 YAML 计算）；其中组织经济学中英文共28个、其余活动网页161个。这个数是导航引用数，**不是**经文件存在检查或在线部署验证过的“可访问文章总量”。

骨架没有进入活动公开导航。旧生产力经济学在 YAML 中只有注释条目，没有活动导航引用。

**重要安全区别：** 注释导航 ≠ 物理文件不公开。MkDocs 仍可能把 `docs/` 中未列导航的 Markdown 构建为网页；旧稿、完整骨架、内部合订本应从公开 `docs/` 物理隔离，或有明确 `exclude_docs` 规则并用实际部署验证。此次 `exclude_docs` 仅显式列出两份 Memo，不得误以为它排除了其他内部稿。

---

## 4｜AI Corpus / Bootstrap 的当前输入规则

本次上传的 `script/build_corpus.py` 对应 Git 中默认位置 `longview-archive/scripts/build_corpus.py`；具体使用时以 Git 真实文件为准。

```text
CURRENT CORPUS
├── CIVILIZATIONAL_STRUCTURAL_ALGORITHM_SKELETON
│   └── index/structural-algorithm/{chinese,english}/
│       两种语言各26篇独立新骨架源文本
├── ORGANISATION_ECONOMICS_OPERATING_MANUAL
│   └── 当前 mkdocs.yml 活动导航中的中英文组织经济学
│       两种语言各14篇
└── YAML_ACTIVE_PUBLIC_ARTICLES
    └── 当前活动导航中剩余的公开文章
```

脚本默认：

```text
repo:        ../longview-archive/
mkdocs:      longview-archive/mkdocs.yml
docs:        longview-archive/docs/
structural:  ../index/structural-algorithm/
output:      ../index/current/corpus/
```

这是**脚本相对于 repo 的示意关系**，不是要求把用户上传的资料库镜像复制到同名本地目录。

`build_corpus.py` 的源白名单只收新版骨架的独立文件与活动 YAML 的文章正文；它跳过旧 `productive-forces-economics/`、注释导航、未在导航中的 Markdown、私人备忘录、合订本和旧 `index/publish` 输入。注意：**Corpus 排除 ≠ MkDocs 网站排除**，两者是不同系统。

上传资料库不等于完整 Git 仓库；尚未用资料库镜像运行完整的 `mkdocs build` 或实际 Corpus 重建，不能据此声称零缺失或部署已同步。

### 2026-09-20 已有 Corpus 历史快照

此前生成的 `Longview_Corpus_2026-09-20_162308.md` 报告：52（骨架）＋28（说明书）＋161（其他活动文章）＝241份正文。该数字仅用来核对当时输入政策；以后重新生成应以新的 Bootstrap 诊断和 Git 源文件为准。

---

## 5｜对外投稿与工作区边界

| 资料库位置 | 职能 |
|---|---|
| `/Longview/对外投稿/EHS/` | EHS 稿件与管理材料；已完成摘要提交及论文准备，不重列为“待写稿” |
| `/Longview/对外投稿/Phenomenal_World/` | 对应投稿方向的中文及英文工作稿 |
| `/Longview/对外投稿/rome cfp/` | 对应会议方向的稿件与材料 |
| `/Longview/对外投稿/SSRN/` | SSRN 完成稿与相关材料；不从文件夹名推断平台审核结果 |
| `/Longview/对外投稿/reddit/` | 中英文独立短文及局部论证 |
| `/Longview/对外投稿/substack-medium/` | 六个英文对外系列与平台发布材料 |
| `/Longview/对外投稿/投稿备忘录/` | 外部联系策略、发布分工、相关内部备忘 |
| `/Longview/投稿与对外联络登记.md` | 投稿及接触记录；以登记日期与实际回执为状态依据 |
| `/Longview/工作文件夹/母版材料/` | 欧洲、人力架构、历史与尚在推进的综合稿 |
| `/Longview/工作文件夹/AI/` | AI 与知识方法论专题稿 |
| `/Longview/工作文件夹/临时文件夹/` | 临时材料，不能自动升级为母版 |

一个论文或专题即使已经在工作文件夹成熟，也只有用户确认、存入正式位置并完成所需校准后才成为当前母版。不同平台的发布稿不是新的基础理论层。

---

## 6｜每次修改时的最小同步流程

1. 确认改变的是**骨架、说明书、深入展开、旧材料、投稿工作区**中的哪一个。
2. 新版母版／历史稿的移动先确定 Git 的真实物理路径，再更新本 Memo；资料库镜像与 Git 需分别核对。
3. 涉及理论定位时，同步 `memo/theory-map.md`；正文冲突以相应最新版母版为准。
4. 涉及网站导航、公开路径时，同步 Git `mkdocs.yml`、内部相对链接和必要的 sitemap。
5. 将不应公开的旧稿、完整骨架和内部合订本从 `docs/` 物理隔离或显式排除，不能只注释 nav。
6. 运行 `mkdocs build`，核查警告和实际生成输出；如改变 Corpus 输入，重新运行 `scripts/build_corpus.py` 并看 diagnostics。
7. Git commit/push 与资料库镜像更新是**两次不同的操作**。检查二者版本以后，再称它们“同步”。

### 新聊天阅读顺序

```text
memo/file_map.md        → 路径、来源、公开状态、旧材料分界
memo/theory-map.md      → 骨架、说明书、其他深入展开
最新版具体母版章节      → 需要讨论的机制
对应历史资料／专题稿     → 证据、反例和新问题
旧材料/                 → 仅在研究演进或另有指定时打开
```

---

## 7｜当前活动 `mkdocs.yml` 完整导航引用（自动核对清单）

下列条目原样按已上传 YAML 的**活动配置**展开；路径均相对于 Git 公共网站的 `docs/`，不应当被解释为资料库镜像内部路径。其主要作用是供重新命名、移动、发布后逐一定位，**不是**新的理论层级清单。

- Home → `index.md`
- **Start Here**
  - Reader Map → `essays/english/framework/reader-map.md`
  - Common Ground → `essays/english/framework/common-ground.md`
  - Core Terms → `essays/english/framework/core-terms-eng.md`
- **Framework**
  - Framework Overview → `essays/english/framework/index.md`
  - Productive Forces and Civilization → `essays/english/framework/geography-productive-forces-and-civilization.md`
  - Civilizational Metabolism → `essays/english/framework/civilizational-metabolism.md`
  - Absorptive Capacity → `essays/english/framework/absorptive-capacity.md`
  - Surplus, Absorption, and Reproduction → `essays/english/framework/surplus-absorption-and-reproduction.md`
  - Value Capture and the Western System → `essays/english/framework/western-system.md`
- **The Economics of Productive Organisation**
  - Overview → `essays/english/organisation_economics/index.md`
  - Reading and Verification Rules → `essays/english/organisation_economics/Reading_and_Verification_Rules.md`
  - Core Terms → `essays/english/organisation_economics/Core_Terms.md`
  - 00｜The Subject and Use of This Manual → `essays/english/organisation_economics/00-The_Subject_and_Use_of_This_Manual.md`
  - 01｜Productive Capacity as Durable Organisational Capability → `essays/english/organisation_economics/01-Productive_Capacity_as_Durable_Organisational_Capability.md`
  - 02｜Production Systems and Interfaces → `essays/english/organisation_economics/02-Production_Systems_and_Interfaces.md`
  - 03｜Failure, Exit, and Restart → `essays/english/organisation_economics/03-Failure_Exit_and_Restart.md`
  - 04｜System Contribution, Price, and Value Capture → `essays/english/organisation_economics/04-System_Contribution_Price_and_Value_Capture.md`
  - 05｜From Growing Demand to Sustainable Orders → `essays/english/organisation_economics/05-From_Growing_Demand_to_Sustainable_Orders.md`
  - 06｜Productive Surplus, Consumption, and Social Absorption → `essays/english/organisation_economics/06-Productive_Surplus_Consumption_and_Social_Absorption.md`
  - 07｜Capabilities That Cannot Simply Wait for the Market → `essays/english/organisation_economics/07-Capabilities_That_Cannot_Simply_Wait_for_the_Market.md`
  - 08｜Localised Correction and Productive Reorganisation → `essays/english/organisation_economics/08-Localised_Correction_and_Productive_Reorganisation.md`
  - 09｜Globalisation, Feedback, and Rebalancing → `essays/english/organisation_economics/09-Globalisation_Feedback_and_Rebalancing.md`
  - 10｜Production–Consumption–Reproduction Circuit → `essays/english/organisation_economics/10-The_Production_Consumption_Reproduction_Circuit.md`
- **The Human Architecture of Industrialization**
  - Overview → `essays/english/industrial-people/index.md`
  - Reading Before → `essays/english/industrial-people/00-reading-before.md`
  - 01｜Before Capital Arrived → `essays/english/industrial-people/01-before-capital-arrived.md`
  - 02｜How Modern Productive Order Traveled Through People → `essays/english/industrial-people/02-spreading-modern-order.md`
  - 03｜What China’s Industrial Results Prove → `essays/english/industrial-people/03-what-industrial-results-prove.md`
  - 04｜Why Capital Cannot Replicate This Preparation → `essays/english/industrial-people/04-why-capital-cannot-replicate.md`
  - Reading After → `essays/english/industrial-people/05-reading-after.md`
- **Standalone Essays**
  - Overview → `essays/english/standalone/standalone_index_en.md`
  - What DoorDash and Uber Eats Can Teach You About Economics → `essays/english/standalone/economics-101-via-doordash-and-uber-eats.md`
  - China+1 101: Whose Capability Are You Actually Trying to Move? → `essays/english/standalone/china_plus_one_101_en.md`
- **Series**
  - **Frontiers**
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
  - **Architecture of Production**
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
  - **Boundaries of Development**
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
  - **Value Capture**
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
  - **China and Production Burden**
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
  - **Technology Amplifier**
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
- **Archive**
  - Author → `author.md`
  - Copyright → `copyright.md`
- **Chinese**
  - 中文总览 → `essays/chinese/index.md`
  - 核心术语 → `essays/chinese/core-terms-chinese.md`
  - 阅读规则 → `essays/chinese/reading-rules.md`
  - **组织经济学**
    - 总览 → `essays/chinese/organisation_economics/index.md`
    - 阅读与校验规则 → `essays/chinese/organisation_economics/阅读与校验规则.md`
    - 核心术语 → `essays/chinese/organisation_economics/核心术语.md`
    - 00｜说明书的对象与读法 → `essays/chinese/organisation_economics/00-说明书的对象与读法.md`
    - 01｜生产力如何成为持续的组织能力 → `essays/chinese/organisation_economics/01-生产力如何成为持续的组织能力.md`
    - 02｜生产系统与接口如何共同组织经济 → `essays/chinese/organisation_economics/02-生产系统与接口如何共同组织经济.md`
    - 03｜失败退出与重启 → `essays/chinese/organisation_economics/03-失败退出与重启.md`
    - 04｜系统贡献价格与价值捕获 → `essays/chinese/organisation_economics/04-系统贡献价格与价值捕获.md`
    - 05｜从需求增长到持续订单 → `essays/chinese/organisation_economics/05-从需求增长到持续订单.md`
    - 06｜生产富余消费与社会承接 → `essays/chinese/organisation_economics/06-生产富余消费与社会承接.md`
    - 07｜不能只等待市场的能力 → `essays/chinese/organisation_economics/07-不能只等待市场的能力.md`
    - 08｜局部纠错与生产重组 → `essays/chinese/organisation_economics/08-局部纠错与生产重组.md`
    - 09｜全球化成功反馈与重新配重 → `essays/chinese/organisation_economics/09-全球化成功反馈与重新配重.md`
    - 10｜一条生产消费再生产闭环 → `essays/chinese/organisation_economics/10-一条生产消费再生产闭环.md`
  - **工业化的人力架构**
    - 总览 → `essays/chinese/industrial-people/index.md`
    - 阅读前约束 → `essays/chinese/industrial-people/00-reading-before.md`
    - 01｜在资本到来之前：中国经历了什么 → `essays/chinese/industrial-people/01-before-capital-arrived.md`
    - 02｜把能够理解工厂的人铺向全国 → `essays/chinese/industrial-people/02-spreading-modern-order.md`
    - 03｜中国的工业结果证明了什么 → `essays/chinese/industrial-people/03-what-industrial-results-prove.md`
    - 04｜为什么资本不能复制这段准备 → `essays/chinese/industrial-people/04-why-capital-cannot-replicate.md`
    - 阅读后约束 → `essays/chinese/industrial-people/05-reading-after.md`
  - **Reality｜现实世界**
    - 阅读前约束 → `essays/chinese/reality/00-c-reading-before.md`
    - 01｜人类文明的三种底层模式 → `essays/chinese/reality/01-c-three-patterns-civilization.md`
    - 02｜中国制度不是消费机器，而是做功机器 → `essays/chinese/reality/02-c-china-sys-work-not-consume.md`
    - 03｜全球南方不是第二个中国 → `essays/chinese/reality/03-c-global-south-not-second-china.md`
    - 04｜中国不能把自己的生存方式当作世界答案 → `essays/chinese/reality/04-c-china-unique-way-not-world-answer.md`
    - 05｜成熟市场为什么不愿承接中国工业 2.0 → `essays/chinese/reality/05-c-mature-markets-reject-china-industry2.md`
    - 06｜不限制生产，只限制变现 → `essays/chinese/reality/06-c-prod-free-circulation-restricted.md`
    - 07｜热战不是最优解 → `essays/chinese/reality/07-c-hotwar-not-opt-solution.md`
    - 08｜中国出海进入秩序闭环阶段 → `essays/chinese/reality/08-c-overseas-invest-closed-loop.md`
    - 09｜从做功机器到闭环机器 → `essays/chinese/reality/09-c-production-consumption-lifecycle.md`
    - 10｜中国是开放问题，西方是封闭策略 → `essays/chinese/reality/10-c-china-open-west-closed.md`
    - 阅读后约束 → `essays/chinese/reality/11-c-reading-after.md`
  - **Future Path｜未来之路**
    - 阅读前约束 → `essays/chinese/future/00-c-reading-before.md`
    - 01｜人类文明的三种底层模式 → `essays/chinese/future/01-c-three-patterns-civilization.md`
    - 02｜中国制度不是消费机器，而是做功机器 → `essays/chinese/future/02-c-china-sys-work-not-consume.md`
    - 03｜全球南方不是第二个中国 → `essays/chinese/future/03-c-global-south-not-second-china.md`
    - 04｜中国不能把自己的生存方式当作世界答案 → `essays/chinese/future/04-c-china-unique-way-not-world-answer.md`
    - 05｜成熟市场为什么不愿承接中国工业 2.0 → `essays/chinese/future/05-c-mature-markets-reject-china-industry2.md`
    - 06｜不限制生产，只限制变现 → `essays/chinese/future/06-c-prod-free-circulation-restricted.md`
    - 07｜热战不是最优解 → `essays/chinese/future/07-c-real-marketwar-target-monetize-not-factories.md`
    - 08｜美国收缩低成本全球秩序 → `essays/chinese/future/08-c-post-pax-americana-order.md`
    - 09｜打破闭环与建立闭环 → `essays/chinese/future/09-c-the-edge-of-tomorrow.md`
    - 10｜阅读后约束 → `essays/chinese/future/10-c-reading-after.md`
  - **独立短文**
    - 总览 → `essays/chinese/standalone/standalone_index_zh.md`
    - 从美团和饿了么看懂西方经济学101 → `essays/chinese/standalone/economics-101-meituan-and-eleme-zh.md`
    - 中国+1 ：到底是搬谁的东西 → `essays/chinese/standalone/china_plus_one_101_zh.md`
  - **中文札记**
    - 札记总览 → `essays/notes/chinese/index.md`
    - **扩张的边界**
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
    - **兜底文明**
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
    - **生产的边界**
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

## 8｜本次快照检验记录

```text
SOURCE:     上传版 mkdocs.yml（2026-09-23）
ACTIVE_NAV: 189
UNIQUE_MD:  189
MANUAL:     28
OTHER_NAV:  161
OLD_PFE_ACTIVE: 0
STRUCTURAL_CORE_ACTIVE: 0
```

下一次如导航变化，请从真实 Git `mkdocs.yml` 重新生成第7节及上述计数，不要只在旧计数上加减。

Longview Archive｜观势档案 · Internal File Map · 2026-09-23
