class Kullanici:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def hosgeldiniz(self):
        print(f"Merhaba {self.ad} {self.soyad}, {self.yas} yaşındasınız. Hoş geldiniz!")

if __name__ == "__main__":
    ad = input("Adınızı giriniz: ")
    soyad = input("Soyadınızı giriniz: ")
    yas = input("Yaşınızı giriniz: ")

    kullanici = Kullanici(ad, soyad, yas)
    kullanici.hosgeldiniz()
