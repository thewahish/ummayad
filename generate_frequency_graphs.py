#!/usr/bin/env python3
"""
Generate professional SVG frequency response graphs for Umayyad Mosque report
Based on ACOUSTIC_SIMULATION_SPECIFICATION.md
"""

import math

def log_position(freq, min_freq=20, max_freq=16000, width=700):
    """Calculate logarithmic X position for frequency"""
    log_min = math.log10(min_freq)
    log_max = math.log10(max_freq)
    log_freq = math.log10(freq)
    return 50 + (log_freq - log_min) / (log_max - log_min) * width

def db_position(db, min_db=-20, max_db=5, height=400):
    """Calculate Y position for dB value"""
    return 50 + (1 - (db - min_db) / (max_db - min_db)) * height

def create_frequency_response_svg(title, legend_text, color, data_points, graph_id):
    """
    Create an SVG frequency response graph

    Args:
        title: Graph title
        legend_text: Legend text
        color: Line color (hex)
        data_points: List of (frequency_hz, gain_db) tuples
        graph_id: Unique identifier for the graph
    """

    svg_width = 800
    svg_height = 500
    plot_width = 700
    plot_height = 400
    margin_left = 50
    margin_top = 50
    margin_right = 50
    margin_bottom = 50

    # Frequency tick marks (logarithmic)
    freq_ticks = [20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    freq_labels = ['20', '31.5', '63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k']

    # dB tick marks (linear)
    db_ticks = list(range(-20, 6, 5))

    # Start SVG
    svg = f'''<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg" id="{graph_id}">
    <!-- Background -->
    <rect width="{svg_width}" height="{svg_height}" fill="white"/>

    <!-- Plot area background -->
    <rect x="{margin_left}" y="{margin_top}" width="{plot_width}" height="{plot_height}" fill="white" stroke="#333" stroke-width="1"/>

    <!-- Grid lines (dB - horizontal) -->'''

    # Draw horizontal grid lines (dB)
    for db in db_ticks:
        y = db_position(db)
        stroke_width = "2" if db == 0 else "0.5"
        opacity = "0.8" if db == 0 else "0.3"
        svg += f'''
    <line x1="{margin_left}" y1="{y}" x2="{margin_left + plot_width}" y2="{y}" stroke="#E0E0E0" stroke-width="{stroke_width}" opacity="{opacity}"/>'''

    # Draw vertical grid lines (frequency - logarithmic)
    svg += '''

    <!-- Grid lines (Frequency - logarithmic vertical) -->'''
    for freq in freq_ticks:
        x = log_position(freq)
        svg += f'''
    <line x1="{x}" y1="{margin_top}" x2="{x}" y2="{margin_top + plot_height}" stroke="#E0E0E0" stroke-width="0.5" opacity="0.3"/>'''

    # Draw axes labels
    svg += '''

    <!-- Y-axis labels (dB) -->'''
    for db in db_ticks:
        y = db_position(db)
        svg += f'''
    <text x="{margin_left - 10}" y="{y + 4}" text-anchor="end" font-family="Arial, sans-serif" font-size="12" fill="#333">{db:+d}</text>'''

    svg += '''

    <!-- X-axis labels (Frequency) -->'''
    for i, freq in enumerate(freq_ticks):
        x = log_position(freq)
        svg += f'''
    <text x="{x}" y="{margin_top + plot_height + 20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#333">{freq_labels[i]}</text>'''

    # Axis titles
    svg += f'''

    <!-- Axis titles -->
    <text x="{margin_left + plot_width/2}" y="{svg_height - 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#333">Frequency (Hz)</text>
    <text x="15" y="{margin_top + plot_height/2}" text-anchor="middle" transform="rotate(-90, 15, {margin_top + plot_height/2})" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#333">Gain (dB)</text>

    <!-- Title -->
    <text x="{svg_width/2}" y="25" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#1a252f">{title}</text>

    <!-- Data curve -->
    <path d="'''

    # Generate path for frequency response curve
    path_commands = []
    for i, (freq, db) in enumerate(data_points):
        x = log_position(freq)
        y = db_position(db)
        if i == 0:
            path_commands.append(f"M {x:.2f} {y:.2f}")
        else:
            path_commands.append(f"L {x:.2f} {y:.2f}")

    svg += " ".join(path_commands)
    svg += f'''" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Data points -->'''

    # Draw data point markers
    for freq, db in data_points:
        x = log_position(freq)
        y = db_position(db)
        svg += f'''
    <circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="{color}" stroke="white" stroke-width="1"/>'''

    # Legend
    svg += f'''

    <!-- Legend -->
    <rect x="{svg_width - 250}" y="45" width="230" height="35" fill="white" stroke="#999" stroke-width="1" rx="3"/>
    <line x1="{svg_width - 240}" y1="62.5" x2="{svg_width - 210}" y2="62.5" stroke="{color}" stroke-width="3"/>
    <text x="{svg_width - 205}" y="67" font-family="Arial, sans-serif" font-size="12" fill="#333">{legend_text}</text>

</svg>'''

    return svg

# Define frequency response data based on ACOUSTIC_SIMULATION_SPECIFICATION.md

# EXISTING SYSTEM - Dynacord Speakers (Aged, Degraded)
dynacord_right_back = [
    (20, -20), (25, -20), (31.5, -19), (40, -18), (50, -17), (63, -15),
    (80, -13), (100, -11), (125, -10), (160, -8), (200, -6), (250, -5),
    (315, -3), (400, -2), (500, -1), (630, 0), (800, 0),
    (1000, -2), (1250, -2), (1600, -2), (2000, -2),
    (2500, -1), (3150, 0), (4000, -2), (5000, 0),
    (6300, 0), (8000, -5), (10000, -10), (12500, -15), (16000, -18)
]

dynacord_left_back = [
    (20, -20), (25, -20), (31.5, -19), (40, -18), (50, -17), (63, -15),
    (80, -13), (100, -11), (125, -10), (160, -8), (200, -6), (250, -5),
    (315, -3), (400, -2), (500, -1), (630, 0), (800, 0),
    (1000, -2), (1250, -2), (1600, -2), (2000, -2),
    (2500, 1), (3150, -1), (4000, -3), (5000, -1),
    (6300, -1), (8000, -6), (10000, -11), (12500, -16), (16000, -19)
]

# EXISTING SYSTEM - Inter-M SE-8 (Moderate Degradation)
interm_right_front = [
    (20, -18), (25, -17), (31.5, -16), (40, -15), (50, -13), (63, -12),
    (80, -10), (100, -8), (125, -6), (160, -5), (200, -4), (250, -3),
    (315, -2), (400, -2), (500, -2), (630, -2), (800, -2),
    (1000, -4), (1250, -2), (1600, 2), (2000, -3), (2500, 0),
    (3150, 1), (4000, 0), (5000, 1), (6300, 1),
    (8000, -1), (10000, -4), (12500, -8), (16000, -10)
]

interm_left_front = [
    (20, -18), (25, -17), (31.5, -16), (40, -15), (50, -13), (63, -12),
    (80, -10), (100, -8), (125, -6), (160, -5), (200, -4), (250, -3),
    (315, -2), (400, -2), (500, -2), (630, -2), (800, -2),
    (1000, -3), (1250, 1), (1600, -4), (2000, 2), (2500, -2),
    (3150, 0), (4000, 1), (5000, 0), (6300, 0),
    (8000, -2), (10000, -5), (12500, -9), (16000, -11)
]

# EXISTING SYSTEM - Mixed positions with comb filtering
mixed_position_5 = [
    (20, -18), (25, -17), (31.5, -15), (40, -13), (50, -11), (63, -10),
    (80, -8), (100, -7), (125, -5), (160, -6), (200, -3), (250, -4),
    (315, -2), (400, 2), (500, -3), (630, 1), (800, -4),
    (1000, 0), (1250, -5), (1600, 3), (2000, -2), (2500, -6),
    (3150, 2), (4000, -4), (5000, 1), (6300, -3),
    (8000, -7), (10000, -12), (12500, -15), (16000, -17)
]

mixed_position_6 = [
    (20, -19), (25, -18), (31.5, -16), (40, -14), (50, -12), (63, -11),
    (80, -9), (100, -7), (125, -6), (160, -4), (200, -5), (250, -2),
    (315, -4), (400, 1), (500, -2), (630, -5), (800, 2),
    (1000, -3), (1250, 4), (1600, -6), (2000, 1), (2500, -4),
    (3150, -1), (4000, 3), (5000, -5), (6300, 0),
    (8000, -8), (10000, -13), (12500, -16), (16000, -18)
]

# REFERENCE SYSTEM - Yamaha HS8 (Flat Response)
yamaha_hs8_right_back = [
    (20, -18), (25, -16), (31.5, -14), (40, -8), (50, -5), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 0), (200, 0), (250, 0),
    (315, 0), (400, 1), (500, 1), (630, 1), (800, 1),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, 0),
    (8000, -1), (10000, -1), (12500, -3), (16000, -6)
]

