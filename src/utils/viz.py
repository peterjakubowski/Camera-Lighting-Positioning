# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/23/2026
# Description:
#

import matplotlib.pyplot as plt
from matplotlib import lines, patches


def plot_lighting_diagram(real_object_width: float, real_object_height: float, radius: float, distance: float, light_1x: float, light_1y: float, max_w_in: float, max_h_in: float):
    """
    Plots the lighting diagram using Matplotlib.
    """

    # Create a figure and axes
    fig, ax = plt.subplots(1, figsize=(6, 5), dpi=300)

    # Camera image area
    camera_view = patches.Rectangle(((-max_w_in / 2), (-max_h_in / 2)),
                                    max_w_in,
                                    max_h_in,
                                    fc='#FF7F00',  # Orange
                                    ec="#FF0000",  # Red
                                    lw=1.0,
                                    alpha=1.0)
    ax.add_patch(camera_view)

    # Artwork rectangle
    artwork = patches.Rectangle(((-real_object_width / 2), (-real_object_height / 2)),
                                real_object_width,
                                real_object_height,
                                fc='#B0E2FF',  # Light Steel Blue
                                ec="#4682B4",  # Steel Blue
                                lw=1.2,
                                alpha=1.0)
    ax.add_patch(artwork)

    # Add a yellow circle between the lights
    circle = patches.Circle((0, 0), radius=radius, color='#FFD700', alpha=0.2)
    ax.add_patch(circle)

    # Add an "x" at the center of the rectangle
    ax.text(0, 0, "x", fontsize=10, ha='center', va='center', color='black')

    # Camera placement arrow
    ax.arrow(0.0, distance, 0.0, -distance * 0.95,  # Changed start and end points
             lw=1.5, color='#000000',
             alpha=1.0,
             head_width=0.35, head_length=0.6,  # Reduced head size
             overhang=0.0,  # No overhang
             length_includes_head=True)

    # Light 1 arrow
    ax.arrow(light_1x, light_1y, -light_1x * 0.95, -light_1y * 0.95,  # Changed start and end points
             lw=1.5, color='#000000',
             head_width=0.35, head_length=0.6,  # Reduced head size
             overhang=0,
             length_includes_head=True)

    light_1a = lines.Line2D((light_1x, light_1x), (0, light_1y), lw=1.5, linestyle=':', color='#778899')
    light_1b = lines.Line2D((light_1x, 0), (0, 0), lw=1.5, linestyle=':',
                            color='#778899')

    # Light 2 arrow
    light_2x = -light_1x
    light_2y = light_1y
    ax.arrow(light_2x, light_2y, -light_2x * 0.95, -light_2y * 0.95,  # Changed start and end points
             lw=1.5, color='#000000',
             head_width=0.35, head_length=0.6,  # Reduced head size
             overhang=0,
             length_includes_head=True)

    # Add elements to the axes
    ax.add_line(light_1a)
    ax.add_line(light_1b)

    # Add text annotations
    ax.text(0, distance * 1.025, "camera", fontsize=10, ha='center', va='bottom', color="#101010")
    ax.text(light_1x, light_1y * 1.025, "light", fontsize=10, ha='center', va='bottom', color="#101010")
    ax.text(light_2x, light_2y * 1.025, "light", fontsize=10, ha='center', va='bottom', color="#101010")
    ax.text(-max_w_in / 2, -max_h_in / 2, "image area", fontsize=8, ha='left', va='top',
            color="#101010")  # Image area
    ax.text(-real_object_width / 2, -real_object_height / 2, "object", fontsize=8, ha='left', va='bottom',
            color="#101010")  # Object area

    # Add labels for light distances
    ax.text(light_1x / 1.5, -1, f'{light_1x:.2f} in', fontsize=8, ha='center', va='top',
            color='black')  # Label for light_1x distance
    ax.text(light_1x - 1, light_1y / 2.5, f'{light_1y:.2f} in', fontsize=8, ha='right', va='center',
            color='black')  # Label for light_1y distance
    ax.text(-1, distance / 1.5, f'{distance:.2f} in', fontsize=8, ha='right', va='center',
            color='black')  # Label for light_2x distance

    # Set axis limits and styling
    ax.set_ylim(-distance * 0.5, distance * 1.2)  # Adjusted ylim
    ax.set_xlim(-light_1x * 1.2, light_1x * 1.2)  # Adjusted xlim
    ax.axis('equal')
    ax.tick_params(axis='both', labelsize=8)

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.3)

    # Set the title
    # ax.set_title('Lighting Diagram\n', fontsize=14, color="#333333")

    # Set x label
    ax.set_xlabel('inches', fontsize=10)

    # Remove the frame
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig
