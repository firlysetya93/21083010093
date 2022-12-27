def menu():
  print ("""
  =====================
      MENU UTAMA     
  =====================
  1. Deret Prima
  2. Deret Pangkat
  3. Deret Genap
  4. Deret Ganjil
  0. Keluar
  """)

  pilihan = int(input("pilih nomer deret: "))
  print ('\n')
  if(pilihan == 1):
    prima()
    ulang()
  elif(pilihan == 2):
    pangkat()
    ulang()
  elif(pilihan == 3):
    genap()
    ulang()
  elif(pilihan == 4):
    ganjil()
    ulang()
  elif(pilihan == 0):
    keluar()
  else:
    print("tidak ada")

def ulang():
  print("\n================")
  ulang = input("apakah ingin coba [Y/N]: ")
  print("================")
  if (ulang=='Y'or ulang=='y'):
    menu()
  elif (ulang=='N' or ulang=='n'):
    print ("thank you")
    quit()
  else:
    print("pilih[Y/N")
  return (menu)

def prima():
  print ("=============PROGRAM PRIMA===========")
  print ("==========================================")
  angka_awal = int(input("Masukkan angka awal: "))
  angka_akhir = int(input("masukkan angka akhir: "))
  list_angka = [i for i in range(angka_awal, angka_akhir + 1)]
  bilangan_prima = []

  for i in list_angka:
    if (i==2 or i==3 or i==5 or i==7) or (i%2 !=0 and i%5 !=0 and i%7 !=0):
      bilangan_prima.append(i)
  print(bilangan_prima)
def pangkat():
  print ("=============PROGRAM PANGKAT===========")
  print ("==========================================")
  a = int (input('Masukkan Angka yang ingin dipangkatkan: '))
  p = int(input('Masukkan berapa deret angka yang akan dipangkatkan: '))
  for n in range(1, (p + 1), 1):
    print(a ** n, end = ' ')

def genap():
  print('============PROGRAM GENAP=============')
  print('========================================')
  print()
  jumlah_deret = int(input('Jumlah deret yang diinginkan: '))
  
  for i in range(1,jumlah_deret+1):
    print(i*2, end=" ")

def ganjil():
  print('=============PROGRAM GANJIL==========')
  print('========================================')
  print()
  jumlah_deret = int(input('Jumlah deret yang diinginkan: '))
  
  for i in range(1,jumlah_deret+1):
    print((i*2)-1, end=" ")

def keluar():
  print("tidak ada")


if __name__=="__main__":
  menu()

