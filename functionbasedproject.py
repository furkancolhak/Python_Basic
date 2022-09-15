# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:03:14 2022

@author: enes
"""
print("1- Sayının karesini alma")
print("2- Sayının ondalığını alma")
print("3- Sayının tam bölenleri")
print("0- Çıkış")

def kare_Alma(x):
    print(x * x)
    
def ondalık_Alma(x):
    print(x/10)

def tambolen_Alma(x):
    for i in range (2,x+1):
        if x % i == 0:
            print(i)
            
       

    
   
while True:
    p_x = int(input("Lütfen sayı seçiniz (0-3) :"))

    if p_x != 1 and p_x != 2 and p_x !=3 and p_x !=0:
        print("Lütfen geçerli bir değer giriniz.")

    else:
        if p_x == 1:
            p_y = int(input("Karesini almak üzere sayı giriniz. :"))
            kare_Alma(p_y)
        elif p_x == 2:
            p_y = int(input("Ondalığını almak üzere sayı giriniz. :"))
            ondalık_Alma(p_y)
        elif p_x == 3:
            p_y = int(input("Tam bölenlerini almak üzere sayı giriniz. :"))
            tambolen_Alma(p_y)
        elif p_x ==0:
            print('Çıkış yapılıyor...')
            break
      
    

                

        
        
        
    
    
    






