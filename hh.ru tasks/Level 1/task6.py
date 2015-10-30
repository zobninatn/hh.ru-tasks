'''
Рассмотрим все возможные числа a**b для 1<a<6 и 1<b<6:
2**2=4, 2**3=8, 2**4=16, 2**5=32 3**2=9, 3**3=27, 3**4=81, 3**5=243 4**2=16,
 4**3=64, 4**4=256, 4**5=1024, 5**2=25, 5**3=125, 5**4=625, 5**5=3125
Если убрать повторения, то получим 15 различных чисел.

Сколько различных чисел ab для 2<a<128 и 2<b<126?
'''
container = []
for a in range(3, 128):
    for b in range(3, 126):
        container.append(a**b)

sorted_container = []
for integer in container:
    if integer not in sorted_container:
        sorted_container.append(integer)

print(len(sorted_container))

#14585
