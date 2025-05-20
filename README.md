# base44-mcp

MCP server for base44

## Running with Podman or Docker

You can run the base44-mcp server in a container using Podman or Docker:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "base44": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "BASE44_API_KEY",
        "quay.io/maorfr/base44-mcp:latest"
      ],
      "env": {
        "BASE44_API_KEY": "REDACTED",
      }
    }
  }
}
```

Replace `REDACTED` with the API key from https://base44.app/user-settings.
