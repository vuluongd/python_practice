import sqlite3
import pandas as pd 
# Kết nối (tạo database file test.db)
conn = sqlite3.connect("test.db")
# Xóa bảng cũ nếu có
conn.execute("DROP TABLE IF EXISTS NhanVien")


#tạo bảng
conn.execute("""
CREATE TABLE IF NOT EXISTS NhanVien(
    id INTEGER PRIMAMY KEY,
    ten TEXT,
    phongban TEXT,
    luong REAL)
""")

#thêm dữ liệu
conn.execute("INSERT INTO NhanVien(ten, phongban, luong) VALUES (?, ?, ?)",("An", "IT", 1500))
conn.execute("INSERT INTO NhanVien(ten, phongban, luong) VALUES (?, ?, ?)",("Bình", "Kế toán", 1200))
conn.commit()

df = pd.read_sql_query("SELECT * FROM NhanVien", conn)
print(df)

conn.close()
