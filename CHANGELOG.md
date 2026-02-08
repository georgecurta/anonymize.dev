# Changelog

All notable changes to the Anonymize.dev website will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.3] - 2026-02-08

### Added
- **llms.txt** - AI crawler-friendly site description
- **security.txt** - Security vulnerability disclosure policy (/.well-known/security.txt)
- **robots.txt** - AI crawler directives (GPTBot, ClaudeBot, Anthropic-AI, PerplexityBot, etc.)

### Changed
- **Open Graph tags** - Added og:image, og:locale, og:site_name meta tags
- **Twitter Cards** - Added twitter:card, twitter:title, twitter:description, twitter:image
- **Contrast fix** - Darkened --syntax-slate color for better WCAG compliance
- **SEO fix** - Replaced generic "Learn more" with descriptive "Explore MCP Server" link text

### Lighthouse Scores
- Performance: 96
- Accessibility: 100
- Best Practices: 100
- SEO: 100

---

## [1.0.1] - 2026-02-08

### Changed
- **Homepage hero**: Clearer messaging - "Data Anonymization for AI Workflows" with "For Developers" badge
- **Terminal example**: Before/after demonstration showing real data → tokenized data transformation
- **New section**: "What is Anonymize.dev?" explaining problem (data leakage) and solution (automatic PII protection)
- **Works with icons**: Visual indicators for Claude Desktop, Cursor IDE, ChatGPT, REST API
- **CTA button**: "See How It Works" scrolls to explanation section

---

## [1.0.0] - 2026-02-08

### Added

#### Website Pages (10 total)
- **Homepage** (`index.html`) - Hero with MCP Server highlight, product cards, how it works flow, pricing preview
- **MCP Server** (`mcp.html`) - Primary product page with installation guides for Claude Desktop & Cursor IDE
- **Desktop App** (`desktop.html`) - Windows download, platform support, supported file formats
- **Office Add-in** (`office.html`) - Word/Excel/PowerPoint integration, use cases
- **Features** (`features.html`) - 50+ entity types, 48 languages, 5 anonymization methods, NLP engines
- **Pricing** (`pricing.html`) - All 4 tiers with feature comparison table, token explanation, FAQ
- **Documentation** (`docs.html`) - MCP setup, API reference, code examples (Python, Node.js, cURL)
- **Contact** (`contact.html`) - Form with reCAPTCHA, interest topics, response time info
- **Privacy Policy** (`datenschutz.html`) - German GDPR privacy notice
- **Imprint** (`impressum.html`) - German legal notice

#### Brand Assets
- Logo with concentric rings and neon glow (PNG, PDF)
- Favicons (16px, 32px, 48px, 64px, 128px, 256px)
- Hero graphic with data flow visualization
- Product icons (MCP Server, Desktop App, Office Add-in, API)
- Entity type icons (Person, Email, Phone, Location, ID Card, Credit Card, Code)
- Feature icons (Shield, Lock, Globe, Speed, Terminal)
- Pattern tile for backgrounds

#### Marketing Materials
- LinkedIn post graphic (1200x627)
- Twitter/X post graphic (1200x675)
- Instagram square (1080x1080)
- Web banner (1920x400)
- Email banner (600x200)
- Product marketing cards (3x 400x500)

#### Design System - "Neon Protocol"
- Cyberpunk/developer-first aesthetic
- Custom dark theme with neon accents:
  - Void Black (#0a0a0f)
  - Electric Cyan (#00ffff)
  - Terminal Green (#00ff41)
  - Neon Magenta (#ff00ff)
- Typography: Space Grotesk + Inter + JetBrains Mono
- CSS animations (matrix rain, scroll reveal, glow effects, typing)

#### Technical
- Responsive CSS with mobile-first approach
- JavaScript with scroll-triggered animations, terminal effects
- Accessibility: skip navigation, ARIA landmarks, reduced motion support
- SEO: robots.txt, sitemap.xml, meta tags, Open Graph
- Contact form backend with MS Graph + reCAPTCHA v3

#### Infrastructure
- GitHub repository configured: github.com/georgecurta/anonymize.dev
- Production deployment via git push
- Ready for nginx configuration with HTTPS, HTTP/2, HSTS

### Notes
- MCP Server is the primary highlight of this site
- All content verified against anonym.legal source material
- Legal pages reference anonym.legal for complete details
- Cyberpunk aesthetic intentionally contrasts with anonymize.education's "Protective Clarity"

---

## [0.1.0] - 2026-02-07

### Added

#### Project Foundation
- Created project structure for anonymize.dev
- Established "Neon Protocol" design philosophy (cyberpunk/developer-first)
- Defined color palette with dark theme and neon accents
- Selected typography stack: Space Grotesk, Inter, JetBrains Mono

#### Brand Assets (brand/)
- DESIGN-PHILOSOPHY.md - Neon Protocol visual philosophy
- THEME-NEON-PROTOCOL.md - Complete color and typography specification

#### Documentation
- CLAUDE.md - Project memory and guidelines
- MARKETING-CONCEPT.md - Comprehensive marketing strategy
- CHANGELOG.md - This file

### Planned Features

#### Website Pages (10 total)
- Homepage with MCP Server highlight
- MCP Server dedicated page (main feature)
- Desktop App page
- Office Add-in page
- Features overview
- Pricing with token explanation
- Documentation with code examples
- Contact form
- Privacy policy (datenschutz)
- Legal notice (impressum)

#### Visual Elements
- Matrix rain background animation
- Terminal typing effects
- Data flow visualizations
- Neon glow hover states
- Interactive code examples

#### Technical
- Same infrastructure as anonymize.education
- Contact form with MS Graph + reCAPTCHA
- Playwright test suites
- Mobile responsive
- Accessibility compliant

### Notes
- MCP Server positioned as primary product highlight
- Target audience: software developers, AI engineers, DevOps
- Aesthetic intentionally contrasts with anonymize.education's "Protective Clarity"
