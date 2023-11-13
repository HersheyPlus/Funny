import random
import string
#! Sentence

def sentences():
    round_of_sentence = int(input("Enter round of sentence: "))
    start_sentence = int(input("Enter start sentence (set): "))
    end_sentence =  int(input("Enter end sentence (set): "))
    for i in range(round_of_sentence):
        random_nubmer = random.randint(start_sentence,end_sentence)
        print("Sentence Set:",random_nubmer)
    print("--------------------------------------")
    
#! New word
def newWords():
    round_of_new_word = int(input("Enter round of new word: "))
    start_new_word = int(input("Enter start new word: "))
    end_new_word =  int(input("Enter end new word: "))
    for i in range(round_of_new_word):
        random_new_word = random.randint(start_new_word,end_new_word)
        print("New Word Set:",random_new_word)
    print("--------------------------------------")
    
#! Character
def groupWords():
    random_oxford  = random.choice(string.ascii_lowercase)
    set_of_verb = ["N & M","S1","S2","T","W","R","Q U V Y Z","P","O","J & K & L","I","H","G","F",   "E","D","C1","C2","B","A","Kithecn",1,2,3,4,5,6]
    random_verb = random.choice(set_of_verb)
    print("Oxford Set:",random_oxford)
    print("Verb Set:",random_verb)
    print("--------------------------------------")

    round_of_group_words = int(input("Enter round of group word: "))
    set_of_group_words = [
        "Taste of Food","Color","Meat","Plant","Festival","Sport","Health","Place","Status",    "Career 2",
        "Career","Cloth","Season","Shape","Drink","Constructon","Course & Subject","Body",  "Mechanic equipment]","Education Aid",
        "Summer","Month","Lavatory","Family","Animal","Weather","Transporation","Habitation",   "Vegetable","Injuries",
        "Narutal disaster","Shop","Room","Education","House equipment","Bedroom","Animal (adult     and little)","Electrical","Landform","Rainy",
        "Winter","Kitchen","At gas station","Driving","Daily routine","Verb daily","Movement",  "Brushing tooth","Laundry","Wash body",
        "Sleeping","Get dressed",
    ]
    for i in range(round_of_group_words):
        random_group_words = random.choice(set_of_group_words)
        print("Group Words Set:",random_group_words)

sentences()
newWords()
groupWords()