import json

file = open("dictionary.txt", "r")
contents = file. read()
data = contents
dic = contents.split("\n")

Dict = {}
for i in range(len(dic)):
    Dict[i] = json.loads(dic[i])
filt ='abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,-:'
data =''.join(filter(filt.__contains__,data))
file.close()

Keys = Dict[0].keys()
Items = Dict[0].items()

print("Τα διαθέσιμα κλειδιά είναι:")
for x in Keys:
    print(x)
key = input("Ποιο από τα διαθέσιμα κλειδιά σας ενδιαφέρει:")

value2 = data.split("\n")
value = []
for i in range(len(value2)):
    val = value2[i].split(",")
    for j in range(len(val)):
        value.append(val[j])
Value = []
for i in range(len(value)):
    val = value[i].split(":")
    for j in range(len(val)):
        Value.append(val[j])

apot = ["" for i in range(len(dic))]
k = 0
for i in range(len(Value)-1):
    if Value[i] == key:
        apot[k] = Value[i+1]
        k = k + 1

integer_map = map(int, apot)
integer_list = list(integer_map)

print("Η μεγαλύτερη τιμή του κλειδιού είναι:",max(integer_list))
print("Η μικρότερη τιμή του κλειδιού είναι:",min(integer_list))

def most_frequent(apot):
    return max(set(apot), key = apot.count)
 
print("Η δημοφιλέστερη τιμή του κλειδιού είναι:",most_frequent(apot))

