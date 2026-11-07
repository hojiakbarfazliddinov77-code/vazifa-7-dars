with open("baholar.txt", "r", encoding="utf-8") as f:
    ballar = [float(qator) for qator in f if qator.strip()]

if ballar:
    print("Ballar:", ballar)
    print("Ballar soni:", len(ballar))
    print("Eng katta ball:", max(ballar))
    print("Eng kichik ball:", min(ballar))
    print("O'rtacha ball:", round(sum(ballar) / len(ballar), 2))
else:
    print("Faylda ballar yo'q")