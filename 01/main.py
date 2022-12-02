INPUT_FILE = "input.txt"

elf_list = []
elf_tmp = []

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        try:
            item_cals = int(line.strip())
            elf_tmp.append(item_cals)
        except ValueError:
            elf_list.append(sum(elf_tmp))
            elf_tmp.clear()
    # Append last elf before closing filehandle
    elf_list.append(sum(elf_tmp))

print(f"Max: {max(elf_list)}")
print(f"Top 3: {sum(sorted(elf_list, reverse=True)[:3])}")
