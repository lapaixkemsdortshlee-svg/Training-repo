# Training-repo — Professional Website Creation Toolkit

This repo is preloaded with design/UI skills and an MCP server so an AI coding
agent can build professional websites out of the box.

## Installed skills (`.claude/skills/`)

- **frontend-design** — distinctive, non-templated visual direction (typography,
  palette, layout). Source: anthropics/skills.
- **ui-ux-pro-max** (+ `design`, `design-system`, `ui-styling`, `brand`,
  `banner-design`, `slides`) — design intelligence: 67 styles, 161 palettes, 57
  font pairings, 25 charts across 21 stacks. Source: nextlevelbuilder.
- **find-skills** — discover/install additional agent skills on demand. Source:
  vercel-labs/skills.
- **gstack** — full 54-skill engineering suite vendored under
  `.claude/skills/gstack/`. Each skill is exposed as a top-level entry (e.g.
  `/design-consultation`, `/design-shotgun`, `/design-html`, `/design-review`,
  `/landing-report`, `/office-hours`, `/autoplan`, `/review`, `/ship`). Start
  with `/gstack` to route. Source: garrytan/gstack.
  - Note: gstack's browser/deploy/iOS skills expect local daemons/binaries that
    are built by its `./setup` script. Those runtime features are not built here;
    the skill guidance is available, but browser-driven skills won't run in an
    ephemeral web session without running gstack's setup locally.

## MCP server — 21st.dev (`.mcp.json`)

The `21st` HTTP MCP server (component generation) reads its key from the
`TWENTYFIRST_API_KEY` environment variable — it is **not** hard-coded.

To use it:
1. Copy `.env.example` to `.env` and set `TWENTYFIRST_API_KEY`, or set the var in
   your Claude Code on the web environment settings.
2. The key is never committed (`.env` is gitignored).

> Security: the API key was shared in plaintext during setup, so treat it as
> exposed and rotate it at https://21st.dev before relying on it.
