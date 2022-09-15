# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:06:42 2022

@author: enes
"""

# -*- coding: utf-8 -*-
def main():
    
    all_list = [add_Student,search_Student,update_Student,list_Info]
    while True:
        print("1- Add Student info")
        print("2- Search Student info")
        print("3- Update Student info")
        print("4- List info")
        print("0- Quit")
        
        p_x = int(input("Please choose one (0-4) :"))
        
        if p_x != 1 and p_x != 2 and p_x !=3 and p_x != 4 and p_x !=0:
            print("Invalid process")
        elif p_x ==0:
            print("Quit")
            break
        else:
            print("Valid process", p_x)
            all_list[p_x - 1]()
   


name_list =[]
grade1_list =[]
grade2_list =[]
grade3_list =[]
avg_list =[]
succes_list=[]



def add_Student():
    name = input("Enter your student's name : ")
    grade1 = int(input("Enter your student's first grade :"))
    grade2 = int(input("Enter your student's second grade :"))
    grade3 = int(input("Enter your student's third grade :"))
    avg = (grade1 + grade2 + grade3) / 3
    
    name_list.append(name)
    grade1_list.append(grade1)
    grade2_list.append(grade2)
    grade3_list.append(grade3)
    avg_list.append(avg)
    if avg > 50 :
        suc = "Succesful"
        succes_list.append(suc)
    else:
        notsuc = "Not Succesful"
        succes_list.append(notsuc)
        
def search_Student():
   ss_name = input("Which students are you looking for? :")
   
   if ss_name in name_list:
       ss_student= name_list.index(ss_name)
       print(f"{'Name':10} {'First Grade':10} {'Second Grade':10} {'Third Grade':10}  {'Average' :10}  {'Succes':10}")
       print(f"{name_list[ss_student]:10} {grade1_list[ss_student]:10} {grade2_list[ss_student]:10} {grade3_list[ss_student]:10}  {avg_list[ss_student]:10}  {succes_list[ss_student]:10} ")
   else :
       print("Invalid Student.")


def update_Student():
   ss_name = input("Which students are you looking for? :")
   
   if ss_name in name_list:
       ss_student= name_list.index(ss_name)
       print(f"{'Name':10} {'First Grade':10} {'Second Grade':10} {'Third Grade':10}  {'Average' :10}  {'Succes':10}")
       print(f"{name_list[ss_student]:10} {grade1_list[ss_student]:10} {grade2_list[ss_student]:10} {grade3_list[ss_student]:10}  {avg_list[ss_student]:10} {succes_list[ss_student]:10}")
       new_name =   input("Enter the new name :")
       new_grade1 = int( input("Enter the new first grade :"))
       new_grade2 = int(input("Enter the new second grade :"))
       new_grade3 = int(input("Enter the new third grade :"))
       
       name_list[ss_student] = new_name
       grade1_list[ss_student] = new_grade1
       grade2_list[ss_student] = new_grade2
       grade3_list[ss_student] = new_grade3
       new_avg = (new_grade1 + new_grade2 + new_grade3) / 3
       avg_list[ss_student] = new_avg
       if new_avg > 50 :
           new_suc = "Succesful"
           succes_list[ss_student] = new_suc
       else:
           new_notsuc = "Not Succesful"
           succes_list[ss_student] = new_notsuc
       
       print("New values are :")
       print(f"{'Name':10} {'First Grade':10} {'Second Grade':10} {'Third Grade':10}  {'Average' :10}  {'Succes':10}")
       print(f"{name_list[ss_student]:10} {grade1_list[ss_student]:10} {grade2_list[ss_student]:10} {grade3_list[ss_student]:10}  {avg_list[ss_student]:10} {succes_list[ss_student]:10}")
       
   else :
       print("Invalid Student.")      
         


def list_Info():
    print(f"{'Name':10} {'First Grade':10} {'Second Grade':10} {'Third Grade':10}  {'Average' :10}  {'Succes':10}")
    
    for i in range (len(name_list)):
        print(f"{name_list[i]:10} {grade1_list[i]:10} {grade2_list[i]:10} {grade3_list[i]:10}  {avg_list[i]:10} {succes_list[i]:10}")
        

   
 
        
    



    


    