yamaha_hs8_left_back = [
    (20, -18), (25, -16), (31.5, -14), (40, -8), (50, -5), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 0), (200, 0), (250, 0),
    (315, 0), (400, 1), (500, 1), (630, 1), (800, 1),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, 0),
    (8000, -1), (10000, -1), (12500, -3), (16000, -6)
]

yamaha_hs8_right_front = [
    (20, -18), (25, -15), (31.5, -13), (40, -7), (50, -4), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 1), (200, 1), (250, 1),
    (315, 1), (400, 1), (500, 1), (630, 1), (800, 1),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, -1),
    (8000, -1), (10000, -2), (12500, -3), (16000, -5)
]

yamaha_hs8_left_front = [
    (20, -18), (25, -15), (31.5, -13), (40, -7), (50, -4), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 1), (200, 1), (250, 1),
    (315, 1), (400, 1), (500, 1), (630, 1), (800, 1),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, -1),
    (8000, -1), (10000, -2), (12500, -3), (16000, -5)
]

yamaha_hs8_position_5 = [
    (20, -18), (25, -16), (31.5, -13), (40, -8), (50, -5), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 0), (200, 0), (250, 0),
    (315, 1), (400, 1), (500, 1), (630, 1), (800, 1),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, -1), (6300, -1),
    (8000, -1), (10000, -2), (12500, -3), (16000, -6)
]

