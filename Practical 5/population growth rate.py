# Make a table of the population data
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]

# Calculate the percentage
growth_rate = []
for i in range(len(countries)):
    rate = ((pop_2024[i] - pop_2020[i]) / pop_2020[i]) * 100
    growth_rate.append(rate)

# Sort from largest increase to largest decrease
pairs = list(zip(countries, growth_rate))
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
print("\nPopulation changes (descending):")
for country, ch in sorted_pairs:
    print(f"The population growth rate of {country} from 2020 to 2024 is {ch:.2f}%.")
largest_inc = sorted_pairs[0]
largest_dec = sorted_pairs[-1]
print(f"{largest_inc[0]} is the country with the largest increase.")
print(f"{largest_dec[0]} is the country with the largest decrease.")

# Create a bar chart
import matplotlib.pyplot as plt
# Ensure the countries and growth rates are in the same order as shown in sorted_pairs
countries = [country for country, _ in sorted_pairs]
growth_rates = [ch for _, ch in sorted_pairs]

plt.figure(figsize=(10, 6))
# The variable "countries" is on the x-axis as typed in the first place
# The variable "growth_rates" is on the y-axis as typed in the second place
# Color setting is based on positive or negative growth
bars = plt.bar(countries, growth_rates, color=['lightgreen' if c>0 else 'lightcoral' for c in growth_rates])
# Name the axes and title
plt.xlabel('Country')
plt.ylabel('Population change (%)')
plt.title('Population Change for five countries from 2020 to 2024')

# Draw a horizontal line at y = 0
plt.axhline(y=0, color='black', linewidth=0.8)

# Calculate the maximum positive and negative growth rates to determine appropriate offsets for label placement
  # "abs()" is to get the absolute value of the negative number
  # "default=0" is to handle the case where there are no positive or negative growth rates, ensuring that max() does not raise an error and returns 0 instead
max_positive = max([c for c in growth_rates if c > 0], default=0)
max_negative = abs(min([c for c in growth_rates if c < 0], default=0))

# Add labels to the bars, adjusting the position based on whether the growth rate is positive or negative
for bar, ch in zip(bars, growth_rates):
    if ch > 0:
        offset = max_positive * 0.013
        y_text = bar.get_height() + offset
        # "va" stands for vertical alignment
        # "bottom" means the text will be aligned with the bottom of the text at the specified y position
        va = 'bottom'
    else:
        offset = max_negative * 0.04
        y_text = bar.get_height() - offset
        va = 'top'
    # "plt.text()" is to add text at the specified position
      # First parameter, which is a formula, is to center the text horizontally
      # Second parameter is the y position of the text
      # Third parameter is the text to be displayed, ".1f" means one decimal place with a percentage sign
      # "ha" stands for horizontal alignment
      # "va" stands for the previous set va standard 
    plt.text(bar.get_x() + bar.get_width()/2, y_text,
             f'{ch:.1f}%', ha='center', va=va)
plt.show()