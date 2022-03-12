Student=[]


def Push(a, name, marks):
    a.append([name, marks])

def Pop(a):
    a.pop()

def Traversal(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])

while True:
    print('1. Add Student Details.')
    print('2. Delete Last Student Details.')
    print('3. Display All Students Details.')
    print('4. Exit.')
    ch = int(input('Enter Your Option : '))
    if ch == 1:
        print('\n\nAdding Student Details....\n\n')
        name = input('Name Of Student : ')
        marks = int(input('Marks Of Student : '))
        Push(Student, name, marks)
        print('\n Successfully Added!!!')
    elif ch == 2:
        if len(Student) == 0:
            print('Stack is Empty!!!')
        else:
            Pop(Student)
            print('Last Detail Deleted')
    elif ch == 3:
        print('\n\nDisplay Data From Stack....\n\n')
        Traversal(Student)
    elif ch ==  4:
        print('\n\n\nCreated By @vinitvijal\nThanks')
        break
    else:
        print('Wrong Input Selected...')
        pass

    


