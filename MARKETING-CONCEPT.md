# Anonymize.dev Marketing Concept

## Brand Positioning

**Domain**: anonymize.dev
**Target Audience**: Software developers, AI engineers, DevOps professionals, tech-forward companies
**Parent Platform**: anonym.legal
**Design Theme**: Neon Protocol (Cyberpunk/Developer-First)

### Value Proposition

**Primary Message**: "Privacy-as-Code. Protect data in your AI workflows."

**Elevator Pitch**: Anonymize.dev is the developer toolkit for data privacy. Integrate our MCP Server to automatically redact PII before it hits your AI models, use our Desktop App for bulk document processing, or embed privacy directly in your Office workflows. Ship features, not data breaches.

### Key Differentiators

1. **MCP-First Architecture**: Native integration with Claude Desktop, Cursor IDE, and AI toolchains
2. **Developer Experience**: CLI tools, SDK access, API documentation
3. **Zero-Knowledge Processing**: Your data stays yours—we process, we don't store
4. **Technical Transparency**: Open about our NLP engines (spaCy, Stanza, XLM-RoBERTa)

---

## Site Structure

### Page 1: Homepage (index.html)
**Hero Section**
- Headline: "Privacy-as-Code"
- Subheadline: "Protect sensitive data in your AI workflows. Automatically."
- Visual: Animated terminal showing data transformation (PII → tokenized)
- CTA: "Install MCP Server" (primary), "View Docs" (secondary)

**Trust Bar**
- ISO 27001 certified
- 50+ entity types
- 48 languages
- German infrastructure

**Product Overview** (3 cards)
1. MCP Server (highlight badge: "FEATURED")
2. Desktop App
3. Office Add-in

**Code Example Section**
```bash
# Install via MCP configuration
{
  "mcpServers": {
    "anonymize": {
      "command": "npx",
      "args": ["-y", "@anonym-legal/mcp-server"]
    }
  }
}
```

**How It Works** (animated data flow diagram)
1. Your prompt with sensitive data
2. MCP intercepts and tokenizes PII
3. Sanitized prompt sent to AI
4. Response with tokens restored

**Pricing Preview** (link to full pricing page)

---

### Page 2: MCP Server (mcp.html) - THE HIGHLIGHT PAGE
**Hero**
- Headline: "Your AI's Privacy Shield"
- Subheadline: "Automatic PII protection for Claude, Cursor, and beyond"
- Visual: Animated MCP proxy diagram

**Integration Cards**
- Claude Desktop
- Cursor IDE
- ChatGPT (Coming Soon)
- Custom HTTP API

**Feature Deep-Dive**
- Real-time interception
- Reversible tokenization
- 50+ entity types detected
- 48-language support

**Code Examples**
```bash
# Claude Desktop configuration
cat ~/.config/claude/claude_desktop_config.json
```

