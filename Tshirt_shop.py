# untuk undian voucher
import time
import random

def undian():
  print('\tLoading......') # string
  time.sleep(5)
  print('\n============================================== Undian Big Sale =====================================================')
  time.sleep(3)


undian()

def random_voucher():
    # Daftar voucher yang mungkin
    Vouchers = [('VOUCHER1', 15), ('VOUCHER2', 25), ('VOUCHER3', 35), ('MEGASALE', 50), ('DEWASHOPPING', 75)]

    # Memilih voucher secara acak
    random_voucher, diskon = random.choice(Vouchers)

    return random_voucher, diskon

# Memanggil fungsi untuk menghasilkan voucher acak
mendapatkan_voucher_random, diskon = random_voucher()

# Menampilkan undian voucher yang dihasilkan
print('========================================================================================================================')
print(f'============= Selamat! Anda mendapatkan voucher {mendapatkan_voucher_random} dengan diskon sebesar {diskon} %, Happy Shopping :) ==============')
print('================================= Vocher berlaku sampai 12 April 2024. ==================================================')


# Page Shop
import time

total_pesanan = [] # Inisialisasi variabel total pesanan
Total_harga = 0 # Inisialisasi variabel total harga
total_pembayaran = 0 # Inisialisasi variabel total pembayaran
diskon = 0 # Inisialisasi variabel diskon
Harga_sebelum_diskon = 0 # Inisialisasi variabel harga sebelum diskon

time.sleep(2)

def tampilkan_pesan():
  print('\n\tLoading......')
  time.sleep(5) # delay 5 detik
  print('\nSelamat Datang')
  time.sleep(2)
  print('\nAyo Ikut undian Big Sale dan dapatkan Voucher hingga diskon 75 % \nJangan sampai ketinggalan!. ')

tampilkan_pesan()
# Tampilkan pesan dengan delay
time.sleep(3) # delay selama 3 detik


print('\n=================================================================')
print('=========================== TryCoolhe ===========================')
print('\nList Item TryCoolhe')

# Data Item
List_Tshirt = [  #List
    'T Shirt - ETNERIS', 'T Shirt - Zoko Hex',  'T Shirt - Kayser Time', 'T Shirt - INDOSAN' # string
    ]

Harga_Tshirt = [
    129999, 132999, 300000, 167999
    ]

Size_Tshirt = [
    'S, M, L, XL', 'S, M, L, XL', 'S, M, L, XL', 'S, M, L, XL'
    ]


# Fungsi untuk menampilkan daftar list T shirt dan harga
def Tampilkan_daftar_baju(): # Fungsi
   for i, item in enumerate(List_Tshirt): # perulangan/looping
       print(f"\n\t{i+1}. {item} | Size {Size_Tshirt[i]} | Rp. {Harga_Tshirt[i]:,.0f}")
       # untuk menampilkan data pada list seperti nama produk, harga dan size

Tampilkan_daftar_baju ()


# Fungsi untuk memproses pembelian
def  Proses_pembelian():
  print('\nNote !\n\tJika ingin membeli lebih dari 1 jenis, pilih nomor dengan tambahan koma (,).')

  # Meminta input pemilihan item pengguna
  pilihan = list(map(int, input('\nMasukkan nomor T-Shirt yang ingin Anda Beli : ').split(',')))
  # split ini  untuk memilih lebih satu jenis item dengan menggunakan tanda koma (2,3,1)
  time.sleep(2)
  jumlah = int(input('Masukkan jumlah T-Shirt yang ingin Anda beli : '))
  size = input("Masukkan ukuran T-Shirt (S, M, L, XL): ")

  print('\n=================================================================')



# Detail Pesanan T-Shrit yang dipilih
  print('Detail Pesanan')
  for pesanan in pilihan:
            if 1 <= pesanan <= len(List_Tshirt):
                print(f'\n\t{List_Tshirt[pesanan - 1]}, {jumlah} Pcs, Size {size}')
                total_pesanan.append((List_Tshirt[pesanan - 1], jumlah, size, Harga_Tshirt[pesanan - 1]))
                # menampilkan detail pesanan dari item yang dipilih oleh user dari list, menampilkan sepeti item yang di pilih, jumlah, size dan harga dari setiap item
            else:
                print(f"\n\tNomor {pesanan} tidak valid. Harap pilih nomor yang valid -_- .")


Proses_pembelian ()

time.sleep(2)

# untuk menentukan diskon berdasarkan Voucher
print('\n\tJika Tidak punya Voucher ketik "Tidak"')
Voucher = { # menggunakan dictionary
    'VOUCHER1': 15,
    'VOUCHER2': 25,
    'VOUCHER3': 35,
    'MEGASALE':50,
    'DEWASHOPPING':75,
    }

# Input code vocuher
Voucher_code = input('\nMasukkan kode voucher yang ingin Anda gunakan : ')

time.sleep(2)
print('=============================================================')

# Cek vocher dari data dictionary
# kondisi/percabangan
if Voucher_code in Voucher:
   diskon += Voucher[Voucher_code] # nilai yang diambil dari Voucher akan menjadi nilai variabel diskon.
   print(f"\nDiskon voucher {Voucher_code}: {Voucher[Voucher_code]} %") # menampilkan voucher apa yang di pakai dan jumlah diskon
else:
   print("\nAnda tidak menggunakan voucher -_- .") # jika tidak punya voucher



# fungsi untuk Menghitung total pembayaran
def Hitung_total_harga():
    global Total_harga, Harga_sebelum_diskon
    Harga_sebelum_diskon = sum(jumlah * harga for _, jumlah, _, harga in total_pesanan) # total harga jika tidak menggunakan voucher
    # jumlah dikali dengan harga dan jumlah dari total pesanan item user
    Total_harga = Harga_sebelum_diskon - (Harga_sebelum_diskon * diskon / 100) # total harga jika menggunakan voucher
    # harga sebelum diskon di kurang dengan harga sebelum diskon yang sudah dikalikan dengan jumlah diskon, per 100 ini untuk persen
    return Total_harga

Hitung_total_harga()

# Menampilkan hasil dari total pembayaran
print(f'\nDiskon : {diskon} %')
print(f'\nHarga sebelum Diskon :\t Rp. {Harga_sebelum_diskon:,.0f}')
print(f'\nTotal Harga :\t Rp. {Total_harga:,.0f}')