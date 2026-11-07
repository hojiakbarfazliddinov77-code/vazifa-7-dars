with open("mahsulotlar.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        mahsulot = input(f"{i + 1}-mahsulot nomini kiriting: ")
        f.write(mahsulot + "\n")

print("\nMahsulotlar:")
with open("mahsulotlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.strip())