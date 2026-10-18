# dsh-eve-widget（伊薇余额挂件）

DeepSeek Harness（DSH）界面右下角的**伊薇**余额挂件。这是 [dsh-whale-widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) **0.3.17** 的个人定制分支：把原版角色换成了伊薇兔，点击音效换成「伊薇」语音并支持随机，任务结束音随机播放，动图换成伊薇 gif 随机池。

## 一键安装

把下面这行**原样发给你的 DSH**（桌面客户端或 `dsh web` 均可），agent 会自动完成下载与安装：

```text
安装 github:13liuthirteen/dsh-eve-widget#v0.1.1
```

> 已经装了原版鲸鱼挂件？没关系，两者可并存互不影响（见下文「与原插件并存的说明」）。

## 与上游（dsh-whale-widget 0.3.17）的差异

|项|上游原版|本分支（伊薇）|
|-|-|-|
|角色本体|`DSniang1.png`（AI 生成形象）|`DSniang1.png` = 使用者提供的 **伊薇.png**（610×610 重采样，保留透明通道）|
|按压/松开音效|预设组「小黄鸭」「音效1」（Ya/D 系列 mp3）|预设组 **「伊薇·单音」**（伊薇10 前半 = 按压、后半 = 松开）与 **「伊薇·随机」**（按压每次从 伊薇1\~11 随机抽一条，不连续重复；松开静音）。出厂默认随机|
|任务结束音|内置 A / Minecraft·经验球|**随机**：每次结束从 伊薇1\~11 抽一条（默认选中「伊薇·随机」组）|
|提问/授权提示默认音|`exp\_orb`|伊薇1（出厂仍默认静音、只冒泡）|
|gif 动图（二次点击 gif 槽 / petpet 泡泡图）|单张 `rua.gif` / `bubble-petpet.gif`|**17 张 gif 随机池**（`assets/gifpool/`，每次展示随机抽一张，服务端不连续重复；gif 来源：案山子）|
|余额预警配图|`bubble-money1.gif`|`bubble-notoken.gif` = **没token了.gif**|
|随机台词|原版台词|「好模型→啥子」「好女孩→啥兔子」等 11 处替换 + 删除 1 句（详见 PROVENANCE.md）|
|界面文字|原版称谓|全部改为 伊薇|
|备用整图 `DSniang02.png` / 展示图 `DSH2.png`|随包|已删除|
|命名空间|`/dsh-whale/\*` 路由、`whale-\*` 资源目录、`.dshw-\*` 数据文件|`/dsh-eve/\*`、`eve-\*`、`.eve-\*` —— **与原插件完全隔离，可并存**|

账号/记账/泡泡编辑器/多厂商余额/吸附拖拽等其余功能与上游 0.3.17 完全一致（继承全部上游修复与安全边界）。

## 安装

### 前提

* **无需安装原版 `dsh-whale-widget`**——本插件完全独立（自带路由、素材与记账内核副本，零依赖）。若已安装原版，二者并存互不影响。

### 方式 A：官方桌面客户端（Electron）

桌面端读的是 `desktop` profile，**不能用** `dsh plugin --profile web`。正确做法是在桌面端会话里让 DSH 自己装（它会调用内置 `plugin\_manager`），比如说一句「把 dsh-eve-widget 装上」，插件源给本目录的绝对路径（`link:` 安装会在 profile 里软链到本目录，改代码即时生效）。

等价的手工路径（不推荐，桌面端自管理）：在本机 `%USERPROFILE%\\.dsh\\profiles\\desktop` 目录里用客户端自带的 pnpm 执行 `pnpm add link:<本目录绝对路径>`，再把 `dsh-eve-widget` 加入该 profile `package.json` 的 `dsh.profile.bundles`，重启客户端。

装完后：

* 新装通常热生效；没出现就**重开一次客户端**（上游也有同样已知问题，issue #162）
* 宿主侧改动（`lib/`）需重启客户端；前端改动（`assets/eve-widget.js`）硬刷新页面即可

### 方式 B：Web（`dsh web`）

```powershell
dsh plugin --profile web add link:<本目录绝对路径>
# 若之前装过同名插件先卸载：dsh plugin --profile web remove dsh-eve-widget
```

