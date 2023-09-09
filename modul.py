from tabulate import tabulate

class Transactions():
    
    
    def __init__(self):
        '''
        Transactions class have atrribute item dictionary 
        that contain item list, price list, and amount of item.
        Transactions have several methods; addItem, updateItem(), deleteItem,
        resetItem, checkItem & totalItem.
        
        '''
        self.listBarang = []
        self.listHarga = []
        self.listJumlah = []
        
        self.dataBarang = {"Nama Barang": self.listBarang, 
                            "Harga Barang": self.listHarga, 
                            "Jumlah Barang": self.listJumlah}


    def addItem(self):
        '''
        method for adding item from user,
        input item name, check type of input data from user,
        item will append to dataBarang dictionary
        '''
        barang = input("Nama item yang dibeli: ")
        program = True
        while program:
            try:
                harga = int(input("masukan Harga barang: Rp "))
                break
            except ValueError:
                print("Harga harus berupa angka")
                continue
        while program:
            try:
                jumlah = int(input("Masukan jumlah barang: "))
                break
            except ValueError:
                print("jumlah harus berupa angka")
                continue
                
        self.barang = barang
        self.harga = harga
        self.jumlah = jumlah

        self.listBarang.append(barang)
        self.listHarga.append(harga)
        self.listJumlah.append(jumlah)
        
        question = input("Apakah Anda Mau Tambah Barang? (Y/N) ")
        if question == 'Y' or question == 'y':
            self.addItem()
        elif  question == 'N' or question =='n':
            print("")
            self.mainMenu()
        else:
            print("Terima kasih")
            exit()
    
    
    def updateItem(self):
        '''
        method for update item, this method will have option for
        go through to updateNama, updateHarga, and updateJumlah method
        '''
        print("Berikut daftar belanja anda:")
        print(tabulate(self.dataBarang, headers="keys"))
        print("")
        print("Pilih opsi:")
        print("Ganti nama barang (1)")
        print("Ganti harga barang (2)")
        print("Ganti jumlah barang (3)")
        print("")
        
        inputNumber = input("Masukan opsi: ") # pilih  menu yang diinginkan.
        if inputNumber == '1':
            self.updateNama()
        elif inputNumber == '2':
            self.updateHarga()
        elif inputNumber == '3':
            self.updateJumlah()
        else:
            print("")
            print("terima Kasih")
            exit()
            
            
    def updateNama(self):
        '''
        Method for update item name,
        update name from user
        '''
        program = True
        while program:
            item = input("Nama Barang yang diganti: ")
            if item in self.dataBarang.get("Nama Barang"):
                newItem = input("Masukan nama barang baru: ")
                idxItem = self.dataBarang['Nama Barang'].index(item)
                self.dataBarang['Nama Barang'][idxItem] = newItem
                print(f"Barang {item} diubah menjadi {newItem}")
                print("")
                print(tabulate(self.dataBarang, headers="keys"))
                print("")
                break
            else:
                print("Nama barang tidak ditemukan")
        self.mainMenu()
        
        
    def updateHarga(self):
        '''
        method for update item price,
        price input from user
        '''

        program = True
        while program:
            item = input("Nama Barang yang diganti: ")
            if item in self.dataBarang.get("Nama Barang"):
                newItem = int(input("Masukan Harga barang baru: "))
                idxItem = self.dataBarang['Nama Barang'].index(item)
                self.dataBarang['Harga Barang'][idxItem] = newItem
                print(f"Harga {item} diubah menjadi {newItem}")
                print("")
                print(tabulate(self.dataBarang, headers="keys"))
                print("")
                break
            else:
                print("Nama barang tidak ditemukan")
        self.mainMenu()
        
        
    def updateJumlah(self):
        '''
        method for updet amount item,
        item input from user
        '''
        program =True
        while program:
            item = input("Nama Barang yang diganti: ")
            if item in self.dataBarang.get("Nama Barang"):
                newItem = int(input("Masukan jumlah pembelian yang sesuai: "))
                idxItem = self.dataBarang['Nama Barang'].index(item)
                self.dataBarang['Jumlah Barang'][idxItem] = newItem
                print(f"Jumlah barang sebelumnya {item}, diubah menjadi {newItem}")
                print("")
                print(tabulate(self.dataBarang, headers="keys"))
                print("")
                break
            else:
                print("Nama barang tidak ditemukan")
        self.mainMenu()
        
        
    def deleteItem(self):
        '''
        method from delete item
        this method will delete item data from database
        '''
        print("Berikut daftar belanjaan anda:")
        print(tabulate(self.dataBarang, headers="keys"))
        print("")

        program =True
        while program:
            item = input("Nama Barang yang dihapus: ")
            if item in self.dataBarang.get("Nama Barang"):
                idxItem = self.dataBarang['Nama Barang'].index(item)
                for key in self.dataBarang.keys():
                    del self.dataBarang[key][idxItem]
                print("")
                print(tabulate(self.dataBarang, headers="keys"))
                print("")
                self.mainMenu()
            else:
                print("Nama barang tidak ditemukan")
        
        
    def resetItem(self):
        '''
        method for clear the cart,
        item will be reset from dictionary
        '''
        self.dataBarang.clear()
        print("")
        print("Keranjang sudah kosong")
        print("")
        self.listBarang = []
        self.listHarga = []
        self.listJumlah = []
        
        self.dataBarang = {"Nama Barang": self.listBarang, 
                            "Harga Barang": self.listHarga, 
                            "Jumlah Barang": self.listJumlah}
        self.mainMenu()

    
    def checkItem(self):
        '''
        method for check the cart include item name, item price, amount of item.
        '''
        print("Berikut daftar belanja anda:")
        pesanan = tabulate(self.dataBarang, headers="keys")
        print(pesanan)
        
        if pesanan == tabulate(self.dataBarang, headers="keys"):
            print("Pesanan Sesuai")
            print("")
            self.mainMenu()
        elif pesanan != tabulate(self.dataBarang, headers="keys"):
            print("Pesanan tidak Sesuai")
            print("")
            self.mainMenu()
    
    
    def totalItem(self):
        '''
        method for calculate total price
        return descount if total price meet the requirements
        '''
        print("Berikut daftar belanja anda:")
        print(tabulate(self.dataBarang, headers="keys"))
        self.listTotal = [self.listHarga[i] * self.listJumlah[i] for i in range(len(self.listHarga))]
        total = sum(self.listTotal)
        print("")
        if total > 500000:
            total = total - (total*10/100)
            print(f"Selamat anda mendapatkan diskon 10% Total Belanjaan anda Rp{total}")
            print("")
        elif total > 300000:
            total = total -(total*8/100)
            print(f"Selamat anda mendapatkan diskon 8% Total Belanjaan anda Rp{total}")
            print("")
        elif total > 200000:
            total = total - (total*5/100)
            print(f"Selamat anda mendapatkan diskon 5% Total Belanjaan anda Rp{total}")
            print("")
        else:
            print(f"Total Belanjaan anda Rp{total}")
            print("")
        self.mainMenu()
        

    def mainMenu(self):
        '''
        method to dispaly main menu,
        main menu provide navigator menu 
        '''
        print("")
        print("Selamat Datang di e-Warung!")
        print("")
        print("Select Menu:")
        print("Masukan Barang (1)") #ini menuju fungsi tambah item
        print("Ubah Barang (2)") #ini fungsi update --> update nama/harga/jumlah, kemudian lanjutkan ke fungsi main()
        print("Hapus Barang (3)") #ini fungsi delete
        print("Kosongkan Keranjang (4)") #ini fungsi reset
        print("Cek Daftar Belanjaan (5)") #ini fungsi cek order 
        print("Lihat Total Harga Belanjaan (6)") #ini fungsi cek total order
        print("Keluar Toko  (7)")  #ini mengakhiri kasir
        print("")
        inputNumber = input("Input Menu Number: ") # pilih  menu yang diinginkan.
        # if inputnumber == 1/2/3/4/5 --> jalankan fungsi sesuai input
        if inputNumber == '1':
            self.addItem()
        elif inputNumber == '2':
            self.updateItem()
        elif inputNumber == '3':
            self.deleteItem()
        elif inputNumber == '4':
            self.resetItem()
        elif inputNumber == '5':
            self.checkItem()
        elif inputNumber == '6':
            self.totalItem()
        elif inputNumber == '7':
            print("Terima kasih")
            exit()
