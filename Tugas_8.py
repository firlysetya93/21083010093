from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
 if i % 2 == 0:
  print(i+1, "Gajil", "-punya ID proses", getpid())
 else:
  print(i+1, "Genap", "-punya ID proses", getpid())
  sleep(1)

a = int(input("input :"))

print("Sekuensial")
sekuensial_awal = time()

for i in range(a):
 cetak(i)
sekuensial_akhir = time()

print("Multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(a):
 p = Process(target=cetak, args=(i,))
 kumpulan_proses.append(p)
 p.start()

for i in kumpulan_proses:
 p.join()

process_akhir = time()

print("Multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,a))
pool.close()

pool_akhir = time()

print("Waktu Eksekusi Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu Eksekusi Multiprocessing.process :", process_akhir - process_awal, "detik")
print("Waktu Eksekusi Multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
