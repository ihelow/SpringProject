# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#name=input("What's your name?\n");
#print("Nice to meet you, ", name , "!");
#print("\n");

#age=input("What's your age?\n");
#print("Wow your are ", age , " years old!");
#print("\n");
import math


#x=20;
#y=30;
#z=x+y;
#print(z);

#count=1;
#count+=1;
#count=count+1;



def toprintname():
    print("My name is Aisylu Iunusova");
    


def myarea():
    radius=int(input("Please enter the radius of the circle: \n"));

    area=round((radius**2)*math.pi);
    print("the area of the circle is: ",  area);
    
    
# you can use eval as a way to convert the input into the iteger or float
#this is used when the user can input both the float and integer


def avv():
    number1=eval(input("give me a first number: \n"));
    number2=eval(input("give me a second number: \n"));
    number3=eval(input("give me a third number: \n"));

    average= (number1 + number2 + number3)/3;
    print("the average is: ", average);
    
avv();
