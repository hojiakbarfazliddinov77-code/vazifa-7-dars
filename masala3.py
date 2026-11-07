yangi_ism = input("Yangi ismni kiriting: ")
with open("ismlar.txt", "a", encoding="utf-8") as f:
    f.write(yangi_ism + "\n")