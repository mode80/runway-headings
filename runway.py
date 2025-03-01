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
]

# Center of the circle
center_x, center_y = width/2, height/2
radius = 150  # radius of the circle
outer_radius = 180  # radius of the background shading
text_radius = radius + 18  # Add padding for text placement
tick_inner_radius = radius - 6  # Inner point of the tick mark
cardinal_radius = radius - 25  # Position for cardinal directions inside the circle

# Define colors for each digit range
digit_colors = {
    "0": {"fill": "#E6F2FF", "stroke": "#2c6aa1"},  # Light blue for headings 01-10
    "1": {"fill": "#FFE6E6", "stroke": "#c13f3c"},  # Light red for headings 11-20
    "2": {"fill": "#FFFFCC", "stroke": "#a37336"},  # Light yellow for headings 21-30
    "3": {"fill": "#E6FFE6", "stroke": "#32795f"}   # Light green for headings 31-36
}

# Create the shaded regions for headings
# In the compass, heading 36=0 degrees (North), and we go clockwise with 10 degrees per heading

# Region 1 (01-10): Blue
# 0° (North) to 100° (Heading 10)
start_angle = 0     # North (heading 36/0)
end_angle = 100     # Heading 10
x1 = center_x + outer_radius * math.sin(math.radians(start_angle))
y1 = center_y - outer_radius * math.cos(math.radians(start_angle))
x2 = center_x + outer_radius * math.sin(math.radians(end_angle))
y2 = center_y - outer_radius * math.cos(math.radians(end_angle))
svg.append(
    f'    <path d="M {center_x} {center_y} L {x1} {y1} A {outer_radius} {outer_radius} 0 0 1 {x2} {y2} Z" fill="{digit_colors["0"]["fill"]}" fill-opacity="0.4" />'
)

# Region 2 (11-20): Red
# 100° (Heading 10) to 200° (Heading 20)
start_angle = 100   # Heading 10
end_angle = 200     # Heading 20
x1 = center_x + outer_radius * math.sin(math.radians(start_angle))
y1 = center_y - outer_radius * math.cos(math.radians(start_angle))
x2 = center_x + outer_radius * math.sin(math.radians(end_angle))
y2 = center_y - outer_radius * math.cos(math.radians(end_angle))
svg.append(
    f'    <path d="M {center_x} {center_y} L {x1} {y1} A {outer_radius} {outer_radius} 0 0 1 {x2} {y2} Z" fill="{digit_colors["1"]["fill"]}" fill-opacity="0.4" />'
)

# Region 3 (21-30): Yellow
# 200° (Heading 20) to 300° (Heading 30)
start_angle = 200   # Heading 20
end_angle = 300     # Heading 30
x1 = center_x + outer_radius * math.sin(math.radians(start_angle))
y1 = center_y - outer_radius * math.cos(math.radians(start_angle))
x2 = center_x + outer_radius * math.sin(math.radians(end_angle))
y2 = center_y - outer_radius * math.cos(math.radians(end_angle))
svg.append(
    f'    <path d="M {center_x} {center_y} L {x1} {y1} A {outer_radius} {outer_radius} 0 0 1 {x2} {y2} Z" fill="{digit_colors["2"]["fill"]}" fill-opacity="0.4" />'
)

# Region 4 (31-36): Green
# 300° (Heading 30) to 360° (North/Heading 36)
start_angle = 300   # Heading 30
end_angle = 360     # North (heading 36/0)
x1 = center_x + outer_radius * math.sin(math.radians(start_angle))
y1 = center_y - outer_radius * math.cos(math.radians(start_angle))
x2 = center_x + outer_radius * math.sin(math.radians(end_angle))
y2 = center_y - outer_radius * math.cos(math.radians(end_angle))
svg.append(
    f'    <path d="M {center_x} {center_y} L {x1} {y1} A {outer_radius} {outer_radius} 0 0 1 {x2} {y2} Z" fill="{digit_colors["3"]["fill"]}" fill-opacity="0.4" />'
)

# Add additional SVG elements
svg.extend([
    '    <!-- Main circle outline -->',
    f'    <circle cx="{width/2}" cy="{height/2}" r="150" fill="none" stroke="#505050" stroke-width="2"/>',
    '    <!-- Center point dot -->',
    f'    <circle cx="{width/2}" cy="{height/2}" r="4" fill="#404040"/>',
    '    <g text-anchor="middle" font-family="Arial">'
])

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
    
    # Determine the color based on the actual heading number
    if 1 <= number <= 10:
        color_key = "0"
    elif 11 <= number <= 20:
        color_key = "1"
    elif 21 <= number <= 30:
        color_key = "2"
    else:  # 31-36
        color_key = "3"
    
    color = digit_colors[color_key]["stroke"]
    
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