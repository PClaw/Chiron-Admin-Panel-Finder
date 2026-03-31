import urllib.request
from urllib.error import URLError, HTTPError
import os

# Renk Kodları (ANSI)
MAVI = '\033[94m'
SARI = '\033[93m'
BEYAZ = '\033[0m' # Renkleri sıfırlamak için

def Credit():
    # KILIÇ ASCII SANATI (MAVİ)
    sword = r"""
              ^
             / \
            /   \
           /     \
          /       \
         /         \
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
      _ |____|_|____| _
     (_|____  _  ____|_)
            | | |
            | | |
            | | |
            |_|_|
             \_/
    """
    
    # Kılıcı Mavi Yazdır
    print(MAVI + sword + BEYAZ)
    
    # Bilgileri Sarı Yazdır
    print(SARI)
    print(" " * 9 + "#####################################")
    print(" " * 9 + "#     +++ CHIRON ADMIN PANEL +++    #")
    print(" " * 9 + "#        SCRIPT BY CLAW24           #")
    print(" " * 9 + "#     CYBERCLAW CYBER GROUPS        #")
    print(" " * 9 + "#####################################")
    print(BEYAZ + "\n")

def findAdmin():
    try:
        f = open("link.txt", "r")
    except FileNotFoundError:
        print(MAVI + "[!]" + BEYAZ + " Hata: link.txt dosyası bulunamadı!")
        return

    link = input(SARI + "Enter Site Name \n(ex : example.com): " + BEYAZ)
    print("\n" + MAVI + "[+]" + BEYAZ + " Scanning available links...\n")
    
    for sub_link in f:
        sub_link = sub_link.strip()
        if not sub_link: continue
        
        req_link = "http://" + link + "/" + sub_link
        
        try:
            # Bazı siteler botları engellediği için User-Agent ekledim
            req = urllib.request.Request(req_link, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
        except (HTTPError, URLError):
            continue
        else:
            print(SARI + "[FOUND] => " + BEYAZ + req_link)
    f.close()

# Programı Başlat
Credit()
findAdmin()
