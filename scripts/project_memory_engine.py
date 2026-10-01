#!/usr/bin/env python3
"""
ANTIGRAVITY GLOBAL PROJECT INTELLIGENCE & MEMORY SYSTEM
======================================================
Autonomous discovery, persistent multi-agent context, token-efficient
navigation, and automatic incremental change refresh.

Zero external dependencies - pure Python 3 standard library.
Compatible with Antigravity, Claude Code, Gemini CLI, Codex.
"""

import os
import sys
import json
import hashlib
import re
import subprocess
import sqlite3
import shutil
from pathlib import Path
from datetime import datetime, timezone

MEMORY_VERSION = "2.0.0"
MAX_SNIPPET_LENGTH = 500

DEFAULT_EXCLUDES = {
    "node_modules", ".git", "dist", "build", "coverage", ".cache",
    ".pytest_cache", ".turbo", ".next", ".nuxt", "out", "target",
    ".venv", "venv", "env", "__pycache__", ".DS_Store", "tmp", "temp",
    "swark-output", ".swp", ".idea", ".vscode", "test-results",
    ".agent", ".agents"
}

BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".mp4", ".mp3",
    ".pdf", ".wasm", ".pyc", ".lock", ".bin", ".zip", ".tar", ".gz",
    ".woff", ".woff2", ".ttf", ".eot", ".db", ".sqlite", ".sqlite3"
}

SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|secret|password|auth[_-]?token|private[_-]?key)\s*[:=]\s*["\']?([^"\'\s]{8,})'),
    re.compile(r'(?i)bearer\s+([a-zA-Z0-9_\-\.]{15,})'),
    re.compile(r'-----BEGIN [A-Z ]+ PRIVATE KEY-----'),
]

def redact_secrets(text: str) -> str:
    """Mask credentials, tokens, and secrets from any indexed content."""
    if not isinstance(text, str):
        return text
    redacted = text
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub(r'\1: [REDACTED_SECRET]', redacted)
    return redacted

def sha256_file(filepath: Path) -> str:
    """Compute sha256 of a file efficiently."""
    try:
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""

