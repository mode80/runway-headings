# Runway Headings Visualizer

A simple tool that generates an SVG visualization of runway headings used in aviation.

## Overview

This project creates a circular diagram representing the standard runway heading system used in aviation. Runway headings are designated by numbers from 01 to 36, representing the compass direction in tens of degrees, where:

- Heading 36 represents North (360°)
- Heading 09 represents East (90°)
- Heading 18 represents South (180°)
- Heading 27 represents West (270°)

## Features

- Color-coded regions for easy visual grouping:
  - Blue (01-10): North to East-Northeast
  - Red (11-20): East-Northeast to South
  - Yellow (21-30): South to West-Northwest
  - Green (31-36): West-Northwest to North
- Clean, modern SVG layout with subtle gradients and shadows
- Divisible-by-3 heading markers (36, 33, 30, ..., 6, 3)

## Files

- `runway.py` - Python script that generates the SVG visualization
- `runway_headings.svg` - The output SVG file

## Usage

Run the Python script to generate the SVG file:

```bash
python runway.py
```

The script will create (or overwrite) `runway_headings.svg` in the same directory.

## Requirements

- Python 3.x
- Standard Python libraries (no external dependencies)

## Example Output

The generated SVG displays a circular compass with runway heading numbers arranged clockwise around the perimeter. Each heading range is color-coded for easy reference.

## License

[MIT License](https://opensource.org/licenses/MIT)
