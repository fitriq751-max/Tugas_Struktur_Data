
from node import Node


class LinkedListProduk:
    """ADT Linked List sederhana untuk menyimpan produk."""

    def __init__(self):
        self.head = None
        self.jumlah = 0

    def tambah_produk(self, id_produk, data_produk):
        """Menambahkan produk di awal Linked List: O(1)."""
        node_baru = Node(id_produk, data_produk)
        node_baru.next = self.head
        self.head = node_baru
        self.jumlah += 1
        return True

    def cari_produk(self, id_produk):
        """Mencari produk berdasarkan ID: O(n)."""
        sekarang = self.head

        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                return sekarang.data_produk

            sekarang = sekarang.next

        return None

    def hapus_produk(self, id_produk):
        """Menghapus produk berdasarkan ID: O(n)."""
        sebelumnya = None
        sekarang = self.head

        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                if sebelumnya is None:
                    self.head = sekarang.next
                else:
                    sebelumnya.next = sekarang.next

                self.jumlah -= 1
                return sekarang.data_produk

            sebelumnya = sekarang
            sekarang = sekarang.next

        return None

    def kosong(self):
        return self.head is None

    def tampilkan_semua(self):
        sekarang = self.head

        while sekarang is not None:
            yield sekarang.id_produk, sekarang.data_produk
            sekarang = sekarang.next
