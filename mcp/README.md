# MCP registry entries

One `server.json` per Actor, published to the [official MCP registry](https://registry.modelcontextprotocol.io) by `.github/workflows/publish-mcp.yml`. Each entry points to the Apify MCP server with only that Actor as a tool (`https://mcp.apify.com/?tools=fguiraud/<actor>`), so any MCP client can add it with an Apify account (OAuth) or an Apify token.

To change an entry, edit its file and increase `version`.
