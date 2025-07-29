import pandas as pd
import numpy as np

data ={
    'Ten':['An','Nam','Luong','Huy','Quoc_Anh'],
    'Lop':['K66','K66','K66','K66','K66'],
    'Dai_so':[8.5,8.4,np.nan,np.nan,7.8],
    'Giai_tich':[8.0,8.0,np.nan,8.4,8.1],
    'Thuat_toan':[7.5,7.4,7.2,8.0,8.0]
}
df = pd.DataFrame(data)
print (df)
df_filled = df.fillna(df.mean(numeric_only=True))
print(df_filled)
df_dropped = df.dropna()
print("\n🗑️ DataFrame sau khi xoá các dòng chứa NaN:")
print(df_dropped)