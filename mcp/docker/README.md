# Docker MCP Layer

## Guidelines
- Container operations interface with the local Docker daemon (`Docker version 29.7.2`).
- Safe operations: inspecting containers, listing images, viewing build logs.
- Destructive operations: stopping running containers, removing volumes or networks, running containers with host mounts (`-v /:/host`) require user confirmation.
