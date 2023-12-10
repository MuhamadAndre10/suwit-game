import random
import sys
from termcolor import colored, cprint

print (colored("\n=======================================","yellow"))
print ("🥰 SELAMAT DATANG DI GAME SUWIT JAWA 🥰")
print (colored("=======================================\n","yellow"))

#FUNGCION PILIHAN KOMPUTER
def PilComp() :
    comp = random.random();    
    if comp < 0.34:
        comp = "semut"
    elif comp >= 0.34 and comp < 0.67:
        comp = "gajah"
    else:
        comp = "orang"
    return comp
# END

# FUNCTION 
def proses(player, comp):
    hasil = ""
    if player == comp:
        hasil = "Seri"
    elif player == "orang":
        if comp == "semut":
            hasil = "Menang"
        else:
            hasil = "Kalah"
    elif player == "semut":
        if comp == "gajah":
            hasil = "Menang"
        else:
            hasil = "Kalah"
    elif player == "gajah":
        if comp == "orang":
            hasil = "Menang"
        else :
            hasil = "Kalah"
            
    return hasil,player,comp

def feedback():
    menang  = str("Selamat kamu Menang permainan".upper())
    kalah   = str("yahh kalah, silahkan mencoba lagi".upper())
    seri    = str("Yah Seri, Silahkan mencoba lagi!".upper())
    return menang, kalah , seri

def garis():
    print (colored("-----------------------------", "yellow"))

#pengulangan game
while (True):        
    print(colored("KAMU DI BERI PILIHAN UNTUK BERMAIN MELAWAN KOMPUTER, SILAHKAN BERMAIN\n", "cyan"))
    print(colored("\tKAMU MEMILIKI PILIHAN INPUTAN ( GAJAH | SEMUT | ORANG )".upper(), "cyan"))

    # cek inputan user/player
    while(True):              
        player = input(str("\nMasukan pilihanmu!! : ").lower())
        if player == 'gajah' or  player == 'semut' or player == 'orang':
            Hakhir = proses(player,PilComp())
            garis()
            print ("Kamu memilih     : ", Hakhir[1])
            print ("Komputer memilih : ", Hakhir[2])
            print ("Hasil            : ", Hakhir[0])
            garis()
            break
        else :
            print(colored("Maaf yang anda inputkan tidak sesuai perintah, Silahkan coba lagi".upper(), "red"))
    #end 
   # memanggil fungsi feedback()
    pesan = feedback()
    garis()
    if Hakhir[0] == "Menang":
        print(pesan[0])
    elif Hakhir[0] == "Kalah":
        print(pesan[1])
    else :
        print(pesan[2])
    garis()
    # END
    
    # PENGECEKAN INPUTAN USER
    while (True):
        ulang = input (colored("\nMau Bermain lagi??? (Y/N)", "cyan"))
        if ulang == "y" or ulang == "Y":
            print("\nSILAHKAN BERMAIN LAGI\n")
            break
        elif ulang == "N" or ulang == "n":
            print ("\nTERIMAKASIH SUDAH BERMAIN\n")
            break
        else:            
            print(colored("\nMAAF YANG ANDA INPUTKAN TIDAK SESUAI PERINTAH", "red"))
            continue
        
    # cek user input n maka stop game
    if ulang == "n" or ulang == "N":
        break
    #end
#END

