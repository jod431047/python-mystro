'''
game :
-wlcome massage to user
-show games
-user can play :game number
-option to exit
-ask play agin
games :
-sentence no duplicate
-names ---> list[count]
-x,y :1-->100
''' 


from typing import Self


class Game :
    def __init__(self):
        print('''welcome to our game
        1 :Sentence No Duplicate
        2 :Names List Count
        3 :Divided By
        ''') 
    user_choice =int (input('Enter Game Number :'))
    if user_choice == 1 :
        sentence = input('Enter sentence :')
    Self.no_duplicate()

    def no_duplicate(self,sentence):
        words = sentence.split(' ')
        new_words =[]
        for w in words :
            if w in new_words:
                continue
            else:
                new_words.append(w)

                new_sentence = ' '.join(new_words)
                print(new_sentence)

    def names_count(self,names):
        count = []
        for n in names:
            count.append(len(n))
        print(count) 


    def divided_by(self,x,y):
        result =[]
        for n in range(1,101):
            if n%x ==0 and n%y == 0:
                result.append(n)
        print(result)   

g1 = Game()






#duplicate('my name is is is jihad') 
#names_count(['ahmad','ali','jihad'])   
#divided_by(5,6)