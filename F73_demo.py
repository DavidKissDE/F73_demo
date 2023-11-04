# %
import pandas as pd
df = pd.read_csv("data.csv")
df.columns # 'country', 'year', 'population', 'continent', 'life_exp', 'gdp_cap'
# %

df.loc[:,["country", "life_exp", "gdp_cap"]]