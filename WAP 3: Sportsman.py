Sport_Stack=[]


def Push(a, name, age):
    a.append([name, age])

def Pop(a):
    a.pop()

def Traversal(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])

while True:
    print('1. Add Sportsman Details.')
    print('2. Delete Last Sportsman Details.')
    print('3. Display All Sportsman Details.')
    print('4. Exit.')
    ch = int(input('Enter Your Option : '))
    if ch == 1:
        print('\n\nAdding New Details....\n\n')
        name = input('Name Of Sportsman : ')
        age = int(input('Age Of Sportsman : '))
        Push(Sport_Stack, name, age)
        print('\n Successfully Added!!!\n\n')
    elif ch == 2:
        if len(Sport_Stack) == 0:
            print('Stack is Empty!!!')
        else:
            Pop(Sport_Stack)
            print('Last Detail Deleted')
    elif ch == 3:
        if len(Sport_Stack) == 0:
            print('Stack is Empty!!!')
        else:      
            print('\n\nDisplay Data From Stack....\n\n')
        Traversal(Sport_Stack)
        print('\n\n')
    elif ch ==  4:
        break
    else:
        print('Wrong Input Selected...')
        pass

    


