#chuyển đổi giữa python và json
import json

json_data = '{"ten":"Luong", "tuoi":22, "datotnghiep":"false"}'
python_obj = json.loads(json_data)

print(python_obj["ten"])
print(python_obj)
