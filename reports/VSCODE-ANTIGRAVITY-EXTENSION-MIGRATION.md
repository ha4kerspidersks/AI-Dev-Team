# VS CODE → ANTIGRAVITY EXTENSION DISCOVERY & COMPATIBILITY MIGRATION REPORT

**Execution Date:** 2026-10-01  
**Host Environment:** Apple Silicon macOS (Darwin)  
**VS Code Target:** `/Applications/Visual Studio Code.app` (v1.111.0, 106 installed extensions)  
**Antigravity Target:** `/Applications/Antigravity IDE.app` (v1.107.0, 73 user + 101 built-in extensions)  
**Master Catalog:** `~/Developer/AI-Dev-Team/Agent-Catalog.xlsx` (Worksheet `17_Extensions`)  
**Timestamped Backup:** `~/Developer/AI-Dev-Team/backups/extension-migration-20261001-101730/`  

---

## 1. Executive Summary & Inventory Totals

- **TOTAL VS CODE EXTENSIONS:** 106
- **TOTAL ANTIGRAVITY EXTENSIONS:** 73 User-Installed (101 Built-in System Extensions, 174 Total)

### Classification Breakdown
- **DIRECTLY COMPATIBLE (Category A):** 27
- **ALREADY PRESENT (Category B):** 11
- **NATIVE ANTIGRAVITY EQUIVALENTS (Category C):** 7
- **REQUIRES CONFIGURATION (Category D):** 9
- **VS CODE ONLY (Category E):** 3
- **INCOMPATIBLE (Category F):** 1
- **UNKNOWN / NOT ON OPEN-VSX (Category G):** 48

### Migration Outcome Totals
- **SUCCESSFULLY MIGRATED:** 36 (27 Category A + 9 Category D)
- **ALREADY PRESENT:** 11 (Category B)
- **SKIPPED:** 59 (7 Category C + 3 Category E + 1 Category F + 48 Category G)
- **FAILED:** 0

---

## 2. Successfully Migrated Extensions (Categories A & D)

