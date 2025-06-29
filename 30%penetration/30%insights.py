# Re-import necessary packages due to kernel reset
import matplotlib.pyplot as plt
import pandas as pd

# Emission data from 30% penetration scenario
data = {
    'type': ['av_car', 'brt', 'hdv_car', 'danfo_bus'],
    'CO2': [1.278399e+09, 1.112369e+08, 2.347806e+09, 1.364180e+09],
    'NOx': [489443.27, 41711.53, 893590.45, 511640.04],
    'fuel': [4.144366e+08, 3.606188e+07, 7.611315e+08, 4.422532e+08]
}
df = pd.DataFrame(data).set_index('type')

# Calculate percentage contributions
percent_df = df.div(df.sum(axis=0), axis=1) * 100

# Plot stacked bar chart for percentage contribution
ax = percent_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20c', edgecolor='black')
plt.title('Percentage Contribution to Emissions by Vehicle Type (30%)')
plt.ylabel('Percentage Contribution (%)')
plt.xlabel('Vehicle Type')
plt.xticks(rotation=0)
plt.legend(title='Emission Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
