# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 03:23:17 2023

@author: PC
"""

print('welcome to my Computer Game')

playing = input('do you want to play? ')
if playing.lower() != 'yes':
    quit()
    
print('lets play! :) ')
score = 0
    
answer =input('what does cpu mean? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
    
else:
    print('incorrect')
    
answer =input('what does psu mean? ')
if answer.lower() == 'power supply unit':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer =input('what does gpu mean? ')
if answer.lower() == 'graphic processing unit':
    print('correct!')
    score += 1
    
else:
    print('incorrect')
    
answer =input('what does ram mean? ')
if answer.lower() == 'random access memory':
    print('correct!')
    score += 1

print('you got', score, 'questions correctly')
print('you have', (score/4)*100, '%.')
