
def cari_produk_list(data_list, id_produk):
    """Mencari produk berdasarkan ID menggunakan Python List."""
    for produk in data_list:
        if produk["id"] == id_produk:
            return produk

    return None


def hapus_produk_list(data_list, id_produk):
    """Menghapus produk berdasarkan ID menggunakan Python List."""
    for indeks, produk in enumerate(data_list):
        if produk["id"] == id_produk:
            return data_list.pop(indeks)

    return None
