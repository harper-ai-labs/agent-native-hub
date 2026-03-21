# Agent Native Hub

> A continuously-updated catalog of services, tools, and platforms built specifically for AI agents to use.

**43 services** across 11 categories | Last updated: 2026-03-21

Maintained by [Harper Labs](https://github.com/harper-labs) | Contributions welcome

## What belongs here

Services where an AI agent is the **primary user** — not a human with an AI assistant bolted on.
A service belongs here if an agent can directly send email, schedule meetings, browse the web,
update CRM records, or take other real-world actions through it.

## Agent-Native Score

- ★★★★★ Built specifically for agents, full autonomous action
- ★★★★☆ Agent-first with some human UI
- ★★★☆☆ Usable by agents via API, not designed primarily for them
- ★★☆☆☆ Agent-adjacent with some automation
- ★☆☆☆☆ Mostly human-first

---

## 📧 Email

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [AgentMail](https://agentmail.to) | ★★★★★ | REST API, webhooks | send, receive, thread | API key | usage-based |
| [Assembled AI Email Agent](https://www.assembled.com/features/ai-email-agent) | ★★★★☆ | REST API | classify, draft, resolve | API key | enterprise |
| [Postmark MCP Server](https://postmarkapp.com) | ★★★★☆ | MCP, REST API | send, template-management, delivery-tracking | API key | usage-based |

## 📅 Calendar & Scheduling

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [MintMCP Google Calendar Server](https://www.mintmcp.com/google-calendar) | ★★★★★ | MCP | create-event, read-events, check-availability | OAuth | free |
| [Beam AI Google Calendar Integration](https://beam.ai/integrations/google-calendar) | ★★★★☆ | REST API | create-event, read-events, update-event | OAuth | usage-based |
| [Cal.com MCP Server](https://cal.com) | ★★★★☆ | MCP, REST API, webhooks | book-meeting, check-availability, reschedule | API key | freemium |
| [SignalWire Aical](https://signalwire.com/blogs/developers/aical) | ★★★★☆ | REST API, voice | schedule, reschedule, cancel | API key | usage-based |

## 🌐 Browser & Web Automation

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [agent-browser](https://agent-browser.dev) | ★★★★★ | REST API, SDK | navigate, click, fill-form | API key | usage-based |
| [Browserbase](https://www.browserbase.com) | ★★★★★ | REST API, SDK, Playwright | navigate, click, fill-form | API key | usage-based |
| [EverWorker Agentic Browser](https://everworker.ai) | ★★★★★ | REST API | navigate, click, fill-form | API key | usage-based |
| [Perplexity Comet](https://perplexity.ai/comet) | ★★★★★ | browser-automation, REST API | autonomous web browsing, research automation, task delegation | None (personal tool) | Subscription-based |
| [Stagehand](https://github.com/browserbase/stagehand) | ★★★★★ | SDK | navigate, act, extract | API key | open-source + hosted |
| [Vercel Labs agent-browser](https://github.com/vercel-labs/agent-browser) | ★★★★★ | SDK | navigate, click, fill-form | none | free |

## 👥 CRM & Sales

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Attio MCP Server](https://attio.com) | ★★★★★ | MCP, REST API | create-contact, update-contact, create-deal | API key | freemium |
| [HubSpot MCP Server](https://www.hubspot.com) | ★★★★☆ | MCP, REST API | manage-contacts, manage-deals, create-tickets | API key / OAuth | freemium |

## 🎧 Support & Ticketing

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Intercom Fin AI Agent](https://www.intercom.com/fin) | ★★★★☆ | REST API, webhooks | resolve-ticket, answer-questions, escalate | API key | usage-based |
| [Zendesk AI Agent](https://www.zendesk.com/ai) | ★★★☆☆ | REST API, webhooks | route-ticket, auto-respond, classify-intent | API key / OAuth | enterprise |

## 💬 Messaging & Chat

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Slack MCP Server](https://slack.com/intl/en-us/help/articles/api) | ★★★★☆ | MCP, REST API, webhooks | send-message, read-messages, search | OAuth | free (via Slack API) |
| [Twilio MCP Server](https://www.twilio.com) | ★★★★☆ | MCP, REST API | send-sms, send-whatsapp, receive-message | API key | usage-based |

## 🎙️ Voice

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Bland AI](https://www.bland.ai) | ★★★★★ | REST API | outbound-call, inbound-call, scripted-conversation | API key | usage-based |
| [Retell AI](https://www.retellai.com) | ★★★★★ | REST API, webhooks, WebSocket | outbound-call, inbound-call, voice-synthesis | API key | usage-based |
| [Vapi](https://vapi.ai) | ★★★★★ | REST API, webhooks, SDK | outbound-call, inbound-call, conversation | API key | usage-based |

## 🏪 Agent Marketplaces & Directories

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Agent.ai](https://agent.ai) | ★★★★☆ | REST API | discover-agents, deploy-agent, invoke-agent | API key | freemium |
| [Google Cloud AI Agent Marketplace](https://cloud.google.com/blog/topics/partners/google-cloud-ai-agent-marketplace) | ★★★★☆ | REST API, A2A | discover-agents, deploy-agent, invoke-agent | OAuth | usage-based |
| [Kore.ai AI Agent Marketplace](https://www.kore.ai/ai-marketplace) | ★★★★☆ | REST API, SDK | discover-agents, deploy-agent, conversation | API key | enterprise |
| [Oracle AI Agent Marketplace](https://www.oracle.com/applications/fusion-ai/ai-agent-marketplace/) | ★★★★☆ | REST API | discover-agents, deploy-agent | OAuth | enterprise |
| [Salesforce AgentExchange](https://agentexchange.salesforce.com) | ★★★★☆ | REST API, SDK | discover-agents, deploy-agent, invoke-agent | OAuth | enterprise |
| [ServiceNow AI Agent Marketplace](https://store.servicenow.com/store/ai-marketplace) | ★★★★☆ | REST API | discover-agents, deploy-agent, workflow-automation | OAuth | enterprise |
| [AI Agents Directory](https://aiagentsdirectory.com) | ★★★☆☆ | web | discover-agents | none | free |

## ⚙️ Orchestration & Protocols

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [A2A (Agent2Agent) Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) | ★★★★★ | A2A | agent-discovery, task-delegation, capability-advertisement | varies | free |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io) | ★★★★★ | MCP | tool-connection, resource-access, prompt-sharing | varies | free |
| [Axiory.ai](https://axiory.ai) | ★★★★★ | REST API, MCP | access global financial markets, trade multiple asset classes, real-time market data | API key | Custom |
| [CrewAI](https://www.crewai.com) | ★★★★★ | SDK | role-based-agents, task-delegation, multi-agent | API key | open-source + enterprise |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | ★★★★★ | SDK, REST API | graph-orchestration, stateful-agents, multi-agent | API key | open-source + hosted |
| [Mistral Agents API](https://mistral.ai/news/agents-api) | ★★★★★ | REST API, Python SDK, MCP | Multi-agent orchestration and handoffs, Code execution in sandboxed environment, Web search and information retrieval | API key | Pay-per-use (API consumption) |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | ★★★★★ | SDK, REST API | agent-creation, tool-use, handoff | API key | usage-based |
| [Tray.ai](https://tray.io) | ★★★★★ | REST API, Webhooks, MCP | No-code agent builder (Merlin), ITSM agent for IT support automation, HR agent for policy automation, PTO, profile updates | API key, OAuth | Enterprise (custom) |

## 🔄 Workflow Automation

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [n8n](https://n8n.io) | ★★★★☆ | REST API, webhooks, SDK | workflow-execution, trigger, condition | API key | open-source + cloud |
| [Make (formerly Integromat)](https://www.make.com) | ★★★☆☆ | REST API, webhooks | trigger-scenario, monitor-run, data-mapping | API key | freemium |

## 🔌 Tool Gateways & MCP

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Arcade AI](https://arcade.ai) | ★★★★★ | REST API, SDK | tool-execution, auth-management, permission-control | API key | usage-based |
| [Composio](https://composio.dev) | ★★★★★ | REST API, SDK, MCP | tool-routing, auth-management, trigger | API key | freemium |
| [MCP Server Directories](https://mcpmarket.com) | ★★★★★ | MCP | tool-discovery, tool-connection | varies | free |
| [Zapier MCP Server](https://zapier.com/mcp) | ★★★★☆ | MCP, REST API | trigger-automation, create-record, update-record | API key | freemium |

---

## Contributing

1. Fork this repo
2. Add a JSON file in `services/<category>/` following `schema/service.schema.json`
3. Run `python3 scripts/generate-readme.py`
4. Submit a PR

## Discovery

This catalog is updated automatically 2x daily by a search agent that scans for new agent-native services.
Discovered candidates go into `staging/` for review before promotion.

## License

MIT — Harper Labs
