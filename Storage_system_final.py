stok = {} # dengan struktur id : ('jenis_barang', 'merk_barang', qty_barang) dict()

def garis () :
    print('='*29)

def menuawal() :
    print("-------------------------------")
    print("      Gudang Penyimpanan      ")
    print("-------------------------------")
    print("Selamat datang di aplikasi kami\n"
          "Gudang kami bisa menyimpan barang\n"
          "seuai kebutuhan anda")
    print("-------------------------------")
def menu():
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print(" ( 1 )  : Input Barang ")
    print(" ( 2 )  : Kirim Barang ")
    print(" ( 3 )  : Stok Barang ")
    print(" ( 99 ) : Mengakhiri Program ")
    print('=============================')
    return  int(input("= "))

run = menuawal()
run = menu()

class sistem : # kelas sistem

    while True :
        if run == 1:

            auth1 = int(input("Barang baru (1) atau Barang lama (2) ? "))
            if auth1 == 1 :
                id_barang = int(input("Masukan Id Barang !\n"
                                      "= "))
                jenis_barang = input("Masukan Jenis Barang !\n"
                                     "= ")
                merk_barang = input("Merk Barang !\n"
                                    "= ")
                qty_barang = int(input("Berapa banyak barangnya ?\n"
                                       "= "))
                garis()
                stok[id_barang] = jenis_barang, merk_barang, qty_barang

                print(stok[id_barang])
                print("Barang Berhasil Di Tambah")


            elif auth1 == 2 :
                print("---    PILIH ID BARANG UNTUK DI INPUT   --")
                print("- Id Barang -- Jenis -- Merk -- Quantity -")
                for key, value in stok.items():
                    print("{} : {}".format(key, value))

                id_barang = int(input("Masukan Id Barang\n"
                                      "= "))
                qty_barang_tambah = int(input("Berapa banyak barang yang ingin di tambah ?\n"
                                       "= "))
                garis()

                con_list = list(stok[id_barang])
                con_list [2] = int(qty_barang) + int(qty_barang_tambah)
                stok[id_barang] = tuple (con_list)
                print(stok[id_barang])
                print("Barang Berhasil Di Tambah")

            run = menu()


        elif run == 3:
            print("---        BARANG YANG TERSEDIA       ---")
            print("- Id Barang -- Jenis -- Merk -- Quantity -")
            for key, value in stok.items():
                print("{} : {}".format(key, value))

            garis()
            CHOICE = int(input('ketik 98 to lanjut atau 99 to keluar: '))
            if CHOICE == 98:
                run = menu()
            else:
                break

        elif run == 2:
            print("---    PILIH ID BARANG UNTUK DI KIRIM   --")
            print("- Id Barang -- Jenis -- Merk -- Quantity -")
            for key, value in stok.items():
                print("{} : {}".format(key, value))

            id_barang = int(input("Masukan Id Barang\n"
                                  "= "))
            qty_barang_kirim = int(input("Berapa banyak barang yang ingin di kirim ?\n"
                                          "= "))
            garis()

            con_list = list(stok[id_barang])
            con_list[2] = int(qty_barang) - int(qty_barang_kirim)
            stok[id_barang] = tuple(con_list)
            print(stok[id_barang])
            print("Barang Berhasil Di Kirim")
            CHOICE = int(input('ketik 98 to lanjut atau 99 to keluar: '))
            if CHOICE == 98:
                run = menu()
            else:
                break

        elif run == 99:
            break
        else:
            print("Kode yang di input salah")
            break

print("Terima Kasih Telah menggunakan Aplikasi kami")