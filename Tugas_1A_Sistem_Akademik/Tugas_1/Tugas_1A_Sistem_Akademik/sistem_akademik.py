from collections import deque

# ==========================================
# DATA MAHASISWA
# Menggunakan List (Array)
# ==========================================

mahasiswa = [
    {"nim": "12550120344", "nama": "Fitri Khairani Sitorus", "prodi": "Teknik Informatika"},
    {"nim": "12550120345", "nama": "Ahmad Fauzan", "prodi": "Teknik Informatika"},
    {"nim": "12550120346", "nama": "Siti Aisyah", "prodi": "Teknik Informatika"}
]


# ==========================================
# STACK UNTUK FITUR UNDO
# ==========================================

stack_undo = []


# ==========================================
# QUEUE UNTUK ANTREAN
# ==========================================

queue = deque()


# ==========================================
# 1. MENAMPILKAN DATA MAHASISWA
# ==========================================

def tampilkan_mahasiswa():
    print("\n=== DATA MAHASISWA ===")

    for mhs in mahasiswa:
        print("NIM   :", mhs["nim"])
        print("Nama  :", mhs["nama"])
        print("Prodi :", mhs["prodi"])
        print("-" * 30)


# ==========================================
# 2. MENCARI MAHASISWA BERDASARKAN NIM
# Menggunakan Linear Search
# ==========================================

def cari_mahasiswa():
    nim_dicari = input("\nMasukkan NIM yang ingin dicari: ")

    ditemukan = False

    for mhs in mahasiswa:
        if mhs["nim"] == nim_dicari:
            print("\nData mahasiswa ditemukan!")
            print("NIM   :", mhs["nim"])
            print("Nama  :", mhs["nama"])
            print("Prodi :", mhs["prodi"])
            ditemukan = True
            break

    if not ditemukan:
        print("\nMahasiswa tidak ditemukan.")


# ==========================================
# 3. MENAMBAHKAN AKTIVITAS
# Menggunakan Stack
# ==========================================

def tambah_aktivitas():
    aktivitas = input("\nMasukkan aktivitas: ")

    # Push ke Stack
    stack_undo.append(aktivitas)

    print("Aktivitas berhasil ditambahkan.")


# ==========================================
# 4. UNDO AKTIVITAS
# Menggunakan Stack
# ==========================================

def undo_aktivitas():

    if len(stack_undo) == 0:
        print("\nTidak ada aktivitas yang dapat di-undo.")
    else:
        # Pop dari Stack
        aktivitas = stack_undo.pop()

        print("\nAktivitas dibatalkan:", aktivitas)


# ==========================================
# 5. MENAMBAHKAN ANTREAN
# Menggunakan Queue
# ==========================================

def tambah_antrean():
    nama = input("\nMasukkan nama mahasiswa: ")

    # Enqueue
    queue.append(nama)

    print("Mahasiswa berhasil masuk antrean.")


# ==========================================
# 6. MEMPROSES ANTREAN
# Menggunakan Queue
# ==========================================

def proses_antrean():

    if len(queue) == 0:
        print("\nAntrean kosong.")
    else:
        # Dequeue
        mahasiswa_diproses = queue.popleft()

        print("\nMemproses mahasiswa:", mahasiswa_diproses)


# ==========================================
# PROGRAM UTAMA
# ==========================================

while True:

    print("\n================================")
    print("       SISTEM AKADEMIK")
    print("================================")
    print("1. Lihat Data Mahasiswa")
    print("2. Cari Mahasiswa")
    print("3. Tambah Aktivitas")
    print("4. Undo Aktivitas")
    print("5. Tambah Antrean")
    print("6. Proses Antrean")
    print("7. Keluar")
    print("================================")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        tampilkan_mahasiswa()

    elif pilihan == "2":
        cari_mahasiswa()

    elif pilihan == "3":
        tambah_aktivitas()

    elif pilihan == "4":
        undo_aktivitas()

    elif pilihan == "5":
        tambah_antrean()

    elif pilihan == "6":
        proses_antrean()

    elif pilihan == "7":
        print("\nProgram selesai. Terima kasih.")
        break

    else:
        print("\nPilihan tidak valid.")
