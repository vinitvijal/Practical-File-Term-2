
StackVow = []


def Push(a, vo):
    a.append(vo)

def Pop(a):
    a.pop()

def Traversal(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])


while True:
    print('1. Add Vowel To Stack.')
    print('2. Delete Last Vowel of Stack.')
    print('3. Display All The Vowels In Stack.')
    print('4. Exit')
    vw = int(input('Select Your Option : '))
    if vw == 1:
        print('\n\n')
        print('Adding Vowel To Stack...\n')
        chr = input('Your Vowel : ')
        if chr in ['a','e','i','o','u','A','E','I','O','U']:
            Push(StackVow, chr)
            print('\nSuccessfully Updated To Stack!!!')
        else:
            print('\nYour Input is Not a Vowel... Try Again')
            pass
    elif vw == 2:
        if len(StackVow) == 0:
            print('Stack is Empty!!!')
        else:
            Pop(StackVow)
            print('Last Vowel Deleted')
    elif vw == 3:
        print('\n\nDisplay Data From Stack....\n\n')
        Traversal(StackVow)
    elif vw ==  4:
        print('\n\n\nCreated By @vinitvijal\nThanks')
        break
    else:
        print('Wrong Input Selected...')
        pass
        
