#%%
import matplotlib.pyplot as plt
import pandas as pd
 

# %%
df = pd.read_excel('house_price_dống-da.xlsx')
df = df.dropna()
df.info()
# %%
#Phân tích mối liên hệ giữa diện tích với giá nhà. Đồng thời, giữa số phòng ngủ với giá nhà và giữa số toilet với giá nhà.
df_1 = df[['price','area','bedroom','toilet']]
df_1 = df_1.set_index(['price'])
df_1=df_1.sort_values(by=['price'])
df_1 = df_1.reset_index()
df_1
# %%
plt.plot(df_1['area'],df['price'])
plt.show()
plt.plot(df_1['area'],df['bedroom'])
plt.show()
plt.plot(df_1['area'],df['toilet'])
plt.show()
# %%
