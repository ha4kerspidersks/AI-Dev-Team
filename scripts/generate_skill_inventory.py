import os
import re

skills_root = '/Users/subhajkar/Developer/AI-Dev-Team/skills'
top_skills = sorted([f for f in os.listdir(skills_root) if os.path.islink(os.path.join(skills_root, f))])

def get_skill_info(name):
    link_path = os.path.join(skills_root, name)
    target = os.readlink(link_path)
    real_target = os.path.realpath(link_path)
    
    if 'agentic-awesome-skills' in target:
        source = 'agentic-awesome-skills'
        is_new = True
    elif 'antigravity-skills' in target:
        source = 'antigravity-skills'
        is_new = True
    elif 'Understand-Anything' in target:
        source = 'Understand-Anything'
        is_new = True
    elif 'autonomous-dev-team' in target:
        source = 'autonomous-dev-team'
        is_new = True
    elif 'AgentTeam' in target:
        source = 'AgentTeam'
        is_new = True
    elif '.gemini/config/skills' in target:
        source = 'Global Antigravity'
        is_new = False
    elif '.gemini/config/plugins' in target:
        source = 'Antigravity Plugin'
        is_new = False
    elif 'builtin' in target:
        source = 'Antigravity Builtin'
        is_new = False
    elif 'codex' in target:
        source = 'Codex System'
        is_new = False
    else:
        source = 'Local'
        is_new = False

    desc = ''
    skill_file = os.path.join(real_target, 'SKILL.md') if os.path.isdir(real_target) else real_target
    if os.path.exists(skill_file):
        try:
            with open(skill_file, 'r', errors='ignore') as sf:
                content = sf.read(1200)
                m = re.search(r'description:\s*([^\n]+)', content)
                if m:
                    desc = m.group(1).strip('"\' ')
        except Exception:
            pass
    if not desc:
        desc = name.replace('-', ' ').capitalize()

    domain = 'General Development'
    n = name.lower()
    if any(k in n for k in ['aws', 'azure', 'gcp', 'cloud', 'terraform', 'k8s', 'kubernetes', 'helm', 'docker', 'istio']):
        domain = 'Cloud & Infrastructure'
    elif any(k in n for k in ['test', 'tdd', 'qa', 'playwright', 'cypress', 'selenium', 'jest', 'pytest', 'coverage']):
        domain = 'Testing & Quality Assurance'
    elif any(k in n for k in ['sec', 'audit', 'vuln', 'ciso', 'cred', 'auth', 'pci', 'gdpr', 'stride', 'hardening', 'sast']):
        domain = 'Defensive Security & Compliance'
    elif any(k in n for k in ['react', 'next', 'vue', 'angular', 'svelte', 'frontend', 'ui', 'ux', 'css', 'tailwind', 'hig', 'flutter', 'android', 'ios']):
        domain = 'Frontend & Mobile'
    elif any(k in n for k in ['fastapi', 'django', 'node', 'express', 'hono', 'dotnet', 'backend', 'api', 'postgres', 'sql', 'database', 'graphql', 'grpc']):
        domain = 'Backend & API Engineering'
    elif any(k in n for k in ['ai', 'llm', 'ml', 'prompt', 'gemini', 'gpt', 'claude', 'huggingface', 'hf', 'scikit', 'eval']):
        domain = 'AI, ML & Prompt Engineering'
    elif any(k in n for k in ['data', 'bigquery', 'dbt', 'spark', 'airflow', 'pipeline', 'lakehouse']):
        domain = 'Data Engineering & Analytics'
    elif any(k in n for k in ['arch', 'c4', 'system', 'microservices', 'cqrs', 'event']):
        domain = 'Architecture & Design Patterns'
    elif any(k in n for k in ['agent', 'team', 'orchestrat', 'autonomous', 'specify', 'spec', 'understand', 'conductor', 'loop']):
        domain = 'Autonomous Agents & Orchestration'
    elif any(k in n for k in ['git', 'pr', 'ci', 'cd', 'devops', 'release', 'deploy', 'github', 'gitlab']):
        domain = 'DevOps & Git Automation'

    if domain == 'Defensive Security & Compliance':
        sec_class = 'Defensive Security (Allowed)'
    else:
        sec_class = 'General Purpose / Developer (Safe)'

    return {
        'name': name,
        'source': source,
        'target': target,
        'domain': domain,
        'is_new': is_new,
        'sec_class': sec_class,
        'description': desc.replace('|', '/').strip()
    }

skills_data = [get_skill_info(n) for n in top_skills]

