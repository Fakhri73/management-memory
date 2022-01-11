# Kelompok 6
# 5200411096	HARIS ANDIKA PRATAMA
# 5200411103	IKHWAN NURALIF
# 5200411104	DAMAR PRASETYO NUGROHO
# 5200411108	FAKHRI TRI ATMAJA
multiProg=[]

print("\n========== Multiprogramming Kelompok 6 ==========")
ram = int(input("\nMasukkan Kapasitas RAM (Gb)\t: "))

#Kapasitas OS
operasi_sistem = 255

# Rumus konversi Gb ke Kbps
konfram = ram * 1024 * 1024

# BanyakNYA partisi seperti pada simulasi = 7
partisi = 7

# Rumus ram di kurangi OS
hasilRam = konfram - operasi_sistem

# Rumus pembagian partisi
pemPartisi = hasilRam / partisi

# Variabel sementara untuk looping
p = partisi
a = 0
x = 0


while a < p:
  program = float(input("\nMasukkan kapasitas program (Kbps) \t: "))
  
  if (a == 7):
    program = program + x
    
    if (program > pemPartisi):
      print("Partisi sudah mencapai maksimal")
      a = 99
    else:
      multiProg.append(program)
  else:
    
    if (x == 0):
      
      if (program < pemPartisi):
        multiProg.append(program)
      else:
        x = program - pemPartisi
        multiProg.append(pemPartisi)
    else: 
      program = program + x
      
      if (program < pemPartisi):
        multiProg.append(program)
      else:
        x = program - pemPartisi
        multiProg.append(pemPartisi)

  
  # KODE untuk membatasi inputan dari user
  if (a >= 7):
    print("Jumlah partisi sudah mencapai batas maksimum")
    a = a + 1
  else:
    pilih = input("Ingin input lagi? (y/t) : ")
    # Memberi pesan kepada user apakah akan menginputkan lagi atau tidak
    if pilih=="y":
      a = a+1
    if pilih=="t":
       
      if (x > 0 and x < pemPartisi):
        multiProg.append(x)
      elif (x > 0 and x >= pemPartisi):
        while x > pemPartisi:      
          x = x - pemPartisi
          multiProg.append(pemPartisi)
          if (x <= pemPartisi):
            multiProg.append(x)
      a = 10


if (a == 100):
  print("Masing-masing partisi terlalu besar")
else :
  
        
  
  if (len(multiProg)>=9):
    print("Partisi sudah mencapai batas")
  else:
    y = 1
    
    print("\n=================== Hasil ====================")
    print("\n Operasi sistem \t:",operasi_sistem,"Kbps")
    print(" Total RAM \t\t:",konfram,"Kbps\n")
    
    for n in range(0, partisi ):
      
    
      
      if (n < len(multiProg)):
        
        print("Partisi",y,"(",pemPartisi,"kbps )", multiProg[n], "Kbps")
   
        y = y + 1
      else:
        
        print("Partisi",y,"(",pemPartisi,"kbps ) 0.0", "Kbps")
        y = y + 1