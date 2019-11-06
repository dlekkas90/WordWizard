# -*- coding: utf-8 -*-
"""
Created on Tue May 01 18:10:23 2018

@author: dlekk
"""
import random
import time

print '\n', '~PROGRAM INITIALIZED~', '\n'

print 'WORDWIZARD (v1.2)'
print '[Conceived and coded by Damien Lekkas (c) 2018]', '\n' 

print '+-------------------------BASIC GAME INSTRUCTIONS-------------------------------+'
print '|', '\t'*10, '|'
print '| Utilize the ten letters drawn at random to create words! Each player\'s', '\t', '|'
print '| score will be based on the length of the words created as well as the', '\t', '|' 
print '| sum of the corresponding values of the letters utilized. The letter', '\t'*2, '|' 
print '| values will adopt the Scrabble(tm) point system. Word length bonuses', '\t'*2, '|'
print '| adopt the following scoring scheme:', '\t'*6, '|'
print '|', '\t'*10, '|'
print '| 5 letters = +5 points', '\t'*7, '|'
print '| 6 letters = 2X word score', '\t'*7, '|'
print '| 7 letters = 3X word score', '\t'*7, '|'
print '| 8 letters = 4X word score', '\t'*7, '|'
print '| 9 letters = 5X word score', '\t'*7, '|'
print '| 10 letters = 5X word score + 50 points', '\t'*5, '|'
print '|', '\t'*10, '|'
print '| In addition to entering words with the letters in possession, one may', '\t', '|' 
print '| also invoke the following COMMANDS during their turn at their', '\t'*2, '|'
print '| discretion:', '\t'*9, '|'
print '|', '\t'*10, '|'
print '| \'-s\' will allow a player to randomly shuffle their current letters;', '\t'*2, '|' 
print '| this can be done as many times as desired without penalty', '\t'*3, '|'
print '|', '\t'*10, '|'
print '| \'-re\' will allow a player to place all current letters into the bag', '\t'*2, '|' 
print '| and resample for a 10 point penalty; the player will not lose their', '\t'*2, '|' 
print '| turn, however, this can only be done once per turn', '\t'*4, '|'                               
print '|', '\t'*10, '|'
print '| \'-forfeit\' will allow a player to forfeit the game and incur a loss', '\t'*2, '|'
print '|', '\t'*10, '|'
print '+-------------------------------------------------------------------------------+', '\n'
raw_input()
print '+---------------ADDITIONAL RULES AND CONVENTIONS TO KEEP IN MIND----------------+'
print '|', '\t'*10, '|'
print '| (i) Each player has a soft 2 minute time limit each turn. Failure to', '\t'*2, '|'
print '| enter a valid move within 2 minutes will result in score penalties', '\t'*2, '|' 
print '| that increase in severity by 5 points for every additional 15 seconds.', '\t', '|'
print '| A player taking more than 3 minutes will incur a 35 point penalty.', '\t'*2, '|' 
print '|', '\t'*10, '|'
print '| (ii) The player with the least amount of overall turn-time elapsed at', '\t', '|'
print '| the end of the game will receive a 25 point bonus to their final score.', '\t', '|'
print '|', '\t'*10, '|'
print '| (iii) The end of the game is defined by an empty letter bag at the end', '\t', '|'
print '| of Player 2\'s turn. Any and all letters remaining with each player at', '\t', '|'
print '| game\'s end will result in a point penalty that is equivalent to the', '\t'*2, '|'
print '| sum of the values for each player\'s respective letters.', '\t'*3, '|'     
print '|', '\t'*10, '|'
print '| (iv) Each player will only be allowed to redraw once per turn.', '\t'*2, '|'
print '|', '\t'*10, '|'
print '| (v) If a player guesses a word that is invalid, either due to a lack', '\t'*2, '|'
print '| of requisite letters or a word not found in the official Scrabble(tm)', '\t', '|'
print '| dictionary, they will lose 5 points for each offense as well as the', '\t'*2, '|'
print '| ability to shuffle or redraw during their current turn.', '\t'*3, '|'
print '|', '\t'*10, '|'
print '+-------------------------------------------------------------------------------+'
raw_input()
print '\n'
#----------------INITIALIZE DICTIONARY OF WORDS WITH SCORE VALUES--------------
letter_scores = {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 'L' : 1, 'N' : 1,
                 'S' : 1, 'T' : 1, 'R' : 1, 'D' : 2, 'G' : 2, 'B' : 3, 'C' : 3,
                 'M' : 3, 'P' : 3, 'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
                 'K' : 5, 'J' : 8, 'X' : 8, 'Q' : 10, 'Z' : 10}

