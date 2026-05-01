# Create the list and calculate the len
heart_rates_list = [72,	60,	126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates_list)
# Calculate the mean heart rate and print it
mean_heart_rate = sum(heart_rates_list) / len(heart_rates_list)
print (f"There are {num_patients} patients in the dataset and the mean heart rate is {mean_heart_rate:.2f} bpm.")

# Sort the list into three categories
i = 0
low = 0
normal = 0
high = 0
while i < len(heart_rates_list):
    if heart_rates_list[i] < 60:
        low += 1
    elif heart_rates_list[i] > 120:
        high += 1
    else:
        normal += 1
    i += 1
# Print the results
print (f"There are {low} patients with low heart rates, {normal} patients with normal heart rates and {high} patients with high heart rates.")

# Identify the category with most patients
if low > normal and low > high:
    print ("The 'low' category contains the most patients.")
elif normal > low and normal > high:
    print ("The 'normal' category contains the most patients.")    
elif high > low and high > normal:
    print ("The 'high' category contains the most patients.")

# Make a pie chart based on the categories
import matplotlib.pyplot as plt
# Define the labels, sizes and colors for the pie chart
# When trying to type words rather than numbers, '' is important
labels = ['Low', 'Normal', 'High']
sizes = [low, normal, high]
colors = ['lightcoral', 'lightgreen', 'lightsalmon']
# Define a function to show the absolute number of patients in each category on the pie chart
# "show_number" is the name of a function, "pct" is the percentage value for each category, "all_vals" is the list of sizes for each category
def show_number(pct, all_vals):
    # Calculate the actual count for each category. The formula is: percentage × total ÷ 100. "round()" rounds to the nearest integer. And "int()" converts it to an integer.
    # This procedure seems a little bit complicated
    absolute = int(round(pct * sum(all_vals) / 100))
    # Convert the calculated count to a string and return it
    return f'{absolute}'
plt.figure(figsize=(6, 6))
# "autopct" is used to display the percentage value on the pie chart. 
# Here a "lambda" function is used to call "show_number" for each category, outputting the absolute number of patients instead of the percentage. 
  # If the percentage is wanted here, the "autopct" code could be: "autopct='%1.1f%%'". The "%1.1f%%" format means to display the percentage with one decimal place followed by a percent sign.
# "startangle" rotates the start of the pie chart by 120 degrees for better visualization.
plt.pie(sizes, labels=labels, colors=colors, autopct=lambda pct: show_number(pct, sizes), startangle=120)
plt.title(' The Distribution of Heart Rate Categories')
# Show the pie chart
plt.show()