```json
{
  "mcpServers": {
    "anonymize": {
      "command": "npx",
      "args": ["-y", "@anonym-legal/mcp-server"],
      "env": {
        "ANONYM_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Architecture Diagram**
Visual showing: User → Prompt → MCP Server → Tokenized Prompt → AI Model → Response → MCP Server → Restored Response → User

**Pricing Note**: Included with Pro & Business plans

---

### Page 3: Desktop App (desktop.html)
**Hero**
- Headline: "Bulk Privacy. Local First."
- Subheadline: "Process documents without leaving your machine"
- Visual: App screenshot in cyberpunk styling

**Platform Support**
- Windows: Available now (FREE)
- macOS: Coming Soon
- Linux: Coming Soon

**Features**
- Drag-and-drop interface
- PDF, DOCX, TXT support
- Local encrypted storage
- Documents never leave your device
- Only extracted text sent for analysis

**Download Section**
- Windows installer download
- System requirements
- Installation guide

---

### Page 4: Office Add-in (office.html)
**Hero**
- Headline: "Privacy in Your Workflow"
- Subheadline: "Anonymize directly in Word, Excel, and PowerPoint"

**Supported Applications**
- Microsoft Word
- Microsoft Excel
- Microsoft PowerPoint

**Workflow Demo**
1. Select text in your document
2. Click Anonymize button
3. Choose anonymization method
4. Text is protected in-place

**Integration with OpenOffice**
- LibreOffice support
- OpenOffice support

---

### Page 5: Features (features.html)
**Entity Detection**
- 50+ entity types
- Visual grid showing: Names, Emails, Phone Numbers, Credit Cards, SSNs, IBANs, IP Addresses, Medical IDs, etc.

**Language Support**
- 48 languages
- RTL support (Arabic, Hebrew, Persian, Urdu)
- Visual language grid

**Anonymization Methods**
1. **Replace**: Swap with realistic fake data
2. **Redact**: Remove completely ([REDACTED])
3. **Hash**: SHA-256 one-way hashing
4. **Encrypt**: AES-256-GCM reversible encryption
5. **Mask**: Partial hiding (John D*** → J*** D***)

**NLP Engine Stack**
- spaCy
- Stanza
- XLM-RoBERTa

**Security**
- ISO 27001:2022 certified
- German Hetzner servers
- Zero-knowledge authentication (Argon2id)
- 24-word BIP39 recovery phrase

---

### Page 6: Pricing (pricing.html)
**Token-Based Pricing**
- Clear explanation of token system
- Token = amount of text processed

**Tiers**
| Plan | Price | Tokens | Best For |
|------|-------|--------|----------|
| Free | €0/month | 200 | Individual developers testing |
| Basic | €3/month | 1,000 | Regular API usage |
| Pro | €15/month | 4,000 | MCP Server + heavy usage |
| Business | €29/month | 10,000 | Teams and enterprises |

**Feature Matrix**
- MCP Server: Pro & Business only
- API Access: All tiers
- Office Add-in: All tiers
- Priority Support: Business only

**Enterprise Section**
- Custom volume
- SSO integration
- Dedicated infrastructure
- Contact sales CTA

---

### Page 7: Docs (docs.html)
**Quick Start**
- MCP Setup (Claude, Cursor)
- API Authentication
- Desktop App Installation

**API Reference**
- Endpoints
- Authentication
- Request/Response examples

**SDK Reference**
- JavaScript/Node.js
- Python
- cURL examples

**Integration Guides**
- Claude Desktop
- Cursor IDE
- Custom integrations

---

### Page 8: Contact (contact.html)
**Developer-focused form**
- Name
- Email
- GitHub username (optional)
- Interest: MCP Server, API Access, Desktop App, Enterprise, Other
- Message

**Quick Links**
- GitHub (if public)
- Discord (if available)
- Main Platform (anonym.legal)

---

### Page 9: Legal (impressum.html, datenschutz.html)
- German legal requirements
- Reference to anonym.legal for complete policies

---

## Visual Components

### Hero Animations
1. **Matrix Rain**: Cascading characters in background
2. **Terminal Typing**: Animated code appearing in hero terminal
3. **Data Flow**: Animated lines showing data transformation
4. **Glow Pulse**: Neon elements pulsing subtly

### Interactive Elements
1. **Code Copy Button**: One-click copy with confirmation
2. **Tab Switcher**: For different platform examples
3. **Terminal Widget**: Interactive command examples
4. **Entity Detector Demo**: Live input showing detected entities

### Card Designs
- Dark background (#12121a)
- 1px border with cyan glow on hover
- Icon in top-left with neon coloring
- Clean typography hierarchy

---

## Content Tone

### Voice
- Technical but accessible
- Direct, no marketing fluff
- First-person plural ("we")
- Developer-to-developer

### Examples
- **Good**: "MCP Server intercepts prompts, tokenizes PII, forwards to your AI."
- **Bad**: "Our revolutionary AI-powered solution leverages cutting-edge technology..."

- **Good**: "Free tier: 200 tokens. That's ~15-18 pages monthly."
- **Bad**: "Generous free tier to get you started on your privacy journey!"

### CTAs
- "Install Now"
- "View Docs"
- "Get API Key"
- "Start Free"

---

## SEO Strategy

### Primary Keywords
- MCP Server privacy
- AI data anonymization
- Claude Desktop privacy
- Cursor IDE PII protection
- Developer privacy tools

### Page-Specific Keywords
- **Homepage**: AI privacy, developer data protection, MCP anonymization
- **MCP Page**: MCP Server, Model Context Protocol, Claude privacy, Cursor privacy
- **Features**: PII detection, GDPR compliance, entity recognition, NER

---

## Technical Implementation

### Stack
- Static HTML/CSS/JavaScript (consistent with anonymize.education)
- No build step required
- CDN-hosted fonts (JetBrains Mono, Space Grotesk, Inter)
- Minimal JavaScript for animations

### Performance Targets
- Lighthouse Performance: 95+
- First Contentful Paint: <1.5s
- Total Bundle Size: <100KB

### Accessibility
- WCAG 2.1 AA compliance
- High contrast mode support
- Reduced motion support
- Keyboard navigation

---

## Deployment

### Infrastructure
- Same server as anonymize.education
- Nginx with HTTPS, HTTP/2, HSTS
- Let's Encrypt SSL

### Git Flow
- **origin**: GitHub repository
- **production**: macxpress.net deployment
- Same SSH key configuration as anonymize.education

---

## File Structure

```
anonymize.dev/
├── index.html              # Homepage
├── mcp.html                # MCP Server (highlight)
├── desktop.html            # Desktop App
├── office.html             # Office Add-in
├── features.html           # All features
├── pricing.html            # Pricing tiers
├── docs.html               # Documentation
├── contact.html            # Contact form
├── impressum.html          # Legal notice
├── datenschutz.html        # Privacy policy
├── api/                    # Backend (same pattern as education)
│   ├── send-message.php
│   └── config.php
├── css/
│   ├── style.css           # Main styles
│   └── animations.css      # Neon effects, matrix rain
├── js/
│   ├── main.js             # Core functionality
│   └── terminal.js         # Terminal animations
├── images/                 # Production assets
├── brand/                  # Source assets (not deployed)
│   ├── DESIGN-PHILOSOPHY.md
│   ├── THEME-NEON-PROTOCOL.md
│   ├── assets/
│   └── marketing/
├── tests/                  # Playwright tests
├── CLAUDE.md               # This project's memory
├── MARKETING-CONCEPT.md    # This file
└── CHANGELOG.md
```

---

## Success Metrics

### Launch Goals
- [ ] All 10 pages live
- [ ] MCP setup working in docs
- [ ] Contact form functional
- [ ] Mobile responsive
- [ ] Accessibility compliant

### Post-Launch
- MCP Server installation tracking
- API key generation metrics
- Contact form submissions
- Documentation page views
