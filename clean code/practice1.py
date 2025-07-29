def do_this():
    print("Doing this")
def do_that():
    print("Doing that")

choice = input ('Doing this or that ? ')

if choice =='this':
    do_this()
elif choice == 'that':
    do_that()
else:
    print("invalid input")

