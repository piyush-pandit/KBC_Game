kbc_dict = {1:["Which among the following river originated in India?", "a) Ganga b) Sutlej c) Chenab d) Brahmaputra", "c"],
            2:["How many times a person can attempt for re-election as the President of India?", "a) Only thrice b) Only once c) Only twice d) Any number of times", "d"],
            3:["The stranger gas is also known as_____.", "a) Xenon b) Argon c) Helium d) Neon", "a"],
            4:["A compact disc (CD) is a type of _____ storage media.", "a) Electrical b) Magnetic c) Optical d) None of these", "c"],
            5:["The British established their first factory in Surat with the permission of ___.", "a) Jahangir b) Sher Shah Suri c) Hemu d) Shah Jahan", "a"],
            6:["Which of the following is not an endocrine gland?", "a) Pituitary gland b) Pancreas c) Pineal gland d) None of these", "d"],
            7:["Which of the following does not produce hormone?", "a) Heart b) Kidney c) Gastro-intestinal tract d) None of these", "d"],
            8:["Who among the following Viceroys wrote the book ‘Problems of the East’?", "a) Lord Curzon b) Lord Clive c) Lord Mayo d) Lord Mountbatten", "a"],
            9:["The speaker of the Lok Sabha appoints who among the following?", "a) Leader of Opposition b) Prime minister c) Two members of the Anglo-Indian community d) Deputy Speaker of the Lok Sabha", "a"],
            10:["King Simuka was the founder of______.", "a) Satavahana dynasty b) Sunga dynasty c) Chola dynasty d) Kanva dynasty", "a"]}
result = 0

name = input ("Enter your name please :-")
print ("Hello " + name +  " You have to answer all the 10 questions correctly to win this game ")
lets_play_kbc = input("Do you want to continue? (Y/N) or (yes/no) : - ")
print ("\n \n")

if (lets_play_kbc.lower()[0] == "y"):
    for index in range(1,11):
        print(f"Your {index} question is :- ")
        print(kbc_dict[index][0])
        print("your options are :-")
        print(kbc_dict[index][1])
        answer = input ("Enter correct options :-")
        if (answer.lower() == kbc_dict[index][2]):
            print ("Yey!... your answer is Correct")
            result = result + 1
        else: 
            print("Sorry!... you have entered wrong answer")
            break

        if (index != 10):
            play_along = input("Do you want to continue or not (Y/N) : -")
            if(play_along.lower()[0] == "y"):
                print("")
            else:
                break
        
    print(f"Your result is {result}/10, You Won the game...! ")

else:
    print("OK Thankyou !, See you soon.....")