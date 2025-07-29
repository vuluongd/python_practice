#cập nhật một dictionary
drone_info = {
    "id": 1,
    "position": (0, 0,0),
    "status": "iddle",
}

drone_info["battery"] = 95

drone_info["status"] = "flying"

del drone_info["position"]

print(drone_info)