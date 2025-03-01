import math

# SVG header and dimensions
width, height = 360, 360  # Increased canvas size for padding
svg = [
    f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">',
    f'    <circle cx="{width/2}" cy="{height/2}" r="120" fill="none" stroke="black" stroke-width="2"/>',
    f'    <circle cx="{width/2}" cy="{height/2}" r="3" fill="black"/>',  # Center point dot
    '    <g text-anchor="middle" font-family="Arial" font-size="16">'
]

# Center of the circle
center_x, center_y = width/2, height/2
radius = 120  # radius of the circle
text_radius = radius + 15  # Add padding for text placement
tick_inner_radius = radius - 5  # Inner point of the tick mark
cardinal_radius = radius - 20  # Position for cardinal directions - just inside the circle

# We'll display 12 headings (36, 33, 30, ..., 6, 3)
num_headings = 12
angle_step = 360 / 36  # Still use 36 segments but only mark every 3rd one

# Dictionary to map cardinal directions to headings
cardinal_directions = {
    36: "N",
    9: "E",
    18: "S",
    27: "W"
}

# Generate headings divisible by 3 (36, 33, 30, ..., 6, 3) clockwise, starting with 36 at top
for i in range(0, 36, 3):
    # Number to display (36, 33, 30, ...)
    number = 36 - i
    if number == 0:  # Handle special case for heading 0
        number = 36
    
    # Format the heading with leading zero if needed
    formatted_heading = f"{number:02d}"  # This adds a leading zero to single digits
    
    # Calculate angle in degrees - now clockwise (0° is at top, going clockwise)
    # To go clockwise, we need to use negative angles from the top position
    angle_deg = -i * angle_step  # 0 is at top (negative for clockwise)
    
    # Convert to radians for math functions
    angle_rad = math.radians(angle_deg)
    
    # Calculate position for text (with padding)
    text_x = center_x + text_radius * math.sin(angle_rad)
    text_y = center_y - text_radius * math.cos(angle_rad)
    
    # Calculate positions for tick marks
    tick_outer_x = center_x + radius * math.sin(angle_rad)
    tick_outer_y = center_y - radius * math.cos(angle_rad)
    tick_inner_x = center_x + tick_inner_radius * math.sin(angle_rad)
    tick_inner_y = center_y - tick_inner_radius * math.cos(angle_rad)
    
    # Add tick mark
    svg.append(
        f'        <line x1="{tick_inner_x:.1f}" y1="{tick_inner_y:.1f}" x2="{tick_outer_x:.1f}" y2="{tick_outer_y:.1f}" stroke="black" stroke-width="2"/>'
    )
    
    # Add text element for the heading (no bold)
    svg.append(
        f'        <text x="{text_x:.1f}" y="{text_y:.1f}" dominant-baseline="middle">{formatted_heading}</text>'
    )
    
    # Check if this is a cardinal direction heading, add the letter
    if number in cardinal_directions:
        # Add cardinal direction letter inside the circle (keep these bold)
        cardinal = cardinal_directions[number]
        cardinal_x = center_x + cardinal_radius * math.sin(angle_rad)
        cardinal_y = center_y - cardinal_radius * math.cos(angle_rad)
        svg.append(
            f'        <text x="{cardinal_x:.1f}" y="{cardinal_y:.1f}" dominant-baseline="middle" font-weight="bold" font-size="18">{cardinal}</text>'
        )

# SVG footer
svg.extend([
    '    </g>',
    '</svg>'
])

# Write to file
with open('runway_headings.svg', 'w') as f:
    f.write('\n'.join(svg))

print("SVG file 'runway_headings.svg' has been generated.")