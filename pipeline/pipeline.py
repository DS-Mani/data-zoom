import sys

import pandas as pd
print('hello from pipeline.py')
print('sys.argv:', sys.argv)

day = int(sys.argv[1])
print(f'Running pipeline for day {day}')

df  = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
df['c'] = df['a'] + df['b']
print(df)
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f'output_Day)_{sys.argv[1]}.parquet')
# df.to_parquet(f"output_day_{sys.argv[1]}.parquet")