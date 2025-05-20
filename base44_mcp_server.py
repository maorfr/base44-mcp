import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("base44")


async def make_api_request(api_path, method="GET", data=None):
    url = f"https://base44.app/api/{api_path}"
    api_key = os.environ["BASE44_API_KEY"]
    headers = {
        "api_key": api_key,
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        if method.upper() == "GET":
            response = await client.request(method, url, headers=headers, params=data)
        else:
            response = await client.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_apps():
    """Get list of applications."""
    api_path = "apps"
    response = await make_api_request(api_path)
    lines = []
    for item in response:
        lines.append(f"App Name: {item['name']}")
        lines.append(f"App ID: {item['id']}")
        lines.append(f"App description: {item['user_description']}")
        lines.append(f"App entities: {item['entities']}")
    return "\n".join(lines)


@mcp.tool()
async def get_app_entities(app_id):
    """Get application entities by application ID."""
    api_path = f"apps/{app_id}"
    response = await make_api_request(api_path)
    lines = []
    for name in response["entities"]:
        lines.append(f"Entity Name: {name}")
    return "\n".join(lines)


@mcp.tool()
async def get_app_entity_instances(app_id, entity_name):
    """Get application entity instances by application ID and entity name."""
    api_path = f"apps/{app_id}/entities/{entity_name}"
    response = await make_api_request(api_path)
    lines = []
    for item in response:
        lines.append(f"Entity Name: {item['name']}")
        lines.append(f"Entity ID: {item['id']}")
        lines.append(f"Entity description: {item['description']}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
