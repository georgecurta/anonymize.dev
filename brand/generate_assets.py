#!/usr/bin/env python3
"""
Anonymize.dev Brand Asset Generator
Neon Protocol Theme - Cyberpunk Developer Aesthetic
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from PIL import Image, ImageDraw, ImageFont
import math

# Neon Protocol Color Palette
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
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_logo(output_dir, size=512):
    """Create the main logo - angular 'A' with neon glow effect."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background circle with glow
    center = size // 2
    radius = size // 2 - 20

    # Outer glow layers
    for i in range(5, 0, -1):
        glow_radius = radius + i * 8
        alpha = int(50 - i * 8)
        glow_color = (*hex_to_rgb(COLORS['electric_cyan']), alpha)
        draw.ellipse(
            [center - glow_radius, center - glow_radius,
             center + glow_radius, center + glow_radius],
            fill=glow_color
        )

    # Main dark circle
    draw.ellipse(
        [center - radius, center - radius,
         center + radius, center + radius],
        fill=hex_to_rgb(COLORS['terminal_dark'])
    )

    # Inner border ring
    border_radius = radius - 4
    draw.ellipse(
        [center - border_radius, center - border_radius,
         center + border_radius, center + border_radius],
        outline=hex_to_rgb(COLORS['electric_cyan']),
        width=2
    )

    # Angular 'A' shape
    a_height = int(size * 0.45)
    a_width = int(size * 0.35)
    a_top = center - a_height // 2
    a_left = center - a_width // 2

    # Draw the 'A' with thick lines
    line_width = 6
    cyan = hex_to_rgb(COLORS['electric_cyan'])

    # Left leg of A
    draw.line(
        [(center, a_top), (a_left, a_top + a_height)],
        fill=cyan, width=line_width
    )
    # Right leg of A
    draw.line(
        [(center, a_top), (a_left + a_width, a_top + a_height)],
        fill=cyan, width=line_width
    )
    # Crossbar
    crossbar_y = a_top + int(a_height * 0.6)
    draw.line(
        [(a_left + int(a_width * 0.2), crossbar_y),
         (a_left + int(a_width * 0.8), crossbar_y)],
        fill=cyan, width=line_width
    )

    # Dot at top of A (data point)
    dot_radius = 8
    draw.ellipse(
        [center - dot_radius, a_top - dot_radius - 5,
         center + dot_radius, a_top + dot_radius - 5],
        fill=hex_to_rgb(COLORS['terminal_green'])
    )

    # Save PNG
    img.save(os.path.join(output_dir, 'logo-anonymize-dev.png'), 'PNG')

    # Create PDF version
    pdf_path = os.path.join(output_dir, 'logo-anonymize-dev.pdf')
    c = canvas.Canvas(pdf_path, pagesize=(size, size))

    # Draw background
    c.setFillColor(HexColor(COLORS['terminal_dark']))
    c.circle(center, size - center, radius, fill=1, stroke=0)

    # Draw border
    c.setStrokeColor(HexColor(COLORS['electric_cyan']))
    c.setLineWidth(2)
    c.circle(center, size - center, border_radius, fill=0, stroke=1)

    # Draw A shape
    c.setStrokeColor(HexColor(COLORS['electric_cyan']))
    c.setLineWidth(line_width)

    # Flip Y coordinates for PDF
    pdf_a_top = size - a_top
    pdf_a_bottom = size - (a_top + a_height)
    pdf_crossbar_y = size - crossbar_y

    c.line(center, pdf_a_top, a_left, pdf_a_bottom)
    c.line(center, pdf_a_top, a_left + a_width, pdf_a_bottom)
    c.line(a_left + int(a_width * 0.2), pdf_crossbar_y,
           a_left + int(a_width * 0.8), pdf_crossbar_y)

    # Dot
    c.setFillColor(HexColor(COLORS['terminal_green']))
    c.circle(center, pdf_a_top + dot_radius + 5, dot_radius, fill=1, stroke=0)

    c.save()
    print(f"Created logo: {output_dir}/logo-anonymize-dev.png")

