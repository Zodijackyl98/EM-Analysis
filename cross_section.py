import matplotlib.pyplot as plt
import numpy as np

def plot_subsurface(layer_depths, resistivities):
    """
    Creates a cross-section plot of the subsurface based on layer depths and resistivities.

    Parameters:
    layer_depths (list of float): Depths of the layers in meters.
    resistivities (list of float): Resistivity values for each layer in Ohm�m.
    """
    # Validation
    if len(layer_depths) + 1 != len(resistivities):
        raise ValueError("Number of resistivities must be one more than number of layer depths.")

    # Prepare data for plotting
    max_depth = sum(layer_depths) if layer_depths else 100  # Default max depth for plotting
    layer_boundaries = [0] + list(np.cumsum(layer_depths))
    
    fig, ax = plt.subplots(figsize=(6, 8))

    # Set up colormap to reflect the actual resistivity range
    cmap = plt.cm.viridis
    norm = plt.Normalize(vmin=min(resistivities), vmax=max(resistivities))
    
    # Create the layers
    for i in range(len(resistivities)):
        top = layer_boundaries[i]
        bottom = max_depth if i == len(resistivities) - 1 else layer_boundaries[i + 1]
        color = cmap(norm(resistivities[i]))
        ax.fill_betweenx([top, bottom], 0, 1, color=color, alpha=0.8)

        # Label layer resistivity
        ax.text(0.5, (top + bottom) / 2, f"{resistivities[i]} Ohm�m", color="white", fontsize=10, ha="center", va="center", 
                transform=ax.transAxes)
    
    # Plot formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(max_depth, 0)
    ax.set_xticks([])
    ax.set_yticks(layer_boundaries)
    ax.set_yticklabels([f"{d} m" for d in layer_boundaries])
    ax.set_ylabel("Depth (m)")
    ax.set_title("Subsurface Cross-Section")
    
    # Add color bar to reflect the true resistivity range
    cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, label="Resistivity (Ohm�m)", orientation="vertical")
    cbar.set_label("Resistivity (Ohm�m)")
    plt.tight_layout()
    plt.show()

# Example Input
layer_depths = [50, 100, 150]  # Depths of the layers in meters
resistivities = [10, 50, 100, 5]  # Resistivity values for each layer in Ohm�m

plot_subsurface(layer_depths, resistivities)
