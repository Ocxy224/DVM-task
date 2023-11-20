import course
import timetable as tt
import section
global stage

print('\n           BITS PILANI')
print('Welcome to the ERP DIVISION.\n')
stage=[1,'']


def stage1():
    #stage 1  login page
    print('1.  STUDENT LOGIN')
    print('2.  STAFF LOGIN')
    c1=int(input('CHOOSE AN OPTION (1/2):'))
    if c1 not in [1,2]:
        print('INVALID CHOICE!!')
        pass
    elif c1==1:
        stage=(2,'student')
        stage2_student()
    elif c1==2:
        stage=(2,'staff')
        stage2_staff()

def stage2_staff():
    # stage 2 for staff
    # Staff password is 1234
    print("\n\n        LOGIN PAGE")
    username=input("Enter username:")
    passw=input("Enter password:")

    if passw=='1234':
        stage=(3,'staff')
    else:
        print("WRONG PASSWORD!!")
        pass

def stage2_student():
    # stage 2 for student
    print('\n\n        LOGIN PAGE')
    email=input("Enter your BITS ID:")
    passw=input("Enter password:")
    # There is no restriction for students any password and any email will work

    stage=(3,'student')



def stage3_staff():
    # satge 3 for staff
    print('\n Welcome to the staff portal')
    print('1. Add new course through excel')
    print('2. Add new course manually(through CLI)')
    print('3. Populate new section')
    #print('4. Populate ')
    c2=int(input("CHOOSE AN OPTION(1/2/3):"))
    
    if c2==1:
        course.add_course_excel()
    elif c2==2:
        course.add_course_cli()
    elif c2==3:
        course.populate_new_section()
    

def stage3_student():
    print("YOUR")
    pass


# while True:
#     if stage[0]==1:
#         stage1()
#     elif stage[0]==2:
#         if stage[1]=='staff':
#             stage2_staff()
#         elif stage[1]=='student':
#             stage3_student()





























# def staff():
#     while True:
#         input("pasw:?")
#         if passw=="1234":
#             staff2()



# while True:
#     print()
#     s=int(input())
#     if c not in [1,2]:
#         print("mvhfsu")
#         continue
#     elif c==1:
#         staff()

