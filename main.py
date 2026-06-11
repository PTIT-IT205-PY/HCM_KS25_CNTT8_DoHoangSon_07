transactions = []

while True:
    print("\n========== QUẢN LÝ GIAO DỊCH TÀI CHÍNH ==========")
    print("1. Hiển thị nhật ký giao dịch")
    print("2. Ghi nhận giao dịch mới")
    print("3. Cập nhật chứng từ giao dịch")
    print("4. Xóa giao dịch lỗi")
    print("5. Tìm kiếm giao dịch")
    print("6. Thống kê tổng dòng tiền")
    print("7. Phân loại quy mô tự động")
    print("8. Thoát chương trình")
    print("=================================================")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        print("\n===== NHẬT KÝ GIAO DỊCH =====")

        if len(transactions) == 0:
            print("Danh sách giao dịch đang trống.")
        else:
            print("-" * 120)
            print(f"{'Mã TX':<10} | {'Nội dung':<30} | {'Loại':<6} | {'Số tiền':<15} | {'Thuế %':<8} | {'Thực tế':<15} | {'Quy mô':<10}")
            print("-" * 120)

            for gd in transactions:
                print(f"{gd['ma_tx']:<10} | {gd['noi_dung']:<30} | {gd['loai']:<6} | {gd['so_tien']:<15,.0f} | {gd['thue_suat']:<8} | {gd['so_tien_thuc_te']:<15,.0f} | {gd['quy_mo']:<10}")

            print("-" * 120)

    elif choice == "2":
        print("\n===== GHI NHẬN GIAO DỊCH MỚI =====")

        while True:
            ma_tx = input("Nhập mã giao dịch: ").strip()

            trung_ma = False

            for gd in transactions:
                if gd["ma_tx"] == ma_tx:
                    trung_ma = True

            if ma_tx == "":
                print("Mã giao dịch không được để trống.")
            elif trung_ma == True:
                print("Mã giao dịch không được trùng.")
            else:
                break

        while True:
            noi_dung = input("Nhập nội dung/lý do thu chi: ").strip()

            if noi_dung == "":
                print("Nội dung không được để trống.")
            else:
                break

        while True:
            loai = input("Nhập loại giao dịch Thu/Chi: ").strip().capitalize()

            if loai == "Thu" or loai == "Chi":
                break
            else:
                print("Loại giao dịch chỉ được nhập Thu hoặc Chi.")

        while True:
            so_tien_input = input("Nhập số tiền phát sinh: ").strip()

            if so_tien_input.replace(".", "", 1).isdigit():
                so_tien = float(so_tien_input)

                if so_tien > 0:
                    break
                else:
                    print("Số tiền phải lớn hơn 0.")
            else:
                print("Số tiền phải là số.")

        while True:
            thue_input = input("Nhập thuế suất (%): ").strip()

            if thue_input.replace(".", "", 1).isdigit():
                thue_suat = float(thue_input)

                if thue_suat >= 0:
                    break
                else:
                    print("Thuế suất phải lớn hơn hoặc bằng 0.")
            else:
                print("Thuế suất phải là số.")

        so_tien_thuc_te = so_tien * (1 + thue_suat / 100)

        if so_tien_thuc_te < 2000000:
            quy_mo = "Nhỏ"
        elif so_tien_thuc_te < 10000000:
            quy_mo = "Vừa"
        elif so_tien_thuc_te < 50000000:
            quy_mo = "Lớn"
        else:
            quy_mo = "Rất lớn"

        giao_dich = {
            "ma_tx": ma_tx,
            "noi_dung": noi_dung,
            "loai": loai,
            "so_tien": so_tien,
            "thue_suat": thue_suat,
            "so_tien_thuc_te": so_tien_thuc_te,
            "quy_mo": quy_mo
        }

        transactions.append(giao_dich)

        print("\nThêm giao dịch thành công.")
        print(f"Số tiền thực tế: {so_tien_thuc_te:,.0f} VNĐ")
        print(f"Phân loại quy mô: {quy_mo}")

    elif choice == "3":
        pass

    elif choice == "4":
        print("\n===== XÓA GIAO DỊCH LỖI =====")

        ma_tx = input("Nhập mã giao dịch cần xóa: ").strip()

        vi_tri = -1

        for i in range(len(transactions)):
            if transactions[i]["ma_tx"] == ma_tx:
                vi_tri = i

        if vi_tri == -1:
            print("Không tìm thấy mã giao dịch.")
        else:
            gd = transactions[vi_tri]

            print("\nThông tin giao dịch tìm thấy:")
            print(f"Mã TX: {gd['ma_tx']}")
            print(f"Nội dung: {gd['noi_dung']}")
            print(f"Loại: {gd['loai']}")
            print(f"Số tiền: {gd['so_tien']:,.0f}")
            print(f"Thuế suất: {gd['thue_suat']}")
            print(f"Số tiền thực tế: {gd['so_tien_thuc_te']:,.0f}")
            print(f"Quy mô: {gd['quy_mo']}")

            confirm = input("Bạn có chắc muốn xóa giao dịch này không? (Y/N): ").strip().upper()

            if confirm == "Y":
                transactions.pop(vi_tri)
                print("Xóa giao dịch thành công.")
            else:
                print("Đã hủy thao tác xóa.")

    elif choice == "5":
        print("\n===== TÌM KIẾM GIAO DỊCH =====")
        print("1. Tìm chính xác theo mã TX")
        print("2. Tìm gần đúng theo nội dung")

        search_choice = input("Nhập lựa chọn: ").strip()

        ket_qua = []

        if search_choice == "1":
            ma_tx = input("Nhập mã TX cần tìm: ").strip()

            for gd in transactions:
                if gd["ma_tx"] == ma_tx:
                    ket_qua.append(gd)

        elif search_choice == "2":
            keyword = input("Nhập nội dung cần tìm: ").strip().lower()

            for gd in transactions:
                if keyword in gd["noi_dung"].lower():
                    ket_qua.append(gd)

        else:
            print("Lựa chọn không hợp lệ.")

        if search_choice == "1" or search_choice == "2":
            if len(ket_qua) == 0:
                print("Không tìm thấy giao dịch phù hợp.")
            else:
                print("\n===== KẾT QUẢ TÌM KIẾM =====")
                print("-" * 120)
                print(f"{'Mã TX':<10} | {'Nội dung':<30} | {'Loại':<6} | {'Số tiền':<15} | {'Thuế %':<8} | {'Thực tế':<15} | {'Quy mô':<10}")
                print("-" * 120)

                for gd in ket_qua:
                    print(f"{gd['ma_tx']:<10} | {gd['noi_dung']:<30} | {gd['loai']:<6} | {gd['so_tien']:<15,.0f} | {gd['thue_suat']:<8} | {gd['so_tien_thuc_te']:<15,.0f} | {gd['quy_mo']:<10}")

                print("-" * 120)

    elif choice == "6":
        pass

    elif choice == "7":
        pass

    elif choice == "8":
        print("\nCảm ơn bạn đã sử dụng chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ.")