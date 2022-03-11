# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 07:18:16 2022

@author: tslupik
"""

#%% *ARGS

def drink (*args):
    print (args)
    print (f'Liczba napojów: {len(args)}')
    
drink ('Monster', 'Kawa', 'Tiger', 'Red-Bull')

x = 'Moje ulubione napoje:'

def like (*args):
    for x in (args):
        x + str(args)
        print (x)
        
like(x, 'Monster', 'Kawa', 'Tiger', 'Red-Bull')
#%% *ARGS

def onlyText (*args):
    args = [arg for arg in args if isinstance (arg, str)]
    result = '#'.join(args)
    return result
        
textOne = onlyText('gym', 'fitness', 'motivation')
print (textOne)

textTwo = onlyText(2, 10, 100, 12, 19, 25, 20)
print (textTwo)

textThree = onlyText('kwiatek', 29, 'w', 15, 'doniczce')
print (textThree)

#%% *ARGS

def sport (x, *args):
    print (f'Mój ulubiony sport to: {x}')
    for arg in args:
        print (f'Kolejne sporty, które lubię: {arg}')
sport ('triathlon', 'snowboard', 'siatkówka')

#%% *ARGS

def person (first_name, last_name, *args):
    print (f'Imię: {first_name}')
    print (f'Nazwisko: {last_name}')
    print (f'Zainteresowania: {args}')
    
person ('Tomek', 'Nowak', 'gry planszowe', 'wyjazdy w ciepłe kraje', 'sushi')

#%% *ARGS

def addition(x, y):
    return x + y

def additionAll(*args):
    return sum (args)

print (addition(10, 7))
print (additionAll(9, 11, 20, 10))

#%% *ARGS

def average (*args):
    return sum (args)/ len (args)

print(f'Średnia dwóch liczb 10 i 20 wynosi: {average(10, 20)}')


#%% *ARGS
import datetime
import time
 
 
def log(message, dt=datetime.datetime.utcnow):
    print(dt(), message)
 
def logi(*args):
    for command in args:
        log(command)
        time.sleep(2)
 
logi('Włączono komputer', 'Logowanie', 'Restart', 'Wyłączenie komputera')
#%% **KWARGS

def mark (**kwargs):
    print (kwargs)
    print (f'Liczba przedmiotów: {len (kwargs)}')
    

userOne = mark (matematyka = 3, polski = 2)
userTwo = mark (angielski = 6, WOS = 4)
userThree = mark (WF = 6, Historia = 4)

def question (**kwargs):
    if 'dostateczny' in kwargs:
        print ("Tak, on dostał ocenę dostateczną")
    else:
        print ("On dostał inną ocenę, spróbuj ponownie!")
        
        
answerOne = question(dobry = 'matematyka')
answerTwo = question(dostateczny = 'matematyka')

#%% **KWARGS

def phonePrice (iphone, **kwargs):
    print (f'Nazwa telefonu: {iphone}')
    if 'cena' in kwargs:
        print (f"Cena telefonu wynosi: {kwargs ['cena']}")

phonePrice(iphone ='Iphone 11pro', cena = 4000)

#%% **KWARGS

def room (**kwargs):
    print (kwargs)
        
room (**{'biurko' : 'duże', 'lampa' :'srednia', 'buty' : 'wygodne'})        

#%% **KWARGS

def countKwargs (**kwargs):
    print (len (kwargs.values()))
    
    
countKwargs(a = 1, b = 2, c = 3)
countKwargs (a = 10, b = 1, c = 2, d = 19)
#%% *ARGS oraz **KWARGS

def checkOne (*args, **kwargs):
    print (f'Args jest to TUPLA: {args}')
    print (f'KWARGS jest to SŁOWNIK: {kwargs}')
    
checkOne()

def checkTwo (*args, **kwargs):
    print (args)
    print (kwargs)
    
checkTwo('ARGS - napoje', 'herbata', 'kawa', 'woda z cytryną',
         kwargs = 'KWARGS', ciastka = 'Pieguski')

#%% *ARGS oraz **KWARGS


def calculations (*args, **kwargs):
    print (sum (args))
    print (kwargs.values())

calculations(10, 80, 10, pierwsza = 1, druga = 2)


