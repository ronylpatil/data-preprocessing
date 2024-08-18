import pandas as pd
import matplotlib.pyplot as plt

# Lists to store the x and y coordinates and their corresponding classes
x = []
y = []
classes = []
points = []
x_min = 0
y_min = 0
x_max = 20
y_max = 20

# Colors for two different classes
colors = {1: "ro", 2: "bo"}  # 'ro' for red, 'bo' for blue
current_class = 1  # Start with class 1


def onclick(event) -> None:
    if event.xdata is not None and event.ydata is not None:
        # Store the x, y coordinates, and the class
        x.append(round(event.xdata, 3))
        y.append(round(event.ydata, 3))
        classes.append(current_class)
        # print(f"Stored: ({event.xdata}, {event.ydata}) as class {current_class}")

        # Plot the point with the corresponding color
        (point,) = plt.plot(event.xdata, event.ydata, colors[current_class])
        points.append(point)
        plt.draw()  # Update the plot


def onkey(event) -> None:
    global current_class
    if event.key == "u" and x and y:
        # Undo the last point when the 'u' key is pressed
        x.pop()
        y.pop()
        classes.pop()
        point = points.pop()
        point.remove()  # Remove the last point from the plot
        plt.draw()  # Update the plot
    elif event.key == "1":
        # Switch to class 1
        current_class = 1
    elif event.key == "2":
        # Switch to class 2
        current_class = 2


# Create a basic plot
fig, ax = plt.subplots()
ax.set_title("Canvas")
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Connect the click event to the onclick function
cid_click = fig.canvas.mpl_connect("button_press_event", onclick)
# Connect the key press event to the onkey function
cid_key = fig.canvas.mpl_connect("key_press_event", onkey)

# Display the plot
plt.show()

# After closing the plot, you can see the collected points and their classes
df = pd.DataFrame(data={"x": x, "y": y, "class": classes})
df.to_csv("data/raw/sample.csv", index=False)
