# base44-mcp

[MCP server](https://modelcontextprotocol.io/introduction) for [base44](https://base44.app)

## Available Tools in this MCP server

The following tools are available in this MCP server (see `base44_mcp_server.py`):

- **get_apps**: Get a list of applications. Returns the app name, ID, user description, and entities for each application.
- **get_app_entities**: Get application entities by application ID. Returns the names of all entities for a given app.
- **get_app_entity_instances**: Get application entity instances by application ID and entity name. Returns the name, ID, and description for each entity instance.

---

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
