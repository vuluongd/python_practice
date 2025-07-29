import pandas as pd
data = {
    'Ten':['An','Nam','Luong','Huy','Quoc_Anh'],
    'Diem':['7.8','7.9','8.5','9','4'],
    'Lop':['K66','K66','K66','K66','K66']
}
df = pd.DataFrame(data)

df['Diem'] = df['Diem'].astype(float)
def xeploai(diem):
    if diem >= 8.5:
        return "Good"
    elif diem>=7:
        return "Credit"
    else:
        return "medium"
df['xếp loại']= df['Diem'].apply(xeploai)
print(df)