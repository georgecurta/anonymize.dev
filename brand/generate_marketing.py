#!/usr/bin/env python3
"""
Anonymize.dev Marketing Materials Generator
Neon Protocol Theme - Social Media & Marketing Assets
"""

import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# Neon Protocol Colors
COLORS = {
    'void_black': '#0a0a0f',
    'terminal_dark': '#12121a',
    'matrix_gray': '#1e1e2e',
    'syntax_slate': '#6b7280',
    'electric_cyan': '#00ffff',
    'neon_magenta': '#ff00ff',
    'terminal_green': '#00ff41',
    'pulse_blue': '#0080ff',
    'hot_coral': '#ff3366',
    'pure_white': '#ffffff',
    'ghost_white': '#e5e5e5',
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_bg(width, height):
    """Create dark gradient background."""
    img = Image.new('RGB', (width, height), hex_to_rgb(COLORS['void_black']))
    draw = ImageDraw.Draw(img)

    # Add subtle grid
    grid_color = hex_to_rgb(COLORS['matrix_gray'])
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(*grid_color, 50), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(*grid_color, 50), width=1)

    return img

def add_glow_text(draw, text, pos, font, color, glow_color=None):
    """Draw text with neon glow effect."""
    if glow_color is None:
        glow_color = color
    x, y = pos

    # Glow layers
    glow_rgb = hex_to_rgb(glow_color) if isinstance(glow_color, str) else glow_color
    for offset in range(5, 0, -1):
        alpha = int(40 - offset * 6)
        glow = (*glow_rgb, alpha)
        for dx in range(-offset, offset + 1):
            for dy in range(-offset, offset + 1):
                try:
                    draw.text((x + dx, y + dy), text, font=font, fill=glow)
                except:
                    pass

    # Main text
    text_color = hex_to_rgb(color) if isinstance(color, str) else color
    draw.text((x, y), text, font=font, fill=text_color)

