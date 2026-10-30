
class Node:
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = str(id_pegawai)
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def __str__(self):
        return (
            f"ID: {self.id_pegawai} | "
            f"Nama: {self.nama} | "
            f"Jabatan: {self.jabatan}"
        )
