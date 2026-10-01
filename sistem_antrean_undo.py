from collections import deque

queue_antrean = deque()
stack_undo = []


# ==============================
# OPERASI QUEUE / ANTREAN
# ==============================

def tambah_antrean(nama):
    queue_antrean.append(nama)
    print(f"Mahasiswa '{nama}' berhasil ditambahkan ke antrean.")


def hapus_antrean():
    if len(queue_antrean) == 0:
        print("Antrean kosong.")
    else:
        mahasiswa = queue_antrean.popleft()
        print(f"Mahasiswa yang dilayani: {mahasiswa}")


def lihat_antrean_depan():
    if len(queue_antrean) == 0:
        print("Antrean kosong.")
    else:
        print(f"Mahasiswa paling depan: {queue_antrean[0]}")


def cek_antrean_kosong():
    if len(queue_antrean) == 0:
        print("Antrean kosong.")
    else:
        print("Antrean tidak kosong.")


# ==============================
# OPERASI STACK / UNDO
# ==============================

def tambah_aktivitas(aktivitas):
    stack_undo.append(aktivitas)
    print(f"Aktivitas '{aktivitas}' berhasil ditambahkan.")


def undo_aktivitas():
    if len(stack_undo) == 0:
        print("Tidak ada aktivitas yang dapat di-undo.")
    else:
        aktivitas = stack_undo.pop()
        print(f"Aktivitas yang dibatalkan: {aktivitas}")


def lihat_aktivitas_teratas():
    if len(stack_undo) == 0:
        print("Stack kosong.")
    else:
        print(f"Aktivitas terakhir: {stack_undo[-1]}")


def cek_stack_kosong():
    if len(stack_undo) == 0:
        print("Stack kosong.")
    else:
        print("Stack tidak kosong.")


# ==============================
# MENU UTAMA
# ==============================

def menu_utama():
    while True:
        print("\n==========================================")
        print("     SISTEM LAYANAN ADMINISTRASI")
        print("==========================================")
        print("1. Tambah mahasiswa ke antrean")
        print("2. Layani mahasiswa terdepan")
        print("3. Lihat mahasiswa terdepan")
        print("4. Cek antrean kosong")
        print("------------------------------------------")
        print("5. Tambah aktivitas")
        print("6. Undo aktivitas")
        print("7. Lihat aktivitas teratas")
        print("8. Cek Stack kosong")
        print("------------------------------------------")
        print("9. Keluar")
        print("==========================================")

        pilihan = input("Pilih menu (1-9): ")

        if pilihan == "1":
            nama = input("Masukkan nama mahasiswa: ")
            tambah_antrean(nama)

        elif pilihan == "2":
            hapus_antrean()

        elif pilihan == "3":
            lihat_antrean_depan()

        elif pilihan == "4":
            cek_antrean_kosong()

        elif pilihan == "5":
            aktivitas = input("Masukkan aktivitas: ")
            tambah_aktivitas(aktivitas)

        elif pilihan == "6":
            undo_aktivitas()

        elif pilihan == "7":
            lihat_aktivitas_teratas()

        elif pilihan == "8":
            cek_stack_kosong()

        elif pilihan == "9":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    menu_utama()