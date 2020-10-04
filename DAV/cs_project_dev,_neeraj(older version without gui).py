import time

def star():
    print('*'*80)

    
f1=0
f2=0
f3=0

std1=dict()
star()
print()
print('\t\t   Welcome to the School Management Software')
print("\tFirst enter the information of students for Student Info. Table ")
print()
star()
print()
n=int(input('Enter the number of students : '))
print()
	
for i in range(n):
    adm=int(input('Enter the admission number of the student : '))
    name=input('Enter the name of the student : ')
    clas=int(input('Enter the class of the student : '))
    sect=input('Enter the section of the student : ')
    number=int(input('Enter the phone number of the student : '))
    print()
    b=(name,clas,sect,number)
    std1[adm]=b
l=std1.keys()	

while True:
    star()
    time.sleep(0.25)
    print()
    time.sleep(0.25)
    print('\t\t\tSchool Mangement System')
    time.sleep(0.25)
    print()
    time.sleep(0.25)
    star()
    time.sleep(0.25)
    print()	
    time.sleep(0.25)
		
    print('1. Add new student info.')
    time.sleep(0.25)
    print('2. Delete a student info.')
    time.sleep(0.25)
    print('3. View student table')
    time.sleep(0.25)
    print('4. Student info to be searched')
    time.sleep(0.25)
    print('5. Exit')
    print()
    time.sleep(0.25)
    choice=int(input('Enter your choice '))
    print()
    star()
    print()
	
    if(choice==1):
        f1=0
        std2=dict()
        adm=int(input('Enter the admission number of the student : '))
        
        for i in l:
            if(i==adm):
                
                f1=1
                print('Entered admission number already exist.')
        if f1==0:
            name=input('Enter the name of the student : ')
            clas=int(input('Enter the class of the student : '))
            sect=input('Enter the section of the student : ')
            number=int(input('Enter the phone number of the student : '))
            print()
            
            time.sleep(3)
            b=(name,clas,sect,number)
            std2[adm]=b
            std1.update(std2)
            l=std1.keys()
            time.sleep(2)
			
    elif(choice==2):
        f2=0
        adm=int(input('Enter the admission number of the student to be deleted : '))
        for i in l:
            if(i==adm):
                f2=1
                print('Deleted info of student (Admission Number) :',adm)
                print()
        if f2==1:
            del std1[adm]
        else:
            print(adm ,'(Admission Number) does not exist .')
        time.sleep(3)
		
    elif(choice==3):
        time.sleep(0.25)
        print('\t\t\tStudent Info. Table')
        print()
        star()
        for i in l:
            time.sleep(0.25)
            print('Admission Number :',i)
            h=std1[i]
            time.sleep(0.25)
            print('Name\t','\tClass\t','\tSection\t','\tPhone Number')
            time.sleep(0.25)
            for j in h:
                print(j,end='\t\t')
            print()
            print()
        time.sleep(3)
			
    elif(choice==4):
        adms=int(input('Enter admission number to be searched : '))
        for i in l:
            if(i==adms):
                print('Name\t','\tClass\t','\tSection\t','\tPhone Number')
                h=std1[adms]
                for j in h:
                    print(j,end='\t\t')
                print()
                print()
                f3=1
        if f3==0:
            print('Entered admission number does not exist.')
        f3=0
        time.sleep(3)
				
    elif(choice==5):
        quit()	
		
    else:
        print('\t\t\t\tInvalid Choice')
        print()
