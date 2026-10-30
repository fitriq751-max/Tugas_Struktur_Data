
import time
import statistics

from linked_list import LinkedListProduk


def median_waktu(fungsi, percobaan=5):
    """Mengembalikan median waktu operasi dalam detik."""
    hasil = []

    for _ in range(percobaan):
        mulai = time.perf_counter()
        fungsi()
        selesai = time.perf_counter()

        hasil.append(selesai - mulai)

    return statistics.median(hasil)


def median_waktu_dengan_persiapan(persiapan, operasi, percobaan=5):
    """
    Menyiapkan salinan data di luar waktu yang diukur.
    Yang diukur hanya operasi yang diberikan pada parameter operasi.
    """
    hasil = []

    for _ in range(percobaan):
        data = persiapan()

        mulai = time.perf_counter()
        operasi(data)
        selesai = time.perf_counter()

        hasil.append(selesai - mulai)

    return statistics.median(hasil)


def buat_data_list(jumlah):
    return [
        {
            "id": f"PRD{i:06d}",
            "nama": f"Produk {i}",
            "harga": 1000.0 + i,
            "stok": 10
        }
        for i in range(jumlah)
    ]


def buat_data_dict(data_list):
    return {
        produk["id"]: {
            "nama": produk["nama"],
            "harga": produk["harga"],
            "stok": produk["stok"]
        }
        for produk in data_list
    }


def buat_linked_list(data_list):
    linked = LinkedListProduk()

    # Dibalik agar urutan ID sama dengan data sumber.
    for produk in reversed(data_list):
        data = {
            "nama": produk["nama"],
            "harga": produk["harga"],
            "stok": produk["stok"]
        }

        linked.tambah_produk(produk["id"], data)

    return linked


def benchmark():
    """Membandingkan waktu tambah, cari, dan hapus."""
    print("\n=== BENCHMARK: LIST vs LINKED LIST vs DICT ===")
    print("Waktu dalam detik; median dari 5 percobaan.")
    print("Persiapan/salinan data tidak dimasukkan ke waktu operasi.")
    print("Pencarian dan penghapusan menguji ID terakhir.\n")

    # Ukuran data yang diuji.
    for n in (1000, 10000, 50000):
        sumber_list = buat_data_list(n)
        sumber_dict = buat_data_dict(sumber_list)

        target = f"PRD{n - 1:06d}"
        id_baru = f"PRD{n:06d}"

        produk_list_baru = {
            "id": id_baru,
            "nama": "Produk Baru",
            "harga": 25000.0,
            "stok": 5
        }

        produk_dict_baru = {
            "nama": "Produk Baru",
            "harga": 25000.0,
            "stok": 5
        }

        # PENCARIAN
        cari_list = median_waktu(
            lambda: next(
                (p for p in sumber_list if p["id"] == target),
                None
            )
        )

        cari_linked = median_waktu_dengan_persiapan(
            lambda: buat_linked_list(sumber_list),
            lambda data: data.cari_produk(target)
        )

        cari_dict = median_waktu(
            lambda: sumber_dict.get(target)
        )

        # PENYISIPAN
        sisip_list = median_waktu_dengan_persiapan(
            lambda: sumber_list.copy(),
            lambda data: data.append(produk_list_baru.copy())
        )

        sisip_linked = median_waktu_dengan_persiapan(
            lambda: buat_linked_list(sumber_list),
            lambda data: data.tambah_produk(
                id_baru, produk_dict_baru.copy()
            )
        )

        sisip_dict = median_waktu_dengan_persiapan(
            lambda: sumber_dict.copy(),
            lambda data: data.__setitem__(
                id_baru, produk_dict_baru.copy()
            )
        )

        # PENGHAPUSAN
        hapus_list = median_waktu_dengan_persiapan(
            lambda: sumber_list.copy(),
            lambda data: hapus_produk_list_benchmark(data, target)
        )

        hapus_linked = median_waktu_dengan_persiapan(
            lambda: buat_linked_list(sumber_list),
            lambda data: data.hapus_produk(target)
        )

        hapus_dict = median_waktu_dengan_persiapan(
            lambda: sumber_dict.copy(),
            lambda data: data.pop(target, None)
        )

        # MENAMPILKAN HASIL
        print(f"JUMLAH DATA: {n:,}")
        print(
            f"{'Operasi':<14}"
            f"{'Python list':>16}"
            f"{'Linked List':>16}"
            f"{'dict':>16}"
        )

        print("-" * 62)

        print(
            f"{'Pencarian':<14}"
            f"{cari_list:>16.9f}"
            f"{cari_linked:>16.9f}"
            f"{cari_dict:>16.9f}"
        )

        print(
            f"{'Penyisipan':<14}"
            f"{sisip_list:>16.9f}"
            f"{sisip_linked:>16.9f}"
            f"{sisip_dict:>16.9f}"
        )

        print(
            f"{'Penghapusan':<14}"
            f"{hapus_list:>16.9f}"
            f"{hapus_linked:>16.9f}"
            f"{hapus_dict:>16.9f}"
        )

        print("-" * 62)

    print("\nCatatan: hasil waktu dapat berbeda tergantung laptop.")
    print("Gunakan hasil yang benar-benar tampil sebagai data laporan.")


def hapus_produk_list_benchmark(data_list, id_produk):
    """Menghapus produk dari list berdasarkan ID."""
    for indeks, produk in enumerate(data_list):
        if produk["id"] == id_produk:
            return data_list.pop(indeks)

    return None
