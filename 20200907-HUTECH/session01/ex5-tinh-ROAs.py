lai_rong_list = []
tong_tai_san_list = []
for i in range(5):
    lai_rong = float(input(f"Nhap lai rong cua nam {i}: "))
    tong_tai_san = float(input(f"Nhap tong tai san cua nam {i}: "))
    # Them lai_rong vao lai_rong_list
    lai_rong_list.append(lai_rong)
    # Them tong_tai_san vao tong_tai_san_list
    tong_tai_san_list.append(tong_tai_san)
print("Danh sach lai rong: ")
print(lai_rong_list)
print("Danh sach tai san: ")
print(tong_tai_san_list)
