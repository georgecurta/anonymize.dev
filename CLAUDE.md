# Claude Memory - Anonymize.dev

## Project Overview

**Domain**: anonymize.dev
**Purpose**: Developer-focused marketing site for data anonymization tools with MCP Server highlight
**Parent Platform**: anonym.legal
**Design Theme**: Neon Protocol (Cyberpunk)
**Status**: In Development

## Key Information

### Content Guidelines
- ALL content must be verified against anonym.legal source material
- NO assumptions or invented features
- Developer-first tone: technical, direct, no marketing fluff
- Code examples must be accurate and tested

### Verified Product Features
- 50+ entity types detected
- 48 languages supported (including RTL)
- 5 anonymization methods: Replace, Redact, Hash (SHA-256), Encrypt (AES-256-GCM), Mask
- NLP engines: spaCy, Stanza, XLM-RoBERTa
- ISO 27001:2022 certified
- 99.9% uptime SLA
- German Hetzner servers
- Zero-knowledge authentication with Argon2id
- 24-word BIP39 recovery phrase

### MCP Server (THE HIGHLIGHT)
- Privacy shield between AI tools and sensitive data
- Automatic PII detection and tokenization
- Reversible tokenization for response restoration
- Supported integrations:
  - Cursor IDE
  - Claude Desktop
  - ChatGPT (coming soon)
  - Custom HTTP integrations
- Requires Pro or Business tier

### Pricing (verified from source)
- Free: €0/month, 200 tokens
- Basic: €3/month, 1,000 tokens
- Pro: €15/month, 4,000 tokens (MCP enabled)
- Business: €29/month, 10,000 tokens (MCP enabled)

### Products
- **MCP Server**: AI tool integration (Pro+ tiers) - THE HIGHLIGHT
- **Desktop App**: Windows only (FREE), macOS/Linux coming soon
- **Office Add-in**: Word, Excel, PowerPoint integration
- **OpenOffice Add-in**: LibreOffice/OpenOffice integration

## Design System

**Theme**: "Neon Protocol"

**Colors**:
- Void Black: #0a0a0f (primary background)
- Terminal Dark: #12121a (cards, surfaces)
- Matrix Gray: #1e1e2e (secondary backgrounds)
- Electric Cyan: #00ffff (primary actions)
- Neon Magenta: #ff00ff (secondary accents)
- Terminal Green: #00ff41 (success, MCP active)
- Pulse Blue: #0080ff (API references)
- Hot Coral: #ff3366 (errors)
- Pure White: #ffffff (headlines)
- Ghost White: #e5e5e5 (body text)

**Typography**:
- Display: Space Grotesk
- Body: Inter
- Code: JetBrains Mono

**Visual Motifs**:
- Terminal windows with traffic light controls
- Matrix rain (animated cascading characters)
- Data flow visualizations
- Hexagonal patterns
- Subtle scanline overlays
- Neon glow effects

## Deployment

### Remotes (to be configured)
- **origin**: https://github.com/georgecurta/anonymize.dev.git
- **production**: ssh://mac46-190@macxpress.net:6535/home/mac46-190/repos/anonymize.dev.git

### Deploy Command
```bash
cd C:\Dev\MacXpress\anonymize.dev
git push origin main
GIT_SSH_COMMAND='ssh -i ~/.ssh/macxpress26 -o IdentitiesOnly=yes' git push production main
```

### Server
- Web root: /var/www/anonymize.dev
- SSL: Let's Encrypt (auto-renewal)
- Nginx with HTTPS, HTTP/2, HSTS, security headers

## File Structure

```
anonymize.dev/
├── *.html              # 10 pages (index, mcp, desktop, office, features, pricing, docs, contact, datenschutz, impressum)
├── api/                # Backend API
│   ├── send-message.php    # Contact form handler
│   └── config.php          # Placeholder config
├── css/
│   ├── style.css           # Main styles (Neon Protocol theme)
│   └── animations.css      # Matrix rain, glow effects
├── js/
│   ├── main.js             # Core functionality
│   └── terminal.js         # Terminal animations
├── images/             # Production assets
├── brand/              # NOT deployed (source assets)
│   ├── DESIGN-PHILOSOPHY.md
│   ├── THEME-NEON-PROTOCOL.md
│   ├── assets/
│   └── marketing/
├── tests/              # Playwright test suites
├── CLAUDE.md           # This file
├── MARKETING-CONCEPT.md
└── CHANGELOG.md
```

## Contact Form Backend

### Configuration
- Production config: `/var/www/config/anonymize-dev-mail.php`
- Uses same reCAPTCHA keys as curta.solutions/anonymize.education
- Uses same MS Graph credentials as macxpress.net
- Emails sent via Microsoft Graph API

### Interest Topics
- mcp: MCP Server Integration
- api: API Access
- desktop: Desktop App
- enterprise: Enterprise Solution
- support: Technical Support
- other: General Inquiry

## Related Sites

| Site | Domain | Purpose |
|------|--------|---------|
| Main Platform | anonym.legal | Source of truth for all features |
| Education | anonymize.education | Schools & universities focus |
| **Developer** | **anonymize.dev** | **This site - MCP & developer tools** |
| Enterprise | anonymize.solutions | Enterprise deployments |

## Important Notes

1. MCP Server is the primary highlight of this site
2. Cyberpunk/developer aesthetic contrasts with education site's "Protective Clarity"
3. Code examples must be accurate and tested before publication
4. Legal pages reference anonym.legal for complete details
5. brand/ directory excluded from production deployment

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-02-07 | Initial concept, design philosophy, project structure |
