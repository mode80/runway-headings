import math

# SVG header and dimensions
width, height = 500, 500  # Increased canvas size for better presentation
svg = [
    '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
    f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">',
    '    <defs>',
    '        <!-- Gradient for background shading -->',
    '        <radialGradient id="backgroundGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">',
    '            <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />',
    '            <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />',
    '        </radialGradient>',
    '        <!-- Filter for subtle shadow effect -->',
    '        <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">',
    '            <feGaussianBlur in="SourceAlpha" stdDeviation="2" />',
    '            <feOffset dx="1" dy="1" result="offsetblur" />',
    '            <feComponentTransfer>',
    '                <feFuncA type="linear" slope="0.3" />',
    '            </feComponentTransfer>',
    '            <feMerge>',
    '                <feMergeNode />',
    '                <feMergeNode in="SourceGraphic" />',
    '            </feMerge>',
    '        </filter>',
    '    </defs>',
    '    <!-- Title of the diagram -->',
    f'    <text x="{width/2}" y="30" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold">Runway Headings</text>',
    '    <!-- Background circle with gradient -->',
    f'    <circle cx="{width/2}" cy="{height/2}" r="180" fill="url(#backgroundGradient)" filter="url(#dropShadow)" />',
    '    <!-- Quadrant shading -->',
    f'    <path d="M {width/2} {height/2} L {width/2} {height/2-180} A 180 180 0 0 1 {width/2+180} {height/2} Z" fill="#e8f4f8" fill-opacity="0.4" />',
    f'    <path d="M {width/2} {height/2} L {width/2+180} {height/2} A 180 180 0 0 1 {width/2} {height/2+180} Z" fill="#f8e8e8" fill-opacity="0.4" />',
    f'    <path d="M {width/2} {height/2} L {width/2} {height/2+180} A 180 180 0 0 1 {width/2-180} {height/2} Z" fill="#f8f8e8" fill-opacity="0.4" />',
    f'    <path d="M {width/2} {height/2} L {width/2-180} {height/2} A 180 180 0 0 1 {width/2} {height/2-180} Z" fill="#e8f8e8" fill-opacity="0.4" />',
    '    <!-- Main circle outline -->',
    f'    <circle cx="{width/2}" cy="{height/2}" r="150" fill="none" stroke="#505050" stroke-width="2"/>',
    '    <!-- Center point dot -->',
    f'    <circle cx="{width/2}" cy="{height/2}" r="4" fill="#404040"/>',
    '    <g text-anchor="middle" font-family="Arial">'
]

# Center of the circle
center_x, center_y = width/2, height/2
radius = 150  # radius of the circle
text_radius = radius + 18  # Add padding for text placement
tick_inner_radius = radius - 6  # Inner point of the tick mark
cardinal_radius = radius - 25  # Position for cardinal directions inside the circle

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

# Color codes for different quadrants
quadrant_colors = {
    "NE": "#2c6aa1",  # Headings 36-09
    "SE": "#c13f3c",  # Headings 09-18
    "SW": "#a37336",  # Headings 18-27
    "NW": "#32795f"   # Headings 27-36
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
    
    # Determine the color based on quadrant (N-E-S-W divisions)
    if 0 <= number <= 9 or number == 36:
        color = quadrant_colors["NE"]
    elif 9 < number <= 18:
        color = quadrant_colors["SE"]
    elif 18 < number <= 27:
        color = quadrant_colors["SW"]
    else:  # 27 < number < 36
        color = quadrant_colors["NW"]
    
    # Determine if this is a cardinal direction
    is_cardinal = number in cardinal_directions
    
    # Add tick mark - thicker for cardinal directions
    stroke_width = 3 if is_cardinal else 1.5
    svg.append(
        f'        <line x1="{tick_inner_x:.1f}" y1="{tick_inner_y:.1f}" x2="{tick_outer_x:.1f}" y2="{tick_outer_y:.1f}" stroke="{color}" stroke-width="{stroke_width}"/>'
    )
    
    # Add text element for the heading
    svg.append(
        f'        <text x="{text_x:.1f}" y="{text_y:.1f}" dominant-baseline="middle" fill="{color}" font-size="16">{formatted_heading}</text>'
    )
    
    # Check if this is a cardinal direction heading, add the letter
    if is_cardinal:
        # Add cardinal direction letter inside the circle
        cardinal = cardinal_directions[number]
        cardinal_x = center_x + cardinal_radius * math.sin(angle_rad)
        cardinal_y = center_y - cardinal_radius * math.cos(angle_rad)
        svg.append(
            f'        <text x="{cardinal_x:.1f}" y="{cardinal_y:.1f}" dominant-baseline="middle" font-weight="bold" font-size="22" fill="{color}">{cardinal}</text>'
        )
        
        # Position the airplane between the center and the cardinal label
        plane_radius = radius - 80  # Place it closer to center than the cardinal labels
        plane_x = center_x + plane_radius * math.sin(angle_rad)
        plane_y = center_y - plane_radius * math.cos(angle_rad)
        
        # Point the airplane TOWARD the cardinal direction (the pointy part toward the label)
        # The angle needs to match the position angle to make it point outward
        plane_rotation = angle_deg
        
        # Draw a triangle pointing outward
        svg.append(
            f'        <path d="M 0,-8 L -5,4 L 5,4 Z" transform="translate({plane_x:.1f},{plane_y:.1f}) rotate({plane_rotation:.1f})" fill="{color}" opacity="0.8" />'
        )

# SVG footer
svg.extend([
    '    </g>',
    '</svg>'
])

# Write to file
with open('runway_headings_enhanced.svg', 'w') as f:
    f.write('\n'.join(svg))

print("SVG file 'runway_headings_enhanced.svg' has been generated.")