yamaha_hs8_middle_front = [
    (20, -18), (25, -15), (31.5, -13), (40, -7), (50, -4), (63, -2),
    (80, -1), (100, 0), (125, 0), (160, 1), (200, 1), (250, 1),
    (315, 1), (400, 1), (500, 1), (630, 1), (800, 0),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, -1),
    (8000, -1), (10000, -2), (12500, -3), (16000, -6)
]

# PROPOSED SYSTEM - Line Array with Room EQ
proposed_m1_front = [
    (20, -20), (25, -19), (31.5, -18), (40, -16), (50, -14), (63, -12),
    (80, -10), (100, -8), (125, -6), (160, -5), (200, -4), (250, -3),
    (315, -4), (400, -5), (500, -4), (630, -3), (800, -2),
    (1000, 0), (1250, 1), (1600, 1), (2000, 2),
    (2500, 2), (3150, 3), (4000, 2), (5000, 2), (6300, 1),
    (8000, 0), (10000, -1), (12500, -2), (16000, -4)
]

proposed_r1_rear = [
    (20, -20), (25, -19), (31.5, -18), (40, -16), (50, -14), (63, -12),
    (80, -10), (100, -8), (125, -6), (160, -5), (200, -4), (250, -3),
    (315, -2), (400, -2), (500, -1), (630, -1), (800, -1),
    (1000, 0), (1250, 1), (1600, 2), (2000, 3),
    (2500, 3), (3150, 4), (4000, 4), (5000, 3), (6300, 3),
    (8000, 2), (10000, 1), (12500, 0), (16000, -2)
]

proposed_y1_courtyard = [
    (20, -20), (25, -18), (31.5, -16), (40, -10), (50, -7), (63, -4),
    (80, -2), (100, -1), (125, -1), (160, 0), (200, 0), (250, 0),
    (315, 0), (400, 0), (500, 0), (630, 0), (800, 0),
    (1000, 0), (1250, 0), (1600, 0), (2000, 0),
    (2500, 0), (3150, 0), (4000, 0), (5000, 0), (6300, 0),
    (8000, -1), (10000, -1), (12500, -2), (16000, -4)
]

# Generate all SVG graphs
graphs = []

