import random
import os
import csv
from parameters import *

output_dir = "inventarios"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, numberInventories + 1):
    file_path = os.path.join(output_dir, f"inventario_{i}.csv")

    with open(file_path, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["produto", "quantidade"])

        for produto in products.values():
            quantidade = random.randint(1, 100)
            writer.writerow([produto, quantidade])