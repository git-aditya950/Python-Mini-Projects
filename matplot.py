import matplotlib.pyplot as plt

# Sample temperature data (in °C) over 7 days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [32, 34, 30, 31, 33, 35, 36]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='orange', linewidth=2)

# Customizations
plt.title('Weekly Temperature Trend', fontsize=16)
plt.xlabel('Days', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)
plt.tight_layout()

# Show the chart
plt.show()
