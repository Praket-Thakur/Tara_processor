import csv

with open("memory_dump.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    with open("high.hex", "w") as high, open("low.hex", "w") as low:
        high.write("v2.0 raw\n")
        low.write("v2.0 raw\n")
        for row in reader:
            address = int(row["address"], 16)
            value = row["hex"]

            if address % 2 == 0:
                high.write(value + "\n")
            else:
                low.write(value + "\n")