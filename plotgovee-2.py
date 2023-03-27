import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator

# Read the CSV file
with open('H5074_8256_export_202303170826.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    data = [(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') - timedelta(hours=24), 
float(row[1]), float(row[2])) for row in reader]

# Extract the temperature and humidity data into separate lists
dates = [row[0] for row in data]
temperatures = [row[1] for row in data]
humidities = [row[2] for row in data]

# Set the figure size and style
plt.figure(figsize=(10, 6))
plt.style.use('ggplot')

# Define the date formatter and locator for the x-axis
date_form = DateFormatter("%m/%d/%y")
date_loc = DayLocator(interval=2)

# Plot the temperature and humidity data
plt.plot(dates, temperatures, label='Temperature')
plt.plot(dates, humidities, label='Humidity')

# Set the x-axis labels and ticks
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(date_form)
plt.gca().xaxis.set_major_locator(date_loc)

# Set the y-axis labels and limits
plt.ylabel('Value')
plt.ylim(0, 100)

# Set the title and legend
plt.title('Temperature and Humidity Data')
plt.legend()

# Show the plot
plt.show()

