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

def no_duplicate(sentence):
    words = sentence.split(' ')
    new_words =[]
    for w in words :
        if w in new_words:
            continue
        else:
            new_words.append(w)

            new_sentence = ' '.join(new_words)
            print(new_sentence)

#no_duplicate('my name is is is jihad') 


def names_count(names):
    count = []
    for n in names:
        count.append(len(n))
    print(count) 

#names_count(['ahmad','ali','jihad'])   
