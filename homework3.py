import random
while True:
    name=input("Enter your name:")
    print(f"Welcome {name.title()}")
    countries=["Switzerland","Zimbabwe","Portugal","Jamaica"]
    fruits=["Pineapple","Watermelon","Strawberry","Pomegranate"]
    animals=["Crocodile","Elephant","Antilope","Chimpanzee"]

    session=input("Select your Session; Press C for Countries, F for Fruits, A for Animals: ")
    if session.upper()=="C":
        selected_session=countries
    elif session.upper()=="F":
        selected_session=fruits
    elif session.upper()=="A":
        selected_session=animals
    else:
        print("No session selected.The game won't start.")
        break

    selected_word=selected_session[random.randint(0,len(selected_session)-1)]
    print(selected_word)
    print("__\n |\n O \n/|\\ \n |\n/ \\")
    print("Let's Start the Game")
    guess=[]
    for m in range(0,len(selected_word)):
        guess.append("_")
    hata=0
    for i in range(0,15):
        print("Enter a letter: ")
        x=input()
        if x in selected_word or x.upper() in selected_word[0]:
            for b in range(0,len(selected_word)):
                if x==selected_word[b] or x==selected_word[b].lower():
                    guess[b]=x
            listToStr=" ".join([str(elem) for elem in guess])
            print(listToStr) 
            if guess==list(selected_word) or guess==list(selected_word.lower()):
                print("Congratulations, YOU WON!")
                break       
            print("\n")
        else:
            if hata==0:
                print("__\n |\n O")
                hata=hata+1
            elif hata==1:
                print("__\n |\n O \n |")
                print(listToStr) 
                hata=hata+1
            elif hata==2:
                print("__\n |\n O \n/|")
                print(listToStr) 
                hata=hata+1
            elif hata==3:
                print("__\n |\n O \n/|\\")
                print(listToStr) 
                hata=hata+1
            elif hata==4:
                print("__\n |\n O \n/|\\ \n |")
                print(listToStr) 
                hata=hata+1
            elif hata==5:
                print("__\n |\n O \n/|\\ \n |\n/")
                print(listToStr)
                hata=hata+1
            elif hata==6:
                print("__\n |\n O \n/|\\ \n |\n/ \\")
                print(listToStr) 
                print("You Failed.The word was \"{}\"".format(selected_word))
                break
    last=input("Press X for Quit: ")
    if last.upper()=="X":
        exit()






