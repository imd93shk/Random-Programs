# -*- coding: utf-8 -*-
"""
Calculator in Command Line
Created on Thu Sep 20 09:38:27 2018

@author: Imaad Shaik
"""
def ent_number(value):
    num = int(value)
    return num
    
def calculation(number_1, sign, number_2):
    if sign == '+':
        res = number_1 + number_2
    elif sign == '-':
        res = number_1 - number_2
    elif sign == '*':
        res = number_1 * number_2
    elif sign == '/':
        res = float(number_1) / number_2
    elif sign == '**':
        res = number_1 ** number_2
    return res

def main():
    number = []
    signs = []
    buffer = [0]
    values = [0]
    
    print("Enter the numbers and signs, seperated by the ENTER KEY. To get the answer, press = and ENTER KEY.")
    print("NOTE: ALWAYS enter ONE number followed by ONE mathematical operation (+, -, *, /, **, =)")
    value = input()
    i = 0 # index for numbers
    j = 0 # index for signs
    k = 0 # index for all entered values
    while value != '=':   
        values.append(value)
        if values[k + 1] == '0' and values[k] == '/':
            break                        
        elif value  == '+' or value  == '-' or value  == '*' or value  == '/' or value  == '**':
            signs.append(value)
        else:
            num = ent_number(value)
            number.append(num)
            i += 1 
            j += 1 
            for buf in buffer:
                if len(number) % 2 == 0:
                    temp_res = calculation(number[i-2], signs[j-2], number[i-1])
                    number.append(temp_res)
                    print(temp_res)
                    i += 1
        k += 1
        value = input()        
    
    if values[k-1] != 0 and values[k-2] != '/':
        print("Final Result: {:.2f}".format(temp_res))
    else:
        print("ERROR: Cannot divide by ZERO. Program ENDS")

main()
