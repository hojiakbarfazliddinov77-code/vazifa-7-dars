with open("matn.txt", "r", encoding="utf-8") as f:
    sozlar = f.read().split()

if sozlar:
    eng_uzun = max(sozlar, key=len)
    print("Eng uzun so'z:", eng_uzun)
    print("Uzunligi:", len(eng_uzun))
else:
    print("Faylda so'z yo'q")