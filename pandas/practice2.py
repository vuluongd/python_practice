import pandas as pd
data = {
    'Ten':['An','Nam','Luong','Huy'],
    'Lop':['K66','K66','K66',"K65"],
    'Diem':[8.7,8.3,8.2,7.8]
}
df = pd.DataFrame(data)

print(df['Ten'])
print(df[df['Diem']>8])
