# Neon Protocol Theme

A cyberpunk-inspired theme for Anonymize.dev - Developer-First Data Protection

## Color Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Void Black** | #0a0a0f | 10, 10, 15 | Primary background, deep sections |
| **Terminal Dark** | #12121a | 18, 18, 26 | Cards, elevated surfaces |
| **Matrix Gray** | #1e1e2e | 30, 30, 46 | Secondary backgrounds, borders |
| **Syntax Slate** | #6b7280 | 107, 114, 128 | Muted text, comments |
| **Electric Cyan** | #00ffff | 0, 255, 255 | Primary actions, links, highlights |
| **Neon Magenta** | #ff00ff | 255, 0, 255 | Warnings, secondary accents |
| **Terminal Green** | #00ff41 | 0, 255, 65 | Success, code output, MCP active |
| **Pulse Blue** | #0080ff | 0, 128, 255 | API references, integrations |
| **Hot Coral** | #ff3366 | 255, 51, 102 | Errors, dangerous actions |
| **Pure White** | #ffffff | 255, 255, 255 | Headlines, important text |
| **Ghost White** | #e5e5e5 | 229, 229, 229 | Body text |

## Extended Palette

### Gradients
- **Hero Gradient**: `linear-gradient(135deg, #0a0a0f 0%, #1e1e2e 50%, #12121a 100%)`
- **Neon Glow**: `linear-gradient(90deg, #00ffff 0%, #ff00ff 50%, #00ff41 100%)`
- **Matrix Rain**: `linear-gradient(180deg, rgba(0,255,65,0.8) 0%, rgba(0,255,65,0) 100%)`

### Glow Effects
```css
--glow-cyan: 0 0 20px rgba(0,255,255,0.5), 0 0 40px rgba(0,255,255,0.3);
--glow-magenta: 0 0 20px rgba(255,0,255,0.5), 0 0 40px rgba(255,0,255,0.3);
--glow-green: 0 0 20px rgba(0,255,65,0.5), 0 0 40px rgba(0,255,65,0.3);
```

## Typography

### Primary Font: JetBrains Mono
- The developer's monospace typeface
- Excellent ligature support
- Perfect for code snippets and technical content
- Use for: Code blocks, API examples, terminal outputs

### Secondary Font: Space Grotesk
- Geometric sans-serif with technical character
- Sharp terminals suggest precision
- Use for: Headlines, navigation, CTAs

### Body Font: Inter
- Clean, readable at all sizes
- Professional without being corporate
- Use for: Body text, descriptions, documentation

### Font Stack
```css
--font-mono: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace;
--font-display: 'Space Grotesk', 'Inter', system-ui, sans-serif;
--font-body: 'Inter', system-ui, -apple-system, sans-serif;
```

## Visual Elements

### Core Motifs
- **Terminal windows**: Rounded-corner frames with traffic light controls
- **Matrix rain**: Cascading code/characters (animated)
- **Data flow lines**: Animated paths showing data transformation
- **Hexagonal patterns**: Cryptographic/blockchain references
- **Scanlines**: Subtle CRT-style overlay for retro-tech feel

### Component Styling
- **Cards**: Dark with subtle border glow on hover
- **Buttons**: Solid neon fills with glow on hover
- **Code blocks**: Terminal-style with syntax highlighting
- **Borders**: 1px solid with low-opacity neon colors
- **Shadows**: Neon glow effects instead of traditional shadows

### Animation Principles
- **Timing**: Technical, precise (150ms, 300ms, 500ms)
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` for most transitions
- **Effects**: Glow pulses, scanline sweeps, typing animations

## Icon Style

- Line-based, 1.5-2px stroke weight
- Geometric, angular designs
- Neon accent coloring
- Subtle glow on interactive states

## Best For

Developer tools, AI/ML products, API services, cybersecurity, data protection, privacy tools, CLI applications, technical SaaS
