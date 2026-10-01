"""Automatic technology stack discovery for PRE-LIVE-FULL-AUDIT.

Inspects any project workspace without modifying files. Identifies:
- Languages, frameworks, package managers, databases, APIs, cloud/IaC,
  CI/CD, testing tools, and web UI presence.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Set


@dataclass
class ProjectTechProfile:
    project_path: str
    project_name: str
    languages: List[str] = field(default_factory=list)
    package_managers: List[str] = field(default_factory=list)
    frameworks: List[str] = field(default_factory=list)
    databases: List[str] = field(default_factory=list)
    apis: List[str] = field(default_factory=list)
    cloud_and_infra: List[str] = field(default_factory=list)
    ci_cd: List[str] = field(default_factory=list)
    test_frameworks: List[str] = field(default_factory=list)
    is_web_app: bool = False
    has_docker: bool = False
    has_kubernetes: bool = False
    has_terraform: bool = False
    has_playwright: bool = False
    has_git: bool = False
    detected_files: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class TechDetector:
    """Discovers project technology footprint."""

    def __init__(self, project_path: str):
        self.project_path = os.path.abspath(project_path)
        self.project_name = os.path.basename(self.project_path)

    def detect(self) -> ProjectTechProfile:
        profile = ProjectTechProfile(
            project_path=self.project_path,
            project_name=self.project_name
        )

        if not os.path.exists(self.project_path):
            return profile

        # Check Git
        profile.has_git = os.path.exists(os.path.join(self.project_path, ".git"))

        # Scan root files
        root_files = set(os.listdir(self.project_path))

        # Languages and package managers
        if "package.json" in root_files:
            profile.languages.append("JavaScript")
            profile.detected_files.append("package.json")
            if "pnpm-lock.yaml" in root_files:
                profile.package_managers.append("pnpm")
            elif "yarn.lock" in root_files:
                profile.package_managers.append("yarn")
            elif "bun.lockb" in root_files or "bun.lock" in root_files:
                profile.package_managers.append("bun")
            else:
                profile.package_managers.append("npm")

            # Inspect package.json for frameworks & tools
            try:
                with open(os.path.join(self.project_path, "package.json")) as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

                    if "typescript" in deps or os.path.exists(os.path.join(self.project_path, "tsconfig.json")):
                        profile.languages.append("TypeScript")

                    # Frameworks
                    if "react" in deps:
                        profile.frameworks.append("React")
                    if "next" in deps:
                        profile.frameworks.append("Next.js")
                    if "vue" in deps:
                        profile.frameworks.append("Vue")
                    if "express" in deps:
                        profile.frameworks.append("Express.js")
                    if "vite" in deps:
                        profile.frameworks.append("Vite")

                    # Databases
                    if "pg" in deps or "postgres" in deps:
                        profile.databases.append("PostgreSQL")
                    if "mysql" in deps or "mysql2" in deps:
                        profile.databases.append("MySQL")
                    if "sqlite3" in deps or "better-sqlite3" in deps:
                        profile.databases.append("SQLite")
                    if "mongoose" in deps or "mongodb" in deps:
                        profile.databases.append("MongoDB")
                    if "redis" in deps or "ioredis" in deps:
                        profile.databases.append("Redis")
                    if "@prisma/client" in deps or "prisma" in deps:
                        profile.databases.append("Prisma ORM")

                    # APIs
                    if "graphql" in deps or "@apollo/client" in deps or "@apollo/server" in deps:
                        profile.apis.append("GraphQL")
                    if "@trpc/server" in deps:
                        profile.apis.append("tRPC")
                    if "ws" in deps or "socket.io" in deps:
                        profile.apis.append("WebSockets")
                    if "express" in deps or "fastify" in deps or "koa" in deps:
                        profile.apis.append("REST")

                    # Tests
                    if "@playwright/test" in deps or "playwright" in deps:
                        profile.test_frameworks.append("Playwright")
                        profile.has_playwright = True
                    if "jest" in deps:
                        profile.test_frameworks.append("Jest")
                    if "vitest" in deps:
                        profile.test_frameworks.append("Vitest")
                    if "cypress" in deps:
                        profile.test_frameworks.append("Cypress")

            except Exception:
                pass

        if "requirements.txt" in root_files or "pyproject.toml" in root_files or "setup.py" in root_files or "Pipfile" in root_files:
            profile.languages.append("Python")
            if "pyproject.toml" in root_files:
                profile.package_managers.append("poetry/flit/uv")
            if "Pipfile" in root_files:
                profile.package_managers.append("pipenv")
            if "requirements.txt" in root_files:
                profile.package_managers.append("pip")

            # Check for python frameworks
            req_path = os.path.join(self.project_path, "requirements.txt")
            if os.path.exists(req_path):
                try:
                    with open(req_path) as f:
                        req_text = f.read().lower()
                        if "fastapi" in req_text:
                            profile.frameworks.append("FastAPI")
                            profile.apis.append("REST")
                        if "flask" in req_text:
                            profile.frameworks.append("Flask")
                            profile.apis.append("REST")
                        if "django" in req_text:
                            profile.frameworks.append("Django")
                        if "pytest" in req_text:
                            profile.test_frameworks.append("Pytest")
                except Exception:
                    pass

        if "pom.xml" in root_files:
            profile.languages.append("Java")
            profile.package_managers.append("Maven")
        if "build.gradle" in root_files or "build.gradle.kts" in root_files:
            profile.languages.append("Java/Kotlin")
            profile.package_managers.append("Gradle")
        if "go.mod" in root_files:
            profile.languages.append("Go")
            profile.package_managers.append("Go Modules")
        if "Cargo.toml" in root_files:
            profile.languages.append("Rust")
            profile.package_managers.append("Cargo")

        # Docker & Container
        if "Dockerfile" in root_files or "docker-compose.yml" in root_files or "compose.yaml" in root_files:
            profile.has_docker = True
            profile.cloud_and_infra.append("Docker")

        # Kubernetes
        k8s_indicators = ["k8s", "kubernetes", "helm", "charts"]
        if any(ind in root_files for ind in k8s_indicators) or any(f.endswith(".k8s.yaml") for f in root_files):
            profile.has_kubernetes = True
            profile.cloud_and_infra.append("Kubernetes")

        # Terraform / IaC
        tf_files = [f for f in root_files if f.endswith(".tf") or f == "terraform"]
        if tf_files or os.path.exists(os.path.join(self.project_path, "terraform")):
            profile.has_terraform = True
            profile.cloud_and_infra.append("Terraform")

        # CI/CD
        gh_actions_dir = os.path.join(self.project_path, ".github", "workflows")
        if os.path.exists(gh_actions_dir):
            profile.ci_cd.append("GitHub Actions")
        if ".gitlab-ci.yml" in root_files:
            profile.ci_cd.append("GitLab CI")

        # Web App detection
        web_indicators = ["index.html", "public", "src/pages", "src/app", "src/components", "templates", "views"]
        for ind in web_indicators:
            if os.path.exists(os.path.join(self.project_path, ind)):
                profile.is_web_app = True
                break
        if any(f in ["React", "Next.js", "Vue", "Vite"] for f in profile.frameworks):
            profile.is_web_app = True

        # Deduplicate
        profile.languages = sorted(list(set(profile.languages)))
        profile.package_managers = sorted(list(set(profile.package_managers)))
        profile.frameworks = sorted(list(set(profile.frameworks)))
        profile.databases = sorted(list(set(profile.databases)))
        profile.apis = sorted(list(set(profile.apis)))
        profile.cloud_and_infra = sorted(list(set(profile.cloud_and_infra)))
        profile.ci_cd = sorted(list(set(profile.ci_cd)))
        profile.test_frameworks = sorted(list(set(profile.test_frameworks)))

        return profile