def create_linkedin_post(output_dir):
    """Create LinkedIn post graphic (1200x627)."""
    width, height = 1200, 627
    img = create_gradient_bg(width, height)
    draw = ImageDraw.Draw(img)

    # Load fonts (fallback to default if not available)
    try:
        font_large = ImageFont.truetype("arial.ttf", 56)
        font_medium = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large
        font_small = font_large

    # Title
    title = "Privacy-as-Code"
    add_glow_text(draw, title, (60, 180), font_large, COLORS['electric_cyan'])

    # Subtitle
    subtitle = "Protect data in your AI workflows"
    draw.text((60, 260), subtitle, font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

    # Features
    features = ["MCP Server for Claude & Cursor", "50+ Entity Types", "48 Languages"]
    y = 340
    for feature in features:
        draw.text((80, y), ">" + feature, font=font_small, fill=hex_to_rgb(COLORS['terminal_green']))
        y += 40

    # URL
    draw.text((60, height - 80), "anonymize.dev", font=font_medium, fill=hex_to_rgb(COLORS['neon_magenta']))

    # Decorative elements
    cyan = hex_to_rgb(COLORS['electric_cyan'])
    draw.rectangle([width - 300, 100, width - 60, 500], outline=cyan, width=2)
    draw.text((width - 280, 120), "MCP", font=font_large, fill=cyan)
    draw.text((width - 280, 200), "Server", font=font_medium, fill=hex_to_rgb(COLORS['terminal_green']))

    img.save(os.path.join(output_dir, 'linkedin-post.png'), 'PNG')
    print("Created: linkedin-post.png (1200x627)")

def create_twitter_post(output_dir):
    """Create Twitter/X post graphic (1200x675)."""
    width, height = 1200, 675
    img = create_gradient_bg(width, height)
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("arial.ttf", 64)
        font_medium = ImageFont.truetype("arial.ttf", 36)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large

    # Centered layout
    title = "Privacy-as-Code"
    subtitle = "MCP Server for AI workflows"
    url = "anonymize.dev"

    # Title with glow
    add_glow_text(draw, title, (width // 2 - 280, height // 2 - 80), font_large, COLORS['electric_cyan'])

    # Subtitle
    draw.text((width // 2 - 220, height // 2 + 20), subtitle, font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

    # URL with magenta accent
    draw.text((width // 2 - 120, height - 100), url, font=font_medium, fill=hex_to_rgb(COLORS['neon_magenta']))

    # Corner decorations
    green = hex_to_rgb(COLORS['terminal_green'])
    draw.line([(40, 40), (40, 120)], fill=green, width=3)
    draw.line([(40, 40), (120, 40)], fill=green, width=3)
    draw.line([(width - 40, height - 40), (width - 40, height - 120)], fill=green, width=3)
    draw.line([(width - 40, height - 40), (width - 120, height - 40)], fill=green, width=3)

    img.save(os.path.join(output_dir, 'twitter-post.png'), 'PNG')
    print("Created: twitter-post.png (1200x675)")

def create_instagram_square(output_dir):
    """Create Instagram square (1080x1080)."""
    size = 1080
    img = create_gradient_bg(size, size)
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("arial.ttf", 72)
        font_medium = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 28)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large
        font_small = font_large

    # Large "A" logo in center
    cyan = hex_to_rgb(COLORS['electric_cyan'])
    center = size // 2

    # Draw concentric circles
    for r in range(200, 50, -30):
        alpha = int(100 - (200 - r) * 0.4)
        draw.ellipse([center - r, center - r - 50, center + r, center + r - 50],
                    outline=(*cyan, alpha), width=2)

    # Title below
    add_glow_text(draw, "Privacy-as-Code", (center - 280, center + 180), font_large, COLORS['electric_cyan'])

    # Tagline
    draw.text((center - 260, center + 280), "Protect your AI workflows", font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

    # URL
    draw.text((center - 120, size - 100), "anonymize.dev", font=font_medium, fill=hex_to_rgb(COLORS['neon_magenta']))

    img.save(os.path.join(output_dir, 'instagram-square.png'), 'PNG')
    print("Created: instagram-square.png (1080x1080)")

def create_web_banner(output_dir):
    """Create web banner (1920x400)."""
    width, height = 1920, 400
    img = create_gradient_bg(width, height)
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("arial.ttf", 64)
        font_medium = ImageFont.truetype("arial.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large

    # Title
    add_glow_text(draw, "Privacy-as-Code", (100, 120), font_large, COLORS['electric_cyan'])

    # Subtitle
    draw.text((100, 210), "MCP Server | Desktop App | Office Add-in", font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

    # Right side: decorative terminal
    terminal_x = width - 600
    draw.rectangle([terminal_x, 80, width - 80, height - 80], outline=hex_to_rgb(COLORS['matrix_gray']), width=2)
    draw.rectangle([terminal_x, 80, width - 80, 120], fill=hex_to_rgb(COLORS['matrix_gray']))

    # Terminal content
    green = hex_to_rgb(COLORS['terminal_green'])
    draw.text((terminal_x + 20, 140), "$ npx @anonym-legal/mcp-server", font=font_medium, fill=green)
    draw.text((terminal_x + 20, 190), "> PII protection enabled", font=font_medium, fill=hex_to_rgb(COLORS['electric_cyan']))
    draw.text((terminal_x + 20, 240), "> 50+ entity types active", font=font_medium, fill=hex_to_rgb(COLORS['syntax_slate']))

    img.save(os.path.join(output_dir, 'web-banner.png'), 'PNG')
    print("Created: web-banner.png (1920x400)")

def create_email_banner(output_dir):
    """Create email banner (600x200)."""
    width, height = 600, 200
    img = create_gradient_bg(width, height)
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("arial.ttf", 36)
        font_medium = ImageFont.truetype("arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large

    # Title
    add_glow_text(draw, "Anonymize.dev", (40, 50), font_large, COLORS['electric_cyan'])

    # Subtitle
    draw.text((40, 110), "Privacy-as-Code for Developers", font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

    # Decorative line
    draw.line([(40, 160), (width - 40, 160)], fill=hex_to_rgb(COLORS['terminal_green']), width=2)

    img.save(os.path.join(output_dir, 'email-banner.png'), 'PNG')
    print("Created: email-banner.png (600x200)")

def create_product_cards(output_dir):
    """Create product marketing cards (400x500 each)."""
    width, height = 400, 500

    products = [
        ('mcp-server', 'MCP Server', 'AI Privacy Shield', COLORS['terminal_green']),
        ('desktop-app', 'Desktop App', 'Bulk Processing', COLORS['electric_cyan']),
        ('office-add-in', 'Office Add-in', 'In-app Protection', COLORS['neon_magenta']),
    ]

    try:
        font_large = ImageFont.truetype("arial.ttf", 36)
        font_medium = ImageFont.truetype("arial.ttf", 24)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large

    for product_id, title, subtitle, accent in products:
        img = create_gradient_bg(width, height)
        draw = ImageDraw.Draw(img)

        # Border
        accent_rgb = hex_to_rgb(accent)
        draw.rectangle([10, 10, width - 10, height - 10], outline=accent_rgb, width=2)

        # Icon placeholder (large circle)
        center_x = width // 2
        draw.ellipse([center_x - 60, 80, center_x + 60, 200], outline=accent_rgb, width=3)

        # Title
        add_glow_text(draw, title, (width // 2 - len(title) * 10, 240), font_large, accent)

        # Subtitle
        draw.text((width // 2 - len(subtitle) * 6, 300), subtitle, font=font_medium, fill=hex_to_rgb(COLORS['ghost_white']))

        # Features
        features = {
            'mcp-server': ['Claude Desktop', 'Cursor IDE', 'Pro+ plans'],
            'desktop-app': ['Windows FREE', 'Drag & drop', 'Local processing'],
            'office-add-in': ['Word, Excel, PPT', 'Select & protect', 'All plans'],
        }

        y = 360
        for feature in features[product_id]:
            draw.text((60, y), "> " + feature, font=font_medium, fill=hex_to_rgb(COLORS['syntax_slate']))
            y += 35

        img.save(os.path.join(output_dir, f'card-{product_id}.png'), 'PNG')

    print("Created: 3 product cards (400x500)")

def main():
    output_dir = os.path.join(os.path.dirname(__file__), 'marketing')
    os.makedirs(output_dir, exist_ok=True)

    print("Generating Anonymize.dev marketing materials...")
    print("=" * 50)

    create_linkedin_post(output_dir)
    create_twitter_post(output_dir)
    create_instagram_square(output_dir)
    create_web_banner(output_dir)
    create_email_banner(output_dir)
    create_product_cards(output_dir)

    print("=" * 50)
    print("Marketing materials generated successfully!")

if __name__ == '__main__':
    main()