| Extension ID | Name | Version | Category | Config Requirement | Repository |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `4ops.terraform` | Terraform | 0.2.5 | A | None (Standard IDE settings) | [vscode-language-terraform](https://github.com/4ops/vscode-language-terraform) |
| `aaron-bond.better-comments` | Better Comments | 3.0.2 | A | None (Standard IDE settings) | [better-comments](https://github.com/aaron-bond/better-comments) |
| `alefragnani.bookmarks` | Bookmarks | 14.1.1 | A | None (Standard IDE settings) | [vscode-bookmarks](https://github.com/alefragnani/vscode-bookmarks) |
| `alefragnani.project-manager` | Project Manager | 13.1.0 | A | None (Standard IDE settings) | [vscode-project-manager](https://github.com/alefragnani/vscode-project-manager) |
| `amazonwebservices.aws-toolkit-vscode` | AWS Toolkit | 4.15.0 | D | AWS CLI & credentials file | [aws-toolkit-vscode](https://github.com/aws/aws-toolkit-vscode) |
| `christian-kohler.npm-intellisense` | npm Intellisense | 1.4.5 | A | None (Standard IDE settings) | [NpmIntellisense](https://github.com/ChristianKohler/NpmIntellisense) |
| `clemenspeters.format-json` | JSON formatter | 1.0.3 | A | None (Standard IDE settings) | [vscode-extension-format-json](https://github.com/clemenspeters/vscode-extension-format-json) |
| `codezombiech.gitignore` | gitignore | 0.10.0 | A | None (Standard IDE settings) | [vscode-gitignore](https://github.com/CodeZombieCH/vscode-gitignore) |
| `cweijan.vscode-office` | Office Viewer | 4.2.0 | A | None (Standard IDE settings) | [vscode-office](https://github.com/cweijan/vscode-office) |
| `dannysteenman.aws-terraform-extension-pack` | AWS Terraform Extension Pack | 1.12.0 | A | None (Standard IDE settings) | [vscode-terraform-extension-pack](https://github.com/towardsthecloud/vscode-terraform-extension-pack) |
| `dannysteenman.iam-actions-snippets` | AWS IAM Actions Snippets | 1.97.0 | A | None (Standard IDE settings) | [vscode-iam-actions-snippets](https://github.com/towardsthecloud/vscode-iam-actions-snippets) |
| `dannysteenman.iam-service-principal-snippets` | AWS IAM Service Principal Snippets | 1.89.0 | A | None (Standard IDE settings) | [vscode-iam-service-principal-snippets](https://github.com/towardsthecloud/vscode-iam-service-principal-snippets) |
| `donjayamanne.githistory` | Git History | 0.6.20 | A | None (Standard IDE settings) | [gitHistoryVSCode](https://github.com/DonJayamanne/gitHistoryVSCode) |
| `eamodio.gitlens` | %gitlens.displayName% | 19.2.0 | A | None (Standard IDE settings) | [vscode-gitlens](https://github.com/gitkraken/vscode-gitlens) |
| `edwinhuish.better-comments-next` | Better Comments Next | 3.5.2 | A | None (Standard IDE settings) | [better-comments-next](https://github.com/edwinhuish/better-comments-next) |
| `felipecaputo.git-project-manager` | Git Project Manager | 1.8.2 | A | None (Standard IDE settings) | [git-project-manager](https://github.com/felipecaputo/git-project-manager) |
| `grapecity.gc-excelviewer` | Spreadsheet Viewer | 4.2.66 | A | None (Standard IDE settings) | [gc-excelviewer](https://github.com/wijmo/gc-excelviewer) |
| `hashicorp.terraform` | HashiCorp Terraform | 2.40.0 | D | Terraform binary on PATH | [vscode-terraform](https://github.com/hashicorp/vscode-terraform) |
| `james-yu.latex-workshop` | LaTeX Workshop | 10.19.0 | D | MacTeX / TeX Live on PATH | [LaTeX-Workshop](https://github.com/James-Yu/LaTeX-Workshop) |
| `mhutchie.git-graph` | Git Graph | 1.30.0 | A | None (Standard IDE settings) | [vscode-git-graph](https://github.com/mhutchie/vscode-git-graph) |
| `ms-kubernetes-tools.vscode-kubernetes-tools` | Kubernetes | 1.4.1 | D | kubectl & ~/.kube/config | [vscode-kubernetes-tools](https://github.com/vscode-kubernetes-tools/vscode-kubernetes-tools) |
| `ms-vscode.azurecli` | Azure CLI Tools | 0.6.0 | D | Azure CLI (az) on PATH | [vscode-azurecli](https://github.com/Microsoft/vscode-azurecli) |
| `ms-vscode.hexeditor` | %name% | 1.11.1 | A | None (Standard IDE settings) | [vscode-hexeditor](https://github.com/microsoft/vscode-hexeditor) |
| `nicolasvuillamy.vscode-groovy-lint` | Groovy Lint, Format and Fix | 4.2.1 | D | Groovy / npm-groovy-lint on PATH | [vscode-groovy-lint](https://github.com/nvuillam/vscode-groovy-lint) |
| `numso.prettier-standard-vscode` | Prettier-Standard - JavaScript formatter | 1.0.2 | A | None (Standard IDE settings) | [prettier-standard-vscode](https://github.com/numso/prettier-standard-vscode) |
| `redhat.java` | Language Support for Java(TM) by Red Hat | 1.56.0 | D | Java JDK 17+ on PATH / JAVA_HOME | [vscode-java](https://github.com/redhat-developer/vscode-java) |
| `redhat.vscode-yaml` | YAML | 1.24.0 | A | None (Standard IDE settings) | [vscode-yaml](https://github.com/redhat-developer/vscode-yaml) |
| `vscjava.vscode-gradle` | Gradle for Java | 3.18.0 | D | Java JDK 17+ on PATH / JAVA_HOME | [](https://github.com/microsoft/vscode-gradle/) |
| `vscjava.vscode-java-debug` | Debugger for Java | 0.59.0 | A | None (Standard IDE settings) | [vscode-java-debug](https://github.com/Microsoft/vscode-java-debug) |
| `vscjava.vscode-java-dependency` | Project Manager for Java | 0.27.6 | A | None (Standard IDE settings) | [vscode-java-dependency](https://github.com/Microsoft/vscode-java-dependency) |
| `vscjava.vscode-java-pack` | Extension Pack for Java | 0.31.1 | A | None (Standard IDE settings) | [vscode-java-pack](https://github.com/Microsoft/vscode-java-pack) |
| `vscjava.vscode-java-test` | Test Runner for Java | 0.46.0 | A | None (Standard IDE settings) | [vscode-java-test](https://github.com/Microsoft/vscode-java-test) |
| `vscjava.vscode-maven` | Maven for Java | 0.45.3 | D | Java JDK 17+ on PATH / JAVA_HOME | [vscode-maven](https://github.com/Microsoft/vscode-maven) |
| `vscode-icons-team.vscode-icons` | vscode-icons | 12.19.0 | A | None (Standard IDE settings) | [vscode-icons](https://github.com/vscode-icons/vscode-icons) |
| `vscodevim.vim` | Vim | 1.32.4 | A | None (Standard IDE settings) | [Vim](https://github.com/VSCodeVim/Vim) |
| `yzhang.markdown-all-in-one` | %ext.displayName% | 3.6.3 | A | None (Standard IDE settings) | [vscode-markdown](https://github.com/yzhang-gh/vscode-markdown) |

---

## 3. Pre-Existing Antigravity Extensions (Category B - Already Present)

| Extension ID | Name | VS Code Ver | Antigravity Status | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `golang.go` | Go | 0.56.1 | INSTALLED (0.56.1) | Rich Go language support for Visual Studio Code |
| `googlecloudtools.datacloud` | Google Cloud Data Agent Kit | 0.11.0 | INSTALLED (1.0.0) | Bring the full power of Google Cloud Data Agent Kit (starter pack) to your intelligent IDE |
| `ms-azuretools.vscode-containers` | Container Tools | 2.5.2 | INSTALLED (2.4.5) | Makes it easy to create, manage, and debug containerized applications. |
| `ms-python.debugpy` | Python Debugger | 2026.6.0 | INSTALLED (2026.6.0) | Python Debugger extension using debugpy. |
| `ms-python.python` | Python | 2026.4.0 | INSTALLED (2026.4.0) | Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, f |
| `ms-python.vscode-python-envs` | Python Environments | 1.38.0 | INSTALLED (1.20.1) | Provides a unified python environment experience |
| `ms-toolsai.jupyter` | Jupyter | 2025.9.1 | INSTALLED (2025.9.1) | Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more. |
| `ms-toolsai.jupyter-keymap` | Jupyter Keymap | 1.1.2 | INSTALLED (1.1.2) | Jupyter keymaps for notebooks |
| `ms-toolsai.jupyter-renderers` | Jupyter Notebook Renderers | 1.3.0 | INSTALLED (1.3.0) | Renderers for Jupyter Notebooks (with plotly, vega, gif, png, svg, jpeg and other such outputs) |
| `ms-toolsai.vscode-jupyter-cell-tags` | Jupyter Cell Tags | 0.1.9 | INSTALLED (0.1.9) | Jupyter Cell Tags support for VS Code |
| `ms-toolsai.vscode-jupyter-slideshow` | Jupyter Slide Show | 0.1.6 | INSTALLED (0.1.6) | Jupyter Slide Show support for VS Code |

---

## 4. Skipped Extensions & Detailed Rationale

### 4.1 Native Antigravity Equivalents (Category C - 7 Extensions)
These extensions provide AI assistant, autonomous agent, or code completion capabilities that directly duplicate Antigravity native Gemini intelligence, Ponytail, Copilot Bridge, or the active `~/Developer/AI-Dev-Team/` orchestrator. In accordance with Phase 8 directives, they were intentionally skipped to protect system stability.

| Extension ID | Name | Reason / Native Antigravity Equivalent |
| :--- | :--- | :--- |
| `kingleo.qwen` | Qwen | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `lod-inc.qwen-commit` | Qwen Commit | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `openai.chatgpt` | Codex – OpenAI’s coding agent | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `openai.codex-audio` | Codex Audio | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `qwenlm.qwen-code-vscode-ide-companion` | Qwen Code Companion | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `vscjava.migrate-java-to-azure` | GitHub Copilot modernization | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |
| `yyyumeniku.vscode-codeqwen-copilot` | Qwen Copilot addon | Replaced by Antigravity Native Gemini Agent & AI-Dev-Team Multi-Model Gateway |

### 4.2 VS Code Proprietary Extensions (Category E - 3 Extensions)
These extensions contain proprietary Microsoft EULA restrictions, telemetry hooks, or VS Code-specific internal APIs that fail or violate licensing in non-Microsoft VS Code distributions:

- `ms-python.vscode-pylance`: Microsoft proprietary language server with strict runtime license check against official Microsoft VS Code binaries. Antigravity uses **Pyrefly (`meta.pyrefly`)** and standard Python LSP.
- `ms-edgedevtools.vscode-edge-devtools`: Proprietary Microsoft Edge browser integration; Antigravity utilizes native Chrome DevTools Protocol (CDP port 9004).
- `matheusq94.tfs`: Proprietary Microsoft Team Foundation Server integration requiring legacy VS Code bindings.

### 4.3 Incompatible Extensions (Category F - 1 Extension)
- `firefox-devtools.vscode-firefox-debug`: Deprecated by Mozilla in 2021; incompatible with modern VS Code / Electron 32+ debug adapter protocols.

### 4.4 Marketplace-Exclusive Extensions (Category G - 48 Extensions)
Antigravity IDE connects to the open, vendor-neutral **Eclipse Open VSX Registry** (`https://open-vsx.org`). Extensions below are published exclusively to Microsoft's closed marketplace. Per strict instructions, unpacked folder copying was bypassed to prevent corrupted state or broken native binaries.

| Extension ID | Name | Publisher | Repository |
| :--- | :--- | :--- | :--- |
| `breaking-point.vsc-postman` | vsc-postman | breaking-point | [vsce-postman](https://github.com/breaking-point/vsce-postman) |
| `codetown-1.note-extension` | Note Extension | Codetown-1 | [note-extension](https://github.com/yourusername/note-extension) |
| `connorslade.note-utils` | note-utils | connorslade | [note-utils](https://github.com/Basicprogrammer10/note-utils) |
| `csholmq.excel-to-markdown-table` | Excel to Markdown table | csholmq | [vscode-excel-to-markdown-table](https://github.com/csholmq/vscode-excel-to-markdown-table) |
| `dautroc.simple-note-vscode` | Simple Note | dautroc | [simple-note-vscode](https://github.com/dautroc/simple-note-vscode) |
| `david-rickard.git-diff-and-merge-tool` | Git Diff and Merge Tool | david-rickard | [VSCodeGitDiffAndMergeTool](https://github.com/RandomEngy/VSCodeGitDiffAndMergeTool) |
| `denwin.terraform-extension-pack` | Terraform Extension Pack | denwin | [vscode_terraform-extension-pack](https://github.com/DenWin/vscode_terraform-extension-pack) |
| `donjayamanne.git-extension-pack` | Git Extension Pack | donjayamanne | [git-extension-pack](https://github.com/DonJayamanne/git-extension-pack) |
| `dwarfpenguin.postman-generator` | postman-generator | dwarfpenguin | SOURCE: UNVERIFIED |
| `ekeel.groovy-beautify` | Groovy Beautify | ekeel | [vscode-groovy-beautify](https://github.com/ekeel/vscode-groovy-beautify) |
| `eridem.vscode-postman` | Postman Runner | eridem | [vscode-postman](https://github.com/eridem/vscode-postman) |
| `eriklynd.json-tools` | JSON Tools | eriklynd | SOURCE: UNVERIFIED |
| `hb432.prettier-eslint-typescript` | Prettier ESLint TypeScript Formatter | hb432 | SOURCE: UNVERIFIED |
| `iamgabs.terraform-gcp-snippets` | Terraform Snippets | iamgabs | [terraform-snippets](https://github.com/iamgabs/terraform-snippets) |
| `igorsbitnev.error-gutters` | Error Gutters | IgorSbitnev | [error-gutters](https://github.com/PinkaminaDianePie/error-gutters) |
| `jinxdash.prettier-rust` | Prettier - Code formatter (Rust) | jinxdash | [prettier-plugin-rust](https://github.com/jinxdash/prettier-plugin-rust) |
| `julientahon.groovy-vscode` | Groovy Language Support | JulienTAHON | [groovy-vscode](https://github.com/djukxe/groovy-vscode) |
| `khaeransori.json2csv` | JSON to CSV | khaeransori | [vscode-json2csv](https://github.com/khaeransori/vscode-json2csv) |
| `l2fprod.terraform-fork` | Terraform (forked) | l2fprod | [vscode-terraform](https://github.com/l2fprod/vscode-terraform) |
| `leytonoday.ghost-note` | Ghost Note | leytonoday | [GhostNote](https://github.com/leytonoday/GhostNote) |
| `mathematic.vscode-latex` | LaTeX | mathematic | [vscode-latex](https://github.com/mathematic-inc/vscode-latex) |
| `meezilla.json` | JSON | Meezilla | [json](https://gitlab.meezilla.com/Meezilla/json) |
| `mgtrrz.terraform-completer` | Terraform Completer | mgtrrz | [terraform-completer](https://github.com/mgtrrz/terraform-completer) |
| `mohsen1.prettify-json` | Prettify JSON | mohsen1 | [vscode-prettify-json](https://github.com/git@github.com:mohsen1/vscode-prettify-json) |
| `mrcodingb.postman-collection-explorer` | Postman Collection Explorer | MrCodingB | [Postman-Collection-Explorer-VS-Code](https://github.com/MrCodingB/Postman-Collection-Explorer-VS-Code) |
| `ms-mssql.data-workspace-vscode` | Data Workspace | ms-mssql | [azuredatastudio](https://github.com/Microsoft/azuredatastudio) |
| `ms-mssql.mssql` | SQL Server (mssql) | ms-mssql | [vscode-mssql](https://github.com/Microsoft/vscode-mssql) |
| `ms-mssql.sql-bindings-vscode` | %displayName% | ms-mssql | [azuredatastudio](https://github.com/Microsoft/azuredatastudio) |
| `ms-mssql.sql-database-projects-vscode` | SQL Database Projects | ms-mssql | [vscode-mssql](https://github.com/Microsoft/vscode-mssql) |
| `ms-vscode-remote.remote-containers` | %displayName% | ms-vscode-remote | [vscode-remote-release](https://github.com/Microsoft/vscode-remote-release) |
| `noahcanadea.terraform-toolbox` | Terraform Toolbox | NoahCanadea | [vscode-terraform-toolbox](https://github.com/Noahnc/vscode-terraform-toolbox) |
| `oferkafry.easy-terraform-commands` | Terraform Plus | oferkafry | [vscode-ext-tf](https://github.com/oferca/vscode-ext-tf) |
| `parthr2031.colorful-comments` | Colorful Comments | ParthR2031 | [Colorful-Comments](https://github.com/Parth2031/Colorful-Comments) |
| `phplasma.csv-to-table` | CSV to Table | phplasma | [csv-to-table](https://github.com/Plasma/csv-to-table) |
| `pjmiravalle.terraform-advanced-syntax-highlighting` | Terraform Advanced Syntax Highlighting | pjmiravalle | [vscode-terraform-advanced-syntax-highlighting](https://github.com/pjmiravalle/vscode-terraform-advanced-syntax-highlighting) |
| `quicktype.quicktype` | Paste JSON as Code | quicktype | [quicktype](https://github.com/glideapps/quicktype) |
| `redhat.vscode-rsp-ui` | Runtime Server Protocol UI | redhat | [vscode-rsp-ui](https://github.com/redhat-developer/vscode-rsp-ui) |
| `repreng.csv` | CSV | ReprEng | [csv](https://github.com/jonaraphael/csv) |
| `richardwillis.vscode-spotless-gradle` | Spotless Gradle | richardwillis | [](https://github.com/badsyntax/vscode-spotless-gradle/) |
| `run-at-scale.terraform-doc-snippets` | Terraform doc snippets | run-at-scale | [vscode-terraform-doc-snippets](https://github.com/run-at-scale/vscode-terraform-doc-snippets) |
| `swark.swark` | Swark | swark | [swark](https://github.com/swark-io/swark) |
| `tecosaur.latex-utilities` | LaTeX Utilities | tecosaur | [LaTeX-Utilities](https://github.com/tecosaur/LaTeX-Utilities) |
| `wraith13.bracket-lens` | Bracket Lens | wraith13 | [bracket-lens-vscode](https://github.com/wraith13/bracket-lens-vscode) |
| `wycliffepepela.live-postman` | Live PostMan | wycliffePepela | [vscode-live-PostMan](https://github.com/pepelawycliffe/vscode-live-PostMan) |
| `xk0der.vsc-postman-collection-syntax` | Postman Collection Syntax Highlighter | xk0der | [vscode-postman-collection-syntax](https://github.com/xk0der/vscode-postman-collection-syntax) |
| `xk0der.vsc-postman-logs-syntax` | Postman Log Syntax Highlighter | xk0der | [vscode-postman-log-syntax](https://github.com/xk0der/vscode-postman-log-syntax) |
| `zainchen.json` | json | ZainChen | [vscode-json](https://github.com/ZainChen/vscode-json) |
| `ziyasal.vscode-open-in-github` | Open in GitHub, Bitbucket, Gitlab, VisualStudio.com ! | ziyasal | [vscode-open-in-github](https://github.com/ziyasal/vscode-open-in-github) |

---

## 5. Settings Migration (Phase 5)

Antigravity `settings.json` was safely merged with portable, developer-focused preferences from VS Code:

### Migrated Settings
- `workbench.iconTheme`: `"vscode-icons"` (leveraging migrated `vscode-icons-team.vscode-icons`)
- `editor.wordWrap`: `"on"`
- `editor.formatOnSave`: `true`
- `editor.formatOnPaste`: `true`
- `editor.accessibilitySupport`: `"off"`
- `workbench.editor.empty.hint`: `"hidden"`
- `terraform.codelens.referenceCount`: `true`
- `terminal.integrated.fontFamily`: `"MesloLGS NF"`
- `security.promptForLocalFileProtocolHandling`: `false`
- `chat.instructionsFilesLocations`: Multi-repo rules enabled (`.github/instructions`, `.claude/rules`, `~/.copilot/instructions`)
- `chat.agentHost.sdkSandbox.enabled`: `"on"`
- `google.cloud.project`: `"dashboard-e3fcb"`
- `redhat.telemetry.enabled`: `true`
- `jdk.telemetry.enabled`: `true`
- `aws.cloudformation.telemetry.enabled`: `true`

### Preserved Critical Settings (Untouched)
- `auto-accept.cdpPort`: `9004` (Guarantees CDP auto-accept daemon connectivity)
- `antigravity-mpa.cdpPort`: `9004`
- `python.languageServer`: `"Default"` (Guarantees Pyrefly / Jedi fallback)

### Intentionally Filtered Settings
- Windows-specific executable paths (`vs-kubernetes` Minikube/Helm/Kubectl pointing to `C:\Users\...`)
- Temporary Postman markdown paths (`C:\Users\...\AppData\Local\Temp`)
- Third-party formatters not installed in Antigravity (`rvest.vs-code-prettier-eslint`, `ms-mssql.mssql`)

---

## 6. Keyboard Shortcuts Migration (Phase 6)

Audit of VS Code `keybindings.json` identified one custom developer keybinding:
```json
[
  {
    "key": "shift+enter",
    "command": "workbench.action.terminal.sendSequence",
    "when": "terminalFocus",
    "args": {
      "text": "\u001b\r"
    }
  }
]
```
**Conflict Check:** Antigravity had no prior `keybindings.json`. The keybinding was created directly with **0 conflicts**.

---

## 7. Workspace & Profile Analysis (Phase 7)

- **Profiles Detected:** Only the default single profile (`builtin`) exists in VS Code.
- **Primary Workspace:** `~/Developer`
- **Ecosystem Preservation:** Full language coverage provided for Python, Java, JavaScript/TypeScript, Terraform, YAML, JSON, Git, GitHub, Docker, Kubernetes, AWS, and Azure.

---

## 8. Extension Health & System Verification (Phase 9)

- **Manifest & Dependency Validation:** 100% of the 73 user extensions pass manifest integrity and dependency validation.
- **Built-in Extensions:** `vscode.git`, `vscode.docker`, and `vscode.yaml` provided by Antigravity core satisfy all container and language requirements.
- **CDP Port 9004:** Fully preserved in `~/.antigravity-ide/argv.json` and `settings.json`.
- **AI-Dev-Team & Copilot Bridge:** Untouched and healthy; no overlapping agent conflict.
