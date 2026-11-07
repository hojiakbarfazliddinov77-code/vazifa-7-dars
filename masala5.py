with open("matn.txt", "r", encoding="utf-8") as f:
    qatorlar_soni = len(f.readlines())

print(qatorlar_soni, "ta qator bor")