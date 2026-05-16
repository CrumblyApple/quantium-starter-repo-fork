import pandas as pd
import glob

files = glob.glob('data/daily_sales_data_*.csv')
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs, ignore_index=True)

df = df[df['product'] == 'pink morsel']
df['sales'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float) * df['quantity']
df = df[['sales', 'date', 'region']]
df.to_csv('data/daily_sales_data.csv', index=False)
