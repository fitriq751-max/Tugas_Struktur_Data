
from inventaris import InventarisProduk
from benchmark import benchmark


def main():
    inventaris = InventarisProduk()

    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS PRODUK ===")
        print("1. Tambah produk")
        print("2. Cari produk berdasarkan ID")
        print("3. Hapus produk berdasarkan ID")
        print("4. Tampilkan semua produk")
        print("5. Bandingkan list, Linked List, dan dict")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            id_produk = input("ID Produk: ").strip()
            nama = input("Nama Produk: ").strip()

            try:
                harga = float(input("Harga Produk: "))
                stok = int(input("Stok Produk: "))

                if not id_produk or not nama:
                    print("ID dan nama produk tidak boleh kosong.")

                elif harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif.")

                else:
                    berhasil, pesan = inventaris.tambah_produk(
                        id_produk, nama, harga, stok
                    )
                    print(pesan)

            except ValueError:
                print(
                    "Input tidak valid. Harga harus angka "
                    "dan stok bilangan bulat."
                )

        elif pilihan == "2":
            id_produk = input("Masukkan ID yang dicari: ").strip()
            data = inventaris.cari_produk(id_produk)

            if data is None:
                print("Produk tidak ditemukan.")

            else:
                print("\n=== DETAIL PRODUK ===")
                print("ID Produk :", id_produk)
                print("Nama      :", data["nama"])
                print(f"Harga     : Rp{data['harga']:,.2f}")
                print("Stok      :", data["stok"])

        elif pilihan == "3":
            id_produk = input("Masukkan ID yang dihapus: ").strip()
            data = inventaris.hapus_produk(id_produk)

            if data is None:
                print("Produk tidak ditemukan.")

            else:
                print(
                    f"Produk '{data['nama']}' berhasil dihapus."
                )

        elif pilihan == "4":
            inventaris.tampilkan_produk()

        elif pilihan == "5":
            benchmark()

        elif pilihan == "6":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")


if __name__ == "__main__":
    main()
