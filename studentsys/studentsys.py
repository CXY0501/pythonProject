def menu():
    print('======================Student Management System================================')
    print('---------------------------Function Menu---------------------------------------')
    print('\t\t\t\t\t\t1.Insert Student Info')
    print('\t\t\t\t\t\t2.Search Student Info')
    print('\t\t\t\t\t\t3.Delete Student Info')
    print('\t\t\t\t\t\t4.Modify Student Info')
    print('\t\t\t\t\t\t5.Sort Student Scores')
    print('\t\t\t\t\t\t6.Total Student Number')
    print('\t\t\t\t\t\t7.Show all Student Info')
    print('\t\t\t\t\t\t0.Log out System')

def main():
    while True:
        menu()
        choice=int(input('Please choose your option:'))
        if choice in range(0,8):
            if choice == 0:
                answer = input('Are you sure you want to exit the system?y/n')
                if answer == 'y' or answer == 'Y':
                    print('Thanks for using Student System')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def insert():
    pass
def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()