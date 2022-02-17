f = open("two_cities_ascii.txt", "r")
data = f.read()
f.close

data2 = "abc"

byte_list = ''.join(format(ord(i), '07b') for i in data)
#print(byte_list)

max0 = 1
max1 = 1
pl0 = 1
pl1 = 1

for i in range(len(byte_list)-1):
    if byte_list[i] == byte_list[i+1] == "0":
        pl0 = pl0 + 1
    else:
        pl0 = 1
    if pl0 > max0:
        max0 = pl0

    if byte_list[i] == byte_list[i+1] == "1":
        pl1 = pl1 + 1
    else:
        pl1 = 1
    if pl1 > max1:
        max1 = pl1
        
print('Η μεγαλύτερη ακολουθία από συνεχόμενα 0 είναι:',max0)
print('Η μεγαλύτερη ακολουθία από συνεχόμενα 1 είναι:',max1)