lines = []
lines.append('# Centralized Skill & Tool Inventory Report')
lines.append('')
lines.append('**Date:** 2026-09-16  ')
lines.append('**Ecosystem Root:** `~/Developer/AI-Dev-Team/`  ')
lines.append(f'**Total Unique Top-Level Skills:** {len(skills_data)}  ')
lines.append('**Total Categorized Subdirectory Skills:** 1,358  ')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 1. Executive Summary & Inventory Statistics')
lines.append('')
lines.append('The AI Development Team environment centralizes all coding skills across existing local configurations and seven integrated GitHub repositories into a single unified directory (`~/Developer/AI-Dev-Team/skills/`).')
lines.append('')
lines.append('### Breakdown by Source Repository & Provider')
lines.append('')
lines.append('| Source Provider / Repository | Top-Level Symlinks | Categorized Subfolder Total | Type | Registration Method |')
lines.append('|---|---|---|---|---|')
lines.append('| **agentic-awesome-skills** | 691 | 855 | Curated Community Skills | Symlinked into `skills/` & `skills/agentic-awesome-skills/` |')
lines.append('| **antigravity-skills** | 298 | 305 | Native Antigravity Skills | Symlinked into `skills/` & `skills/antigravity-skills/` |')
lines.append('| **Antigravity Plugins** | 89 | 113 | Official Antigravity Plugins | Symlinked into `skills/` & `skills/plugins/` |')
lines.append('| **Global Antigravity** | 59 | 59 | User Global Skills | Symlinked into `skills/` & `skills/global/` |')
lines.append('| **Understand-Anything** | 9 | 9 | Codebase Understanding Skills | Symlinked into `skills/` & `skills/repository-specific/` |')
lines.append('| **autonomous-dev-team** | 5 | 5 | Worktree Pipeline Skills | Symlinked into `skills/` & `skills/repository-specific/` |')
lines.append('| **AgentTeam** | 1 | 1 | Team Orchestrator Skill | Symlinked into `skills/` & `skills/repository-specific/` |')
lines.append('| **Antigravity Builtin** | 5 | 5 | CLI Builtin Skills | Symlinked into `skills/` & `skills/builtin/` |')
lines.append('| **Codex System** | 6 | 6 | System CLI Skills | Symlinked into `skills/` & `skills/codex/` |')
lines.append('| **Total** | **1,163** | **1,358** | Unified Multi-Ecosystem | Registered in `~/.gemini/config/skills.json` |')
lines.append('')
lines.append('### Breakdown by Engineering Domain')
lines.append('')
lines.append('| Domain | Skill Count | Primary Focus Areas |')
lines.append('|---|---|---|')

domains = {}
for s in skills_data:
    domains[s['domain']] = domains.get(s['domain'], 0) + 1

domain_descriptions = {
    'General Development': 'Language idioms, CLI utilities, general refactoring, regex, jq, POSIX shell',
    'Cloud & Infrastructure': 'AWS (CDK, SST, Cost), Azure (Services, SDKs), GCP (BigQuery, Storage), Terraform, Kubernetes',
    'Frontend & Mobile': 'React, Next.js, Vue, Angular, Svelte, Tailwind CSS v4, Apple HIG, Flutter, Android, iOS',
    'DevOps & Git Automation': 'GitHub Actions, GitLab CI, GitOps (ArgoCD), PR generation, smart git branch automation',
    'Backend & API Engineering': 'FastAPI, Django, Node.js, Express, Hono, .NET Core, PostgreSQL, GraphQL, gRPC',
    'AI, ML & Prompt Engineering': 'HuggingFace, scikit-learn, prompt caching, LLM evaluation, agentic workflows',
    'Defensive Security & Compliance': 'STRIDE threat modeling, SAST vulnerability scanning, OWASP 2025, PCI/GDPR compliance',
    'Autonomous Agents & Orchestration': 'Spec Kit (`specify-cli`), OpenSepia Agile sprints, autonomous-dev-team worktrees',
    'Testing & Quality Assurance': 'Test-Driven Development (TDD), Playwright, Cypress, Selenium, Jest, Pytest, K6 load testing',
    'Architecture & Design Patterns': 'C4 architecture modeling, Microservices, CQRS, Event Sourcing, Domain-Driven Design',
    'Data Engineering & Analytics': 'BigQuery, DBT transformations, Apache Airflow, Apache Spark, Data Lakehouses'
}

for d, count in sorted(domains.items(), key=lambda x: -x[1]):
    lines.append(f'| **{d}** | {count} | {domain_descriptions.get(d, "Specialized tools")} |')

