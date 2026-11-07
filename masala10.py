jami = 0

with open("xarajatlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.strip()
        if not qator:
            continue
        nom, summa = qator.rsplit(" ", 1)
        summa = int(summa)
        jami += summa
        print(f"{nom}: {summa} so'm")

print("-" * 25)
print("Jami xarajat:", jami, "so'm")