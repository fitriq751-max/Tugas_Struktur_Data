
from .data_organisasi import buat_data_contoh
from .traversal import tampilkan_traversal


def main():
    organisasi = buat_data_contoh()

    while True:
        print("\n" + "=" * 52)
        print(" SISTEM MANAJEMEN SILSILAH ORGANISASI")
        print("=" * 52)
        print("1. Tampilkan struktur organisasi")
        print("2. Tambah pegawai atau jabatan")
        print("3. Cari pegawai")
        print("4. Preorder Traversal")
        print("5. Inorder Traversal")
        print("6. Postorder Traversal")
        print("7. Tampilkan semua traversal")
        print("8. Keluar")
        print("=" * 52)

        pilihan = input("Pilih menu (1-8): ").strip()

        if pilihan == "1":
            print("\nSTRUKTUR ORGANISASI")
            organisasi.tampilkan_struktur()

        elif pilihan == "2":
            print("\nTAMBAH PEGAWAI/JABATAN")

            id_pegawai = input("ID pegawai: ").strip()
            nama = input("Nama pegawai: ").strip()
            jabatan = input("Jabatan: ").strip()
            id_atasan = input(
                "ID atasan (kosongkan hanya jika membuat root): "
            ).strip()

            organisasi.insert_node(
                id_pegawai,
                nama,
                jabatan,
                id_atasan if id_atasan else None
            )

        elif pilihan == "3":
            kata_kunci = input(
                "Masukkan nama atau jabatan: "
            ).strip()

            hasil = organisasi.search_node(kata_kunci)

            if hasil:
                print(f"\nDitemukan {len(hasil)} hasil:")

                for node in hasil:
                    print(node)
            else:
                print("Data pegawai tidak ditemukan.")

        elif pilihan == "4":
            tampilkan_traversal(
                "HASIL PREORDER TRAVERSAL",
                organisasi.preorder_traversal()
            )

        elif pilihan == "5":
            tampilkan_traversal(
                "HASIL INORDER TRAVERSAL "
                "(ATURAN KHUSUS GENERAL TREE)",
                organisasi.inorder_traversal()
            )

        elif pilihan == "6":
            tampilkan_traversal(
                "HASIL POSTORDER TRAVERSAL",
                organisasi.postorder_traversal()
            )

        elif pilihan == "7":
            tampilkan_traversal(
                "PREORDER TRAVERSAL",
                organisasi.preorder_traversal()
            )

            tampilkan_traversal(
                "INORDER TRAVERSAL "
                "(ATURAN KHUSUS GENERAL TREE)",
                organisasi.inorder_traversal()
            )

            tampilkan_traversal(
                "POSTORDER TRAVERSAL",
                organisasi.postorder_traversal()
            )

        elif pilihan == "8":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-8.")


if __name__ == "__main__":
    main()
