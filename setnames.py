names = {"Sorena", "Kave", "Pendar"}
names.add("Dara")
result = names.difference({"Kave"})
print(result)
names.discard("Korosh")
print(names)

group1 = {"Sorena", "Kave", "Dara"}
group2 = {"Korosh", "Adan", "Sorena"}
print(group1.union(group2))
print(group1.intersection(group2))