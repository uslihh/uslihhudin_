# PROJECT SISTEM KASIR SEDERHANA

# CLASS PRODUK
class Produk:

    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # PROPERTY GETTER NAMA
    @property
    def nama(self):
        return self.__nama

    # PROPERTY SETTER NAMA
    @nama.setter
    def nama(self, nama_baru):
        if nama_baru.strip() == "":
            raise ValueError("Nama produk tidak boleh kosong!")
        self.__nama = nama_baru

    # PROPERTY GETTER HARGA
    @property
    def harga(self):
        return self.__harga

    # PROPERTY SETTER HARGA
    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga harus lebih dari 0!")
        self.__harga = harga_baru

    # PROPERTY GETTER STOK
    @property
    def stok(self):
        return self.__stok

    # METHOD MENGURANGI STOK
    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            raise ValueError("Stok tidak mencukupi!")
        self.__stok -= jumlah

    # CLASS METHOD
    @classmethod
    def dari_data(cls, data):
        return cls(
            data["nama"],
            data["harga"],
            data["stok"]
        )


# CLASS KASIR
class Kasir:

    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.__keranjang = {}
        self.__total = 0

    # STATIC METHOD
    @staticmethod
    def format_rupiah(angka):
        return "Rp {:,}".format(angka).replace(",", ".")

    # METHOD MENAMPILKAN PRODUK
    def tampilkan_produk(self, daftar_produk):
        print("\n========== DAFTAR PRODUK ==========")

        for i, produk in enumerate(daftar_produk, start=1):
            print(
                f"{i}. {produk.nama}"
                f" | Harga: {self.format_rupiah(produk.harga)}"
                f" | Stok: {produk.stok}"
            )

        print("===================================")

    # METHOD MENAMBAHKAN PRODUK
    def tambah_produk(self, produk, jumlah):

        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0!")
            return

        if jumlah > produk.stok:
            print("Maaf, stok produk tidak mencukupi!")
            return

        produk.kurangi_stok(jumlah)

        if produk not in self.__keranjang:
            self.__keranjang[produk] = 0

        self.__keranjang[produk] += jumlah

        print(f"{produk.nama} berhasil ditambahkan ke keranjang!")

    # METHOD MENAMPILKAN KERANJANG
    def tampilkan_keranjang(self):

        print("\n============ KERANJANG ============")

        if not self.__keranjang:
            print("Keranjang masih kosong!")
            return

        self.__total = 0

        for produk, jumlah in self.__keranjang.items():

            subtotal = produk.harga * jumlah
            self.__total += subtotal

            print(f"Produk  : {produk.nama}")
            print(f"Jumlah  : {jumlah}")
            print(f"Subtotal: {self.format_rupiah(subtotal)}")
            print("-----------------------------------")

        print(f"TOTAL BELANJA: {self.format_rupiah(self.__total)}")
        print("===================================")

    # METHOD CHECKOUT / PEMBAYARAN
    def checkout(self):

        if not self.__keranjang:
            print("Keranjang masih kosong!")
            return

        self.tampilkan_keranjang()

        print("\n========== PEMBAYARAN ==========")

        print("Total:", self.format_rupiah(self.__total))

        while True:
            try:
                uang = int(input("Masukkan uang pembayaran: Rp "))

                if uang < 0:
                    print("Pembayaran tidak boleh negatif!")
                    continue

                if uang < self.__total:
                    print("Uang pembayaran kurang!")
                    continue

                break

            except ValueError:
                print("Masukkan nominal berupa angka!")

        kembalian = uang - self.__total

        # MENAMPILKAN STRUK
        print("\n========== STRUK PEMBELIAN ==========")
        print("Kasir:", self.nama_kasir)
        print("-------------------------------------")

        for produk, jumlah in self.__keranjang.items():
            subtotal = produk.harga * jumlah

            print(f"{produk.nama} x {jumlah}")
            print(f"Subtotal: {self.format_rupiah(subtotal)}")

        print("-------------------------------------")
        print("Total     :", self.format_rupiah(self.__total))
        print("Bayar     :", self.format_rupiah(uang))
        print("Kembalian :", self.format_rupiah(kembalian))
        print("=====================================")
        print("Terima kasih sudah berbelanja!")

        # MENGOSONGKAN KERANJANG
        self.__keranjang.clear()
        self.__total = 0


# ==========================================
# PROGRAM UTAMA
# ==========================================

# DATA PRODUK
data_produk = [
    {"nama": "Indomie Goreng", "harga": 3500, "stok": 50},
    {"nama": "Aqua 600ml", "harga": 4000, "stok": 40},
    {"nama": "Roti Coklat", "harga": 5000, "stok": 30},
    {"nama": "Chitato", "harga": 10000, "stok": 20},
    {"nama": "Susu Ultra", "harga": 7000, "stok": 25}
]

# MEMBUAT OBJECT PRODUK MENGGUNAKAN CLASS METHOD
daftar_produk = [
    Produk.dari_data(data) for data in data_produk
]

# MEMBUAT OBJECT KASIR
kasir = Kasir("Uslihhudin")


# MENU UTAMA
while True:

    print("\n===================================")
    print("       APLIKASI SISTEM KASIR")
    print("===================================")
    print("1. Lihat Daftar Produk")
    print("2. Tambah Produk ke Keranjang")
    print("3. Lihat Keranjang")
    print("4. Pembayaran / Checkout")
    print("5. Keluar")
    print("===================================")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":

        kasir.tampilkan_produk(daftar_produk)

    elif pilihan == "2":

        kasir.tampilkan_produk(daftar_produk)

        try:
            nomor = int(input("Pilih nomor produk: "))

            if nomor < 1 or nomor > len(daftar_produk):
                print("Nomor produk tidak tersedia!")
                continue

            jumlah = int(input("Masukkan jumlah pembelian: "))

            kasir.tambah_produk(
                daftar_produk[nomor - 1],
                jumlah
            )

        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "3":

        kasir.tampilkan_keranjang()

    elif pilihan == "4":

        kasir.checkout()

    elif pilihan == "5":

        print("\nTerima kasih telah menggunakan aplikasi kasir!")
        break

    else:

        print("Pilihan tidak valid! Silakan coba lagi.")
