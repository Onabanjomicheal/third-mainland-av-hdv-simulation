import pandas as pd
import matplotlib.pyplot as plt

# 10% penetration emissions
data = {
    'type': ['av_car', 'brt', 'hdv_car', 'danfo_bus'],
    'CO2': [4.374334e+08, 1.132759e+08, 3.064816e+09, 1.394119e+09],
    'NOx': [1.663427e+05, 4.262828e+04, 1.169791e+06, 5.247764e+05],
    'fuel': [1.418088e+08, 3.672293e+07, 9.935790e+08, 4.519593e+08]
}

df = pd.DataFrame(data).set_index('type')

# Calculate column-wise (pollutant-wise) percentage
df_percentage = df.divide(df.sum(axis=0), axis=1) * 100

# Plot stacked percentage bar chart
df_percentage.plot(kind='bar', stacked=True, figsize=(10, 6),
                   color=['#1f77b4', '#2ca02c', '#d3d3d3'])

plt.title('Percentage Contribution to Emissions by Vehicle Type (10%)')
plt.ylabel('Percentage Contribution (%)')
plt.xlabel('Vehicle Type')
plt.legend(title='Emission Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
