from .tree import Tree


def buat_data_contoh():
    organisasi = Tree()

    organisasi.insert_node(
        "ORG001", "Dr. Ahmad", "Rektor"
    )

    organisasi.insert_node(
        "ORG002", "Dr. Siti", "Dekan FST", "ORG001"
    )

    organisasi.insert_node(
        "ORG003", "Dr. Budi",
        "Dekan Fakultas Tarbiyah", "ORG001"
    )

    organisasi.insert_node(
        "ORG004", "M. Rafi",
        "Ketua Prodi Teknik Informatika", "ORG002"
    )

    organisasi.insert_node(
        "ORG005", "Nadia Putri",
        "Ketua Prodi Sistem Informasi", "ORG002"
    )

    organisasi.insert_node(
        "ORG006", "Andi Saputra",
        "Dosen Teknik Informatika", "ORG004"
    )

    organisasi.insert_node(
        "ORG007", "Dewi Lestari",
        "Staf Fakultas Tarbiyah", "ORG003"
    )

    return organisasi