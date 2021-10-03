import random

                   
print("\n\nWelcome To Guessing Game !! ");
print("\nRemember You Will Be given  6 Lives !!\n\n");

stages=['''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list=["ardvark","baboon","camel","wildcraft"];

# For selecting random word 
word_1=str(random.choice(word_list));
# Initialing a empty list
str1=[];
# adding '_' as number of times as the size of word 
for i in range (0,len(word_1)):
 str1+='_';

print(str1,end='\n\n'); 
live1=6;
liv=0;
while 1 and live1>liv:
  if('_' not in str1):
    break;
  check1=0;  
  guess_1=input("\nGuess the Word : ").lower();      
  for i in range(len(word_1)) :
    if guess_1==word_1[i] and str1[i] =='_':
        str1[i]=guess_1;
        check1=1;
  if(check1==1):
    print(str1,end='\n');
  else :
      
    print(stages[liv]);
    print(f"----Remaining lives are ---> {live1-liv-1}");
    liv+=1;
if(liv<live1):    
 print("\nYou Win !!\n");

else:
 print("\nYou Lose !!\n");       