# Existing System (RED and ORANGE)
graphs.append({
    'svg': create_frequency_response_svg(
        "Right Back - Dynacord (Aged Speaker Response)",
        "Right Back - Dynacord",
        "#E74C3C",
        dynacord_right_back,
        "graph_dynacord_right_back"
    ),
    'filename': 'freq_dynacord_right_back.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Left Back - Dynacord (Aged Speaker Response)",
        "Left Back - Dynacord",
        "#E74C3C",
        dynacord_left_back,
        "graph_dynacord_left_back"
    ),
    'filename': 'freq_dynacord_left_back.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Right Front - Inter-M SE-8 (Moderate Age Degradation)",
        "Right Front - Inter-M SE-8",
        "#E67E22",
        interm_right_front,
        "graph_interm_right_front"
    ),
    'filename': 'freq_interm_right_front.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Left Front - Inter-M SE-8 (Asymmetry - Suspected Blown Driver)",
        "Left Front - Inter-M SE-8",
        "#E67E22",
        interm_left_front,
        "graph_interm_left_front"
    ),
    'filename': 'freq_interm_left_front.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Position 5 - Mixed System (Comb Filtering)",
        "Position 5 - Mixed Speakers",
        "#E67E22",
        mixed_position_5,
        "graph_mixed_position_5"
    ),
    'filename': 'freq_mixed_position_5.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Position 6 - Mixed System (Phase Interference)",
        "Position 6 - Mixed Speakers",
        "#E67E22",
        mixed_position_6,
        "graph_mixed_position_6"
    ),
    'filename': 'freq_mixed_position_6.svg'
})

# Reference System - Yamaha HS8 (BLUE)
graphs.append({
    'svg': create_frequency_response_svg(
        "Right Back - Yamaha HS8 (Reference Test)",
        "Right Back - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_right_back,
        "graph_yamaha_right_back"
    ),
    'filename': 'freq_yamaha_right_back.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Left Back - Yamaha HS8 (Reference Test)",
        "Left Back - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_left_back,
        "graph_yamaha_left_back"
    ),
    'filename': 'freq_yamaha_left_back.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Right Front - Yamaha HS8 (Reference Test)",
        "Right Front - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_right_front,
        "graph_yamaha_right_front"
    ),
    'filename': 'freq_yamaha_right_front.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Left Front - Yamaha HS8 (Reference Test)",
        "Left Front - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_left_front,
        "graph_yamaha_left_front"
    ),
    'filename': 'freq_yamaha_left_front.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Position 5 - Yamaha HS8 (Reference Test)",
        "Position 5 - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_position_5,
        "graph_yamaha_position_5"
    ),
    'filename': 'freq_yamaha_position_5.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Middle Front - Yamaha HS8 (Reference Test)",
        "Middle Front - Yamaha HS8",
        "#3498DB",
        yamaha_hs8_middle_front,
        "graph_yamaha_middle_front"
    ),
    'filename': 'freq_yamaha_middle_front.svg'
})

# Proposed System (GREEN and CYAN)
graphs.append({
    'svg': create_frequency_response_svg(
        "Proposed System - Position M1 (Front Center, Below Dome)",
        "Proposed Line Array + Room EQ",
        "#27AE60",
        proposed_m1_front,
        "graph_proposed_m1"
    ),
    'filename': 'freq_proposed_m1.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Proposed System - Position R1 (Rear Center, 120m)",
        "Proposed Line Array + Room EQ (Long Throw)",
        "#27AE60",
        proposed_r1_rear,
        "graph_proposed_r1"
    ),
    'filename': 'freq_proposed_r1.svg'
})

graphs.append({
    'svg': create_frequency_response_svg(
        "Proposed System - Position Y1 (Courtyard Center, Open Air)",
        "Weatherproof Column Speakers (Exterior)",
        "#1ABC9C",
        proposed_y1_courtyard,
        "graph_proposed_y1"
    ),
    'filename': 'freq_proposed_y1.svg'
})

# Save all SVG files
import os
output_dir = "/Volumes/Ai/Projects/ummayad/freq_graphs"
os.makedirs(output_dir, exist_ok=True)

for graph in graphs:
    filepath = os.path.join(output_dir, graph['filename'])
    with open(filepath, 'w') as f:
        f.write(graph['svg'])
    print(f"Generated: {graph['filename']}")

print(f"\nAll {len(graphs)} SVG graphs generated successfully in {output_dir}")

# Also save graphs dict for embedding in HTML
print("\n" + "="*80)
print("SVG graphs ready for HTML embedding")
print("="*80)
