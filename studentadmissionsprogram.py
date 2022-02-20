import math
import os
from re import S
#int student 215
#dom student 45
#total 362
#base class
class student():
    #constructor
    def __init__(self,first_name=None,last_name=None,research_score=None,cgpa=None):
        self._first_name = first_name
        self._last_name = last_name
        self._research_score = research_score
        self._cgpa = cgpa
    
    #accessor and mutators ---------------------
    #4 data points for base, firstname lastname, researchscore, cgpa
    def set_first_name(self,first_name):
        self._first_name = first_name
        
    def set_last_name(self,last_name):
        self._last_name = last_name
        
    def set_research_score(self,research_score):
        self._research_score = research_score
        
    def set_cgpa(self,cgpa):
        self._cgpa = cgpa
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    def get_research_score(self):
        return self._research_score
    
    def get_cgpa(self,):
        return self._cgpa
    #-------------------------------------------
    #returns object value
    def __str__(self):
        return f'("{self._first_name}","{self._last_name}","{self._research_score}","{self._cgpa}")'
    
    #print function
    def print_student_info(self):
        print('Student :', self._first_name,' ',self._last_name, ', Research Score :',self._research_score,
              ', Cgpa :', self._cgpa)
    
    
#domestic students (child class)  
class domesticStudent(student):
    
    D_student_list = []
    student_list = []
    
    #constructor
    def __init__(self,province=None):
        super(domesticStudent,self).__init__(first_name=None,last_name=None,research_score=None,cgpa=None)
    
    #------- accessors & mutators
    #dom stu derived has additional member var province    
    def set_province(self,province):
        self._province = province
        
    def get_province(self):
        return self._province
    # ---------------------------
    
    # ------ class methods
    
    #return object string data
    def __str__(self):
        return f'{self._province}'
    
    #print function, prints list of domestic students
    def print_student_list(self):
        print('Domestic student list : ')
        for i in self.student_list:
            print(' ' ,i, end='')
        
    #groups data for each student, appends it to list, copy->clear-> repeat
    def stu_list(self):
        self.D_student_list.append(self._first_name)
        self.D_student_list.append(self._last_name)
        self.D_student_list.append(self._province)
        self.D_student_list.append(self._research_score)
        self.D_student_list.append(self._cgpa)
        self.student_list.append(self.D_student_list.copy())
        self.D_student_list.clear()
    
    #merge sort, Big- O : O(n*logn)  
    def stu_sort_merge(self,i,left,right):
        
        if(len(left)== 0):
            return right
        if(len(right)== 0):
            return left
        result =[]
        l_index = r_index = 0
        
        while(len(result) < len(left) + len(right)):
            #merge sort conditional logic, self evident,the extra index [i] is for data points
            if(left[l_index][i] <= right[r_index][i]):
                result.append(left[l_index])
                l_index+=1   
            else:
                result.append(right[r_index])
                r_index+=1
                
            if(r_index == len(right)):
                result += (left[l_index:])
                break
            if(l_index == len(left)):
                result+= (right[r_index:])
                break
            
        return result
    
    #2nd merge sort method for recursive portion, i parameter is for member variable types
    def merge_sort(self,array,i):
        if(len(array) < 2):
            return array
        midpoint = len(array)//2
        return self.stu_sort_merge(i,left=self.merge_sort(array[:midpoint],i),right = self.merge_sort(array[midpoint:],i))
    
    #derived class print
    def print_student_info(self):
        print('Domestic Student : ', domesticStudent._first_name,domesticStudent._last_name, ', Research Score : ',domesticStudent._research_score,
              ', Cgpa : ', domesticStudent._cgpa, ', Province: ', self._province)
    
    #method to merge individual lists
    def sort_merge_lists(self,domesticStudent):
        print('Enter A to sort by first name, B to sort by last name, c to sort by province, d to sort by cgpa,'
              'e to sort by research score, f to return registry.')           
        flag = True
        while(flag == True):
            
            E = input('Enter: ')
            #sorting by first name
            if(E.lower() == 'a'):
                self.student_list = self.merge_sort(self.student_list,0)
                print('List sorted by first name: ')
                for i in self.student_list:
                    print(i,sep =' ',end='')

            #sorting by last name  
            elif(E.lower() == 'b'):
                self.student_list = self.merge_sort(self.student_list,1)
                print('List sorted by last name: ')
                for i in self.student_list:
                    print(i,sep =' ',end='')
                    
            #sort by province
            elif(E.lower() == 'c'):
                self.student_list = self.merge_sort(self.student_list,2)
                print('List sorted by province:')
                for i in self.student_list:
                        print(i,sep =' ',end='')
                        
            #sort by cgpa
            elif(E.lower() == 'd'):
                self.student_list = self.merge_sort(self.student_list,3)
                print('List sorted by research score:')
                for i in self.student_list:
                        print(i,sep =' ',end='')
            
            #sort by research score
            elif(E.lower() == 'e'):
                self.student_list = self.merge_sort(self.student_list,4)
                print('List sorted by cgpa:')
                for i in self.student_list:
                        print(i,sep =' ',end='')
            
            #return sorted list in order last sorted
            elif(E.lower() == 'f'):
                
                return self.student_list
                
            else:
                print('Incorrect selection, please re-enter.')
            
     #look for domestic students in registry        
    def search_student(self,domesticStudent):
        
        print('Would you like to find a student from the registry?')
        print('enter y to find or n to return')
        Z = input()
        
        if(Z.lower() == 'y'):
         
          print('Would you like to find a student based on their name or academic record?')
          print('enter name to find by name or academic to find by academic record, or enter n to exit')
          E = input()
            
          while(E.lower() != 'n'):
            #look up student by name
            if(E.lower() == 'name'):
                
                print('Input a first Name')
                first = input()
                print('input a last name')
                last = input()
                f_name = False
                l_name = False
                
                for i in self.student_list:
                       
                        if first in i[0] and last in i[1]:
                            print(first,' ',last)
                            f_name = True
                            l_name = True
                            print(i)

                        if(f_name == True and l_name == True):
                            print('Do you want to delete student?, enter y, else enter any key to exit.')
                            print(i)
                            #delete student then break
                            E = input()
                            if (E.lower() == 'y'):
                                self.student_list.remove(i)
                                break
                            
                            else:
                                break
                        
                else:
                    print('value doesnt exist, make another selection')
                    E = input()
                
            #search students by academic score    
            if(E.lower() == 'academic'):
                flag = True
                print('Enter cgpa to search students based on cgpa minimum.')
                print('Enter rs to search students based on research score minimum.')
                print('Enter y to delete students who fail to meet minimum threshold.')
                print('Enter n to quit.')
                
                while(flag == True):
                    cin = input()
                    if(cin.lower() == 'cgpa'):
                        for i in self.student_list:
                            if(i[4] < 3):
                                print(i)
                                
                    if(cin.lower() == 'rs'):
                        for i in self.student_list:
                            if(i[3] < 75):
                                print(i)
                                
                        print('Would you like to remove all students under 3.0 cgpa and 76 research score threshold?')
                        print('would if yes enter y, else enter n to exit')
                    
                    #deletes all students who dont make the defined threshold for research score and cgpa
                    if(cin.lower() == 'y'):
                        for i in self.student_list:
                            flag = True
                            
                            #removes student with low research score or above max
                            if(i[3] < 75 or i[3] > 100):
                                print(i)
                                self.student_list.remove(i)
                                flag = False
                                
                            #removes student with low cgpa or above max
                            elif(i[4] < 3 or i[4] > 4.33 and flag == True):
                                print(i)
                                self.student_list.remove(i)
                                
                     #exit condition           
                    if(cin.lower() == 'n'):
                        flag = False
                    #return list with removed students
                    if(cin.lower() == 'e'):
                        return self.student_list
                    
                    print('Input n to exit to previous menu, or e to return to start menu.')    
             
            #returns to student list   
            if(E.lower == 'n'):
                return self.student_list
            else:
                print('please make another selection again.')
                print('Would you like to search a student based on their name or academic record?')
                print('enter name to search by name or academic to search by academic record, or enter n to exit')
                E = input()
    
    
    #add new student method    
    def add_student(self):
        i = 0
        #4 entry values
        while(i < 5):
            print('Input first name')
            f_name = input()
            if(error_check_str(f_name) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input Last Name')
            l_name = input()
            if(error_check_str(l_name) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            # canadian provinces, incase something wrong is entered
            print('Input province initials.')
            prov_list =['bc','ab','mb','sk','on','qc','ns','pe','wh','nl','yt','nt']
            prov = input()
            if(error_check_str(prov) == True):
                if(prov in prov_list):
                    i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input cpga.')
            s_cgpa = input()
            if(error_check_float(s_cgpa) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input research score.')
            s_research_score = input()
            if(error_check_int(s_research_score) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            #sets new student if every value is correct
            if(i == 4):
                self.set_first_name(f_name)
                self.set_last_name(l_name)
                self.set_province(prov)
                self.set_cgpa(s_cgpa)
                self.set_research_score(s_research_score)
                self.stu_list()
                
                print('Would you like to enter another student? type y to enter a new student or any key to quit')
                enter = input()
                if(enter.lower() == 'y'):
                    i = 0
                else:
                    i = 5
    
    
    #add student entry error message
    def print_entry_error():
        print('You have made an entry error, you will have to restart')
            
                   
#international students (child class)
class internationalStudent(student):
    
    #international student lists
    I_student_list = []
    student_list = []
    
    #derived constructor
    def __init__(self,country = None,score = None):
        super(internationalStudent,self).__init__(first_name = None,last_name = None,research_score = None,cgpa
        =None)
             
    #accessor & mutators----------------------------
    #extra data points country and score
    def set_country(self,country):
        if(country[1] == 'd'):
            self._country = 'india'
        else:
            self._country = country
        
    def get_country(self):
        return self._country

    def set_score(self,score):
            self._score = score
    
    def get_score(self):
        return self._score
    #-----------------------------------------------     
    
    #derived print method for international student list
    def print_student_list(self):
        print('Printing student list: ')
        for i in self.student_list:
            print(' ',i,sep='')
      
      
    #international student list data appender, copy list -> clear ->repeat
    def I_stu_list(self):
            self.I_student_list.append(self._first_name)
            self.I_student_list.append(self._last_name)
            self.I_student_list.append(self._country)
            self.I_student_list.append(self._research_score)
            self.I_student_list.append(self._cgpa)
            self.I_student_list.append(self._score)
            self.student_list.append(self.I_student_list.copy())            
            self.I_student_list.clear()
 
    #merge sort method, Big- O : O(n*logn)  
    def stu_sort_merge(self,i,left,right):
        if(len(left)== 0):
            return right
        if(len(right)== 0):
            return left
        result =[]
        l_index = r_index = 0
        
        #same sorting method as domesstic student
        while(len(result) < len(left) + len(right)):
       
            if(left[l_index][i] <= right[r_index][i]):
                result.append(left[l_index])
                l_index+=1
            else:
                result.append(right[r_index])
                r_index+=1
            if(r_index == len(right)):
                result += (left[l_index:])
                break
            if(l_index == len(left)):
                result+= (right[r_index:])
                break
        return result
    
    
    #2nd merge sort method for recursive portion, sorts based on data point insdie list
    def merge_sorts(self,array,i):
        if(len(array) < 2):
            return array
        midpoint = len(array)//2
        return self.stu_sort_merge(i,left=self.merge_sorts(array[:midpoint],i),right = self.merge_sorts(array[midpoint:],i))
    
    #method to initiate the sorting
    def I_sort_merge_lists(self):
        print('Enter A to sort by first name, B to sort by last name, c to sort by province, d to sort by cgpa,'
              'e to sort by research score.')           
        
        flag = True
        while(flag == True):
            E = input()
            
            #conditional statements on what data point to sort by
            #first name
            if(E.lower() == 'a'):
                self.student_list = self.merge_sorts(self.student_list,0)
                print('List sorted by first name:')
                for i in self.student_list:
                    print(i)
                    
            #last name
            elif(E.lower() == 'b'):
                self.student_list = self.merge_sorts(self.student_list,1)
                print('List sorted by last name:')
                for i in self.student_list:
                    print(i)
            
            #country
            elif(E.lower() == 'c'):
                self.student_list = self.merge_sorts(self.student_list,2)
                print('List sorted by last country:')
                for i in self.student_list:
                    print(i)
            
            #research score
            elif(E.lower() == 'd'):
                self.student_list = self.merge_sorts(self.student_list,3)
                print('List sorted by research score:')
                for i in self.student_list:
                    print(i)
            
            #cgpa
            elif(E.lower() == 'e'):
                self.student_list = self.merge_sorts(self.student_list,4)
                print('List sorted by cgpa:')
                for i in self.student_list:
                    print(i)
            
            #total score
            elif(E.lower() == 'f'):
                self.student_list = self.merge_sorts(self.student_list,5)
                print('List sorted by total score:')
                for i in self.student_list:
                    print(i)
            
            #returns sorted list
            elif(E.lower() == 'r'):
                return self.student_list
                
            else:
                print('Incorrect selection, please re-enter.')
                
                
    #search for international student name in registry           
    def search_student(self,internationalStudent):
        
        print('Would you like to find a student from the registry?')
        print('enter y to find or n to return')
        Z = input()
        
        #decision tree, same structure as domestic student method
        if(Z.lower() == 'y'):
         
          print('Would you like to find a student based on their name or academic record?')
          print('enter name to find by name or academic to find by academic record, or enter n to exit')
          E = input()
            
          while(E.lower() != 'n'):
             
            if(E.lower() == 'name'):
                
                print('Input a first Name')
                first = input()
                print('input a last name')
                last = input()
                f_name = False
                l_name = False
                
                #looks for first and last name in list               
                
                for i in self.student_list:
                        if first in i[0] and last in i[1]:
                            print(first,' ',last)
                            f_name = True
                            l_name = True
                            print(i)
                        
                        #if found, do you want to delete?
                        if(f_name == True and l_name == True):
                            print('Do you want to delete student?, enter y, else enter any key to exit.')
                            print(i)
                            
                            E = input()
                            if (E.lower() == 'y'):
                                
                                self.student_list.remove(i)
                 #name doesnt exist, try again or quit       
                else:
                    print('value doesnt exist, make another selection')
                    E = input()
             
            #same structure as the domestic student class but one data point added for total socre      
            if(E.lower() == 'academic'):
                flag = True
                while(flag == True):
                    print('Enter cgpa to search students based on cgpa minimum')
                    print('Enter rs to search students based on research score minimum')
                    print('Enter ts to search students based on total score minimum')
                    cin = input()
                    
                    if(cin.lower() == 'cgpa'):
                        for i in self.student_list:
                            if(i[4] < 3):
                                print(i)
                    if(cin.lower() == 'rs'):
                        for i in self.student_list:
                            if(i[3] < 75):
                                print(i)
                    if(cin.lower() == 'ts'):
                        for i in self.student_list:
                            if(i[5] > 120 or i[5] < 80):
                                print(i)
                        
                    print('Would you like to remove all students under 3.0 cgpa and 76 research score threshold'+
                          'and 80 total score threshold along with any other data errors')
                    print('would if yes enter y, else enter n to exit, or enter orginal search terms to look at other scores.')
                    #removes students based on under minima or above maxima scores
                    if(cin.lower() == 'y'):
                        for i in self.student_list:
                            if(i[3] < 75 or i[3] > 100):
                                self.student_list.remove(i)
                            if(i[4] < 3 or i[4] > 4.33):
                                self.student_list.remove(i)
                            if(i[5] < 80 or i[5] > 120):
                                self.student_list.remove(i)
                                
                    if(cin.lower() == 'n'):
                        flag = False
                                
                
            if(E.lower == 'n'):
                return
            else:
                print('please make another selection again.')
                print('Would you like to search a student based on their name or academic record?')
                print('enter name to search by name or academic to search by academic record, or enter n to exit')
                E = input()
    
    #adds new student to the registry, same structure as dom student but extra point for score
    def add_student(self):
        i = 0
        while(i < 6):
            print('Input first name')
            f_name = input()
            
            if(error_check_str(f_name) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input Last Name')
            l_name = input()
            
            if(error_check_str(l_name) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input country.')
            print('Currently, were only accepting international students from iran, china, korea, and india.')
            country_list =['iran','china','korea','india']
            s_country = input()
            
            if(error_check_str(s_country) == True):
                if(s_country.lower() in country_list):
                    i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input cpga.')
            s_cgpa = input()
            
            if(error_check_float(s_cgpa) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            print('Input research score.')
            s_research_score = input()
                
            if(error_check_int(s_research_score) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
                
            print('Input total score.')
            t_score = input()
            if(error_check_int(t_score) == True):
                i+=1
            else:
                self.print_entry_error()
                i = 0
            
            #sets new student if every value is correct
            if(i == 5):
                self.set_first_name(f_name)
                self.set_last_name(l_name)
                self.set_country(s_country)
                self.set_cgpa(s_cgpa)
                self.set_research_score(s_research_score)
                self.set_score(t_score)
                self.I_stu_list()
                
                print('Would you like to enter another student? type y to enter a new student or any key to quit')
                enter = input()
                #restart loop for another entry
                if(enter.lower() == 'y'):
                    i = 0
                #quit while
                else:
                    i = 6
    #print method for error
    def print_entry_error():
        print('You have made an entry error, you will have to restart')
                    
                    
#class for handling total score, complete arbitrary decision to just add unecessary complexity to
#the program, this could have been put in the i student class               
class totalScore():
    def __init__(reading,writing,speaking,listeing):
        pass
    def get_writing(self):
        return self._writing
    def get_listening(self):
        return self._listening
    def get_speaking(self):
        return self._speaking
    def get_reading(self):
        return self._reading
    
    def get_score(self):
        return self._score
    
    def set_writing(self,writing):
        self._writing = writing
    def set_reading(self,reading):
        self._reading = reading
    def set_listening(self,listening):
        self._listening = listening
    def set_speaking(self,speaking):
        self._speaking = speaking
    
    def __add__(self):
        self.score = self._reading + self._writing + self._listening + self._speaking
    
    def set_score(self):
            self.__add__(self)
            
    
#function for domestic stu data reading
def dom_stu_list(): 
    
    #instantiation of derived class
    domestic_stu = domesticStudent()   
    print('File extraction') 
    try:
        with open("C:\\Users\\cfarb\\Documents\\domestic-stu.txt","r") as file:
                lines = file.readlines()[1:]
                for line in lines:
                    string = line.strip().split(",")
                    first_name = string[0]
                    last_name = string[1]
                    province = string[2]
                    str_cgpa = string[3].strip('.')
                    str_research_score = string[4]
                    cgpa = float(str_cgpa)
                    research_score = int(str_research_score)
                    
                    #error checking data, if any line as an error in any field,skip it
                    if(error_check_str(first_name) == True):
                        domestic_stu.set_first_name(first_name)
                    else:
                        print('first')
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        lines+=1
                        
                    if(error_check_str(last_name) == True):
                         domestic_stu.set_last_name(last_name)
                    else:
                        print('second')
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        line+=1
                    if(error_check_str(province) == True):
                        domestic_stu.set_province(province)
                    else:
                        print('third')
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        line+=1
                    if(error_check_float(cgpa) == True):
                        domestic_stu.set_cgpa(cgpa)
                    else:
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        line+=1
                    if(error_check_int(research_score) == True):
                        domestic_stu.set_research_score(research_score)
                    else:
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        line+=1
                    domestic_stu_data_list = domestic_stu.stu_list()
                    
    except:
        print('Unable to extract data from file.') 
    
    #choice tree or menu if you will for class methiods
    flag = True
    while(flag == True):
        print('To search students input 1, to sort students input 2, to print students input 3, to'+
              ' add a student to the registry input 4, to exit input e.')
        i = input()
    
        if(i == '1'):
            domestic_stu_data_list = domestic_stu.search_student(domestic_stu_data_list)
        elif(i == '2'):      
            list1 = domestic_stu.sort_merge_lists(domestic_stu_data_list)
        elif(i == '3'):
            domestic_stu.print_student_list()
        elif(i == '4'):
            domestic_stu.add_student()
        elif(i.lower() == 'e'):
            flag = False
        else:
            print('Make another selection or enter')
            
    return list1  
 
 
#second helper function for reading international stu data, same structure as domestic student
#but adds the totalscore that international students have
def int_stu_list():
    
    international_stu = internationalStudent()
    tot_Score = totalScore()  
     
    print('File extraction')
    try:
        with open("C:\\Users\\cfarb\\Documents\\international-stu.txt","r") as file:
                lines = file.readlines()[1:]
                #data being read from a file to be processed for object creation
                for line in lines:
                    string = line.strip().split(",")
                    first_name = string[0]
                    last_name  = string[1]
                    country    = string[2]
                    str_cgpa  = string[3].strip('.')
                    str_research_score = string[4]
                    
                    cgpa = float(str_cgpa)
                    research_score = int(str_research_score)
                    str_reading = string[5]
                    reading = int(str_reading)
                    str_listening = string[6]
                    listening = int(str_listening)
                    str_speaking = string[7]
                    speaking = int(str_speaking)
                    str_writing = string[8]
                    writing = int(str_writing)
                    
                    #error checking data before creation of object
                    if(error_check_int(reading) == True):
                        tot_Score.set_reading(reading)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_int(listening) == True):
                        tot_Score.set_listening(listening)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                        
                    if(error_check_int(speaking) == True):
                        tot_Score.set_speaking(speaking)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_int(writing) == True):
                        tot_Score.set_writing(writing)
                        tot_Score.set_score()
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
            
                    if(error_check_str(first_name) == True):
                        international_stu.set_first_name(first_name)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_str(last_name) == True):
                         international_stu.set_last_name(last_name)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_str(country) == True):
                        international_stu.set_country(country)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_float(cgpa) == True):
                        international_stu.set_cgpa(cgpa)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    if(error_check_int(research_score) == True):
                        international_stu.set_research_score(research_score)
                    else:
                        data_corrupted_warning()
                        del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                        line+=1
                    
                    #if no errors, add objects to object list
                    international_stu.set_score(tot_Score.get_score())
                    I_stu_data_list = international_stu.I_stu_list()
    except:
        print('Unable to extract data from file.')       
        
    flag = True
    while(flag == True):
        print('To search students input 1, to sort students input 2, to print a list of students input 3'+
              ',to add an international student input 4, to exit enter e.')
        
        i = input()
        if(i == '1'):
          international_stu.search_student(I_stu_data_list)    
        elif(i == '2'):      
           list2 = international_stu.I_sort_merge_lists(international_stu)  
        elif(i == '3'):
            international_stu.print_student_list()
        elif(i == '4'):
            international_stu.add_student()
        elif(i.lower() == 'e'):
            flag = False
        else:
            print('Make another selection or enter')
            
    return list2  


#first class helper function
def main(dom_stu_list,int_stu_list):
    complete_student_list = []
    list1 = dom_stu_list()
    list2 = int_stu_list()
    
    #merging the sorted lists
    complete_student_list = student_operations(list1,list2,complete_student_list)
    print_list(complete_student_list)
    
     
#helper function, mixing OOP with functional programming
def student_operations(list1,list2,complete_student_list):
    
    def merge_lists(list1,list2,complete_student_list):
        counter1 = 0
        counter2 = 0
        
        #user prompt to merge the lists based on previous sorting protocal
        print('Merge lists based on initial sorting protocol')
        print('Enter 1 for first name, 2 for last name, 3 for province/country,4 for research score, 5 for cgpa.')
        
        #error check for arbitray number entered
        i = input()
        i = int(i)
        while(incorrect_int() == False):
            
            i = input()
            i = int(i)
        
        if(len(list1) == 0):
            complete_student_list = list2
        if(len(list2)==0):
            complete_student_list = list1
      
        #overall sorting favours domestic students, sorts low to high
        while(counter1 != len(list1) and counter2 != len(list2)):
         
            if(list1[counter1][i] > list2[counter2][i]):
                complete_student_list.append(list2[counter2])
                counter2+=1
            elif(list1[counter1][i] < list2[counter2][i]):
                complete_student_list.append(list1[counter1])
                counter1+=1
            else:
                complete_student_list.append(list1[counter1])
                counter1+=1

        #delete initial lists freeing memory
        del list1
        del list2
        #return new sorted list
        return complete_student_list
        
    return merge_lists(list1,list2,complete_student_list)
                     
# ---------- helper functions ------------------------------------------

#helper function to print merged list 
def print_list(complete_student_list):
    print('Printing merged list...')
    
    for i in complete_student_list:
        print(i)
        
        
#error check func to make sure arg only contains int
def error_check_int(integer):
    if(isinstance(integer,int) == False):
        print('Data is not an int')
        return False
    else:
        return True
    
    
# error check func to make sure arg only contains float
def error_check_float(flt):
    if(isinstance(flt,float) == False):
        print('Data is not a float')
        return False
    else:
        return True
    
    
#error check func to make sure arg only contains alpha chars
def error_check_str(string):
    string = string.lower()
    
    if(isinstance(string,str) == False):
        return False
    elif():
        for char in string:
            if(char < 'a' or char > 'z'):
             return False
    else:
        return True
    
    
#error func return false, print func  
def data_corrupted_warning():
    print('Data corrupted, deleting student.')
    
    
def incorrect_int(i):
    if(i > 0 and i <=5):
        return True
    else:
        return False
#---------------------------------------------------------------------------------       
    
#first class function call
main(dom_stu_list,int_stu_list)
