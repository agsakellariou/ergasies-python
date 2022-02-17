import random

sump1 = 0
sump2 = 0
sumd = 0
sump12 = 0
sump22 = 0
sumd2 = 0

for i in range(100):

    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        #print (player1)
        for card in player1:
            if card[0] in figures: 
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(sum1)
    if sum1>21:
        print("P2 wins!")
        sump2 = sump2 + 1
    else:
        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            sump1 = sump1 + 1
        elif sum2>sum1:
            print("P2 wins!")
            sump2 = sump2 + 1
        else:
            print("draw!")
            sumd = sumd + 1

print("Με κανονικό μοίρασμα:")            
print("Ο πρώτος παίκτης κερδίζει σε",sump1,"παιχνίδια")
print("Ο δεύτερος παίκτης κερδίζει σε",sump2,"παιχνίδια")
print("Ισοπαλία έχουμε σε",sumd,"παιχνίδια")
         
for i in range(100):

    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    
    xartia1 = []
    xarti1 = ["10", "J", "Q", "K"]
    for i in xarti1:
        for j in color:
            xartia1.append([i,j])

    random.shuffle(xartia)
    random.shuffle(xartia1)
    
    player1=[]
    sum1=0
    player1.append(xartia1.pop())
    for i in xarti:
        if i == player1[0]:
            for j in color:
                if j == player1[1]:
                    xartia.remove([i,j])
    sum1 = sum1 + 10
    print(sum1)
    
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        #print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+int(card[0])
        print(sum1)
        
    if sum1>21:
        print("P2 wins!")
        sump22 = sump22 + 1
    else:
        print("P2 joins the game") #let me add one more player

        xartia2 = []
        xarti2 = [i for i in range(1, 10)]
        for i in xarti2:
            for j in color:
                xartia2.append([i,j])
        random.shuffle(xartia2)
        player2=[]
        sum2=0

        player2.append(xartia2.pop())
        for i in xarti:
            if i == player2[0]:
                for j in color:
                    if j == player2[1]:
                        xartia.remove([i,j])
        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
        
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            sump12 = sump12 + 1
        elif sum2>sum1:
            print("P2 wins!")
            sump22 = sump22 + 1
        else:
            print("draw!")
            sumd2 = sumd2 + 1

print("Πειραγμένο μοίρασμα ώστε ο πρώτος παίκτης να ξεκινάει με 10 ή φιγούρα (J,Q, K) και ο δεύτερος ποτέ με 10 ή φιγούρα:")
print("Ο πρώτος παίκτης κερδίζει σε",sump12,"παιχνίδια")
print("Ο δεύτερος παίκτης κερδίζει σε",sump22,"παιχνίδια")
print("Ισοπαλία έχουμε σε",sumd2,"παιχνίδια")

