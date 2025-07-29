import pandas as pd
import re
import json
import os


file_path = 'data/Cars Datasets 2025.csv'
df = pd.read_csv(file_path, encoding='latin1')


def extract_numeric(value):
    if pd.isna(value):
        return None
    nums = re.findall(r'\d+(?:,\d+)?(?:\.\d+)?', value.replace(',', ''))
    if not nums:
        return None
    try:
        return float(nums[0])
    except:
        return None

df['HorsePower_clean'] = df['HorsePower'].apply(extract_numeric)
df['TopSpeed_clean'] = df['Total Speed'].apply(extract_numeric)
df['Acceleration_clean'] = df['Performance(0 - 100 )KM/H'].apply(extract_numeric)
df['Price_clean'] = df['Cars Prices'].apply(lambda x: extract_numeric(str(x).replace('$', '')))
df['EngineSize_clean'] = df['CC/Battery Capacity'].apply(extract_numeric)
df['Torque_clean'] = df['Torque'].apply(extract_numeric)
df['Fuel Types Clean'] = df['Fuel Types'].str.strip().str.lower()

df['HP_to_Price'] = df['HorsePower_clean'] / df['Price_clean']
df['Speed_to_Accel'] = df['TopSpeed_clean'] / df['Acceleration_clean']
df['Speed_to_Price'] = df['TopSpeed_clean'] / df['Price_clean']

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

summary = {
    'Total Entries': len(df),
    'Average HorsePower': round(df['HorsePower_clean'].mean(), 2),
    'Maximum HorsePower Car': df.loc[df['HorsePower_clean'].idxmax(), ['Company Names', 'Cars Names', 'HorsePower_clean']].to_dict(),
    'Average Price (USD)': round(df['Price_clean'].mean(), 2),
    'Most Expensive Car': df.loc[df['Price_clean'].idxmax(), ['Company Names', 'Cars Names', 'Price_clean']].to_dict(),
    'Least Expensive Car': df.loc[df['Price_clean'].idxmin(), ['Company Names', 'Cars Names', 'Price_clean']].to_dict(),
    'Fastest Acceleration (0–100 km/h)': df.loc[df['Acceleration_clean'].idxmin(), ['Company Names', 'Cars Names', 'Acceleration_clean']].to_dict(),
    'Top Speed Car': df.loc[df['TopSpeed_clean'].idxmax(), ['Company Names', 'Cars Names', 'TopSpeed_clean']].to_dict(),
    'Average Top Speed': round(df['TopSpeed_clean'].mean(), 2),
    'Average Acceleration': round(df['Acceleration_clean'].mean(), 2),
    'HorsePower by Fuel Type': df.groupby('Fuel Types Clean')['HorsePower_clean'].mean().round(2).dropna().to_dict(),
    'Price by Fuel Type': df.groupby('Fuel Types Clean')['Price_clean'].mean().round(2).dropna().to_dict(),
    'HorsePower by Seat Count': df.groupby('Seats')['HorsePower_clean'].mean().round(2).dropna().to_dict(),
    'Acceleration by Fuel Type': df.groupby('Fuel Types Clean')['Acceleration_clean'].mean().round(2).dropna().to_dict(),
    'Average Engine Size (cc)': round(df['EngineSize_clean'].mean(), 2),
    'Average Torque (Nm)': round(df['Torque_clean'].mean(), 2),
    'Fuel Type Distribution': df['Fuel Types Clean'].value_counts().to_dict(),
    'Seats Distribution': df['Seats'].value_counts().to_dict(),
    'Models per Company': df['Company Names'].value_counts().to_dict(),
    'Top Companies by Avg HorsePower': df.groupby('Company Names')['HorsePower_clean'].mean().dropna().sort_values(ascending=False).head(10).round(2).to_dict(),
    'Top Companies by Avg Price': df.groupby('Company Names')['Price_clean'].mean().dropna().sort_values(ascending=False).head(10).round(2).to_dict()
}

with open(os.path.join(output_dir, 'summary_stats.json'), 'w') as f:
    json.dump(summary, f, indent=4)

with open(os.path.join(output_dir, 'top_performers.txt'), 'w') as f:
    f.write("Top 5 Horsepower Cars:\n")
    top_hp = df.sort_values(by='HorsePower_clean', ascending=False).head(5)[['Company Names', 'Cars Names', 'HorsePower_clean']]
    f.write(top_hp.to_string(index=False))

    f.write("\n\nTop 5 Fastest Accelerating Cars (0–100 km/h):\n")
    fast_accel = df.sort_values(by='Acceleration_clean').head(5)[['Company Names', 'Cars Names', 'Acceleration_clean']]
    f.write(fast_accel.to_string(index=False))

    f.write("\n\nTop 5 Most Expensive Cars:\n")
    top_price = df.sort_values(by='Price_clean', ascending=False).head(5)[['Company Names', 'Cars Names', 'Price_clean']]
    f.write(top_price.to_string(index=False))

    f.write("\n\nTop 5 Speed-to-Price Ratio Cars:\n")
    top_speed_price = df.sort_values(by='Speed_to_Price', ascending=False).head(5)[['Company Names', 'Cars Names', 'TopSpeed_clean', 'Price_clean']]
    f.write(top_speed_price.to_string(index=False))

    f.write("\n\nTop 5 HP-to-Price Ratio Cars:\n")
    top_hp_price = df.sort_values(by='HP_to_Price', ascending=False).head(5)[['Company Names', 'Cars Names', 'HorsePower_clean', 'Price_clean']]
    f.write(top_hp_price.to_string(index=False))

    f.write("\n\nTop 5 Speed-to-Acceleration Ratio Cars:\n")
    top_efficiency = df.sort_values(by='Speed_to_Accel', ascending=False).head(5)[['Company Names', 'Cars Names', 'TopSpeed_clean', 'Acceleration_clean']]
    f.write(top_efficiency.to_string(index=False))

print("✅ All basic and advanced statistics saved in the 'output/' folder.")
