nums = int(input())
hasil = 0
while nums > 0:
    a = nums%10
    hasil = hasil+a
    nums = nums//10
while hasil>=9:
    a = hasil%10
    hasil = hasil//10
    hasil = hasil + a
print(hasil)