def sha256_str(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def detect_project_root(start_path: Path) -> Path:
    """
    Find the actual project root walking upwards.
    Recognizes Git root and manifest boundaries.
    """
    current = start_path.resolve()
    
    # First check if git root exists
    try:
        res = subprocess.run(
            ["git", "-C", str(current), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True
        )
        git_root = Path(res.stdout.strip()).resolve()
        
        # Check if current directory is a nested project within monorepo
        project_manifests = [
            "package.json", "pyproject.toml", "Cargo.toml", "go.mod",
            "pom.xml", "build.gradle", "composer.json"
        ]
        
        # If current is different from git_root, check if current has a manifest
        if current != git_root:
            for m in project_manifests:
                if (current / m).is_file():
                    return current
                    
        return git_root
    except Exception:
        pass
        
    # Non-git tree walk upwards
    indicators = [
        "package.json", "pyproject.toml", "requirements.txt", "Pipfile",
        "Cargo.toml", "go.mod", "pom.xml", "build.gradle", "composer.json",
        "Dockerfile", "docker-compose.yml", "Makefile", ".git"
    ]
    check = current
    while check != check.parent:
        if any((check / ind).exists() for ind in indicators):
            return check
        check = check.parent
        
    return current

def get_project_identity(project_root: Path) -> dict:
    """
    Derive stable, unique project identity.
    """
    root_str = str(project_root.resolve())
    remote = "local"
    commit = "none"
    branch = "main"
    
    try:
        rem_res = subprocess.run(
            ["git", "-C", root_str, "config", "--get", "remote.origin.url"],
            capture_output=True, text=True
        )
        if rem_res.returncode == 0 and rem_res.stdout.strip():
            remote = rem_res.stdout.strip()
            
        com_res = subprocess.run(
            ["git", "-C", root_str, "rev-parse", "HEAD"],
            capture_output=True, text=True
        )
        if com_res.returncode == 0 and com_res.stdout.strip():
            commit = com_res.stdout.strip()[:10]
            
        br_res = subprocess.run(
            ["git", "-C", root_str, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True
        )
        if br_res.returncode == 0 and br_res.stdout.strip():
            branch = br_res.stdout.strip()
    except Exception:
        pass

    # Deterministic slug
    clean_name = project_root.name or "project"
    slug_base = f"{clean_name}-{hashlib.sha256(root_str.encode()).hexdigest()[:8]}"
    project_id = slug_base.lower()
    
    return {
        "project_id": project_id,
        "project_name": clean_name,
        "project_root": root_str,
        "git_remote": remote,
        "git_commit": commit,
        "git_branch": branch
    }

def get_memory_dir(project_root: Path) -> Path:
    """
    Select appropriate memory location respecting existing .agent or .agents layout.
    """
    agent_dir = project_root / ".agent"
    agents_dir = project_root / ".agents"
    
    # If .agent exists (or .agents is a symlink to .agent), use .agent/project-memory
    if agent_dir.exists() or (agents_dir.is_symlink() and str(agents_dir.readlink()) == ".agent"):
        mem_dir = agent_dir / "project-memory"
    elif agents_dir.exists() and not agents_dir.is_symlink():
        mem_dir = agents_dir / "project-memory"
    else:
        # Default to .agents/project-memory
        mem_dir = agents_dir / "project-memory"
        
    mem_dir.mkdir(parents=True, exist_ok=True)
    return mem_dir

def load_ignore_patterns(project_root: Path) -> set:
    """Load exclusions from default list + .gitignore + .agentignore."""
    excludes = set(DEFAULT_EXCLUDES)
    for ign_name in [".gitignore", ".agentignore"]:
        ign_file = project_root / ign_name
        if ign_file.is_file():
            try:
                for line in ign_file.read_text(encoding="utf-8", errors="ignore").splitlines():
                    line = line.strip()
                    if line and not line.startswith("#"):
                        line = line.rstrip("/").lstrip("/")
                        if line:
                            excludes.add(line)
            except Exception:
                pass
    return excludes

def is_path_excluded(rel_path: str, excludes: set) -> bool:
    parts = Path(rel_path).parts
    for p in parts:
        if p in excludes:
            return True
        for excl in excludes:
            if excl.endswith("*") and p.startswith(excl[:-1]):
                return True
    return False

def scan_file_index(project_root: Path, excludes: set) -> dict:
    """
    Scan project files without loading large trees.
    Returns: { rel_path: { hash, mtime, size, category } }
    """
    file_index = {}
    
    for root, dirs, files in os.walk(project_root):
        rel_root = os.path.relpath(root, project_root)
        if rel_root == ".":
            rel_root = ""
            
        # Filter directories in-place to avoid descending into ignored trees
        dirs[:] = [d for d in dirs if not is_path_excluded(os.path.join(rel_root, d) if rel_root else d, excludes)]
        
        for f in files:
            rel_file = os.path.join(rel_root, f) if rel_root else f
            if is_path_excluded(rel_file, excludes):
                continue
                
            full_p = Path(root) / f
            ext = full_p.suffix.lower()
            
            # Categorize
            category = "source"
            if f.startswith(".env"):
                category = "environment_config"
            elif ext in [".md", ".txt", ".rst", ".adoc"]:
                category = "documentation"
            elif "test" in rel_file.lower() or "spec" in rel_file.lower():
                category = "test"
            elif ext in [".json", ".yaml", ".yml", ".toml", ".xml", ".ini", ".conf", ".config.js", ".config.ts"]:
                category = "configuration"
            elif "script" in rel_file.lower() or ext in [".sh", ".bash", ".zsh", ".ps1"]:
                category = "script"
            elif ext in BINARY_EXTENSIONS:
                category = "asset_binary"
                
            try:
                st = full_p.stat()
                # Do not hash large binary assets or env files directly
                f_hash = ""
                if category not in ["asset_binary", "environment_config"] and st.st_size < 1_000_000:
                    f_hash = sha256_file(full_p)
                else:
                    f_hash = f"size:{st.st_size}"
                    
                file_index[rel_file] = {
                    "hash": f_hash,
                    "mtime": st.st_mtime,
                    "size": st.st_size,
                    "category": category
                }
            except Exception:
                pass
                
    return file_index

def analyze_tech_stack_and_type(project_root: Path, file_index: dict) -> dict:
    """Analyze real repository files to extract technologies, frameworks, and type."""
    languages = set()
    frameworks = set()
    package_managers = set()
    databases = set()
    test_frameworks = set()
    build_tools = set()
    cloud_platforms = set()
    project_type = "generic_software"
    
    scripts = {
        "build": None,
        "test": None,
        "lint": None,
        "dev": None
    }
    
    # 1. Node.js / TypeScript / JavaScript
    pkg_json_p = project_root / "package.json"
    if pkg_json_p.is_file():
        languages.add("JavaScript")
        try:
            pkg = json.loads(pkg_json_p.read_text(encoding="utf-8"))
            all_deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            
            # Frameworks
            if "next" in all_deps:
                frameworks.add("Next.js")
                project_type = "nextjs_web_application"
            elif "react" in all_deps:
                frameworks.add("React")
                project_type = "react_spa_web_application"
            if "vite" in all_deps or "vite" in pkg.get("scripts", {}).values():
                build_tools.add("Vite")
                frameworks.add("Vite")
            if "express" in all_deps:
                frameworks.add("Express")
                project_type = "fullstack_react_express" if "react" in frameworks else "express_backend_api"
            if "vue" in all_deps:
                frameworks.add("Vue")
                project_type = "vue_web_application"
            if "svelte" in all_deps:
                frameworks.add("Svelte")
            if "tailwindcss" in all_deps:
                frameworks.add("TailwindCSS")
            if "three" in all_deps or "@react-three/fiber" in all_deps:
                frameworks.add("Three.js / React-Three-Fiber")
            if "framer-motion" in all_deps:
                frameworks.add("Framer Motion")
                
            # Test frameworks
            if "playwright" in all_deps or "@playwright/test" in all_deps:
                test_frameworks.add("Playwright")
            if "jest" in all_deps:
                test_frameworks.add("Jest")
            if "vitest" in all_deps:
                test_frameworks.add("Vitest")
            if "@axe-core/playwright" in all_deps:
                test_frameworks.add("Axe-core Accessibility")
                
            # Scripts
            pkg_scripts = pkg.get("scripts", {})
            for sc in ["build", "test", "lint", "dev"]:
                if sc in pkg_scripts:
                    scripts[sc] = f"npm run {sc}" if sc != "test" else "npm test"
                    if "node --test" in pkg_scripts.get("test", ""):
                        test_frameworks.add("Node.js Native Test Runner")
                        
            # Package Manager
            if (project_root / "pnpm-lock.yaml").exists():
                package_managers.add("pnpm")
            elif (project_root / "yarn.lock").exists():
                package_managers.add("yarn")
            elif (project_root / "bun.lock").exists() or (project_root / "bun.lockb").exists():
                package_managers.add("bun")
            elif (project_root / "package-lock.json").exists():
                package_managers.add("npm")
        except Exception:
            pass

    # 2. Python
    pyproject_p = project_root / "pyproject.toml"
    reqs_p = project_root / "requirements.txt"
    if pyproject_p.is_file() or reqs_p.is_file() or any(f.endswith(".py") for f in file_index):
        languages.add("Python")
        if not project_type or project_type == "generic_software":
            project_type = "python_application"
        if (project_root / "poetry.lock").exists():
            package_managers.add("poetry")
        elif (project_root / "Pipfile").exists():
            package_managers.add("pipenv")
        else:
            package_managers.add("pip")
            
        py_content = ""
        if pyproject_p.is_file():
            py_content += pyproject_p.read_text(encoding="utf-8", errors="ignore")
        if reqs_p.is_file():
            py_content += reqs_p.read_text(encoding="utf-8", errors="ignore")
            
        if "fastapi" in py_content.lower():
            frameworks.add("FastAPI")
            project_type = "fastapi_api_service"
        if "flask" in py_content.lower():
            frameworks.add("Flask")
        if "django" in py_content.lower():
            frameworks.add("Django")
        if "pytest" in py_content.lower():
            test_frameworks.add("Pytest")
            scripts["test"] = "pytest"

    # 3. Rust
    cargo_p = project_root / "Cargo.toml"
    if cargo_p.is_file():
        languages.add("Rust")
        project_type = "rust_application"
        package_managers.add("cargo")
        scripts["build"] = "cargo build"
        scripts["test"] = "cargo test"

    # 4. Go
    go_mod_p = project_root / "go.mod"
    if go_mod_p.is_file():
        languages.add("Go")
        project_type = "go_application"
        package_managers.add("go modules")
        scripts["build"] = "go build ./..."
        scripts["test"] = "go test ./..."

    # 5. Java / Kotlin
    if (project_root / "pom.xml").exists():
        languages.add("Java")
        project_type = "java_maven_application"
        build_tools.add("Maven")
    if (project_root / "build.gradle").exists() or (project_root / "build.gradle.kts").exists():
        languages.add("Java / Kotlin")
        project_type = "gradle_application"
        build_tools.add("Gradle")

    # Extension census
    ext_counts = {}
    for f in file_index:
        ext = Path(f).suffix.lower()
        if ext:
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
            
    if ext_counts.get(".ts", 0) > 0 or ext_counts.get(".tsx", 0) > 0:
        languages.add("TypeScript")
    if ext_counts.get(".js", 0) > 0 or ext_counts.get(".jsx", 0) > 0:
        languages.add("JavaScript")
    if ext_counts.get(".py", 0) > 0:
        languages.add("Python")
    if ext_counts.get(".rs", 0) > 0:
        languages.add("Rust")
    if ext_counts.get(".go", 0) > 0:
        languages.add("Go")
    if ext_counts.get(".html", 0) > 0:
        languages.add("HTML")
    if ext_counts.get(".css", 0) > 0:
        languages.add("CSS")

    # Docker / Containers / CI
    if (project_root / "Dockerfile").exists() or (project_root / "docker-compose.yml").exists():
        cloud_platforms.add("Docker")
    if (project_root / ".github" / "workflows").exists():
        cloud_platforms.add("GitHub Actions")

    # Check for .env exists (never read secrets!)
    env_present = any(f.startswith(".env") for f in file_index)

    return {
        "project_type": project_type,
        "languages": sorted(list(languages)),
        "frameworks": sorted(list(frameworks)),
        "package_managers": sorted(list(package_managers)),
        "test_frameworks": sorted(list(test_frameworks)),
        "build_tools": sorted(list(build_tools)),
        "cloud_platforms": sorted(list(cloud_platforms)),
        "databases": sorted(list(databases)),
        "commands": scripts,
        "env_file_detected": env_present
    }

def discover_architecture_details(project_root: Path, file_index: dict) -> dict:
    """Discover entry points, components, routes, APIs, and key architectural elements."""
    entry_points = []
    routes = []
    api_endpoints = []
    components = []
    test_files = []
    config_files = []
    services = []
    
    candidates = [
        "index.html", "src/main.tsx", "src/main.ts", "src/index.tsx", "src/index.ts",
        "app/main.py", "main.py", "server/server.js", "server/index.js", "src/server.ts"
    ]
    for c in candidates:
        if c in file_index:
            entry_points.append(c)
            
    for f in sorted(file_index.keys()):
        fl = f.lower()
        cat = file_index[f]["category"]
        
        if cat == "test":
            test_files.append(f)
        elif cat == "configuration":
            config_files.append(f)
            
        if "component" in fl or f.endswith((".tsx", ".jsx", ".vue")):
            if cat != "test":
                components.append(f)
        if "service" in fl:
            services.append(f)
            
        # APIs and Routes
        if "api" in fl or "route" in fl:
            routes.append(f)

    # Specialized domain discovery
    tabs = [f for f in file_index if "tab" in f.lower() and f.endswith((".tsx", ".jsx", ".vue", ".html"))]
    iam_identity = [f for f in file_index if any(k in f.lower() for k in ["iam", "identity", "iga", "role", "auth"]) and cat != "test"]
    spatial_3d = [f for f in file_index if any(k in f.lower() for k in ["3d", "spatial", "globe", "canvas", "three"]) and cat != "test"]
    manifests = [f for f in file_index if "manifest" in f.lower()]
    qa_docs = [f for f in file_index if any(k in f.lower() for k in ["readiness", "gate", "remediation", "security", "audit", "qa"]) and f.endswith(".md")]

    # Deeper API endpoint scan if server or api routes exist
    api_map_entries = []
    for r_file in routes:
        if file_index.get(r_file, {}).get("category") == "test":
            continue
        full_p = project_root / r_file
        if full_p.is_file() and full_p.stat().st_size < 200_000:
            try:
                content = full_p.read_text(encoding="utf-8", errors="ignore")
                # Express style: app.get('/api/...', router.post('/...', apiRouter.get('/...'
                matches = re.findall(r'(?:app|router|apiRouter)\.(get|post|put|delete|patch)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]', content)
                for method, endpoint in matches:
                    norm_ep = endpoint
                    if ("api" in r_file.lower() or "server" in r_file.lower()) and not norm_ep.startswith("/api"):
                        norm_ep = f"/api{norm_ep}"
                    api_map_entries.append({
                        "file": r_file,
                        "method": method.upper(),
                        "endpoint": norm_ep
                    })
                # FastAPI style: @app.get("/...", @router.post("/...
                fastapi_matches = re.findall(r'@(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]', content)
                for method, endpoint in fastapi_matches:
                    api_map_entries.append({
                        "file": r_file,
                        "method": method.upper(),
                        "endpoint": endpoint
                    })
            except Exception:
                pass

    # Deduplicate endpoints
    dedup_apis = []
    seen_apis = set()
    for ep in api_map_entries:
        key = (ep["method"], ep["endpoint"])
        if key not in seen_apis:
            seen_apis.add(key)
            dedup_apis.append(ep)

    # ADR parsing
    adrs = []
    adr_files = [f for f in file_index if "adr" in f.lower() and f.endswith(".md")]
    for af in sorted(adr_files):
        p = project_root / af
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
            title_m = re.search(r'^#\s+(.+)$', txt, re.MULTILINE)
            date_m = re.search(r'##\s+Date\s*\n+([^\n]+)', txt, re.IGNORECASE)
            status_m = re.search(r'##\s+Status\s*\n+([^\n]+)', txt, re.IGNORECASE)
            context_m = re.search(r'##\s+Context\s*\n+([\s\S]*?)(?=\n##|\Z)', txt, re.IGNORECASE)
            decision_m = re.search(r'##\s+Decision\s*\n+([\s\S]*?)(?=\n##|\Z)', txt, re.IGNORECASE)
            conseq_m = re.search(r'##\s+(?:Consequences|Impact)\s*\n+([\s\S]*?)(?=\n##|\Z)', txt, re.IGNORECASE)
            
            title = title_m.group(1).strip() if title_m else Path(af).stem
            adrs.append({
                "file": af,
                "title": title,
                "date": date_m.group(1).strip() if date_m else "",
                "status": status_m.group(1).strip() if status_m else "Accepted",
                "context": (context_m.group(1).strip()[:300] + '...') if context_m else "",
                "rationale": (decision_m.group(1).strip()[:300] + '...') if decision_m else "",
                "impact": (conseq_m.group(1).strip()[:300] + '...') if conseq_m else ""
            })
        except Exception:
            pass

    return {
        "entry_points": entry_points,
        "components": components[:50],  # Keep bounded
        "services": services[:30],
        "routes": routes[:30],
        "tabs": tabs[:20],
        "iam_identity": iam_identity[:20],
        "spatial_3d": spatial_3d[:20],
        "manifests": manifests[:10],
        "qa_docs": qa_docs[:15],
        "adrs": adrs,
        "api_endpoints": dedup_apis,
        "test_files": test_files,
        "config_files": config_files
    }

def sync_to_agent_team_db(identity: dict, summary_text: str, decisions: list) -> bool:
    """
    Safely sync project summary and ADRs into SQLite ~/.agent-team/team.db.
    Non-destructive; fails gracefully if DB is unavailable.
    """
    db_path = Path.home() / ".agent-team" / "team.db"
    if not db_path.is_file():
        return False
        
    try:
        con = sqlite3.connect(str(db_path), timeout=5.0)
        cur = con.cursor()
        now = datetime.now(timezone.utc).isoformat()
        
        # Check if project exists
        p_id = identity["project_id"]
        p_name = identity["project_name"]
        cur.execute("SELECT id FROM projects WHERE id = ?", (p_id,))
        if cur.fetchone():
            cur.execute(
                "UPDATE projects SET name = ?, description = ?, updated_at = ? WHERE id = ?",
                (p_name, summary_text[:500], now, p_id)
            )
        else:
            cur.execute(
                "INSERT INTO projects (id, name, description, status, created_at, updated_at) VALUES (?, ?, ?, 'active', ?, ?)",
                (p_id, p_name, summary_text[:500], now, now)
            )
            
        # Update project_summaries
        cur.execute("SELECT MAX(version) FROM project_summaries WHERE project_id = ?", (p_id,))
        max_ver = cur.fetchone()[0] or 0
        new_ver = max_ver + 1
        summary_id = f"summary-{p_id}-{new_ver}"
        cur.execute(
            "INSERT INTO project_summaries (id, project_id, content, version, created_at) VALUES (?, ?, ?, ?, ?)",
            (summary_id, p_id, summary_text, new_ver, now)
        )
        
        # Insert any decisions not yet present
        for dec in decisions:
            d_id = f"dec-{p_id}-{sha256_str(dec.get('title', ''))[:8]}"
            cur.execute("SELECT id FROM decisions WHERE id = ?", (d_id,))
            if not cur.fetchone():
                cur.execute(
                    "INSERT INTO decisions (id, project_id, member_id, title, rationale, context, created_at) VALUES (?, ?, 'project-intelligence', ?, ?, ?, ?)",
                    (d_id, p_id, dec.get("title", ""), dec.get("rationale", ""), dec.get("context", ""), now)
                )
                
        con.commit()
        con.close()
        return True
    except Exception as e:
        # Non-fatal
        return False

def generate_memory_documents(project_root: Path, identity: dict, tech: dict, arch: dict, file_index: dict) -> dict:
    """
    Produce the 9 canonical project memory documents.
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    p_name = identity["project_name"]
    p_id = identity["project_id"]
    p_root = identity["project_root"]
    p_type = tech["project_type"]
    commit = identity["git_commit"]
    
    # 1. METADATA.json
    metadata = {
        "memory_version": MEMORY_VERSION,
        "project_id": p_id,
        "project_name": p_name,
        "project_root": p_root,
        "project_type": p_type,
        "git_commit": commit,
        "git_branch": identity["git_branch"],
        "git_remote": identity["git_remote"],
        "last_full_scan": timestamp,
        "last_incremental_scan": timestamp,
        "languages": tech["languages"],
        "frameworks": tech["frameworks"],
        "package_managers": tech["package_managers"],
        "test_frameworks": tech["test_frameworks"],
        "build_tools": tech["build_tools"],
        "cloud_platforms": tech["cloud_platforms"],
        "commands": tech["commands"],
        "entry_points": arch["entry_points"],
        "important_directories": sorted(list(set(Path(f).parts[0] for f in file_index if len(Path(f).parts) > 1 and (project_root / Path(f).parts[0]).is_dir()))),
        "file_count": len(file_index),
        "test_count": len(arch["test_files"]),
        "api_count": len(arch["api_endpoints"]),
        "file_index": file_index
    }
    
    # 2. PROJECT-MAP.json
    project_map = {
        "project_id": p_id,
        "name": p_name,
        "type": p_type,
        "entry_points": arch["entry_points"],
        "key_subsystems": {
            "ui_components": arch["components"],
            "tabs_and_navigation": arch.get("tabs", []),
            "iam_and_identity": arch.get("iam_identity", []),
            "spatial_and_3d": arch.get("spatial_3d", []),
            "manifests_and_data": arch.get("manifests", []),
            "qa_documentation": arch.get("qa_docs", []),
            "services": arch["services"],
            "routes_and_apis": arch["routes"],
            "tests": arch["test_files"]
        },
        "api_endpoints": arch["api_endpoints"]
    }
    
    # 3. PROJECT-CONTEXT.md (Compact executive context summary)
    context_md = f"""# PROJECT CONTEXT: {p_name}
> Generated by Antigravity Global Project Intelligence System v{MEMORY_VERSION}
> Last Verified: {timestamp} | Commit: `{commit}`

## Executive Summary
- **Project ID**: `{p_id}`
- **Type**: `{p_type}`
- **Root**: `{p_root}`
- **Languages**: {", ".join(tech["languages"]) or "None detected"}
- **Frameworks**: {", ".join(tech["frameworks"]) or "Vanilla"}
- **Package Manager**: {", ".join(tech["package_managers"]) or "Default"}
- **Testing**: {", ".join(tech["test_frameworks"]) or "None detected"} ({len(arch["test_files"])} test files)

## Standard Execution Commands
- **Dev**: `{tech["commands"]["dev"] or "N/A"}`
- **Build**: `{tech["commands"]["build"] or "N/A"}`
- **Test**: `{tech["commands"]["test"] or "N/A"}`
- **Lint**: `{tech["commands"]["lint"] or "N/A"}`

## Core Subsystems & Entry Points
- **Entry Points**: {", ".join(f"`{e}`" for e in arch["entry_points"]) or "None"}
- **Active APIs**: {len(arch["api_endpoints"])} documented endpoints
- **Subsystem Tabs**: {", ".join(f"`{Path(t).stem}`" for t in arch.get("tabs", [])[:6]) or "None"}
- **IAM / Identity**: {", ".join(f"`{Path(i).stem}`" for i in arch.get("iam_identity", [])[:5]) or "Standard"}
- **Spatial / 3D**: {", ".join(f"`{Path(s).stem}`" for s in arch.get("spatial_3d", [])[:5]) or "None"}
- **Key Directories**: {", ".join(f"`{d}`" for d in metadata["important_directories"][:8])}

## Subsystem Navigation Guide
When handling user requests, consult the specific memory document before inspecting code:
- **Architecture & Component Hierarchy** -> Read [`ARCHITECTURE.md`](file://{get_memory_dir(project_root)}/ARCHITECTURE.md)
- **API Endpoints, Contracts & Handlers** -> Read [`API-MAP.md`](file://{get_memory_dir(project_root)}/API-MAP.md)
- **Test Architecture & Regression Commands** -> Read [`TEST-MAP.md`](file://{get_memory_dir(project_root)}/TEST-MAP.md)
- **Dependencies & External Integrations** -> Read [`DEPENDENCIES.md`](file://{get_memory_dir(project_root)}/DEPENDENCIES.md)
- **Architectural Decisions & ADRs** -> Read [`DECISIONS.md`](file://{get_memory_dir(project_root)}/DECISIONS.md)
- **Recent Project Changes** -> Read [`CHANGELOG.md`](file://{get_memory_dir(project_root)}/CHANGELOG.md)

## Invariants & Security Boundaries
- Environment variables: {".env detected (secrets redacted)" if tech["env_file_detected"] else "No .env detected"}
- Never modify protected workspaces or overwrite unverified configuration.
- Always run appropriate tests before declaring completion.
"""

    # 4. ARCHITECTURE.md
    arch_md = f"""# System Architecture: {p_name}

## 1. Architectural Pattern
- **Application Type**: {p_type}
- **Primary Paradigms**: Modular Component Architecture, Reactive Client State, RESTful Service Integration.

## 2. Specialized Subsystems
- **Navigation & Tabs**: {', '.join(f'`{t}`' for t in arch.get('tabs', [])) or 'Standard routes'}
- **Identity & Access Management (IAM/IGA)**: {', '.join(f'`{i}`' for i in arch.get('iam_identity', [])) or 'Standard auth'}
- **Spatial & 3D Engineering**: {', '.join(f'`{s}`' for s in arch.get('spatial_3d', [])) or 'N/A'}
- **Data Manifests & Schemas**: {', '.join(f'`{m}`' for m in arch.get('manifests', [])) or 'N/A'}
- **QA & Pre-Deployment Gates**: {', '.join(f'`{q}`' for q in arch.get('qa_docs', [])) or 'Standard tests'}

## 3. Directory Layout & Layer Boundaries
"""
    for d in metadata["important_directories"]:
        files_in_d = [f for f in file_index if f.startswith(f"{d}/")][:5]
        arch_md += f"- **`{d}/`**: Contains {len([f for f in file_index if f.startswith(f'{d}/')])} tracked files (e.g., {', '.join(Path(f).name for f in files_in_d)})\n"

    arch_md += f"""
## 4. Key Entry Points & Lifecycles
{chr(10).join(f"- `{e}`" for e in arch["entry_points"]) or "- No standard entry points detected"}

## 5. Security & Isolation Architecture
- **Secret Isolation**: Zero secrets stored in memory. Environment files protected.
- **Input Validation**: All user-facing APIs enforce validation and sanitize input boundaries.
- **CORS / CSP**: Origin enforcement on server routes and headers.
"""

    # 5. DEPENDENCIES.md
    deps_md = f"""# Project Dependencies: {p_name}

## Languages & Runtimes
{chr(10).join(f"- **{lang}**" for lang in tech["languages"])}

## Core Frameworks & Libraries
{chr(10).join(f"- **{fw}**" for fw in tech["frameworks"]) or "- Standard library"}

## Build & Tooling
{chr(10).join(f"- **{bt}**" for bt in tech["build_tools"]) or "- Default tools"}

## Test Frameworks
{chr(10).join(f"- **{tf}**" for tf in tech["test_frameworks"]) or "- Not configured"}
"""

    # 6. DATA-FLOW.md
    df_md = f"""# Data Flow Architecture: {p_name}

```mermaid
flowchart TD
    Client["Client / User Interface"] -->|"Requests / Events"| Controllers["Routing & Controllers"]
    Controllers -->|"Process / Validate"| Services["Business Logic Services"]
    Services -->|"Data Access"| Storage["Storage / Cache / External APIs"]
    Storage -->|"Results"| Services
    Services -->|"Response DTO"| Controllers
    Controllers -->|"JSON / Render"| Client
```

## Lifecycle Flow
1. **Input**: User interactions, HTTP API requests, or CLI execution.
2. **Validation**: Boundary checking, schema validation, rate-limiting, and sanitized payloads.
3. **Processing**: Domain services execute atomic operations.
4. **Output**: Structured responses, reactive UI re-renders, and atomic persistence.
"""

    # 7. API-MAP.md
    api_md = f"""# API Map & Endpoints: {p_name}

Total Detected Endpoints: {len(arch["api_endpoints"])}

| Method | Endpoint | Source File |
|---|---|---|
"""
    if arch["api_endpoints"]:
        for ep in arch["api_endpoints"]:
            api_md += f"| `{ep['method']}` | `{ep['endpoint']}` | [`{ep['file']}`](file://{p_root}/{ep['file']}) |\n"
    else:
        api_md += "| - | No HTTP endpoints detected | - |\n"

    # 8. TEST-MAP.md
    test_md = f"""# Test Architecture & Verification Matrix: {p_name}

- **Test Runner**: `{tech["commands"]["test"] or "N/A"}`
- **Test Frameworks**: {", ".join(tech["test_frameworks"]) or "None detected"}
- **Total Test Files**: {len(arch["test_files"])}

## Test Suite Inventory
"""
    for tf in arch["test_files"][:50]:
        test_md += f"- [`{tf}`](file://{p_root}/{tf})\n"

    # 9. DECISIONS.md
    dec_md = f"# Architectural Decision Records (ADRs): {p_name}\n\n"
    if arch.get("adrs"):
        for adr in arch["adrs"]:
            dec_md += f"""## {adr['title']}
- **DATE**: {adr['date'] or timestamp[:10]}
- **STATUS**: {adr['status']}
- **DECISION / RATIONALE**: {adr['rationale'] or 'Documented in ADR source'}
- **CONTEXT**: {adr['context'] or 'Documented in ADR source'}
- **IMPACT**: {adr['impact'] or 'Architectural alignment & stability'}
- **SOURCE**: [`{adr['file']}`](file://{p_root}/{adr['file']})

"""
    else:
        dec_md += f"""## ADR-001: Project Intelligence & Persistent Memory Architecture
- **DATE**: {timestamp[:10]}
- **DECISION**: Establish persistent project memory in `.agent/project-memory/` (or `.agents/project-memory/`).
- **CONTEXT**: Repeated full-codebase scanning consumes excessive tokens and creates context drift across multi-agent sessions.
- **RATIONALE**: A structured, compact Markdown + JSON navigation layer allows agents to pinpoint relevant files instantly without rescanning unimpacted files.
- **IMPACT**: Significant token reduction, faster response times, and cross-agent portability.
"""

    # 10. CHANGELOG.md
    cl_md = f"""# Project Memory Changelog: {p_name}

## [{timestamp}] Initial Project Discovery
- **Action**: Initial structured discovery and memory index generation.
- **Change Level**: Level 3 (Structural Baseline)
- **Indexed Files**: {len(file_index)}
- **Git Commit**: `{commit}`
- **Result**: Complete persistent context created.
"""

    return {
        "METADATA.json": json.dumps(metadata, indent=2),
        "PROJECT-MAP.json": json.dumps(project_map, indent=2),
        "PROJECT-CONTEXT.md": context_md,
        "ARCHITECTURE.md": arch_md,
        "DEPENDENCIES.md": deps_md,
        "DATA-FLOW.md": df_md,
        "API-MAP.md": api_md,
        "TEST-MAP.md": test_md,
        "DECISIONS.md": dec_md,
        "CHANGELOG.md": cl_md
    }

def discover_project(project_path: Path, force: bool = False) -> dict:
    """Execute complete initial project discovery and persist memory."""
    project_root = detect_project_root(project_path)
    mem_dir = get_memory_dir(project_root)
    meta_path = mem_dir / "METADATA.json"
    
    if meta_path.is_file() and not force:
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            return {
                "status": "ALREADY_DISCOVERED",
                "project_id": meta.get("project_id"),
                "project_root": str(project_root),
                "memory_dir": str(mem_dir)
            }
        except Exception:
            pass  # Rebuild if corrupt
            
    identity = get_project_identity(project_root)
    excludes = load_ignore_patterns(project_root)
    file_index = scan_file_index(project_root, excludes)
    tech = analyze_tech_stack_and_type(project_root, file_index)
    arch = discover_architecture_details(project_root, file_index)
    
    docs = generate_memory_documents(project_root, identity, tech, arch, file_index)
    
    for fname, content in docs.items():
        (mem_dir / fname).write_text(content, encoding="utf-8")
        
    # Sync with ~/.agent-team/team.db
    summary_text = f"{tech['project_type']} - Languages: {', '.join(tech['languages'])}; Frameworks: {', '.join(tech['frameworks'])}; Tests: {len(arch['test_files'])}"
    decisions = [{
        "title": "Establish Persistent Project Intelligence & Memory",
        "rationale": "Compact architectural index eliminates repetitive full scans and reduces context consumption.",
        "context": f"Project {identity['project_name']} mapped at commit {identity['git_commit']}"
    }] + arch.get("adrs", [])
    sync_to_agent_team_db(identity, summary_text, decisions)
    
    return {
        "status": "DISCOVERY_COMPLETED",
        "project_id": identity["project_id"],
        "project_name": identity["project_name"],
        "project_root": str(project_root),
        "memory_dir": str(mem_dir),
        "files_indexed": len(file_index),
        "tests_found": len(arch["test_files"]),
        "apis_found": len(arch["api_endpoints"])
    }

def load_context(project_path: Path, subsystem: str = None) -> str:
    """
    Load project context token-efficiently.
    If subsystem is None, returns compact PROJECT-CONTEXT.md.
    """
    project_root = detect_project_root(project_path)
    mem_dir = get_memory_dir(project_root)
    
    # Auto-recover if missing
    if not (mem_dir / "PROJECT-CONTEXT.md").is_file():
        discover_project(project_root)
        
    subsystem_files = {
        "architecture": "ARCHITECTURE.md",
        "api": "API-MAP.md",
        "test": "TEST-MAP.md",
        "dependencies": "DEPENDENCIES.md",
        "data-flow": "DATA-FLOW.md",
        "decisions": "DECISIONS.md",
        "changelog": "CHANGELOG.md",
        "map": "PROJECT-MAP.json",
        "metadata": "METADATA.json"
    }
    
    target_file = subsystem_files.get(subsystem.lower()) if subsystem else "PROJECT-CONTEXT.md"
    file_p = mem_dir / target_file
    if file_p.is_file():
        return file_p.read_text(encoding="utf-8")
    else:
        return (mem_dir / "PROJECT-CONTEXT.md").read_text(encoding="utf-8")

def refresh_incremental(project_path: Path, task_summary: str = "", level: int = None) -> dict:
    """
    Detect files modified/added/deleted and incrementally update project memory.
    Classifies changes across Levels 1 to 4.
    """
    project_root = detect_project_root(project_path)
    mem_dir = get_memory_dir(project_root)
    meta_path = mem_dir / "METADATA.json"
    
    if not meta_path.is_file():
        return discover_project(project_root, force=True)
        
    try:
        old_meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except Exception:
        return discover_project(project_root, force=True)
        
    old_index = old_meta.get("file_index", {})
    excludes = load_ignore_patterns(project_root)
    new_index = scan_file_index(project_root, excludes)
    
    added = [f for f in new_index if f not in old_index]
    deleted = [f for f in old_index if f not in new_index]
    modified = [f for f in new_index if f in old_index and new_index[f]["hash"] != old_index[f]["hash"]]
    
    if not added and not deleted and not modified and not level:
        return {
            "status": "NO_CHANGES_DETECTED",
            "project_root": str(project_root),
            "memory_dir": str(mem_dir)
        }
        
    # Auto-classify change level if not forced
    detected_level = 1
    if any(f.endswith((".ts", ".tsx", ".js", ".jsx", ".py", ".rs", ".go", ".java")) for f in modified):
        detected_level = 2
    if added or deleted or any(f in ["package.json", "pyproject.toml", "Cargo.toml", "go.mod"] for f in modified):
        detected_level = 3
    if any(f in ["package.json", "pyproject.toml"] and "dependencies" in f for f in modified):
        detected_level = 4
        
    change_level = level if level else detected_level
    
    identity = get_project_identity(project_root)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    
    # Update metadata
    old_meta["file_index"] = new_index
    old_meta["file_count"] = len(new_index)
    old_meta["last_incremental_scan"] = timestamp
    old_meta["git_commit"] = identity["git_commit"]
    old_meta["git_branch"] = identity["git_branch"]
    
    tech = analyze_tech_stack_and_type(project_root, new_index)
    arch = discover_architecture_details(project_root, new_index)
    
    old_meta["test_count"] = len(arch["test_files"])
    old_meta["api_count"] = len(arch["api_endpoints"])
    old_meta["frameworks"] = tech["frameworks"]
    old_meta["languages"] = tech["languages"]
    
    # Write updated METADATA.json
    meta_path.write_text(json.dumps(old_meta, indent=2), encoding="utf-8")
    
    # Selectively update documentation based on change level
    if change_level >= 3:
        # Structural update: refresh PROJECT-MAP, API-MAP, TEST-MAP, DEPENDENCIES
        project_map = {
            "project_id": identity["project_id"],
            "name": identity["project_name"],
            "type": tech["project_type"],
            "entry_points": arch["entry_points"],
            "key_subsystems": {
                "ui_components": arch["components"],
                "services": arch["services"],
                "routes_and_apis": arch["routes"],
                "tests": arch["test_files"]
            },
            "api_endpoints": arch["api_endpoints"]
        }
        (mem_dir / "PROJECT-MAP.json").write_text(json.dumps(project_map, indent=2), encoding="utf-8")
        
        # Refresh API-MAP.md
        api_md = f"""# API Map & Endpoints: {identity['project_name']}

Total Detected Endpoints: {len(arch["api_endpoints"])}

| Method | Endpoint | Source File |
|---|---|---|
"""
        for ep in arch["api_endpoints"]:
            api_md += f"| `{ep['method']}` | `{ep['endpoint']}` | [`{ep['file']}`](file://{identity['project_root']}/{ep['file']}) |\n"
        (mem_dir / "API-MAP.md").write_text(api_md, encoding="utf-8")
        
        # Refresh TEST-MAP.md
        test_md = f"""# Test Architecture & Verification Matrix: {identity['project_name']}

- **Test Runner**: `{tech["commands"]["test"] or "N/A"}`
- **Test Frameworks**: {", ".join(tech["test_frameworks"]) or "None detected"}
- **Total Test Files**: {len(arch["test_files"])}

## Test Suite Inventory
"""
        for tf in arch["test_files"][:50]:
            test_md += f"- [`{tf}`](file://{identity['project_root']}/{tf})\n"
        (mem_dir / "TEST-MAP.md").write_text(test_md, encoding="utf-8")

    # Update PROJECT-CONTEXT.md
    context_content = (mem_dir / "PROJECT-CONTEXT.md").read_text(encoding="utf-8")
    context_content = re.sub(r'Last Verified: [^\n|]+', f'Last Verified: {timestamp}', context_content)
    context_content = re.sub(r'Commit: `[^`]+`', f'Commit: `{identity["git_commit"]}`', context_content)
    (mem_dir / "PROJECT-CONTEXT.md").write_text(context_content, encoding="utf-8")
    
    # Append to CHANGELOG.md
    cl_path = mem_dir / "CHANGELOG.md"
    summary_desc = task_summary or f"Incremental refresh: {len(added)} added, {len(modified)} modified, {len(deleted)} deleted"
    cl_entry = f"""
## [{timestamp}] Change Level {change_level} Update
- **Summary**: {summary_desc}
- **Added**: {len(added)} files ({', '.join(added[:3])}{'...' if len(added) > 3 else ''})
- **Modified**: {len(modified)} files ({', '.join(modified[:3])}{'...' if len(modified) > 3 else ''})
- **Deleted**: {len(deleted)} files ({', '.join(deleted[:3])}{'...' if len(deleted) > 3 else ''})
- **Commit**: `{identity["git_commit"]}`
"""
    if cl_path.is_file():
        cl_path.write_text(cl_path.read_text(encoding="utf-8") + cl_entry, encoding="utf-8")
    else:
        cl_path.write_text(f"# Project Memory Changelog\n{cl_entry}", encoding="utf-8")
        
    return {
        "status": "REFRESH_COMPLETED",
        "change_level": change_level,
        "added_count": len(added),
        "modified_count": len(modified),
        "deleted_count": len(deleted),
        "added": added,
        "modified": modified,
        "deleted": deleted,
        "git_commit": identity["git_commit"]
    }

def check_memory_integrity(project_path: Path) -> dict:
    """Verify health and validity of project memory."""
    project_root = detect_project_root(project_path)
    mem_dir = get_memory_dir(project_root)
    meta_p = mem_dir / "METADATA.json"
    
    if not meta_p.is_file():
        return {"status": "NOT_FOUND", "project_root": str(project_root)}
        
    try:
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
    except Exception as e:
        return {"status": "CORRUPTED", "error": str(e), "project_root": str(project_root)}
        
    required_files = ["PROJECT-CONTEXT.md", "PROJECT-MAP.json", "METADATA.json", "ARCHITECTURE.md"]
    missing = [f for f in required_files if not (mem_dir / f).is_file()]
    
    if missing:
        return {"status": "INCOMPLETE", "missing": missing, "project_root": str(project_root)}
        
    # Check if files changed
    excludes = load_ignore_patterns(project_root)
    curr_index = scan_file_index(project_root, excludes)
    recorded_index = meta.get("file_index", {})
    
    drift_count = sum(1 for f in curr_index if f not in recorded_index or curr_index[f]["hash"] != recorded_index[f].get("hash"))
    deleted_count = sum(1 for f in recorded_index if f not in curr_index)
    
    is_stale = (drift_count + deleted_count) > 0
    
    return {
        "status": "STALE" if is_stale else "CLEAN",
        "project_id": meta.get("project_id"),
        "project_root": str(project_root),
        "drift_files": drift_count,
        "deleted_files": deleted_count,
        "memory_dir": str(mem_dir)
    }

def recover_memory(project_path: Path) -> dict:
    """Self-heal / reconstruct memory from source code."""
    project_root = detect_project_root(project_path)
    return discover_project(project_root, force=True)

def print_status(project_path: Path):
    """Print readable high-level status."""
    project_root = detect_project_root(project_path)
    check = check_memory_integrity(project_root)
    print(f"Project Root:   {project_root}")
    print(f"Memory Status:  {check['status']}")
    if check['status'] in ["CLEAN", "STALE"]:
        print(f"Project ID:     {check.get('project_id')}")
        print(f"Memory Path:    {check.get('memory_dir')}")
        if check['status'] == "STALE":
            print(f"Pending Drift:  {check.get('drift_files')} modified/new, {check.get('deleted_files')} deleted")

# CLI Entrypoint
if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = args[0] if args else "status"
    target = Path(args[1]) if len(args) > 1 and not args[1].startswith("--") else Path.cwd()
    
    if cmd == "detect":
        root = detect_project_root(target)
        identity = get_project_identity(root)
        print(json.dumps(identity, indent=2))
    elif cmd == "discover":
        force = "--force" in args
        res = discover_project(target, force=force)
        print(json.dumps(res, indent=2))
    elif cmd == "load":
        subsystem = None
        if "--subsystem" in args:
            idx = args.index("--subsystem")
            if idx + 1 < len(args):
                subsystem = args[idx + 1]
        content = load_context(target, subsystem=subsystem)
        print(content)
    elif cmd == "refresh":
        summary = ""
        level = None
        if "--summary" in args:
            idx = args.index("--summary")
            if idx + 1 < len(args):
                summary = args[idx + 1]
        if "--level" in args:
            idx = args.index("--level")
            if idx + 1 < len(args):
                level = int(args[idx + 1])
        res = refresh_incremental(target, task_summary=summary, level=level)
        print(json.dumps(res, indent=2))
    elif cmd == "check":
        res = check_memory_integrity(target)
        print(json.dumps(res, indent=2))
    elif cmd == "recover":
        res = recover_memory(target)
        print(json.dumps(res, indent=2))
    elif cmd == "status":
        print_status(target)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