def create_favicon(output_dir, sizes=[16, 32, 48, 64, 128, 256]):
    """Create favicon at multiple sizes."""
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        center = size // 2
        radius = size // 2 - 1

        # Background
        draw.ellipse(
            [center - radius, center - radius,
             center + radius, center + radius],
            fill=hex_to_rgb(COLORS['terminal_dark'])
        )

        # Border
        draw.ellipse(
            [center - radius + 1, center - radius + 1,
             center + radius - 1, center + radius - 1],
            outline=hex_to_rgb(COLORS['electric_cyan']),
            width=max(1, size // 32)
        )

        # Simplified A for small sizes
        if size >= 32:
            a_height = int(size * 0.4)
            a_width = int(size * 0.3)
            a_top = center - a_height // 2
            a_left = center - a_width // 2
            line_width = max(1, size // 16)

            cyan = hex_to_rgb(COLORS['electric_cyan'])
            draw.line([(center, a_top), (a_left, a_top + a_height)], fill=cyan, width=line_width)
            draw.line([(center, a_top), (a_left + a_width, a_top + a_height)], fill=cyan, width=line_width)

            crossbar_y = a_top + int(a_height * 0.6)
            draw.line([(a_left + int(a_width * 0.15), crossbar_y),
                      (a_left + int(a_width * 0.85), crossbar_y)], fill=cyan, width=line_width)

        img.save(os.path.join(output_dir, f'favicon-{size}.png'), 'PNG')

    print(f"Created favicons: {sizes}")

def create_product_icon(output_dir, name, icon_type, size=200):
    """Create product icons with neon glow."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center = size // 2

    # Background with glow
    bg_radius = size // 2 - 15

    # Glow effect
    glow_color = COLORS['electric_cyan'] if icon_type != 'mcp' else COLORS['terminal_green']
    for i in range(4, 0, -1):
        glow_radius = bg_radius + i * 5
        alpha = int(40 - i * 8)
        draw.ellipse(
            [center - glow_radius, center - glow_radius,
             center + glow_radius, center + glow_radius],
            fill=(*hex_to_rgb(glow_color), alpha)
        )

    # Main background
    draw.ellipse(
        [center - bg_radius, center - bg_radius,
         center + bg_radius, center + bg_radius],
        fill=hex_to_rgb(COLORS['terminal_dark']),
        outline=hex_to_rgb(glow_color),
        width=2
    )

    icon_color = hex_to_rgb(glow_color)

    if icon_type == 'mcp':
        # MCP Server - network/proxy symbol
        # Central node
        node_r = 12
        draw.ellipse([center - node_r, center - node_r, center + node_r, center + node_r],
                    fill=icon_color)

        # Outer nodes
        outer_r = 8
        positions = [
            (center - 35, center - 25),
            (center + 35, center - 25),
            (center - 35, center + 25),
            (center + 35, center + 25),
        ]
        for x, y in positions:
            draw.ellipse([x - outer_r, y - outer_r, x + outer_r, y + outer_r], fill=icon_color)
            draw.line([(x, y), (center, center)], fill=icon_color, width=2)

        # Shield outline around center
        shield_points = [
            (center, center - 30),
            (center + 25, center - 15),
            (center + 25, center + 10),
            (center, center + 30),
            (center - 25, center + 10),
            (center - 25, center - 15),
        ]
        draw.polygon(shield_points, outline=icon_color, width=2)

    elif icon_type == 'desktop':
        # Desktop app - monitor with terminal
        # Monitor frame
        m_left = center - 40
        m_top = center - 30
        m_width = 80
        m_height = 50
        draw.rectangle([m_left, m_top, m_left + m_width, m_top + m_height],
                      outline=icon_color, width=2)
        # Screen content - terminal lines
        for i in range(3):
            y = m_top + 12 + i * 12
            width = 50 - i * 10
            draw.line([(m_left + 10, y), (m_left + 10 + width, y)], fill=icon_color, width=2)
        # Stand
        draw.line([(center, m_top + m_height), (center, m_top + m_height + 15)], fill=icon_color, width=2)
        draw.line([(center - 20, m_top + m_height + 15), (center + 20, m_top + m_height + 15)], fill=icon_color, width=3)

    elif icon_type == 'office':
        # Office add-in - document with plugin symbol
        # Document
        doc_left = center - 30
        doc_top = center - 40
        doc_width = 50
        doc_height = 65
        # Folded corner
        fold = 12
        points = [
            (doc_left, doc_top),
            (doc_left + doc_width - fold, doc_top),
            (doc_left + doc_width, doc_top + fold),
            (doc_left + doc_width, doc_top + doc_height),
            (doc_left, doc_top + doc_height),
        ]
        draw.polygon(points, outline=icon_color, width=2)
        # Fold line
        draw.line([(doc_left + doc_width - fold, doc_top),
                  (doc_left + doc_width - fold, doc_top + fold),
                  (doc_left + doc_width, doc_top + fold)], fill=icon_color, width=1)
        # Lines on document
        for i in range(3):
            y = doc_top + 20 + i * 12
            draw.line([(doc_left + 8, y), (doc_left + doc_width - 15, y)], fill=icon_color, width=2)
        # Plugin symbol (plus)
        plus_x = doc_left + doc_width - 8
        plus_y = doc_top + doc_height - 15
        draw.line([(plus_x - 8, plus_y), (plus_x + 8, plus_y)], fill=hex_to_rgb(COLORS['terminal_green']), width=3)
        draw.line([(plus_x, plus_y - 8), (plus_x, plus_y + 8)], fill=hex_to_rgb(COLORS['terminal_green']), width=3)

    elif icon_type == 'api':
        # API - brackets with connection
        # Left bracket
        draw.line([(center - 35, center - 25), (center - 45, center - 25)], fill=icon_color, width=3)
        draw.line([(center - 45, center - 25), (center - 45, center + 25)], fill=icon_color, width=3)
        draw.line([(center - 35, center + 25), (center - 45, center + 25)], fill=icon_color, width=3)
        # Right bracket
        draw.line([(center + 35, center - 25), (center + 45, center - 25)], fill=icon_color, width=3)
        draw.line([(center + 45, center - 25), (center + 45, center + 25)], fill=icon_color, width=3)
        draw.line([(center + 35, center + 25), (center + 45, center + 25)], fill=icon_color, width=3)
        # Connection dots
        for x in [-15, 0, 15]:
            draw.ellipse([center + x - 5, center - 5, center + x + 5, center + 5], fill=icon_color)

    img.save(os.path.join(output_dir, f'icon-{name}.png'), 'PNG')
    print(f"Created icon: icon-{name}.png")

def create_hero_graphic(output_dir, width=1200, height=600):
    """Create hero graphic with data flow visualization."""
    img = Image.new('RGBA', (width, height), hex_to_rgb(COLORS['void_black']) + (255,))
    draw = ImageDraw.Draw(img)

    # Grid pattern (subtle)
    grid_color = (*hex_to_rgb(COLORS['matrix_gray']), 100)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # Data flow visualization
    # Left side - "sensitive data"
    left_x = 150
    center_y = height // 2

    # Data blocks on left (representing sensitive data)
    block_color = hex_to_rgb(COLORS['hot_coral'])
    for i in range(4):
        y = center_y - 90 + i * 60
        draw.rectangle([left_x - 60, y - 15, left_x + 60, y + 15],
                      fill=(*block_color, 180), outline=block_color, width=2)

    # MCP Server in center (shield shape)
    mcp_x = width // 2
    shield_points = [
        (mcp_x, center_y - 100),
        (mcp_x + 80, center_y - 60),
        (mcp_x + 80, center_y + 40),
        (mcp_x, center_y + 100),
        (mcp_x - 80, center_y + 40),
        (mcp_x - 80, center_y - 60),
    ]

    # Shield glow
    green = hex_to_rgb(COLORS['terminal_green'])
    for i in range(5, 0, -1):
        alpha = int(30 - i * 5)
        draw.polygon([(p[0], p[1]) for p in shield_points],
                    fill=(*green, alpha))

    # Shield border
    draw.polygon(shield_points, outline=green, width=3)

    # "MCP" text placeholder (center of shield)
    mcp_text_y = center_y - 10
    draw.rectangle([mcp_x - 35, mcp_text_y - 12, mcp_x + 35, mcp_text_y + 12],
                  fill=hex_to_rgb(COLORS['terminal_dark']), outline=green, width=1)

    # Right side - "protected data"
    right_x = width - 150

    # Data blocks on right (protected - tokenized)
    cyan = hex_to_rgb(COLORS['electric_cyan'])
    for i in range(4):
        y = center_y - 90 + i * 60
        draw.rectangle([right_x - 60, y - 15, right_x + 60, y + 15],
                      fill=(*hex_to_rgb(COLORS['terminal_dark']), 200), outline=cyan, width=2)
        # Asterisks to show tokenized
        for j in range(5):
            draw.ellipse([right_x - 40 + j * 20, y - 3, right_x - 34 + j * 20, y + 3], fill=cyan)

    # Flow lines left to MCP
    for i in range(4):
        y = center_y - 90 + i * 60
        # Animated-looking dashed line
        for x in range(left_x + 70, mcp_x - 90, 20):
            draw.line([(x, y), (x + 10, y)], fill=block_color, width=2)

    # Flow lines MCP to right
    for i in range(4):
        y = center_y - 90 + i * 60
        for x in range(mcp_x + 90, right_x - 70, 20):
            draw.line([(x, y), (x + 10, y)], fill=cyan, width=2)

    # Arrow heads
    arrow_size = 8
    for i in range(4):
        y = center_y - 90 + i * 60
        # Left arrow (into MCP)
        ax = mcp_x - 90
        draw.polygon([(ax, y), (ax - arrow_size, y - arrow_size), (ax - arrow_size, y + arrow_size)],
                    fill=block_color)
        # Right arrow (out of MCP)
        ax = right_x - 70
        draw.polygon([(ax, y), (ax - arrow_size, y - arrow_size), (ax - arrow_size, y + arrow_size)],
                    fill=cyan)

    # Labels
    # These would need a font, so we'll use simple shapes
    # "SENSITIVE" label area
    draw.rectangle([left_x - 50, height - 60, left_x + 50, height - 40],
                  outline=block_color, width=1)

    # "PROTECTED" label area
    draw.rectangle([right_x - 50, height - 60, right_x + 50, height - 40],
                  outline=cyan, width=1)

    # "MCP SERVER" label
    draw.rectangle([mcp_x - 60, height - 60, mcp_x + 60, height - 40],
                  outline=green, width=1)

    img.save(os.path.join(output_dir, 'hero-graphic.png'), 'PNG')
    print(f"Created hero graphic: hero-graphic.png")

def create_pattern_tile(output_dir, size=100):
    """Create repeating pattern tile for backgrounds."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Dot grid pattern
    dot_color = (*hex_to_rgb(COLORS['matrix_gray']), 80)
    spacing = 20
    dot_r = 2

    for x in range(0, size, spacing):
        for y in range(0, size, spacing):
            draw.ellipse([x - dot_r, y - dot_r, x + dot_r, y + dot_r], fill=dot_color)

    img.save(os.path.join(output_dir, 'pattern-tile.png'), 'PNG')
    print(f"Created pattern tile: pattern-tile.png")

def create_entity_icons(output_dir, size=80):
    """Create entity type icons."""
    entities = [
        ('person', 'User silhouette'),
        ('email', 'Envelope'),
        ('phone', 'Phone'),
        ('location', 'Pin'),
        ('id-card', 'Card'),
        ('credit-card', 'Payment card'),
        ('code', 'Code brackets'),
    ]

    for name, _ in entities:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        center = size // 2
        cyan = hex_to_rgb(COLORS['electric_cyan'])

        # Background circle
        bg_r = size // 2 - 4
        draw.ellipse([center - bg_r, center - bg_r, center + bg_r, center + bg_r],
                    fill=(*hex_to_rgb(COLORS['terminal_dark']), 200),
                    outline=cyan, width=1)

        # Simple geometric representation
        if name == 'person':
            # Head
            draw.ellipse([center - 8, center - 20, center + 8, center - 4], outline=cyan, width=2)
            # Body
            draw.arc([center - 15, center - 5, center + 15, center + 25], 0, 180, fill=cyan, width=2)
        elif name == 'email':
            # Envelope
            draw.rectangle([center - 18, center - 10, center + 18, center + 12], outline=cyan, width=2)
            draw.line([(center - 18, center - 10), (center, center + 5), (center + 18, center - 10)], fill=cyan, width=2)
        elif name == 'phone':
            # Phone
            draw.rounded_rectangle([center - 10, center - 18, center + 10, center + 18], radius=3, outline=cyan, width=2)
            draw.line([(center - 5, center + 12), (center + 5, center + 12)], fill=cyan, width=2)
        elif name == 'location':
            # Pin
            draw.ellipse([center - 8, center - 15, center + 8, center + 1], outline=cyan, width=2)
            draw.polygon([(center - 8, center - 2), (center, center + 18), (center + 8, center - 2)], outline=cyan, width=2)
        elif name == 'id-card':
            # Card
            draw.rounded_rectangle([center - 20, center - 12, center + 20, center + 12], radius=2, outline=cyan, width=2)
            draw.line([(center - 15, center - 5), (center - 5, center - 5)], fill=cyan, width=2)
            draw.line([(center - 15, center + 2), (center + 10, center + 2)], fill=cyan, width=2)
            draw.line([(center - 15, center + 7), (center + 5, center + 7)], fill=cyan, width=2)
        elif name == 'credit-card':
            draw.rounded_rectangle([center - 22, center - 14, center + 22, center + 14], radius=2, outline=cyan, width=2)
            draw.line([(center - 22, center - 6), (center + 22, center - 6)], fill=cyan, width=2)
            draw.rectangle([center - 18, center + 2, center - 8, center + 8], outline=cyan, width=1)
        elif name == 'code':
            # Brackets
            draw.line([(center - 12, center - 12), (center - 18, center - 12)], fill=cyan, width=2)
            draw.line([(center - 18, center - 12), (center - 18, center + 12)], fill=cyan, width=2)
            draw.line([(center - 12, center + 12), (center - 18, center + 12)], fill=cyan, width=2)
            draw.line([(center + 12, center - 12), (center + 18, center - 12)], fill=cyan, width=2)
            draw.line([(center + 18, center - 12), (center + 18, center + 12)], fill=cyan, width=2)
            draw.line([(center + 12, center + 12), (center + 18, center + 12)], fill=cyan, width=2)

        img.save(os.path.join(output_dir, f'entity-{name}.png'), 'PNG')

    print(f"Created entity icons: {len(entities)} icons")

def create_feature_icons(output_dir, size=100):
    """Create feature icons."""
    features = ['shield', 'lock', 'globe', 'speed', 'terminal']

    for name in features:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        center = size // 2
        cyan = hex_to_rgb(COLORS['electric_cyan'])
        green = hex_to_rgb(COLORS['terminal_green'])

        if name == 'shield':
            points = [
                (center, center - 35),
                (center + 30, center - 20),
                (center + 30, center + 10),
                (center, center + 35),
                (center - 30, center + 10),
                (center - 30, center - 20),
            ]
            draw.polygon(points, outline=green, width=3)
            # Checkmark
            draw.line([(center - 12, center), (center - 2, center + 10), (center + 15, center - 12)], fill=green, width=3)
        elif name == 'lock':
            # Lock body
            draw.rounded_rectangle([center - 18, center - 5, center + 18, center + 25], radius=3, outline=cyan, width=2)
            # Lock shackle
            draw.arc([center - 12, center - 25, center + 12, center], 0, 180, fill=cyan, width=2)
            draw.line([(center - 12, center - 12), (center - 12, center - 5)], fill=cyan, width=2)
            draw.line([(center + 12, center - 12), (center + 12, center - 5)], fill=cyan, width=2)
        elif name == 'globe':
            r = 28
            draw.ellipse([center - r, center - r, center + r, center + r], outline=cyan, width=2)
            draw.ellipse([center - r//2, center - r, center + r//2, center + r], outline=cyan, width=1)
            draw.line([(center - r, center), (center + r, center)], fill=cyan, width=1)
            draw.arc([center - r, center - r//2, center + r, center + r//2 + r], 200, 340, fill=cyan, width=1)
        elif name == 'speed':
            # Speedometer
            r = 28
            draw.arc([center - r, center - r, center + r, center + r], 135, 405, fill=cyan, width=3)
            # Needle
            draw.line([(center, center), (center + 15, center - 20)], fill=green, width=3)
            draw.ellipse([center - 5, center - 5, center + 5, center + 5], fill=cyan)
        elif name == 'terminal':
            # Terminal window
            draw.rounded_rectangle([center - 30, center - 22, center + 30, center + 22], radius=4, outline=cyan, width=2)
            # Title bar
            draw.line([(center - 30, center - 14), (center + 30, center - 14)], fill=cyan, width=1)
            # Traffic lights
            colors = [COLORS['hot_coral'], COLORS['neon_magenta'], COLORS['terminal_green']]
            for i, c in enumerate(colors):
                draw.ellipse([center - 24 + i * 10, center - 20, center - 18 + i * 10, center - 14], fill=hex_to_rgb(c))
            # Prompt
            draw.line([(center - 22, center - 2), (center - 12, center - 2)], fill=green, width=2)
            draw.line([(center - 22, center + 8), (center + 15, center + 8)], fill=cyan, width=2)

        img.save(os.path.join(output_dir, f'icon-{name}.png'), 'PNG')

    print(f"Created feature icons: {len(features)} icons")

def main():
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'assets')
    os.makedirs(output_dir, exist_ok=True)

    print("Generating Anonymize.dev brand assets...")
    print("=" * 50)

    # Generate all assets
    create_logo(output_dir)
    create_favicon(output_dir)
    create_product_icon(output_dir, 'mcp-server', 'mcp')
    create_product_icon(output_dir, 'desktop-app', 'desktop')
    create_product_icon(output_dir, 'office-addin', 'office')
    create_product_icon(output_dir, 'api', 'api')
    create_hero_graphic(output_dir)
    create_pattern_tile(output_dir)
    create_entity_icons(output_dir)
    create_feature_icons(output_dir)

    print("=" * 50)
    print("Brand assets generated successfully!")

if __name__ == '__main__':
    main()
