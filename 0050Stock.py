import pandas as pd
df = pd.read_json('https://www.yuantaetfs.com/api/Stkweights?date=&fundid=1066')
print(df['code'])