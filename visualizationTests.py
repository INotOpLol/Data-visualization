# import numpy as np
# import matplotlib.pyplot as plt

# # Generate x values
# x = np.linspace(0, 20, 101)

# # Calculate y1 (sine) and y2 (cosine)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # Create the plot
# fig, ax = plt.subplots()

# # Plot both sine and cosine
# ax.plot(x, y1, label="Sine", linewidth=2.0)
# ax.plot(x, y2, label="Cosine", linewidth=2.0)

# # Add title and labels
# ax.set_title("Sine and Cosine Waves")
# ax.set_xlabel("X values")
# ax.set_ylabel("Y values")

# # Show legend
# ax.legend()

# # Display the plot
# plt.show()

##################################################################################################################################################


# import numpy as np
# import matplotlib.pyplot as plt

# # Generate x values
# x = np.linspace(0, 20, 21)
# y = np.random.rand(21)

# # Create the plot
# fig, ax = plt.subplots()

# # Scatter plot for random data
# ax.scatter(x, y, label="Random", color='r')

# # Add title and labels
# ax.set_title("Random Scatter Plot")
# ax.set_xlabel("X values")
# ax.set_ylabel("Y values")

# # Show legend
# ax.legend()

# # Display the plot
# plt.show()

##################################################################################################################################################


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Generate normal x values
# x = 1 + np.random.normal(0, 5, 200)

# # Create the plot
# fig, ax = plt.subplots()

# # Hist plot for random normal data
# ax.hist(x,bins= 30, linewidth = 0.5, edgecolor = "white", density=True)

# sns.kdeplot(x , ax = ax, color = "red", linewidth = 2)

# # Add title and labels
# ax.set_title("Hist Plot")
# ax.set_xlabel("X values")
# ax.set_ylabel("Y values")

# # Show legend
# ax.legend()

# # Display the plot
# plt.show()

##################################################################################################################################################


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# # Load Dataset
# data = sns.load_dataset("iris")
# # Remove species column to have all num values
# data.drop(columns=["species"])
# # Convert to corrolation matrix
# data.corr()

# # Create heatmap using seaborn and matplotlib
# sns.heatmap(data= data, annot= True, cmap= "coolwarm")
# plt.title("Iris Corrolation Table")

# # Display the plot
# plt.show()

##################################################################################################################################################


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Dataset
data = sns.load_dataset("tips")

# Create boxplot
sns.boxplot(x = "day", y = "total_bill", hue="sex", data= data, palette= ["g", "m"])
plt.title("Box Plot")

plt.show()