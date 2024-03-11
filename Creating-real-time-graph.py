import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Read data from Excel file
df = pd.read_excel('flowdata.xlsx')

# Separate data for chart
Flow_Time = df['Flow-Time']
P1_Bar = df['P1']
P2_Bar = df['P2']
P3_Bar = df['P3']
P4_Bar = df['P4']

# Create a single chart
fig, ax1 = plt.subplots(figsize=(10, 6))  # Width: 10, Height: 6

# P1 for left y-axis
ax1.set_xlabel('Flow-Time')
ax1.set_ylabel('P1', color='k')
line_p1, = ax1.plot([], [], 'b-', label='P1_[Bar]')
ax1.tick_params('y', colors='k')

# P2, P3 ve P4 for right y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('P2, P3, P4', color='k')
line_p2, = ax2.plot([], [], 'g-', label='P2_[Bar]')
line_p3, = ax2.plot([], [], 'r-', label='P3_[Bar]')
line_p4, = ax2.plot([], [], 'm-', label='P4_[Bar]')
ax2.tick_params('y', colors='k')

# Mark table
legend_lines = [line_p1, line_p2, line_p3, line_p4]
legend_labels = [line.get_label() for line in legend_lines]
ax1.legend(legend_lines, legend_labels, loc='lower left')

# Clear excess space for activated right y-axis
fig.subplots_adjust(right=0.85)  # Set spacing for axes shifted to the right

# Update function of animation
def update(frame):
    line_p1.set_data(Flow_Time[:frame], P1_Bar[:frame])
    line_p2.set_data(Flow_Time[:frame], P2_Bar[:frame])
    line_p3.set_data(Flow_Time[:frame], P3_Bar[:frame])
    line_p4.set_data(Flow_Time[:frame], P4_Bar[:frame])
    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
    return line_p1, line_p2, line_p3, line_p4

# Create animation
ani = FuncAnimation(fig, update, frames=len(Flow_Time), blit=True, interval=100)  # Create a frame every 100 milliseconds

# Save animation as GIF
ani.save('flowdata.gif', writer='pillow')

# Show charts
plt.show()
