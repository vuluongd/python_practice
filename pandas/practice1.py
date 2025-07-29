import pandas as pd

data = {
    'Ten':['An','Nam','Luong'],
    'Tuổi':[21,20,22],
    'Điểm':[8.8,8.5,8.0]
}
df = pd.DataFrame(data)
print(df)
df.info()
df.describe()