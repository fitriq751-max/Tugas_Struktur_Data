
class InventarisProduk:
    """
    ADT inventaris dengan dict sebagai struktur data utama.
    Key dict adalah ID produk agar produk mudah ditemukan.
    """

    def __init__(self):
        self.produk = {}

    def tambah_produk(self, id_produk, nama, harga, stok):
        """Menyisipkan produk. Kompleksitas rata-rata: O(1)."""
        if id_produk in self.produk:
            return False, "ID produk sudah terdaftar."

        self.produk[id_produk] = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }

        return True, "Produk berhasil ditambahkan."

    def cari_produk(self, id_produk):
        """Mencari produk berdasarkan ID. Kompleksitas rata-rata: O(1)."""
        return self.produk.get(id_produk)

    def hapus_produk(self, id_produk):
        """Menghapus produk berdasarkan ID. Kompleksitas rata-rata: O(1)."""
        return self.produk.pop(id_produk, None)

    def tampilkan_produk(self):
        if not self.produk:
            print("Inventaris masih kosong.")
            return

        print("\n=== DAFTAR INVENTARIS PRODUK ===")

        for id_produk, data in self.produk.items():
            print(
                f"ID: {id_produk} | Nama: {data['nama']} | "
                f"Harga: Rp{data['harga']:,.2f} | Stok: {data['stok']}"
            )
