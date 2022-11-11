stream = [1, 2, 3, 4, 5, 6, 4, 2, 5, 9, 1, 6, 3, 7, 1, 2, 2, 4, 2, 1]
print('Using Flajolet Martin Algorithm:')

maxnum = 0
for i in range(0, len(stream)):
    val = bin(3*stream[i] + 6)[2:] # 3*x + 6
    su = 0
    for char in str(val)[::-1]:
        if char == '0': su += 1
        else: break
    if su > maxnum:
        maxnum = su
 
print("Distinct elements are : ", 2**maxnum)