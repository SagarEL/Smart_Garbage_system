import pandas as pd
from collections import Counter

# Load CSV data
df = pd.read_csv('/home/sagar/Desktop/Smart_dustbin_ai/Backend/dustbin_data.csv')

# Clean column names (remove leading/trailing spaces)
df.columns = [col.strip() for col in df.columns]

# Step 1: Group by Street
grouped = df.groupby('Street')

# Step 2: Analyze each street
predictions = []

for street, group in grouped:
    avg_fill_time = group['Time_To_Fill_Hours'].mean()
    
    # Basic bin requirement logic:
    # Faster fill time → need more bins
    if avg_fill_time < 6:
        bin_count = 4
    elif avg_fill_time < 12:
        bin_count = 3
    elif avg_fill_time < 18:
        bin_count = 2
    else:
        bin_count = 1

    # Determine dominant waste type
    organic_avg = group['Organic_%'].mean()
    plastic_avg = group['Plastic_%'].mean()
    metal_avg = group['Metal_%'].mean()

    # Get top 2 types for bin diversity
    waste_types = {
        'Organic': organic_avg,
        'Plastic': plastic_avg,
        'Metal': metal_avg
    }
    sorted_types = sorted(waste_types.items(), key=lambda x: x[1], reverse=True)
    bin_types = [w[0] for w in sorted_types[:2]]  # Top 2 waste types

    # Estimate a suggested bin location (mean lat/lon)
    avg_lat = group['Latitude'].mean()
    avg_lon = group['Longitude'].mean()

    predictions.append({
        'street': street,
        'predicted_bin_count': bin_count,
        'suggested_bin_types': bin_types,
        'suggested_location': {'latitude': round(avg_lat, 6), 'longitude': round(avg_lon, 6)}
    })

# Convert to DataFrame or export to JSON
import json

with open('data.json', 'w') as f:
    json.dump(predictions, f, indent=2)

print("✅ Prediction completed! Output saved to 'predicted_smart_bins.json'")