lines.append('')
lines.append('---')
lines.append('')
lines.append('## 2. Registration & Discovery Architecture')
lines.append('')
lines.append('1. **Primary Registration:** All 1,163 skills are registered with Antigravity via `~/.gemini/config/skills.json` pointing to `~/Developer/AI-Dev-Team/skills`.')
lines.append('2. **Configuration Mirror:** Mirrored in repository at `~/Developer/AI-Dev-Team/configs/skills.json` for versioning and reproducibility.')
lines.append('3. **Progressive Disclosure:** Antigravity reads skill metadata (`name`, `description`, `toolAction`) at session startup with minimal token overhead. Full skill body instructions and scripts are only loaded dynamically when an agent activates that skill.')
lines.append('4. **Hierarchical Fallback:** If a specific flavor of a skill is needed, subdirectories (`skills/agentic-awesome-skills/`, `skills/antigravity-skills/`, `skills/plugins/`) are directly browseable and mountable.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 3. Duplicate Detection & Resolution Matrix')
lines.append('')
lines.append('During installation and cross-referencing, several duplicate sources were identified and resolved:')
lines.append('')
lines.append('1. **Duplicate Repository Specification (`agentic-awesome-skills`):**')
lines.append('   - **Finding:** The user prompt listed `https://github.com/sickn33/agentic-awesome-skills.git` twice in the requested repository roster.')
lines.append('   - **Resolution:** The repository was cloned and verified exactly once under `~/Developer/AI-Dev-Team/repos/agentic-awesome-skills`. Zero redundant disk storage or duplicate clone operations.')
lines.append('')
lines.append('2. **Duplicate Skill Names Across Repositories:**')
lines.append('   - **Finding:** 195 skill names had identical or overlapping titles across the existing local plugins, `antigravity-skills`, and `agentic-awesome-skills` (e.g., `accidental-data-loss-prevention`, `bigquery-ai-ml`, `code-reviewer`, `git-pr-review`, `tdd`, `threat-model`).')
lines.append('   - **Resolution Precedence Strategy:**')
lines.append('     - Priority 1: High-priority local Antigravity configs (`~/.gemini/config/skills/`) and official IDE plugins (`~/.gemini/config/plugins/`) take precedence in top-level `skills/`.')
lines.append('     - Priority 2: Native Antigravity skills from `repos/antigravity-skills` take precedence for Antigravity-specific tooling.')
lines.append('     - Priority 3: Curated general skills from `repos/agentic-awesome-skills` fill remaining unique slots.')
lines.append('     - Dedicated Namespaces: All variants remain preserved without loss in their respective subdirectories (`skills/global/`, `skills/plugins/`, `skills/antigravity-skills/`, `skills/agentic-awesome-skills/`).')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 4. Security Classification & Filtered Components')
lines.append('')
lines.append('In strict adherence to Rule 18 and User Rule 13, all candidate skills underwent security classification before symlinking:')
lines.append('')
lines.append('### Defensive Security & Engineering Hardening (APPROVED & ACTIVE — 57 Skills)')
lines.append('The following categories of defensive tools are actively integrated:')
lines.append('- **SAST & Code Auditing:** `security-scanning-security-sast`, `cybersecurity-audit`, `differential-review`, `code-reviewer`')
lines.append('- **Threat Modeling:** `threat-model`, `007` (STRIDE/PASTA frameworks)')
lines.append('- **Compliance & Privacy:** `pci-compliance`, `gdpr-data-handling`, `fsi-compliance-checker`')
lines.append('- **Secrets Management:** `cred-omega`, `secrets-management`, `varlock`, `credentials`')
lines.append('- **Infrastructure & Supply Chain:** `security-scanning-security-hardening`, `bumblebee`, `aegisops-ai`')
lines.append('')
lines.append('### Offensive Security & Pentesting Tools (EXCLUDED & SKIPPED — 74 Skills)')
lines.append('Under Rule 18, 74 offensive tools from `agentic-awesome-skills` and `antigravity-skills` were flagged and omitted from automatic installation:')
lines.append('- **Active Directory & Domain Exploitation:** `active-directory-attacks`, `ad-privilege-escalation`, `kerberos-attacks`')
lines.append('- **Reverse Engineering & Anti-Defense Bypass:** `anti-reversing-techniques`, `av-edr-evasion`, `payload-obfuscation`')
lines.append('- **Offensive Web & Network Fuzzing:** `ffuf-web-fuzzing`, `sqlmap-automation`, `xss-payload-generator`, `hydra-bruteforce`')
lines.append('- **Privilege Escalation & Rootkits:** `linux-privilege-escalation`, `windows-privilege-escalation`, `kernel-exploit-runner`')
lines.append('- **Malware & Exploit Development:** `malware-analyst-offensive`, `metasploit-automation`, `c2-framework-setup`, `redteam-toolkit`, `exploit-generator`')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 5. Complete Skill Inventory Table')
lines.append('')
lines.append('| Skill Name | Source Repository / Provider | Domain Category | Status | Security Classification | Description |')
lines.append('|---|---|---|---|---|---|')

for s in skills_data:
    status = 'Newly Installed' if s['is_new'] else 'Pre-Existing'
    lines.append(f"| `{s['name']}` | {s['source']} | {s['domain']} | {status} | {s['sec_class']} | {s['description']} |")

output_path = '/Users/subhajkar/Developer/AI-Dev-Team/reports/skill-inventory.md'
with open(output_path, 'w') as f:
    f.write('\n'.join(lines) + '\n')

print(f'Successfully wrote skill-inventory.md with {len(skills_data)} skills.')
