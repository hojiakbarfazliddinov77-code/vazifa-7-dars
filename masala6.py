qidirilgan = input("Qidirilayotgan ismni kiriting: ")

with open("ismlar.txt", "r", encoding="utf-8") as f:
    ismlar = [qator.strip() for qator in f]

if qidirilgan in ismlar:
    print("Ism topildi")
else:
    print("Ism topilmadi")