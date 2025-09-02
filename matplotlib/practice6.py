import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile("multi_position_sheet.xlsx")

chosen_sheet = input("Nhap_sheet ")

df = xls.parse(chosen_sheet)

plt.plot(df['x'],df['y'],label=chosen_sheet)
plt.title(f"plot từ sheet: {chosen_sheet}")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()