装完重启 `dsh web` 并 F5。

### 方式 C：从 GitHub 仓库安装

把本目录推上 GitHub 后，任何人（或你自己的其他机器）都可以直接用 git spec 安装——DSH 的插件管理器原生接受 `github:`/`git+https` 形式的安装 spec（内部就是 pnpm）：

```text
github:<用户名>/dsh-eve-widget            # 跟踪默认分支
github:<用户名>/dsh-eve-widget#v0.1.1     # 钉住某个 tag（推荐）
```

* 桌面端：在 DSH 会话里说「安装 github:<用户名>/dsh-eve-widget#v0.1.1」（走内置 plugin\_manager），或在插件管理界面粘贴该 spec。
* Web 端：`dsh plugin --profile web add github:<用户名>/dsh-eve-widget#v0.1.1`。
* **私有仓库也能装**：安装走本机 git（凭据管理器认证）。素材说明：本仓库 `assets/` 为**二创素材**——语音取自游戏《二重螺旋》（Duet Night Abyss），图片与 gif 为同人二创作品（见 PROVENANCE.md），按同人惯例**非商业**随包分发并保留完整出处标注；公开/私有均可，如权利人提出异议会立即下架相关素材。

发布新版本的流程：

```powershell
# 1. 改完代码，提版本号（package.json 的 version）
# 2. 生成/刷新市场索引文件 market.json（自动填入版本号与当前 commit）
python tools/update-market.py
# 3. 提交 + 打 tag + 推送
git add -A; git commit -m "release v0.1.1"
git tag v0.1.1; git push origin main --tags
```

### 方式 D（可选）：让插件出现在「发现」页

DSH 插件市场的「发现」页读取**可自定义的市场索引 URL**（一个 format 1 的 JSON 文件，http/https、无凭据、无查询串）。把下面这份 `market.json` 放进仓库（`tools/update-market.py` 会自动生成），推送后 raw URL 即可作为索引源：

```text
https://raw.githubusercontent.com/<用户名>/dsh-eve-widget/main/market.json
```

在客户端「插件市场 / 发现」的索引设置里添加该 URL，即可搜索并一键安装（安装时按索引里钉死的 commit 走 `git+https`）。索引里只放元数据，不含素材文件；仓库设为私有则索引无法公开托管（raw 需要认证），此时请用方式 C。



## 与原插件并存的说明

* 路由：本插件全部接口走 `/dsh-eve/\*`（原插件 `/dsh-whale/\*`），互不干扰
* 数据：外观/账本/泡泡配置等全部落在独立的 `.eve-\*.json` 与 `eve-roles/`、`eve-audio/`、`eve-bubble-imgs/` 目录；**记账从零起算**，两个挂件各自独立记账
* 环境变量：`EVE\_TRUSTED\_HOSTS` / `EVE\_ADMIN\_HOSTS`（缺省回落读上游同名的 `DSHW\_\*`，即沿用同一台机器的既有配置）
* localStorage / 提示卡 DOM id / 全局哨兵均已改名，两套挂件可同时拖拽、同时冒泡

## 验证

```
# 端口以本机为准：web 默认 3080；桌面端端口随机（每次启动变化，见客户端设置/标题栏）
curl http://127.0.0.1:3080/dsh-eve/balance.json        # 401/403 = 路由已注册（信任栅栏在工作）
curl http://127.0.0.1:3080/dsh-eve/widget.js           # 同上
curl "http://127.0.0.1:3080/dsh-eve/audio-fragment.wav?id=eve10"   # 伊薇10 片段
```

浏览器 F5 后右下角出现伊薇；点按出随机伊薇音；一轮回答结束随机播一条伊薇；二次点击泡泡按权重出「随机语句」或 gif 池动图。

## 目录结构

