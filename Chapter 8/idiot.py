# Project from Chapter 8

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')

# Spanish version
#while True:
    #prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    #response = pyip.inputYesNo(prompt, yesVal = 'sí', noVal = 'no')
    #if response == 'no':
        #break

#print('¡Gracis. Que tenga un buen día!')