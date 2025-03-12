from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Python Programi: Kullanici Girdisi', ln=True, align='C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Sayfa {self.page_no()}', align='C')

# PDF'e eklemek istediğimiz Python kodu
code_text = """class Kullanici:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def hosgeldiniz(self):
        print(f"Merhaba {self.ad} {self.soyad}, {self.yas} yasindasiniz. Hos geldiniz!")

if __name__ == "__main__":
    ad = input("Adinizi giriniz: ")
    soyad = input("Soyadinizi giriniz: ")
    yas = input("Yasinizi giriniz: ")

    kullanici = Kullanici(ad, soyad, yas)
    kullanici.hosgeldiniz()"""

# PDF dosyasi olusturulmasi
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

for line in code_text.split("\n"):
    pdf.cell(0, 10, txt=line, ln=True)

pdf.output("kullanici_programi.pdf")
