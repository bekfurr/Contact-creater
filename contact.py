import pickle
import os
class Contact:
    def __init__(self, ism, telefon, email):
        self.ism = ism or 'Noma\'lum'
        self.telefon = telefon or 'Noma\'lum'
        self.email = email or 'Noma\'lum'

    def __str__(self):
        return f"Ism: {self.ism}, Telefon: {self.telefon}, Email: {self.email}"

class ContactManager:

    def __init__(self):
        self.kontaktlar = self.kontaktlarni_yuklash()

    def kontaktlarni_yuklash(self):
        if os.path.exists('kontaktlar.txt'):
            with open('kontaktlar.txt', 'rb') as f:
                return pickle.load(f)
        else:
            return {}

    def kontaktlarni_saqlash(self):
        with open('kontaktlar.txt', 'wb') as f:
            pickle.dump(self.kontaktlar, f)

    def kontakt_qo_shish(self, ism, telefon, email):
        if ism not in self.kontaktlar:
            self.kontaktlar[ism] = Contact(ism, telefon, email)
        else:
            print(f"{ism} nomli kontakt allaqachon mavjud.")

    def kontakt_ma_lumotlarini_ko_rsating(self, ism):
        if ism in self.kontaktlar:
            return str(self.kontaktlar[ism])
        else:
            return "Kontakt topilmadi."

    def kontakt_yangilash(self, ism, telefon=None, email=None):
        if ism in self.kontaktlar:
            if telefon:
                self.kontaktlar[ism].telefon = telefon
            if email:
                self.kontaktlar[ism].email = email
        else:
            print("Yangilash uchun kontakt topilmadi.")

    def kontakt_o_chirish(self, ism):
        if ism in self.kontaktlar:
            del self.kontaktlar[ism]
        else:
            print("O'chirish uchun kontakt topilmadi.")
    def ma_lumotlarni_chiqarish(self):
        for ism, kontakt in self.kontaktlar.items():
            print(f"Ism: {kontakt.ism}, Telefon: {kontakt.telefon}, Email: {kontakt.email}")

def main():
    manager = ContactManager()
    try:
        while True:
            action = input("Qo'shish, Yangilash, Ko'rsatish yoki O'chirish (chiqish uchun exit tering): ").lower()
            if action == 'exit':
                print("MAVJUD MA'LUMOTLAR:")
                manager.ma_lumotlarni_chiqarish()
                break

            ism = input("Ismni kiriting: ")
            if action in ['qo\'shish', 'yangilash']:
                telefon = input("Telefon raqamini kiriting (bo'sh qoldirish uchun Enter ni bosing): ") or None
                email = input("Email manzilini kiriting (bo'sh qoldirish uchun Enter ni bosing): ") or None
            if action == 'qo\'shish':
                manager.kontakt_qo_shish(ism, telefon, email)
            elif action == 'ko\'rsatish':
                print(manager.kontakt_ma_lumotlarini_ko_rsating(ism))
            elif action == 'yangilash':
                manager.kontakt_yangilash(ism, telefon, email)
            elif action == 'o\'chirish':
                manager.kontakt_o_chirish(ism)
            else:
                print("Noto'g'ri buyruq kiritildi.")
            
            print(f"Kiritilgan ma\'lumotlar saqlandi")
            print("Yana ma'lumot kiritiasizmi chiqish uchun exit ni kiriting")
       
    finally:
        manager.kontaktlarni_saqlash()   
        


xabar = '''
Hammaga samol bizning dasturimizga hush kelibsiz bu dastur orqali o'zningizga kontaktlar saqlashingiz mumkin
'''
print(xabar)

main()
    
