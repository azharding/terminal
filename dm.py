from instagrapi import Client
from colorama import Fore
import json, re, random, sys, os, time

CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N='\x1b[0m' # WARNA MATI

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()
os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
print(f"""\033[96;1m
TOOLS INSTAGRAM BUSINESS

▀█▀ ░█▄─░█ ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ 　 ░█▀▀▄ ░█▀▄▀█
░█─ ░█░█░█ ─▀▀▀▄▄ ─░█── ░█▄▄█ 　 ░█─░█ ░█░█░█
▄█▄ ░█──▀█ ░█▄▄▄█ ─░█── ░█─░█ 　 ░█▄▄▀ ░█──░█

WELCOME TO INSTADM DESIGNED BY AZHARDING""")

# Masukkan username dan password Instagram
username = input("Masukkan username Anda: ")
password = input("Masukkan password Anda: ")

# Buat objek Client
cl = Client()

# Login ke akun Instagram Anda
try:
    cl.login(username, password)
    print(Fore.GREEN + "\nLogin berhasil!!\n\n\nSedang Proses, Silahkan Tunggu Sebentar...")
except Exception as e:
    print(Fore.RED + "\nLogin gagal, silakan cek username dan password Anda.")
    print(Fore.RED + f"Error: {str(e)}")
    exit()

# Dapatkan user ID Anda
user_id = cl.user_id_from_username(username)

# Dapatkan followers Anda
followers = cl.user_followers(user_id)

# Buat daftar ID followers
followers_ids = list(followers.keys())

# Pesan Yang akan dikrim
message = input("\nMasukkan Pesan Broadcast: ")

# Inisialisasi variabel untuk menghitung jumlah username terkirim
jumlah_terkirim = 1

os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
time.sleep(1)
InsPi = f"""\033[33m
 +-> WELLCOME DESIGN BY AZHARDING
 |
 | ▀█▀ ░█▄─░█ ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ 　 ░█▀▀▄ ░█▀▄▀█
 | ░█─ ░█░█░█ ─▀▀▀▄▄ ─░█── ░█▄▄█ 　 ░█─░█ ░█░█░█
 | ▄█▄ ░█──▀█ ░█▄▄▄█ ─░█── ░█─░█ 　 ░█▄▄▀ ░█──░█
 |
 +-------------------------------------------------->
 | DEVELOVER : AZHARDING           |   MIT License  |
 | INSTAGRAM AUTO DM TO FOLLOWERS  |   Instagrapi   |
 +--------------------------------------------------+
 +----------------[INFO AKUN INSTAGRAM]-------------->
 | USERNAME : \033[36m{username}\033[33m
 | PASSWORD : \033[36m{password}\033[33m
 +-------------------------------------------------->
 |
 +> MESSAGES : \033[36m{message}\033[33m\n
 +> Sedang Mengirim Pesan Silahkan Tunggu....
 """
typewriter(InsPi)


# Kirim DM ke semua followers
for follower_id in followers_ids:
    try:
        cl.direct_send(text=message, user_ids=[follower_id])
        username_follower = cl.username_from_user_id(follower_id)
        print(f"\033[32mPesan Ke \033[31m{jumlah_terkirim} \033[32m Berhasil Terkirim ke \033[33m @{username_follower}")
        jumlah_terkirim += 1
    except Exception as e:
        username_follower = cl.username_from_user_id(follower_id)
        print(f"\033[32mPesan Ke \033[31m{jumlah_terkirim} \033[32m Berhasil Terkirim ke \033[33m @{username_follower}")
        jumlah_terkirim += 1
        time.sleep(5)
# Cetak jumlah username terkirim

print(f"\n\033[96;1mJumlah username yang terkirim: {jumlah_terkirim-1}\033[0m")

# Tutup koneksi
cl.logout()
