import unittest
import sistem_antrean_undo


# ==============================
# UNIT TESTING QUEUE / ANTREAN
# ==============================

class TestAntrean(unittest.TestCase):

    def setUp(self):
        sistem_antrean_undo.queue_antrean.clear()

    def test_penambahan_data(self):
        sistem_antrean_undo.tambah_antrean("Andi")

        self.assertEqual(
            list(sistem_antrean_undo.queue_antrean),
            ["Andi"]
        )

    def test_penghapusan_data(self):
        sistem_antrean_undo.tambah_antrean("Andi")
        sistem_antrean_undo.tambah_antrean("Budi")

        sistem_antrean_undo.hapus_antrean()

        self.assertEqual(
            list(sistem_antrean_undo.queue_antrean),
            ["Budi"]
        )

    def test_melihat_data_terdepan(self):
        sistem_antrean_undo.tambah_antrean("Andi")
        sistem_antrean_undo.tambah_antrean("Budi")

        self.assertEqual(
            sistem_antrean_undo.queue_antrean[0],
            "Andi"
        )

    def test_memeriksa_kondisi_kosong(self):
        self.assertEqual(
            len(sistem_antrean_undo.queue_antrean),
            0
        )


# ==============================
# UNIT TESTING STACK / UNDO
# ==============================

class TestUndo(unittest.TestCase):

    def setUp(self):
        sistem_antrean_undo.stack_undo.clear()

    def test_penambahan_data(self):
        sistem_antrean_undo.tambah_aktivitas("Login ke sistem")

        self.assertEqual(
            sistem_antrean_undo.stack_undo,
            ["Login ke sistem"]
        )

    def test_penghapusan_data(self):
        sistem_antrean_undo.tambah_aktivitas("Login ke sistem")
        sistem_antrean_undo.tambah_aktivitas(
            "Menambahkan data mahasiswa"
        )

        sistem_antrean_undo.undo_aktivitas()

        self.assertEqual(
            sistem_antrean_undo.stack_undo,
            ["Login ke sistem"]
        )

    def test_melihat_data_teratas(self):
        sistem_antrean_undo.tambah_aktivitas("Login ke sistem")
        sistem_antrean_undo.tambah_aktivitas(
            "Menambahkan data mahasiswa"
        )

        self.assertEqual(
            sistem_antrean_undo.stack_undo[-1],
            "Menambahkan data mahasiswa"
        )

    def test_memeriksa_kondisi_kosong(self):
        self.assertEqual(
            len(sistem_antrean_undo.stack_undo),
            0
        )


# ==============================
# MENJALANKAN UNIT TEST
# ==============================

if __name__ == "__main__":
    unittest.main()