import pandas as pd
import random
from datetime import datetime, timedelta

# Updated coordinates with new street names
dustbins = {
    "Channasandra": [("DB1", 12.918112, 77.495323), ("DB2", 12.917826, 77.496185)],
    "Srinivasapura": [("DB1", 12.917681, 77.497245), ("DB2", 12.917413, 77.498030)],
    "Hemmigepura": [("DB1", 12.917364, 77.497137), ("DB2", 12.917118, 77.497962)],
    "Dubasipalya": [("DB1", 12.917602, 77.494877), ("DB2", 12.917171, 77.496221), ("DB3", 12.916775, 77.497507)],
    "Kodipalya": [("DB1", 12.917500, 77.495800), ("DB2", 12.917200, 77.496400)],
    "Komaghatta": [("DB1", 12.916800, 77.497100), ("DB2", 12.916500, 77.498200)],
    "Kengeri Upanagara": [("DB1", 12.917000, 77.495500), ("DB2", 12.916700, 77.496700)],
    "Mailsandra": [("DB1", 12.918000, 77.497300), ("DB2", 12.917600, 77.498000)],
    "Pattanagere": [("DB1", 12.917300, 77.495900), ("DB2", 12.916900, 77.496500)]
}

data = []

for _ in range(100):
    street = random.choice(list(dustbins.keys()))
    dustbin = random.choice(dustbins[street])
    fill_count = random.randint(1, 10)
    fill_time = round(random.uniform(2.0, 24.0), 2)
    arrival_time = round(random.uniform(1.0, 3.0), 2)
    date = datetime.now() - timedelta(days=random.randint(0, 30))
    pickup_time = date + timedelta(hours=fill_time)
    organic = random.randint(30, 60)
    plastic = random.randint(10, 40)
    metal = max(0, 100 - (organic + plastic))

    data.append({
        "Street": street,
        "Dustbin_ID": dustbin[0],
        "Latitude": dustbin[1],
        "Longitude": dustbin[2],
        "Fill_Count_Per_Day": fill_count,
        "Time_To_Fill_Hours": fill_time,
        "Time_To_Arrive_Hours": arrival_time,
        "Fill_Date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "Pickup_Date": pickup_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Organic_%": organic,
        "Plastic_%": plastic,
        "Metal_%": metal
    })

df = pd.DataFrame(data)
df.to_csv("C:\Users\Admin\OneDrive\Desktop\smart-dustbin-ai", index=False)
print("Sample data created!")
