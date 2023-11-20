import csv
l=[]
class Course:

    def __init__(self,name,code,units,lect,tut,lab):
        self.name=name.upper()
        self.code=code.upper()
        self.units=units
        self.parts=[lect,tut,lab]
        # self.sections has the format {'section':[day,time,room,instructor,type]}
        self.sections={}
        l.append(self)



    def get_all_sections(self):
        print('\nHERE ARE ALL THE AVAILABLE SECTONS:')
        for i in self.sections:
            print(i)
            


    def __str__(self):
        print("\nBasic information about the course.")
        print("The course name is:",self.name)
        print("The course code is:",self.code)
        print("The course is worth:",self.units,"units")
        for i in range(len(self.parts)):
            if self.parts[i]=='YES' and i==0:
                print("This course contains lecture component.")
            elif self.parts[i]=='YES' and i==1:
                print("This course contains tutorial component.")
            elif self.parts[i]=='YES' and i==2:
                print("This course contains lab component.")
        l[0].get_all_sections()



    def populate_sections(self,course_code,section,time,day,room,instructor,type1):
        self.sections[section]=[course_code,day,time,room,instructor,type1]


#meow=Course('Mechanical Ocsillations and waves','PHY F111',3,'YES','YES','NO')
#print(meow.name,meow.code)

#print(l)
def populate_new_section():
    print("Choose a course to add sctions to:")
    for i in range(len(l)):
        print(i+1,l[i].name)
    choice=int(input("Enter your choice:"))
    if choice not in list(range(len(l)+1)):
        print("INVALID CHOICE!!!")
        populate_new_section()
        pass

    print('\nADD THE SECTION DETAILS:')
    course_code=input("Enter course code:").upper()
    #course=get_instance(course_code)
    section=input("Enter section number:").upper()
    time=input("Enter time:")
    day=input("Enter day:").upper()
    room=int(input("Enter room number:"))
    instructor=input("Enter instructor name:").upper()
    type1=input("Enter type(lect/tut/lab):").upper()
    l[choice-1].populate_sections(course_code,section,time,day,room,instructor,type1)


#populate_new_section()
#print(meow.sections)
meow=Course('Mechanical Ocsillations and waves','PHY F111','3','YES','YES','NO')


def add_course_cli():
    print('\nADD THE COURSE DETAILS:')
    name=input("Enter course name:")
    code=input("Enter course code:")
    units=input("Enter unit weightage of the course:")
    lect=input("Are there lectures?(yes/no)")
    tut=input("Are there tutorials?(yes/no)")
    lab=input("Are there labs?(yes/no)")
    for i in l:
        if i.code==code.upper():
            print("COURSE ALREADY EXITS.")
            print("COURSE NOT ADDED.")
            return None
    Course(name,code,units,lect,tut,lab)


#add_course_cli()

def add_course_excel():
    file=input("Enter file name of the csv file:")
    file_name=file+'.csv'
    with open(file_name,"r") as f:
        r=csv.reader(f)
        next(r)
        for i in r:
            add=True
            for j in l:
                if i[1].upper()==j.code:
                    print("COURSE WITH THE CODE",j.code," ALREADY EXITS.")
                    print("COURSE NOT ADDED.")
                    add=False
            if add:
                Course(i[0],i[1],i[2],i[3],i[4],i[5])
    pass


