""" Create a simple line chart using Matplotlib that displays square numbers.
Requirements:
  - Use two lists:
      - input_values = [1, 2, 3, 4, 5]
      - squares = [1, 4, 9, 16, 25]
  - Plot the data using a line chart
  - Set line width to improve visibility
  - Apply a built-in Matplotlib style (Solarize_Light2 or similar)
  - Add a chart title: "Square Numbers"
  - Label the x-axis as "Value"
  - Label the y-axis as "Square of Value"
  - Increase tick label size for better readability
  - Display the final chart.   """



import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of thick labels.
ax.tick_params(labelsize=14)

plt.show()
