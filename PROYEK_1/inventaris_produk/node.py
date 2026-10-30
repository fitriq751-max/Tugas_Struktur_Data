
class Node:
    """Satu simpul pada Linked List."""

    def __init__(self, id_produk, data_produk):
        self.id_produk = id_produk
        self.data_produk = data_produk
        self.next = None
