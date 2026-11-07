with open("ismlar.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        ism = input(f"{i + 1}-ismni kiriting: ")
        f.write(ism + "\n")