import pandas as pd
import requests

# Create a session object for making requests
session = requests.Session()

# Collection url
directus_instance = "http://directus.dbgi.org"
directus_collection = f"{directus_instance}/items/Labels/?limit=-1"

response = session.get(url=directus_collection)

data = response.json()["data"]
df_data = []
for i in range(len(data)):
    df_data.append(data[i])

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(df_data)
df = df.rename(columns={"field_sample_id": "container_id"})
print(df)
