
from .node import Node


class Tree:
    def __init__(self):
        self.root = None

    # INSERT NODE: menambahkan pegawai
    def insert_node(
        self, id_pegawai, nama, jabatan, id_atasan=None
    ):
        if not id_pegawai or not nama or not jabatan:
            print("Gagal: ID, nama, dan jabatan wajib diisi.")
            return False

        id_pegawai = str(id_pegawai).strip()
        nama = nama.strip()
        jabatan = jabatan.strip()

        if not id_pegawai or not nama or not jabatan:
            print("Gagal: data tidak boleh kosong.")
            return False

        if self.root is None:
            if id_atasan is not None:
                print("Gagal: tambahkan root terlebih dahulu.")
                return False

            self.root = Node(id_pegawai, nama, jabatan)
            print("Root berhasil ditambahkan.")
            return True

        if self.search_by_id(id_pegawai) is not None:
            print("Gagal: ID pegawai sudah digunakan.")
            return False

        if id_atasan is None:
            print("Gagal: ID atasan harus diisi.")
            return False

        atasan = self.search_by_id(id_atasan)

        if atasan is None:
            print("Gagal: data atasan tidak ditemukan.")
            return False

        node_baru = Node(id_pegawai, nama, jabatan)
        atasan.children.append(node_baru)

        print(
            f"Pegawai {nama} berhasil ditambahkan "
            f"di bawah {atasan.nama}."
        )
        return True

    # SEARCH BERDASARKAN ID
    def search_by_id(self, id_pegawai):
        if self.root is None:
            return None

        target = str(id_pegawai).strip()
        stack = [self.root]

        while stack:
            node = stack.pop()

            if node.id_pegawai == target:
                return node

            stack.extend(reversed(node.children))

        return None

    # SEARCH BERDASARKAN NAMA ATAU JABATAN
    def search_node(self, kata_kunci):
        hasil = []

        if self.root is None or not kata_kunci.strip():
            return hasil

        kata_kunci = kata_kunci.strip().casefold()
        stack = [self.root]

        while stack:
            node = stack.pop()

            if (
                kata_kunci in node.nama.casefold()
                or kata_kunci in node.jabatan.casefold()
            ):
                hasil.append(node)

            stack.extend(reversed(node.children))

        return hasil

    # PREORDER TRAVERSAL
    def preorder_traversal(self, node=None, hasil=None):
        if hasil is None:
            hasil = []

        if node is None:
            node = self.root

        if node is None:
            return hasil

        hasil.append(node)

        for anak in node.children:
            self.preorder_traversal(anak, hasil)

        return hasil

    # INORDER KHUSUS GENERAL TREE
    def inorder_traversal(self, node=None, hasil=None):
        if hasil is None:
            hasil = []

        if node is None:
            node = self.root

        if node is None:
            return hasil

        if node.children:
            self.inorder_traversal(node.children[0], hasil)

        hasil.append(node)

        for anak in node.children[1:]:
            self.inorder_traversal(anak, hasil)

        return hasil

    # POSTORDER TRAVERSAL
    def postorder_traversal(self, node=None, hasil=None):
        if hasil is None:
            hasil = []

        if node is None:
            node = self.root

        if node is None:
            return hasil

        for anak in node.children:
            self.postorder_traversal(anak, hasil)

        hasil.append(node)

        return hasil

    # MENAMPILKAN STRUKTUR TREE
    def tampilkan_struktur(self, node=None, level=0):
        if node is None:
            node = self.root

        if node is None:
            print("Struktur organisasi masih kosong.")
            return

        print(
            "    " * level
            + f"|-- {node.nama} ({node.jabatan}) "
            + f"[{node.id_pegawai}]"
        )

        for anak in node.children:
            self.tampilkan_struktur(anak, level + 1)
