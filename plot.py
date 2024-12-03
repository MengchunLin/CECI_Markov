import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('predict_result_entire.csv', header=None)

# Load the data into a numpy array for easier handling
array_data = data.to_numpy()

# Define a color map for the geological types
# Assuming values are integers, with each integer representing a type
colors = {
    1: "peachpuff",   # Sand
    2: "skyblue",     # Silty Sand
    3: "plum",        # Sandy Silt
    4: "khaki",       # Clayey Silt
    5: "tan",         # Clay
}

# Create a custom colormap and normalize
unique_values = np.unique(array_data)
color_list = [colors[val] for val in unique_values if val in colors]
cmap = plt.matplotlib.colors.ListedColormap(color_list)
bounds = unique_values
norm = plt.matplotlib.colors.BoundaryNorm(bounds, cmap.N)

# Update soil_colors and soil_names
soil_colors = {
    1: 'lightsalmon',       # Sand
    2: 'lightsteelblue',    # Silty Sand
    3: 'plum',              # Sandy Silt
    4: 'darkkhaki',         # Clayey Silt
    5: 'burlywood',         # Clay
}

soil_names = {
    1: 'Sand',
    2: 'Silty Sand',
    3: 'Sandy Silt',
    4: 'Clayey Silt',
    5: 'Clay',
}

# Define updated colormap and norm
updated_colors = [soil_colors[val] for val in unique_values if val in soil_colors]
updated_cmap = plt.matplotlib.colors.ListedColormap(updated_colors)
updated_norm = plt.matplotlib.colors.BoundaryNorm(bounds, updated_cmap.N)

# Adjust the x-axis values to be 13 times larger
x_ticks = np.arange(0, array_data.shape[1], 10)  # Original tick positions (every 10 columns)
x_labels = x_ticks * 13  # Scale the labels by 13

# Plot the updated section
plt.figure(figsize=(12, 6))
plt.imshow(array_data, cmap=updated_cmap, norm=updated_norm, aspect='auto', origin='upper')

# Add a custom legend for the geological types
legend_labels = [plt.matplotlib.patches.Patch(color=soil_colors[val], label=f"{soil_names[val]} ({val})")
                 for val in unique_values if val in soil_colors]
plt.legend(handles=legend_labels, title="Geological Types", loc='upper right', bbox_to_anchor=(1.3, 1))

# Label the axes
plt.title("Geological Cross-Section")
plt.xlabel("Width (units)")
plt.ylabel("Depth (units)")

# Show the plot
plt.tight_layout()
plt.show()