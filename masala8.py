with open("sonlar.txt", "r", encoding="utf-8") as f:
    sonlar = [int(qator) for qator in f if qator.strip()]

with open("juft_sonlar.txt", "w", encoding="utf-8") as f:
    for son in sonlar:
        if son % 2 == 0:
            f.write(str(son) + "\n")

print("Juft sonlar fayliga yozildi")