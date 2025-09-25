import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

#adding new row to be appended
new_row = {'Name': 'F1', 'Age': 20, 'City': 'C1'}

df.loc[len(df.index)] = new_row


data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')

df.to_csv(file_path, index=False)

print(f"CSV Saved to {file_path}")