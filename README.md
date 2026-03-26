# Agent Native Hub

> A continuously-updated catalog of services, tools, and platforms built specifically for AI agents to use.

**77 services** across 11 categories | Last updated: 2026-03-26

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
| [IRONSCALES AI Email Agents](https://ironscales.com/platform/agents) | ★★★★★ | REST API, Microsoft 365 API, Google Workspace API | Continuous reconnaissance and attack simulation (Red Teaming Agent), Rapid forensic investigation of suspicious emails (Phishing SOC Agent), Hyper-personalized phishing simulations based on OSINT (Phishing Simulation Agent) | API key, OAuth 2.0 (Microsoft 365, Google Workspace) | Enterprise (contact for details) |
| [Assembled AI Email Agent](https://www.assembled.com/features/ai-email-agent) | ★★★★☆ | REST API | classify, draft, resolve | API key | enterprise |
| [Carly](https://www.usecarly.com) | ★★★★☆ | REST API, email integration, calendar sync | Email parsing for scheduling content, Automatic calendar event creation, Meeting request processing | OAuth | Freemium + premium |
| [Postmark MCP Server](https://postmarkapp.com) | ★★★★☆ | MCP, REST API | send, template-management, delivery-tracking | API key | usage-based |

## 📅 Calendar & Scheduling

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [MintMCP Google Calendar Server](https://www.mintmcp.com/google-calendar) | ★★★★★ | MCP | create-event, read-events, check-availability | OAuth | free |
| [Beam AI Google Calendar Integration](https://beam.ai/integrations/google-calendar) | ★★★★☆ | REST API | create-event, read-events, update-event | OAuth | usage-based |
| [Cal.ai](https://cal.ai) | ★★★★☆ | REST API, Cal.com Workflows integration, phone API | AI phone calls for reminders, Booking confirmations, No-show follow-ups | API key | Included with Cal.com premium |
| [Cal.com MCP Server](https://cal.com) | ★★★★☆ | MCP, REST API, webhooks | book-meeting, check-availability, reschedule | API key | freemium |
| [SignalWire Aical](https://signalwire.com/blogs/developers/aical) | ★★★★☆ | REST API, voice | schedule, reschedule, cancel | API key | usage-based |

## 🌐 Browser & Web Automation

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [agent-browser](https://agent-browser.dev) | ★★★★★ | REST API, SDK | navigate, click, fill-form | API key | usage-based |
| [Browserbase](https://www.browserbase.com) | ★★★★★ | REST API, SDK, Playwright | navigate, click, fill-form | API key | usage-based |
| [BrowserOS](https://github.com/browseros-ai/BrowserOS) | ★★★★★ | AI API (Claude, OpenAI, Gemini), Ollama (local), Chrome extensions | Native AI agent execution, Browser automation, Content summarization | API key (optional for local execution) | Free and open-source |
| [ChatGPT Atlas](https://openai.com) | ★★★★★ | Browser API, OpenAI API integration | autonomous multi-step task execution, computer vision for web understanding, form navigation and filling | OpenAI account + API key | Premium tier (pricing TBD) |
| [EverWorker Agentic Browser](https://everworker.ai) | ★★★★★ | REST API | navigate, click, fill-form | API key | usage-based |
| [Fellou](https://fellou.ai) | ★★★★★ | browser automation, computer use, agentic memory API | Multi-source web research automation, Logged-in account access (Reddit, etc.), Complex data scraping | API key | Free tier + paid plans |
| [Google Colab MCP Server](https://colab.google/) | ★★★★★ | MCP, Model Context Protocol | Add and structure notebook cells, Write and execute Python code in real-time, Move and organize cells | Google account / OAuth | Free (Google Colab standard) |
| [Perplexity Comet](https://www.perplexity.ai) | ★★★★★ | Browser API, Native integration | autonomous web navigation, form filling and data extraction, product comparison | Perplexity account | Freemium with premium tier |
| [Stagehand](https://github.com/browserbase/stagehand) | ★★★★★ | SDK | navigate, act, extract | API key | open-source + hosted |
| [Vercel Labs agent-browser](https://github.com/vercel-labs/agent-browser) | ★★★★★ | SDK | navigate, click, fill-form | none | free |
| [Bright Data Agent Browser](https://brightdata.com/products/scraping-browser) | ★★★★☆ | REST API, Puppeteer, Playwright | Scalable browser automation, Built-in CAPTCHA solving, Automatic proxy rotation | API credentials | Pay-as-you-go at $8/GB or included GB plans ($5-7/GB, 71-399GB/month) |

## 👥 CRM & Sales

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Attio MCP Server](https://attio.com) | ★★★★★ | MCP, REST API | create-contact, update-contact, create-deal | API key | freemium |
| [Intellebox.ai](https://intellebox.ai) | ★★★★★ | REST API, SDK | AI Virtual Advisors (avatars trained on firm expertise), Autonomous client engagement and inquiry handling, Personalized wealth management recommendations | API key / OAuth | Contact for pricing |
| [Salesforce Agentforce Sales](https://www.salesforce.com) | ★★★★★ | REST API, Salesforce SDK, MCP | lead qualification, pipeline management, proposal generation | OAuth 2.0 | Enterprise pricing (part of Salesforce suite) |
| [Confirm](https://www.confirm.com) | ★★★★☆ | REST API, Slack integration, Microsoft Teams integration | Autonomous performance review facilitation, Manager coaching and capability building, Real-time bias detection in calibration sessions | OAuth | $8-14 per person per month (base + optional add-ons) |
| [HubSpot MCP Server](https://www.hubspot.com) | ★★★★☆ | MCP, REST API | manage-contacts, manage-deals, create-tickets | API key / OAuth | freemium |

## 🎧 Support & Ticketing

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Console](https://www.console.com) | ★★★★★ | REST API, webhook, natural language playbooks | Auto-resolve IT service requests, Password reset automation, Access provisioning | OAuth | Enterprise (custom) |
| [Lucidya](https://lucidya.com) | ★★★★★ | REST API, webhook, SDK | handle customer conversations autonomously, detect and respond to customer intents, understand 15+ Arabic dialects with 92%+ accuracy | API key | Enterprise tier (ROI-based: 60-70% cost reduction, 90%+ FCR) |
| [Intercom Fin AI Agent](https://www.intercom.com/fin) | ★★★★☆ | REST API, webhooks | resolve-ticket, answer-questions, escalate | API key | usage-based |
| [Zendesk AI Agent](https://www.zendesk.com/ai) | ★★★☆☆ | REST API, webhooks | route-ticket, auto-respond, classify-intent | API key / OAuth | enterprise |

## 💬 Messaging & Chat

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Sierra](https://sierra.ai) | ★★★★★ | REST API, Webhook, Native integrations | Multi-turn conversational reasoning, Autonomous issue resolution, Cross-channel messaging (digital, SMS, voice) | API key, OAuth | Outcome-based pricing model; contracts typically start $150K-$1.5M+ annually |
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
| [Agentuity](https://agentuity.com) | ★★★★★ | REST API, SDK, gRPC | Build and deploy agentic applications, Long-running agent execution with pausing/resuming, Stateful persistence and session management | API key / SDK auth | Usage-based (compute, storage, execution time) |
| [Alibaba Wukong](https://www.alibaba.com) | ★★★★★ | REST API, SDK | coordinate multiple agents, document automation, transcription processing | API key | Invitation-only beta (pricing TBD) |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io) | ★★★★★ | MCP | tool-connection, resource-access, prompt-sharing | varies | free |
| [Axiory.ai](https://axiory.ai) | ★★★★★ | REST API, MCP | access global financial markets, trade multiple asset classes, real-time market data | API key | Custom |
| [Beam AI Platform (Agent OS)](https://beam.ai) | ★★★★★ | REST API, web interface | No-code agent creation from SOPs, Multi-language customer support, 24/7 availability automation | OAuth, API key | Enterprise (contact sales) |
| [Calljmp](https://calljmp.com) | ★★★★★ | REST API, SDK, TypeScript | Execute agents as code in TypeScript, Manage agent state and retries, Persistent memory across agents | API key | Usage-based (contact for details) |
| [CrewAI](https://www.crewai.com) | ★★★★★ | SDK | role-based-agents, task-delegation, multi-agent | API key | open-source + enterprise |
| [Discern Security](https://www.discernsecurity.com) | ★★★★★ | REST API, integration hub | Automated security controls assessment, Real-time security posture visibility, Vulnerability prioritization and remediation planning | API key | Enterprise (contact sales) |
| [Domo MCP Server](https://www.domo.com/) | ★★★★★ | MCP, REST API | Query datasets and analytics, Trigger workflows and automation, Create dashboards and applications | OAuth | Enterprise (contact sales) |
| [JetBrains Central](https://console.jetbrains.cloud/) | ★★★★★ | REST API, cloud-execution, IDE-integration | Multi-agent orchestration and coordination, Cloud agent runtimes and computation provisioning, Policy enforcement and identity/access management | OAuth / API key (details pending EAP) | Per-organization pricing model (details pending Q2 2026 launch) |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | ★★★★★ | SDK, REST API | graph-orchestration, stateful-agents, multi-agent | API key | open-source + hosted |
| [Mistral Agents API](https://mistral.ai/news/agents-api) | ★★★★★ | REST API, Python SDK, MCP | Multi-agent orchestration and handoffs, Code execution in sandboxed environment, Web search and information retrieval | API key | Pay-per-use (API consumption) |
| [Nutanix Agentic AI](https://www.nutanix.com/products/agentic-ai) | ★★★★★ | Kubernetes, MCP, REST API | Agent infrastructure orchestration, MCP server integration for tool connectivity, Model-as-a-Service (MaaS) | Enterprise authentication | Enterprise licensing |
| [Nvidia Agent Toolkit](https://www.nvidia.com) | ★★★★★ | Python SDK, REST API | agent creation and deployment, autonomous agent orchestration, multi-agent coordination | API key | Open source (free) |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | ★★★★★ | SDK, REST API | agent-creation, tool-use, handoff | API key | usage-based |
| [Tray.ai](https://tray.io) | ★★★★★ | REST API, Webhooks, MCP | No-code agent builder (Merlin), ITSM agent for IT support automation, HR agent for policy automation, PTO, profile updates | API key, OAuth | Enterprise (custom) |
| [Vellum AI](https://vellum.ai) | ★★★★★ | REST API, Python SDK, TypeScript SDK | Agent building from natural language prompts, Multi-step workflow orchestration, Autonomous agent execution | API key, SSO/SAML | Custom enterprise pricing |
| [Microsoft Copilot Cowork](https://www.microsoft.com) | ★★★★☆ | REST API, Azure SDK | multi-agent orchestration, autonomous task execution, enterprise system integration | Azure AD / OAuth | Enterprise (part of Microsoft 365/Azure) |

## 🔄 Workflow Automation

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Novaworks.ai](https://novaworks.ai) | ★★★★★ | REST API, ServiceNow integration, OAuth | AI agents for employee lifecycle management, Autonomous payroll and benefits processing, Workforce planning agents | OAuth, ServiceNow authentication | Enterprise (contact sales) |
| [Oracle Fusion Agentic Applications](https://www.oracle.com/applications/) | ★★★★★ | REST API, native Oracle APIs, webhook | execute business decisions autonomously within guardrails, coordinate multi-agent teams with specific roles and expertise, maintain shared context across workflow steps and time | OAuth 2.0, Oracle Cloud Identity | Included with Oracle Fusion Cloud Applications subscriptions (ERP, HCM, SCM, CX) |
| [Workday Sana Self-Service Agent](https://www.workday.com/en-us/products/sana.html) | ★★★★★ | REST API, Custom Workday API | HR workflow automation (300+ skills), Finance operations automation, Payroll management | Workday OAuth | Enterprise licensing (part of Workday Cloud suite) |
| [n8n](https://n8n.io) | ★★★★☆ | REST API, webhooks, SDK | workflow-execution, trigger, condition | API key | open-source + cloud |
| [Reclaim.ai](https://reclaim.ai) | ★★★★☆ | REST API, calendar integration, automation workflows | Intelligent time blocking, Focus time protection, Habit and task scheduling | OAuth | Freemium + premium |
| [Make (formerly Integromat)](https://www.make.com) | ★★★☆☆ | REST API, webhooks | trigger-scenario, monitor-run, data-mapping | API key | freemium |

## 🔌 Tool Gateways & MCP

| Service | Score | Protocols | Capabilities | Auth | Pricing |
|---------|-------|-----------|--------------|------|---------|
| [Agentic Fabriq](https://www.agenticfabriq.com) | ★★★★★ | REST API, OAuth 2.0, SAML | Agent registration and lifecycle management, Agent-specific SSO/MFA, Identity provider (IDP) linking | OAuth 2.0, SAML, API key | Custom enterprise pricing |
| [Arcade AI](https://arcade.ai) | ★★★★★ | REST API, SDK | tool-execution, auth-management, permission-control | API key | usage-based |
| [Base44](https://base44.com) | ★★★★★ | REST API, SDK, CLI | Autonomous backend generation from descriptions, Database management with MongoDB-compatible queries, User authentication (OAuth, Email/Password) | API key / OAuth | Usage-based (storage, compute, functions) |
| [Composio](https://composio.dev) | ★★★★★ | REST API, SDK, MCP | tool-routing, auth-management, trigger | API key | freemium |
| [E2B Code Interpreter Sandbox](https://e2b.dev) | ★★★★★ | SDK (Python/TypeScript/Node.js), REST API, Firecracker microVMs | Secure code execution (Python, JavaScript, Ruby, C++), File system access and manipulation, Terminal command execution | API key | Pay-as-you-go + enterprise plans |
| [Fast.io Agentic Workspace](https://fast.io) | ★★★★★ | REST API, MCP (14 native tools), CLI | Shared project workspaces for agents and humans, Semantic search across files (AI-indexed), Retrieval-augmented generation (RAG) | API key, OAuth | 50GB free tier with credits; $10-40/mo plans; enterprise licensing |
| [MCP Server Directories](https://mcpmarket.com) | ★★★★★ | MCP | tool-discovery, tool-connection | varies | free |
| [TestMu AI](https://testmuai.com) | ★★★★★ | REST API, CI/CD integration, Cloud infrastructure | Agent-to-agent testing validation, Autonomous multi-agent scenario generation, Multi-modal testing (text, voice, hybrid) | API key, OAuth | Custom enterprise pricing with usage-based tiers |
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