```
dsh-eve-widget/
├── package.json              # dsh-eve-widget 元数据（bundle patch 指向 cordis.patch.yml）
├── cordis.patch.yml          # 插件挂载声明（id: dsh-eve-widget）
├── LICENSE / PROVENANCE.md   # MIT 许可（含上游版权行）/ 素材与改动溯源
├── market.json               # 插件市场索引（tools/update-market.py 生成，首次 push 前生成）
├── tools/
│   └── update-market.py      # 刷新 market.json（版本号 + commit + 远端地址自动填入）
├── lib/
│   ├── index.js              # 宿主侧本体（/dsh-eve/\* 路由 + 记账 + 伊薇音效/gif 池服务）
│   └── accounting.mjs        # 记账内核（与上游一致）
└── assets/
    ├── eve-widget.js         # 前端挂件本体
    ├── DSniang1.png          # 伊薇本体（610×610）
    ├── eve01..11.wav        # 伊薇 1-11（48kHz 单声道 16bit PCM，静音裁剪 + 峰值归一 -3dBFS）
    ├── eve10-press.wav      # 伊薇10 前半（0.02-0.64s，按压音）
    ├── eve10-release.wav    # 伊薇10 后半（0.86-1.16s，松开音）
    ├── bubble-notoken.gif    # 余额预警默认配图（没token了.gif 压缩版，gif 来源：案山子）
    └── gifpool/g01..g17.gif  # 17 张伊薇 gif 随机池（300×300，128 色重编码；gif 来源：案山子）
```

## 卸载

```powershell
# Web profile
dsh plugin --profile web remove dsh-eve-widget
# 桌面端：在会话里让 DSH 卸载，或从 profile 的 bundles 里移除后重启
```

数据目录（`\~/.dsh/eve-\*`、`.eve-\*.json`）按需手工删除。

## 参考与致谢（这个分支站在谁的肩膀上）

* **上游本体**：[MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget)（作者 **MeteorNOX**，`main` 分支 v0.3.17，MIT）。本分支的全部核心功能——余额取数与峰谷定价、小记账内核（amounting 定点运算、余额观测/校正账本）、泡泡模块化编辑器、音效组/片段体系、角色图库、多厂商 API 模板、信任栅栏与 0.3.15/0.3.16/0.3.17 的安全/音量修复——均直接继承自上游代码，本分支只做了**命名空间隔离、素材替换、伊薇随机音效池、gif 随机池**四类改动。
* **上游 README 记录的贡献者**：@ztzpro（标准化插件包结构）、@under-the-ocean（自动发布 npm）、@21253soursweetlemon（gif 降级/滚动条避让/位置记忆）、@fangbm（多币种、周末谷价、记账币种感知）、@xiaolinnnnnnn（Windows 桌面端重构）、@Yang-huai406（充值记账修复方案）、@yybai25（DSH 账号登录态读余额）、星丶白羽莲（凭据安全报告）、@Jy-EggRoll（提问/授权提示音 #160/#161）、@VaeKaras（下载管理器问题 #158）、@MengLs1620（桌面端重启实测 #162）、@0Sakura721（记账分本 #163）、@ELFsay（OpenCode Go 订阅额度 #99）以及上游 README 致谢节里那位做了音量滑块完整代码分析的 QQ 群友。
* **DSH 插件体系**：`dsh bundle` + `cordis.patch.yml` 挂载、`tapIndex` / `webserver/index-inject` 双通道注入的用法参考上游实现与 DSH 官方文档。
* **价格参考**：DeepSeek 官方定价页（峰谷时段与 CNY/百万 tokens 价目，见上游 `lib/index.js` 顶部 `PRICING` 注释）。

素材说明（均**不在 MIT 覆盖范围内**，为二创/同人素材，详见 [PROVENANCE.md](PROVENANCE.md)）：

* **伊薇语音**（eve01–11 及切分片段）：来自游戏**《二重螺旋》（Duet Night Abyss）**的角色语音，版权归游戏开发商及发行商所有
* **伊薇立绘**：同人二创作品，由使用者收集提供
* **全部 gif**（`gifpool/` 17 张与 `bubble-notoken.gif`）：gif 来源 案山子（同人二创），由使用者收集提供

以上均按同人惯例以非商业个人装饰用途使用，并保留出处标注。如你是相关权利人（游戏官方或二创作者），希望调整授权或要求移除，请开 issue（见 PROVENANCE.md「权利主张」）。

## 许可证

代码：**MIT**（继承自上游，版权行见 [LICENSE](LICENSE)；本分支的修改同样以 MIT 提供）。
素材：不属于 MIT 范围，按 PROVENANCE.md 单独说明。

