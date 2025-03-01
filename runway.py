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

# Define positions for arrows in the middle of each region
arrow_positions = [
    5,   # Blue region (50 degrees)
    15,  # Red region (150 degrees)
    25,  # Brown region (250 degrees)
    33   # Green region (330 degrees)
]

# Only display specific headings (3, 5, 7, 13, 15, 17, 23, 25, 27, 31, 33, 35)
specific_headings = [3, 5, 7, 13, 15, 17, 23, 25, 27, 31, 33, 35]

# Headings that should be semi-transparent 
transparent_labels = [3, 7, 13, 17, 23, 27, 31, 35]

# Generate the specific headings we want to display
for heading in specific_headings:
    # Format the heading with leading zero if needed
    formatted_heading = f"{heading:02d}"  # This adds a leading zero to single digits
    
    # Calculate angle in degrees - aviation heading to degrees
    # Heading 36/0 is 0° (North), heading 9 is 90° (East), etc.
    angle_deg = heading * 10
    
    # Convert to SVG coordinate system (0° is East, 90° is South)
    svg_angle_deg = angle_deg - 90
    angle_rad = math.radians(svg_angle_deg)
    
    # Calculate position for text (with padding)
    text_x = center_x + text_radius * math.cos(angle_rad)
    text_y = center_y + text_radius * math.sin(angle_rad)
    
    # Calculate positions for tick marks
    tick_outer_x = center_x + radius * math.cos(angle_rad)
    tick_outer_y = center_y + radius * math.sin(angle_rad)
    tick_inner_x = center_x + tick_inner_radius * math.cos(angle_rad)
    tick_inner_y = center_y + tick_inner_radius * math.sin(angle_rad)
    
    # Determine the color based on the actual heading number
    if 1 <= heading <= 10:
        color_key = "0"
    elif 11 <= heading <= 20:
        color_key = "1"
    elif 21 <= heading <= 29:  # 21-29 instead of 21-30
        color_key = "2"
    else:  # 31-36
        color_key = "3"
    
    color = digit_colors[color_key]["stroke"]
    
    # Determine opacity based on label type
    text_opacity = "0.3" if heading in transparent_labels else "1.0"
    
    # Add tick mark with appropriate transparency
    svg.append(
        f'        <line x1="{tick_inner_x:.1f}" y1="{tick_inner_y:.1f}" x2="{tick_outer_x:.1f}" y2="{tick_outer_y:.1f}" stroke="{color}" stroke-width="1.5" opacity="{text_opacity}"/>'
    )
    
    # Add text element for the heading with appropriate transparency
    svg.append(
        f'        <text x="{text_x:.1f}" y="{text_y:.1f}" dominant-baseline="middle" fill="{color}" font-size="16" opacity="{text_opacity}">{formatted_heading}</text>'
    )

# Add arrows at the centers of each region with colors matching the region's labels
for i, position in enumerate(arrow_positions):
    # Calculate the angle for this position - directly convert heading to degrees
    # In aviation, heading 5 corresponds to 50 degrees, heading 15 to 150 degrees, etc.
    angle_deg = position * 10
    
    # Convert to SVG coordinate system (0° is East, 90° is South)
    # For this we need to subtract 90 degrees from our aviation angle and convert to radians
    svg_angle_deg = angle_deg - 90
    angle_rad = math.radians(svg_angle_deg)
    
    # Determine color based on the position index
    if i == 0:
        color = digit_colors["0"]["stroke"]  # Blue for 50 degrees (heading 5)
    elif i == 1:
        color = digit_colors["1"]["stroke"]  # Red for 150 degrees (heading 15)
    elif i == 2:
        color = digit_colors["2"]["stroke"]  # Brown for 250 degrees (heading 25)
    else:  # i == 3
        color = digit_colors["3"]["stroke"]  # Green for 330 degrees (heading 33)
    
    # Calculate exact position for the arrow using the angle
    # Use a consistent distance from center for all arrows
    plane_radius = radius * 0.6  # 60% of the radius gives a good position within each colored region
    plane_x = center_x + plane_radius * math.cos(angle_rad)
    plane_y = center_y + plane_radius * math.sin(angle_rad)
    
    # Point the arrow outward from the center
    # For outward pointing: Use the same angle as the position
    plane_rotation = svg_angle_deg
    
    # Draw a triangle pointing outward
    # Redefine the triangle to point right by default (toward 3 o'clock)
    # This way when we rotate it by the same angle as its position, it points outward
    svg.append(
        f'        <path d="M 10,0 L -5,-6 L -5,6 Z" transform="translate({plane_x:.1f},{plane_y:.1f}) rotate({plane_rotation:.1f})" fill="{color}" opacity="0.9" />'
    )

# SVG footer
svg.extend([
    '    </g>',
    '</svg>'
])

# Write to file
with open('runway_headings.svg', 'w') as f:
    f.write('\n'.join(svg))

print("SVG file 'runway_heading.svg' has been generated.")