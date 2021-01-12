def Klir():
    import os
    os.system('clear') # on windows

def XL():
    
    Klir()
    
    NomorXL = input("Masukan Nomor: +62")

    Klir()

    print"1.Kuota Unlimited Youtube 30 Hari Rp.0"
    print"2.Kuota 1 GB 15 Hari Rp.0"
    print"3.Kuota 5 GB 30 Hari Rp.0"
    print"4.Kuota 10 GB 30 Hari Rp.0"
    print"5.Kuota 20 GB (10 GB Internet + 10 GB Youtube)"
    print"0.Close"

    KuotaXL = input("Pilih: ")

    Klir()

    if KuotaXL==1:

        Klir()
        
        print"Selamat Kuota Unlimited Youtube 30 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaXL==2:

        Klir()
        
        print"Selamat Kuota 1 GB 15 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaXL==3:

        Klir()
        
        print"Selamat Kuota 5 GB 30 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaXL==4:

        Klir()
        
        print"Selamat Kuota 10 GB 30 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaXL==5:

        Klir()
        
        print"Selamat Kuota 20 GB (10 GB Internet + 10 GB Youtube) Anda Sudah Aktif"

        
        
    elif KuotaXL==0:

        Klir()
        
        print"Bye!"
        exit()

def Telkomsel():

    Klir()

    NomorTelkom = input("Masukan Nomor: +62")

    print"1.Kuota 1 GB 30 Hari Rp.5"
    print"2.Kuota 5 GB 60 Hari Rp.0"
    print"3.Kuota 10 GB 30 Hari Rp.0"
    print"4.Kuota 30 GB 30 Hari Rp.0"
    print"0.Close"

    KuotaTelkom = input("Pilih Menu: ")

    if KuotaTelkom==1:

        Klir()
        print"Kuota 1 GB 30 Hari Rp.5 Anda Sudah Aktif"

        
        
    elif KuotaTelkom==2:

        Klir()
        print"Kuota 5 GB 60 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaTelkom==3:

        Klir()
        print"10 GB 30 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaTelkom==4:

        Klir()
        print"30 GB 30 Hari Rp.0 Anda Sudah Aktif"

        
        
    elif KuotaTelkom==0:

        Klir()
        print"Bye!"
        exit()

def Indosat():

    Klir()
    NomorIndo = input("Masukan Nomor: +62")

    Klir()
    print"1.Unlimited 1 Hari"
    print"2.Unlimited 5 Hari"
    print"3.Unlimited 10 Hari"
    print"4.Unlimited 15 Hari"
    print"0.Close"

    KuotaIndo = input("Pilih Menu: ")

    if KuotaIndo==1:

        Klir()
        print"Kuota Unlimited 1 Hari Anda Sudah Aktif"
    elif KuotaIndo==2:
        Klir()
        print"Kuota Unlimited 5 Hari Anda Sudah Aktif"
    elif KuotaIndo==3:
        Klir()
        print"Kuota Unlimited 10 Hari Anda Sudah Aktif"
    elif KuotaIndo==4:
        Klir()
        print"Kuota Unlimited 15 Hari Anda Sudah Aktif"
    elif KuotaIndo==0:
        Klir()
        print"Bye!"
        exit()

def tri():
       Klir()
       
       print"Coming Soon!"

def Close():
       Klir()
       print"Bye!"
        

print"###Paket Data Gratis###"

#Menu Pilihan

print"1.XL"
print"2.Telkomsel"
print"3.Indosat"
print"4. 3"
print"0.Close"

#Input Menu

menu = input("Pilih Operator Anda: ")

#Check Menu

if menu==1:
    
    XL()

elif menu==2:

    Telkomsel()

elif menu==3:

     Indosat()

elif menu==4:

     tri()

elif menu==0:

      Close()

else: print"Gaada Njing"
