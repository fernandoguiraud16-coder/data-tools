# Use these tools from AI agents (MCP)

Every Actor here is available to AI agents through the [Apify MCP server](https://mcp.apify.com). Add it to your MCP client and the agent can call Google Trends, Google News, document parsing, domain lookups and transcription by itself.

## Server URL

Pick the tools you want with the `tools` parameter:

```text
https://mcp.apify.com?tools=fguiraud/google-trends-scraper,fguiraud/google-news-scraper,fguiraud/document-to-markdown-tables,fguiraud/website-tech-dns-whois-ssl,fguiraud/audio-video-transcriber
```

You connect with your own Apify account (sign-in or API token, depending on the client), and runs are billed to that account. See the [Apify MCP docs](https://docs.apify.com/platform/integrations/mcp) for client-specific setup.

## Claude Code

```bash
claude mcp add --transport http apify "https://mcp.apify.com?tools=fguiraud/google-trends-scraper,fguiraud/google-news-scraper"
```

## Claude Desktop, Cursor, VS Code and others

Add a remote MCP server with the URL above in the client's MCP settings. For clients that need a JSON config:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com?tools=fguiraud/google-trends-scraper,fguiraud/google-news-scraper"
    }
  }
}
```

## Things to ask

- *"Is interest in heat pumps growing in Germany? Show me the last 5 years."*
- *"Find this week's news about Tesla's robotaxi and summarize what analysts say."*
- *"Convert this PDF to Markdown and list every table: https://example.com/report.pdf"*
- *"What CMS and email provider do stripe.com and shopify.com use?"*
- *"Transcribe this recording and give me the key points: https://example.com/call.mp3"*
