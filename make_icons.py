#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

def make_icon(size):
    img = Image.new('RGB', (size, size), '#0f0f0f')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple clock/timer symbol
    cx, cy = size // 2, size // 2
    r = int(size * 0.35)
    
    # Outer circle
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline='#1D9E75', width=max(2, size//32))
    
    # Clock hands
    import math
    # Hour hand (pointing to ~10)
    h_len = r * 0.5
    draw.line([cx, cy, cx + h_len * math.cos(math.radians(-60)), cy + h_len * math.sin(math.radians(-60))],
              fill='#f0ede8', width=max(2, size//40))
    # Minute hand (pointing to ~2)
    m_len = r * 0.7
    draw.line([cx, cy, cx + m_len * math.cos(math.radians(60)), cy + m_len * math.sin(math.radians(60))],
              fill='#f0ede8', width=max(1, size//64))
    # Center dot
    dot = max(3, size // 24)
    draw.ellipse([cx-dot, cy-dot, cx+dot, cy+dot], fill='#4ecba0')
    
    img.save(f'icons/icon-{size}.png')
    print(f'Created icon-{size}.png')

make_icon(192)
make_icon(512)
print('Icons created successfully!')