all_words = open('30_sowpods.txt').readlines()
all_words = [s.rstrip() for s in all_words]
word_value_dict = {}

for word in all_words:
    value = 0
    for letter in word:
        value = value + letter_scores[letter]         
        
    word_value_dict[word] = value             


print '+-----------------PARAMETER DEFINITION AND GAME INITIALIZATION------------------+', '\n'
print ' Set the desired length of your match - this will scale the size of the'
print ' letter bag from which you will draw (1 = very short, 2 = short, 3 = average'
print ' 4 = long, 5 = very long): '
x = input(' ...') 

while x not in range(1,6):
    x = input(' Please enter a valid value (1-5): ')

print '\n'
raw_input(' Ok! Press any key when you are ready to begin the game.')
print '+-------------------------------------------------------------------------------+', '\n'

#-------------------------INITIALIZE LETTER BAG--------------------------------
letter_bag = x * (['A']*9 + ['E']*12 + ['I']*9 + ['O']*8 + ['U']*4 + ['L']*4 + ['N']*6 + ['S']*4 + ['T']*6 + ['R']*6 + ['D']*4 + ['G']*3 + ['B']*2 + ['C']*2 + ['M']*2 + ['P']*2 + ['F']*2 + ['H']*2 + ['V']*2 + ['W']*2 + ['Y']*2 + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z'])

#-----------------------DISTRIBUTE STARTING LETTERS TO PLAYERS-----------------
p1_letters = []
p2_letters = []
for x in range(10):
    p1_random = random.randint(0, len(letter_bag)-1)
    p1_letters.append(letter_bag[p1_random])
    letter_bag.remove(letter_bag[p1_random])

for y in range(10):
    p2_random = random.randint(0, len(letter_bag)-1)
    p2_letters.append(letter_bag[p2_random])
    letter_bag.remove(letter_bag[p2_random]) 

print '\n', 'Player 1 has drawn the following starting letters:', ' '.join(p1_letters), '\n'
print 'Player 2 has drawn the following starting letters:', ' '.join(p2_letters), '\n'*2 
                                                           
#ACCEPT INPUT AND TALLY SCORE UNTIL THERE ARE NO MORE LETTERS REMAINING IN THE BAG                                                           

p1_score = 0
p1_wordlist = []
p1_wordscores = []
p1_start_time = 0
p1_end_time = 0
p1_elapsed = 0
p1_game_time = 0

p2_score = 0
p2_wordlist = []
p2_wordscores = []
p2_start_time = 0
p2_end_time = 0
p2_elapsed = 0
p2_game_time = 0

game_round = 0
forfeit = False

print '                       [', str(len(letter_bag)), 'letters remain in the bag ]', '\n'*2  

while len(letter_bag) > 0:
    game_round += 1
    
#---------------------------PLAYER 1 PHASE-------------------------------------    
    print '+-------------------------- PLAYER 1 ROUND', str(game_round), 'START ----------------------------+' 
    print '                        <<<<< Current Score:', str(p1_score), '>>>>>', '\n'
    print '\n'*2, '\t'*2, '   ', '   '.join(p1_letters), '\n'*2
    
#PLAYER 1 TIMER START
    p1_start_time = time.time()
                  
    p1_word_input = raw_input('Enter a word or valid command: ')
    p1_word_input = p1_word_input.upper()

#ALLOW PLAYER 1 TO SHUFFLE CURRENT LETTERS
    while p1_word_input == '-S':
        random.shuffle(p1_letters)
        print '\n'*2, '\t'*2, '   ', '   '.join(p1_letters), '\n'*2 
        p1_word_input = raw_input('Enter a word or valid command: ')
        p1_word_input = p1_word_input.upper()                       

#ALLOW PLAYER 1 TO REDRAW LETTERS FOR A PENALTY
    if p1_word_input == '-RE':
        p1_score = p1_score - 10
        
        for letter in p1_letters:
            letter_bag.append(letter)
    
        p1_letters = []
    
        if len(letter_bag) > 9:
            for x in range(10):
                p1_random = random.randint(0, len(letter_bag)-1)
                p1_letters.append(letter_bag[p1_random])
                letter_bag.remove(letter_bag[p1_random])
        
        else:
             for x in range(len(letter_bag)):
                p1_random = random.randint(0, len(letter_bag)-1)
                p1_letters.append(letter_bag[p1_random])
                letter_bag.remove(letter_bag[p1_random])       
        
        print 'Player 1 has redrawn the following letters:', ' '.join(p1_letters), '\n'
        print '                        <<<<< Current Score:', str(p1_score), '>>>>>', '\n'
        print '\n'*2, '\t'*2, '   ', '   '.join(p1_letters), '\n'*2 
        
        p1_word_input = raw_input('Enter a word or valid command: ')
        p1_word_input = p1_word_input.upper()    

#ALLOW PLAYER 1 TO SHUFFLE REDRAWN LETTERS
    while p1_word_input == '-S':
        random.shuffle(p1_letters)
        print '\n'*2, '\t'*2, '   ', '   '.join(p1_letters), '\n'*2 
        p1_word_input = raw_input('Enter a word or valid command: ')
        p1_word_input = p1_word_input.upper()   
        
#ALLOW PLAYER 1 TO FORFEIT
    if p1_word_input == '-FORFEIT':
        print '\n', 'Player 1 forfeits!', '\n'
        forfeit = True
        break

#CHECK FOR VALID LETTER USAGE FOR PLAYER 1       
    letter_check = True    
    word_check = True
    
    while letter_check == True or word_check == True:
        if letter_check == True:    
            letter_mismatch = 0
            redundancy_counter_p1 = 0
            redundancy_check_p1 = [letter for letter in p1_letters]  
            
            for letter in p1_word_input:
                if letter in redundancy_check_p1:
                    redundancy_check_p1.remove(letter)
                
                elif letter not in redundancy_check_p1:
                    redundancy_counter_p1 += 1
                
                if letter not in p1_letters:
                    letter_mismatch += 1
 
            if letter_mismatch > 0:
                p1_score = p1_score - 5
                print '-5 POINTS'
                p1_word_input = raw_input('That is invalid given your current letters! Enter a valid word: ').upper()
                
            
            elif redundancy_counter_p1 > 0:
                p1_score = p1_score - 5
                print '-5 POINTS'
                p1_word_input = raw_input('That is invalid given your current letters! Enter a valid word: ').upper()
                
            else:
                letter_check = False

#CHECK FOR VALID WORD ENTRY FOR PLAYER 1
        if word_check == True and letter_check == False: 
            if p1_word_input not in word_value_dict:
                p1_score = p1_score - 5
                print '-5 POINTS'
                p1_word_input = raw_input('That\'s not in the dictionary! Enter a valid word: ').upper()
                letter_check = True
            else:
                word_check = False
                
#IF VALID, SCORE WORD, REMOVE USED LETTERS FROM PLAYER 1, AND REPLENISH WITH NEW LETTERS OF APPROPRIATE AMOUNT FROM BAG                       
    if p1_word_input in word_value_dict:
        p1_wordlist.append(p1_word_input)
        print '\n'
        for letter in p1_word_input: 
            print '\t'*4, letter, ': +', str(letter_scores[letter])
        print '\t'*4, '-------------'
        print '\t'*4, word_value_dict[p1_word_input], 'POINTS!', '\n'
        
        if len(p1_word_input) == 5:
            print '+5 word length bonus!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] + 5)
            p1_score = p1_score + word_value_dict[p1_word_input] + 5
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif len(p1_word_input) == 6:
            print '2X word length bonus!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] *2)
            p1_score = p1_score + word_value_dict[p1_word_input] * 2
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3
        
        elif len(p1_word_input) == 7:
            print '3X word length bonus!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] * 3)
            p1_score = p1_score + word_value_dict[p1_word_input] * 3
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif len(p1_word_input) == 8:
            print '4X word length bonus!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] * 4)
            p1_score = p1_score + word_value_dict[p1_word_input] * 4
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif len(p1_word_input) == 9:
            print '5X word length bonus!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] * 5)
            p1_score = p1_score + word_value_dict[p1_word_input] * 5
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif len(p1_word_input) == 10:
            print '5X word length bonus!'
            print '+50 FULL CLEAR BONUS!', '\n'
            p1_wordscores.append(word_value_dict[p1_word_input] * 5 + 50)
            p1_score = p1_score + word_value_dict[p1_word_input] * 5 + 50
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        else:
            p1_wordscores.append(word_value_dict[p1_word_input])
            p1_score = p1_score + word_value_dict[p1_word_input]
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
    
#PLAYER 1 TIME END AND PENALTY APPLICATION
        p1_end_time = time.time()
        p1_elapsed = round(p1_end_time - p1_start_time)
        p1_game_time = p1_game_time + p1_elapsed
        
        if p1_elapsed > 120 and p1_elapsed < 135:
            p1_score = p1_score - 5 
            print 'Player 1 took too long!', str(p1_elapsed), 'seconds elapsed!'
            print '-5 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif p1_elapsed > 135 and p1_elapsed < 150:
            p1_score = p1_score - 10 
            print 'Player 1 took too long!', str(p1_elapsed), 'seconds elapsed!'
            print '-10 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        elif p1_elapsed > 150 and p1_elapsed < 165:
            p1_score = p1_score - 15 
            print 'Player 1 took too long!', str(p1_elapsed), 'seconds elapsed!'
            print '-15 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3

        elif p1_elapsed > 165 and p1_elapsed < 180:
            p1_score = p1_score - 20 
            print 'Player 1 took too long!', str(p1_elapsed), 'seconds elapsed!'
            print '-20 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3
        
        elif p1_elapsed > 180:
            p1_score = p1_score - 35
            print 'Player 1 took way too long!', str(p1_elapsed), 'seconds elapsed!'
            print '-35 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p1_score, '>>>>>', '\n'*3 
        
        for i in p1_word_input:
            p1_letters.remove(i)
        
        if len(p1_word_input) > len(letter_bag) and len(letter_bag) != 0:
            for j in range(len(letter_bag)):
                p1_random = random.randint(0, len(letter_bag)-1)
                p1_letters.append(letter_bag[p1_random])
                letter_bag.remove(letter_bag[p1_random])
        
        elif len(p1_word_input) == len(letter_bag) and len(letter_bag) != 0:
            for j in range(len(letter_bag)):
                p1_random = random.randint(0, len(letter_bag)-1)
                p1_letters.append(letter_bag[p1_random])
                letter_bag.remove(letter_bag[p1_random])
        
        elif len(p1_word_input) < len(letter_bag):
            for j in range(len(p1_word_input)):
                p1_random = random.randint(0, len(letter_bag)-1)
                p1_letters.append(letter_bag[p1_random])
                letter_bag.remove(letter_bag[p1_random])
        
        elif len(p1_word_input) > len(letter_bag) and len(letter_bag) == 0:
            continue
    
    print '+-------------------------- PLAYER 1 ROUND', str(game_round), 'END ------------------------------+', '\n'*2
    print '[  Player 1 Score:', p1_score, ' ]', '\t'*3, '       ', '[  Player 2 Score:', p2_score, ' ]', '\n'                                                       
    print '                       [ ', str(len(letter_bag)), 'letters remain in the bag  ]', '\n'*2        

#------------------------------PLAYER 2 PHASE----------------------------------   
    print '+-------------------------- PLAYER 2 ROUND', str(game_round), 'START ----------------------------+' 
    print '                       <<<<< Current Score:', str(p2_score), '>>>>>', '\n'
    print '\n'*2, '\t'*2, '   ', '   '.join(p2_letters), '\n'*2  
    
#PLAYER 2 TIMER START
    p2_start_time = time.time()
                            
    p2_word_input = raw_input('Enter a word or valid command: ')
    p2_word_input = p2_word_input.upper()

#ALLOW PLAYER 2 TO SHUFFLE CURRENT LETTERS
    while p2_word_input == '-S':
        random.shuffle(p2_letters)
        print '\n'*2, '\t'*2, '   ', '   '.join(p2_letters), '\n'*2
        p2_word_input = raw_input('Enter a word or valid command: ')
        p2_word_input = p2_word_input.upper()   

#ALLOW PLAYER 2 TO REDRAW LETTERS FOR A PENALTY
    if p2_word_input == '-RE':
        p2_score = p2_score - 10
        
        for letter in p2_letters:
            letter_bag.append(letter)
        
        p2_letters = []    
        
        if len(letter_bag) > 9:
            for y in range(10):
                p2_random = random.randint(0, len(letter_bag)-1)
                p2_letters.append(letter_bag[p2_random])
                letter_bag.remove(letter_bag[p2_random])

        else:
            for y in range(len(letter_bag)):
                p2_random = random.randint(0, len(letter_bag)-1)
                p2_letters.append(letter_bag[p2_random])
                letter_bag.remove(letter_bag[p2_random])

        print 'Player 2 has redrawn the following letters:', ' '.join(p2_letters), '\n'
        print '                        <<<<< Current Score:', str(p2_score), '>>>>>', '\n'
        print '\n'*2, '\t'*2, '   ', '   '.join(p2_letters), '\n'*2
        p2_word_input = raw_input('Enter a word or valid command: ')
        p2_word_input = p2_word_input.upper()

#ALLOW PLAYER 2 TO SHUFFLE REDRAWN LETTERS
    while p2_word_input == '-S':
        random.shuffle(p2_letters)
        print '\n'*2, '\t'*2, '   ', '   '.join(p2_letters), '\n'*2
        p2_word_input = raw_input('Enter a word or valid command: ')
        p2_word_input = p2_word_input.upper()   

#ALLOW PLAYER 2 TO FORFEIT
    if p2_word_input == '-FORFEIT':
        print '\n', 'Player 2 forfeits!', '\n'
        forfeit = True
        break
    
#CHECK FOR VALID LETTER USAGE FOR PLAYER 2       
    letter_check = True    
    word_check = True
    
    while letter_check == True or word_check == True:
        if letter_check == True:    
            letter_mismatch = 0
            redundancy_counter_p2 = 0
            redundancy_check_p2 = [letter for letter in p2_letters]  
            
            for letter in p2_word_input:
                if letter in redundancy_check_p2:
                    redundancy_check_p2.remove(letter)
                
                elif letter not in redundancy_check_p2:
                    redundancy_counter_p2 += 1
                
                if letter not in p2_letters:
                    letter_mismatch += 1
            
            if letter_mismatch > 0:
                p2_score = p2_score - 5
                print '-5 POINTS'
                p2_word_input = raw_input('That is invalid given your current letters! Enter a valid word: ').upper()
            
            elif redundancy_counter_p2 > 0:
                p2_score = p2_score - 5
                print '-5 POINTS'
                p2_word_input = raw_input('That is invalid given your current letters! Enter a valid word: ').upper()
            
            else:
                letter_check = False

#CHECK FOR VALID WORD ENTRY FOR PLAYER 2
        while word_check == True and letter_check == False: 
            if p2_word_input not in word_value_dict:
                p2_score = p2_score - 5
                print '-5 POINTS'
                p2_word_input = raw_input('That\'s not in the dictionary! Enter a valid word: ').upper()
                letter_check = True
            else:
                word_check = False

#IF VALID, SCORE WORD, REMOVE USED LETTERS FROM PLAYER 2, AND REPLENISH WITH NEW LETTERS OF APPROPRIATE AMOUNT FROM BAG   
    if p2_word_input in word_value_dict:
        p2_wordlist.append(p2_word_input)
        print '\n'
        for letter in p2_word_input: 
            print '\t'*4, letter, ': +', str(letter_scores[letter])
        
        print '\t'*4, '-------------'
        print '\t'*4, word_value_dict[p2_word_input], 'POINTS!', '\n'
        
        if len(p2_word_input) == 5:
            print '+5 word length bonus!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] + 5)
            p2_score = p2_score + word_value_dict[p2_word_input] + 5
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif len(p2_word_input) == 6:
            print '2X word length bonus!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] * 2)
            p2_score = p2_score + word_value_dict[p2_word_input] * 2
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif len(p2_word_input) == 7:
            print '3X word length bonus!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] * 3)
            p2_score = p2_score + word_value_dict[p2_word_input] * 3
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3 
        
        elif len(p2_word_input) == 8:
            print '4X word length bonus!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] * 4)
            p2_score = p2_score + word_value_dict[p2_word_input] * 4
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif len(p2_word_input) == 9:
            print '5X word length bonus!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] * 5)
            p2_score = p2_score + word_value_dict[p2_word_input] * 5
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif len(p2_word_input) == 10:
            print '5X word length bonus!'
            print '+50 FULL CLEAR BONUS!', '\n'
            p2_wordscores.append(word_value_dict[p2_word_input] * 5 + 50)
            p2_score = p2_score + word_value_dict[p2_word_input] * 5 + 50
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
    
        else:
            p2_wordscores.append(word_value_dict[p2_word_input])
            p2_score = p2_score + word_value_dict[p2_word_input]
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3

#PLAYER 2 TIME END AND PENALTY APPLICATION
        p2_end_time = time.time()
        p2_elapsed = round(p2_end_time - p2_start_time)
        p2_game_time = p2_game_time + p2_elapsed
        
        if p2_elapsed > 120 and p2_elapsed < 135:
            p2_score = p2_score - 5 
            print 'Player 2 took too long!', str(p2_elapsed), 'seconds elapsed!'
            print '-5 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif p2_elapsed > 135 and p2_elapsed < 150:
            p2_score = p2_score - 10 
            print 'Player 2 took too long!', str(p2_elapsed), 'seconds elapsed!'
            print '-10 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif p2_elapsed > 150 and p2_elapsed < 165:
            p2_score = p2_score - 15 
            print 'Player 2 took too long!', str(p2_elapsed), 'seconds elapsed!'
            print '-15 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3

        elif p2_elapsed > 165 and p2_elapsed < 180:
            p2_score = p2_score - 20 
            print 'Player 2 took too long!', str(p2_elapsed), 'seconds elapsed!'
            print '-20 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3
        
        elif p2_elapsed > 180:
            p2_score = p2_score - 35
            print 'Player 2 took way too long!', str(p2_elapsed), 'seconds elapsed!'
            print '-35 POINTS', '\n'                                    
            print '                        <<<<< Current Score:', p2_score, '>>>>>', '\n'*3 

        for i in p2_word_input:
            p2_letters.remove(i)
        
        if len(p2_word_input) > len(letter_bag) and len(letter_bag) != 0:
            for j in range(len(letter_bag)):
                p2_random = random.randint(0, len(letter_bag)-1)
                p2_letters.append(letter_bag[p2_random])
                letter_bag.remove(letter_bag[p2_random])
        
        elif len(p2_word_input) == len(letter_bag) and len(letter_bag) != 0:
            for j in range(len(letter_bag)):
                p2_random = random.randint(0, len(letter_bag)-1)
                p2_letters.append(letter_bag[p2_random])
                letter_bag.remove(letter_bag[p2_random])
        
        elif len(p2_word_input) < len(letter_bag):
            for j in range(len(p2_word_input)):
                p2_random = random.randint(0, len(letter_bag)-1)
                p2_letters.append(letter_bag[p2_random])
                letter_bag.remove(letter_bag[p2_random])
        
        elif len(p2_word_input) > len(letter_bag) and len(letter_bag) == 0:
            continue
    print '+-------------------------- PLAYER 2 ROUND', str(game_round), 'END ------------------------------+', '\n'*2
    print '[  Player 1 Score:', p1_score, ' ]', '\t'*3, '       ', '[  Player 2 Score:', p2_score, ' ]', '\n'                                                       
    print '                       [ ', str(len(letter_bag)), 'letters remain in the bag  ]', '\n'*2             

#GAME END; PRINT FINAL SCORES, DECLARE WINNER, AND LIST WORDS GENERATED ALONG WITH CORRESPONDING VALUES
if forfeit == False:
    print 'No more letters remain in the bag!', '\n'
    print '+----------------------------------GAME OVER------------------------------------+'
    print '|', '\t'*10, '|'
    p1_penalty_sum = 0
    if len(p1_letters) > 0:
        for letter in p1_letters:
            p1_penalty_sum = p1_penalty_sum + letter_scores[letter]
                
        p1_score = p1_score - p1_penalty_sum        
        print '| Player 1 loses', str(p1_penalty_sum), 'points from letters remaining in their possession!', '\t'*2, '|'
    
    p2_penalty_sum = 0
    if len(p2_letters) > 0:    
        for letter in p2_letters:
            p2_penalty_sum = p2_penalty_sum + letter_scores[letter]
    
        p2_score = p2_score - p2_penalty_sum
        print '| Player 2 loses', str(p2_penalty_sum), 'points from letters remaining in their possession!', '\t'*2, '|'
    
    print '|', '\t'*10, '|' 
    print '| Player 1 total time:', p1_game_time, 's', '\t'*7, '|'
    print '| Player 2 total time:', p2_game_time, 's', '\t'*7, '|'
    print '|', '\t'*10, '|' 
    
    if p1_game_time < p2_game_time:
        p1_score = p1_score + 25
        print '| Player 1 had a faster time! +25 POINTS!', '\t'*5, '|'
        print '|', '\t'*10, '|' 
    elif p2_game_time < p1_game_time:
        p2_score  = p2_score + 25
        print '| Player 2 had a faster time! +25 POINTS!', '\t'*5, '|'
        print '|', '\t'*10, '|' 
        
    print '| Player 1 final score:', p1_score, '\t'*7, '|'
    print '| Player 2 final score:', p2_score, '\t'*7, '|'
    print '|', '\t'*10, '|' 
    
    if p1_score > p2_score:
        print '|', '\t'*4, 'PLAYER 1 WINS!', '\t'*5, '|'
        print '|', '\t'*10, '|' 
    elif p1_score < p2_score:
        print '|', '\t'*4, 'PLAYER 2 WINS!', '\t'*5, '|'
        print '|', '\t'*10, '|' 
    else:
        print '|', '\t'*5, 'HEY! WE TIED!', '\t'*5, '|'   
        print '|', '\t'*10, '|' 
    print '+-------------------------------------------------------------------------------+', '\n'
    
    raw_input('Press enter for word summary: ')
    
    print '\n'
    print '+--------------------------------WORD SUMMARY-----------------------------------+'
    print '|', '\t'*10, '|' 
    print '|      /---------------------------PLAYER 1-------------------------------/     |'
    print '|', '\t', '<WORD>', '\t' * 7, '<SCORE>', '\t', '|'

    p1_word_dict = {}
    for word in range(len(p1_wordlist)):
        p1_word_dict[p1_wordlist[word]] = p1_wordscores[word] 

    for entry in p1_word_dict:
        print '|', '\t', entry.ljust(10, ' '), '\t' * 6, p1_word_dict[entry], '\t'*2, '|'
    
    print '|', '\t'*10, '|'                                               
    print '|      /---------------------------PLAYER 2------------------------------/      |'
    print '|', '\t', '<WORD>', '\t' * 7, '<SCORE>', '\t', '|'

    p2_word_dict = {}
    for word in range(len(p2_wordlist)):
        p2_word_dict[p2_wordlist[word]] = p2_wordscores[word] 

    for entry in p2_word_dict:
        print '|', '\t', entry.ljust(10, ' '), '\t' * 6, p2_word_dict[entry], '\t'*2, '|'
    
    print '|', '\t'*10, '|'
    print '+-------------------------------------------------------------------------------+', '\n'
    
    raw_input('Thanks for playing! Press any key to exit: ')
    
    print '\n' '~PROGRAM TERMINATED~'  

else:
    print '+----------------------------------GAME OVER------------------------------------+'
    print '|', '\t'*10, '|'
    print '| Player 1 total time:', p1_game_time, 's', '\t'*7, '|'
    print '| Player 2 total time:', p2_game_time, 's', '\t'*7, '|'
    print '|', '\t'*10, '|'
    print '| Player 1 final score:', p1_score, '\t'*7, '|'
    print '| Player 2 final score:', p2_score, '\t'*7, '|'
    print '|', '\t'*10, '|'
    print '+-------------------------------------------------------------------------------+', '\n'
    
    raw_input('Press enter for word summary: ')
    print '\n'
    print '+--------------------------------WORD SUMMARY-----------------------------------+'
    print '|', '\t'*10, '|' 
    print '|      /---------------------------PLAYER 1-------------------------------/     |'
    print '|', '\t', '<WORD>', '\t' * 7, '<SCORE>', '\t', '|'

    p1_word_dict = {}
    for word in range(len(p1_wordlist)):
        p1_word_dict[p1_wordlist[word]] = p1_wordscores[word] 

    for entry in p1_word_dict:
        print '|', '\t', entry.ljust(10, ' '), '\t' * 6, p1_word_dict[entry], '\t'*2, '|'
    
    print '|', '\t'*10, '|'                                               
    print '|      /---------------------------PLAYER 2-------------------------------/     |'
    print '|', '\t', '<WORD>', '\t' * 7, '<SCORE>', '\t', '|'

    p2_word_dict = {}
    for word in range(len(p2_wordlist)):
        p2_word_dict[p2_wordlist[word]] = p2_wordscores[word] 

    for entry in p2_word_dict:
        print '|', '\t', entry.ljust(10, ' '), '\t' * 6, p2_word_dict[entry], '\t'*2, '|'
    
    print '|', '\t'*10, '|'
    print '+-------------------------------------------------------------------------------+', '\n'
    
    raw_input('Thanks for playing! Press ENTER to exit: ')
    
    print '\n' '~PROGRAM TERMINATED~'     