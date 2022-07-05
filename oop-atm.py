class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad = ad
        self.soyad = soyad
        self.kartsifre = kartsifre
        self.hesapbakiye = hesapbakiye
        self.kredikartborc = kredikartborc
        self.sonodeme = sonodeme

Ahmethesap = Musteri("Ahmet", "Candan", "1357", 5000,4200,20/11/2022)
Mehmethesap = Musteri("Mehmet", "Duyar", "2468",6000 ,3800 ,15/12/2022)

takılankart = Ahmethesap

class ATM : 
    def __init__(self,atmad):
        self.atmad = atmad
        self.giriskontrol()
        self.dongu = True



    def giriskontrol(self):
        Hak = 2
        for i in range(0,3):
            sifre = input("Lütfen 4 Haneli Şifrenizi Giriniz >> ")
            if sifre == takılankart.kartsifre:
                self.program()
            elif sifre != takılankart.kartsifre and Hak !=0:
                print("Hayalı şifre girdiniz . Kalan Hakkınız {}".format(Hak)) 
                Hak -=1
            elif sifre != takılankart.kartsifre and Hak ==0:
                print("3 Defa Hatalı Girdiniz. Bloke Olmuştur")
                exit()

    def program (self):
        secim = self.menu()
    
        if secim == 1:
            self.bakiye()
        elif secim ==2 :
            self.kkborc()
        elif secim ==3 :
            self.paracek()
        elif secim ==4:
            self.parayatir()
        elif secim ==5:
            self.cikis()
        
    def menu (self):
        secim = int(input("""*** Merhabalar {} ' a Hoşgeldiniz  Sayın  {} {} \nLütfen Yapmak İstedğiniz İşlemi  Seçiniz...\n\n[1] Bakiye Sorgulama
        \n[2] Kredi Kartı Sorgulana
        \n[3] Para Çekme
        \n[4] Para Yatırma
        \n[5] Kart İade
        \n\nSeçim >> """
        .format(self.atmad, takılankart.ad, takılankart.soyad)))


        while  secim < 1 or secim > 5 : 
            print("\n\n Lütfen 1 ve 5 Arasında Geçerli bir değer Giriniz... \nAna Menüye Dönülüyor...")
            self.program()
        
        return secim
    
    def bakiye(self):
        print("Hesap Bakiyeniz {}" .format(takılankart.hesapbakiye))
        self.dongu = False
        self.menudon()


    def kkborc(self):
        print("Kredi Kartı Borcunuz {} Son Ödeme Tarihli {} TL'dir.".format(takılankart.sonodeme,takılankart.kredikartborc))
        self.dongu = False
        self.menudon() 
   
    def paracek(self):
        miktar = int(input("Lütfen Çekeceğiniz Tutarı Giriniz >> "))
        

        if miktar > takılankart.hesapbakiye:
            print("Yetersiz Bakiye")
            self.menudon()

        else :
            takılankart.hesapbakiye = takılankart.hesapbakiye - miktar
            print("Lütfen Paranızı Alınız Hesabınızda Kalan Tutar {} TL'dir".format(takılankart.hesapbakiye))
            self.menudon()
    
    def parayatir(self):
          miktar2 = int(input("Lütfen Yatırılacak Tutarı Giriniz >> "))
          takılankart.hesapbakiye = takılankart.hesapbakiye + miktar2

          print("Para Yatırma İşlemİ Başarıyla Gerçeklemiştir. Yeni Bakiye {} TL'dir ".format(takılankart.hesapbakiye))
          self.menudon()
    
    
    def cikis(self):
        print("İyi Günler")
        self.dongu = False
        exit()

    def menudon(self):
        x = int(input("""Ana Menüye Dönmek İçin Lütfen 7 Tuşuna Basınız Yada Kart İade için 5 Tuşuna Basınız"""))
        if x ==7:
            self.program()
        elif x == 5 :
            self.cikis()

Banka = ATM("AKBANK")


while Banka.dongu:
    Banka.program()
