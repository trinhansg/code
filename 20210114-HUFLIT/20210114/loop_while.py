while True:
    print(" ==== currency exchange ===")
    usd = input("Nhap so tien usd: ")
    tygia = input("Nhap ty gia: ")
    vnd = float(usd) * float(tygia)
    print(f"Ket qua: VND{vnd:,.2f}")
    answer = input("Ban co muon tiep tuc khong (y/n)? ")
    if answer == 'n':
        break