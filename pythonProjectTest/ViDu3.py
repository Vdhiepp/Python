#In ra các số chẵn <= 100
i = 1
for i in range(1, 101):
    if i % 2 != 0:
        continue
    print("%d" % i)
