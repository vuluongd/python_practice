import pandas as pd
import numpy as np

angles = np.linspace(0,2*np.pi,100)
sheets = {
    "Circle_10":pd.DataFrame({
        'x':10*np.cos(angles),
        'y':10*np.sin(angles)
    }),
    "Circle_5":pd.DataFrame({
        'x':5*np.cos(angles),
        'y':5*np.cos(angles)
    }),
    "Spiral":pd.DataFrame({
        'x':angles*np.cos(angles),
        'y':angles*np.sin(angles)
    })
}

with pd.ExcelWriter("multi_position_sheet.xlsx") as writer:
    for name, df in sheets.items():
        df.to_excel(writer, sheet_name=name, index=False)
