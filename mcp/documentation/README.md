# Documentation MCP Layer

## Architecture
The documentation layer combines three complementary, non-duplicative engines:
1. **Google Gemini API & SDK Docs (`gemini-api_gemini-api-docs`)**: Preinstalled eager MCP providing authoritative, live Gemini API docs, SDK references, guides, and migration manuals (`gemini_search_docs`, `gemini_get_doc`).
2. **Context7 Documentation Platform (`@upstash/context7-mcp` / `ctx7` CLI)**: Dedicated, verified documentation retrieval engine for rapidly changing modern libraries and frameworks (React, Next.js, Vite, Three.js, Playwright, Prisma, etc.) via `resolve-library-id` and `query-docs`.
3. **General Web / DevDocs (`mcp-server-fetch`)**: Universal web documentation fetcher converting online URLs and static manuals into clean, structured Markdown for agent consumption without client-side script execution.
