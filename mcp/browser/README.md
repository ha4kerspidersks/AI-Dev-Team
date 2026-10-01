# Browser Puppeteer MCP Module

- **Package**: `@modelcontextprotocol/server-puppeteer` (Official Model Context Protocol)
- **Runtime**: Node.js 22 LTS (`~/Developer/AI-Dev-Team/environments/node22/bin/node`)
- **Transport**: Stdio (JSON-RPC 2.0)
- **Runner**: `~/Developer/AI-Dev-Team/mcp/browser/run.sh`

## Capabilities (7 Tools)
- `puppeteer_navigate`: Navigate to URL in headless Chromium
- `puppeteer_screenshot`: Capture full-page or element screenshot
- `puppeteer_click`: Click on page elements
- `puppeteer_fill`: Fill input fields
- `puppeteer_select`: Select dropdown options
- `puppeteer_hover`: Hover over elements
- `puppeteer_evaluate`: Execute JS within browser page context

## Security
- Runs in headless sandbox.
- No access to user's real browser profile, sessions, or stored credentials/cookies.
