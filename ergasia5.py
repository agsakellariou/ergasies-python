#επεξεργασία ώστε να σας μείνει κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά) και τον κενό χαρακτήρα (space)

f = open("two_cities_ascii.txt", "r")
data = f.read()
filt ='abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ'
data=''.join(filter(filt.__contains__,data))
f.close()
file = data.lower()

#οι δέκα δημοφιλέστερες λέξεις
gram = file.split("\n")

words = []
for i in range(len(gram)):
    lista = gram[i].split(" ")
    for j in range(len(lista)): 
        words.append(lista[j])
words.sort()

word = [words[0]]
for i in range(len(words)-1):
    if words[i+1] != words[i]:
        word.append(words[i+1])
word.remove("")

pl = [0 for i in range(len(word))]
for i in range(len(word)):
    for j in range(len(words)):
        if word[i] == words[j]:
            pl[i] = pl[i] + 1            

word.sort(key=dict(zip(word, pl)).get)

print("Οι δέκα δημοφιλέστερες λέξεις είναι:")
for i in range(10):
   print(word[len(word)-i-1])

#οι τρεις πρώτοι συνδυασμοί των δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις

plgr = [0 for i in range(len(word))]
for i in range(len(word)):
    for j in range(len(word[i])):
        plgr[i] = plgr[i] + 1

letters1 = []
for i in range(len(word)):
    if plgr[i] >= 2:
        for j in range(0,2):
            letters1.append(word[i][j])

j = 0
le = len(letters1)//2
letters2 = ["" for i in range(le)]
for i in range(1,len(letters1),2):
    letters2[j] = letters1[i-1] + letters1[i]
    j = j + 1
letters2.sort()

letter2 = [letters2[0]]
for i in range(len(letters2)-1):
    if letters2[i+1] != letters2[i]:
        letter2.append(letters2[i+1])

pl2 = [0 for i in range(len(letter2))]
for i in range(len(letter2)):
    for j in range(len(letters2)):
        if letter2[i] == letters2[j]:
            pl2[i] = pl2[i] + 1
            
letter2.sort(key=dict(zip(letter2, pl2)).get)
print("Οι τρεις πρώτοι συνδυασμοί των δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι:")
for i in range(3):
   print(letter2[len(letter2)-i-1])

#οι τρεις πρώτοι συνδυασμοί των τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις

letters4 = []
for i in range(len(word)):
    if plgr[i] >= 3:
        for j in range(0,3):
            letters4.append(word[i][j])
            
k = 0
le2 = len(letters4)//3
letters3 = ["" for i in range(le2)]
for i in range(2,len(letters4)+1,3):
    letters3[k] = letters4[i-2] + letters4[i-1] + letters4[i]
    k = k + 1
letters3.sort()

letter3 = [letters3[0]]
for i in range(len(letters3)-1):
    if letters3[i+1] != letters3[i]:
        letter3.append(letters3[i+1])

pl3 = [0 for i in range(len(letter3))]
for i in range(len(letter3)):
    for j in range(len(letters3)):
        if letter3[i] == letters3[j]:
            pl3[i] = pl3[i] + 1

letter3.sort(key=dict(zip(letter3, pl3)).get)
print("Οι τρεις πρώτοι συνδυασμοί των τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι:")
for i in range(3):
   print(letter3[len(letter3)-i-1])