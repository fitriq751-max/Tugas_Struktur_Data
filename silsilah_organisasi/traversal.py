def tampilkan_traversal(judul, daftar_node):
    print(f"\n{judul}")

    if not daftar_node:
        print("Tidak ada data.")
        return

    for nomor, node in enumerate(daftar_node, start=1):
        print(
            f"{nomor}. {node.nama} - {node.jabatan}"
        )