songs = []

def add_song():
    pass

def view_playlist():
    pass

def search_by_artist():
    pass

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

def add_song():
    print("\n--- Thêm bài hát mới ---")
    title = input("Tên bài hát: ")
    artist = input("Tên ca sĩ: ")
    # Bắt lỗi khi nhập số (tránh crash nếu người dùng nhập chữ)
    while True:
        dur = input("Thời lượng (giây): ")
        if dur.isdigit():
            duration = int(dur)
            break
        else:
            print("Vui lòng nhập số nguyên (ví dụ: 240).")
    songs.append({'title': title, 'artist': artist, 'duration': duration})
    print("Đã thêm bài hát vào playlist!")

def view_playlist():
# Duyệt list songs và in ra
# Ví dụ: 1. Lạc Trôi - Sơn Tùng MTP (240s)
pass