# Re-import necessary packages due to kernel reset
import matplotlib.pyplot as plt
import pandas as pd

# Emission data from 50% penetration scenario
data = {
    'type': ['av_car', 'brt', 'hdv_car', 'danfo_bus'],
    'CO2': [2.123036e+09, 1.149242e+08, 1.758585e+09, 1.419551e+09],
    'NOx': [817405.50, 43066.29, 666733.45, 531185.57],
    'fuel': [6.882551e+08, 3.725727e+07, 5.701124e+08, 4.602037e+08]
}
df = pd.DataFrame(data).set_index('type')

# Calculate percentage contributions
percent_df = df.div(df.sum(axis=0), axis=1) * 100

# Plot stacked bar chart for percentage contribution
ax = percent_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20c', edgecolor='black')
plt.title('Percentage Contribution to Emissions by Vehicle Type (50%)')
plt.ylabel('Percentage Contribution (%)')
plt.xlabel('Vehicle Type')
plt.xticks(rotation=0)
plt.legend(title='Emission Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
s