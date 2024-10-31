luong = float(input("Nhập lương nhân viên (triệu đồng): "))
thue = 0
luong_rong = 0
if luong > 15:
    thue = luong * 0.30
elif luong >= 7:
    thue = luong * 0.20
else:
    thue = luong * 0.10
luong_rong = luong - thue
print(f"Thuế thu nhập: {thue:.2f} triệu đồng")
print(f"Lương ròng: {luong_rong:.2f} triệu đồng")