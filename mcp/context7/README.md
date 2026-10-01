# Context7 Documentation MCP Layer

## Overview
Context7 provides up-to-date, authoritative documentation and code examples directly to AI coding agents for modern frameworks, libraries, and SDKs.

## MCP Server Architecture
- **Implementation**: `@upstash/context7-mcp` (Node.js ESM)
- **Local Location**: `/Users/subhajkar/Developer/AI-Dev-Team/mcp/node_modules/@upstash/context7-mcp/dist/index.js`
- **Runtime**: `/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node`
- **Transport**: Stdio (standard input/output JSON-RPC)
- **Version**: 4.1.1
- **Authentication**: Optional (`CONTEXT7_API_KEY` or `--api-key`). Works unauthenticated for standard open-source library documentation lookups.

## Capabilities & Tools
1. `resolve-library-id`: Resolves package or product names to Context7-compatible library identifiers (e.g. `react` -> `/reactjs/react.dev`).
2. `query-docs`: Queries and retrieves structured documentation snippets, API references, and verified code examples from Context7 for any programming library.

## Routing Policy
- **Trigger**: Materially relevant external library/framework questions (e.g., React 19, Next.js App Router, Vite, Three.js, Playwright, Tailwind v4, Prisma, etc.).
- **Boundary**: Do NOT invoke for local repository reasoning, internal codebase symbol lookups, or unrelated local file tasks.
