import random
def nextlettergen():
    nextletter=letlist[lastlet][random.randint(0,len(letlist[lastlet])-1)]
    return nextletter
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letlist=[["B","C","D","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"],
         ["A","E","I","O","R","U","Y"],
         ["A","E","H","I","K","L","O","R","U","Y"],
         ["A","E","I","O","R","U","Y"],
         ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"],
         ["A","E","I","L","O","R","U","Y"],
         ["A","E","I","L","O","R","U","Y",],
         ["A","E","I","O","U","Y"],
         ["A","B","C","D","F","G","J","K","L","M","N","O","P","Q","R","S","T","V","X","Z"],
         ["A","E","I","O","U"],
         ["A","E","I","L","O","R","U","Y"],
         ["A","E","I","O","U","Y"],
         ["A","E","I","O","U","Y"],
         ["A","E","I","O","U","Y"],
         ["B","C","D","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"],
         ["A","E","H","I","L","O","R","U","Y"],
         ["U"],
         ["A","E","I","O","U","Y"],
         ["A","E","I","O","U","Y"],
         ["A","E","H","I","O","R","U","Y"],
         ["B","C","D","F","G","H","J","K","L","M","N","P","R","S","T","V","X","Z"],
         ["A","E","I","O","U","Y"],
         ["A","E","I","O","U","Y"],
         ["A"],
         ["A","E","I","O","U"],
         ["A","E","I","O","U","Y"]]
vowels=["A","E","I","O","U"]
while True:
    length=("")
    while length==("")or length==("0"):
        length=input("Length: ")
    length=int(length)
    word=[]
    word.append(alphabet[random.randint(0,25)])
    length-=1
    while length!=0:
        lastlet=word[len(word)-1]
        lastlet=ord(lastlet)
        lastlet-=65
        if len(word)>1 and word [len(word)-2]== "Q":
            word.append(vowels[random.randint(0,3)])

        else:
            nextletter=nextlettergen()
            while nextletter in vowels and word[len(word)-1]in vowels and word[len(word)-2]in vowels:
                nextletter=nextlettergen()
            while nextletter=="Q" and length<=2:
                nextletter=nextlettergen()
            word.append(nextletter)
        length-=1
    first=True
    for letter in word:
        if first==True:
            print(letter, end="")
        else:
            print(letter.lower(), end="")
        first=False
    print("\n")
