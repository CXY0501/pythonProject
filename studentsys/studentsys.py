import os
filename = 'studentsys.txt'
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
    print('--------------------------------------------------------------------------------')

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
    student_list = []
    while True:
        id = input('Please input Student No.(eg.1001):')
        if not id:
            break
        name = input('Please input Student name:')
        if not name:
            break
        try:
            English = int(input('Please input English Score:'))
            Python = int(input('Please input Python Score:'))
            Java = int(input('Please input Java Score:'))
        except:
            print('Invalid Score, please input Int type')
            continue

        student = {'id':id,'name':name,'English':English,'Python':Python,'Java':Java}
        student_list.append(student)

        keepOnInput = input('Keep on Inputting another Student?y/n')

        if keepOnInput == 'y':
            continue
        else:
            break

    print(student_list)

    save(student_list)
    print('Insert Student Info Completed')

def save(list):
    try:
        student_file = open(filename,'a',encoding='UTF-8')
    except:
        student_file = open(filename,'w',encoding='UTF-8')
    for item in list:
        student_file.write(str(item)+'\n')
    student_file.close()

def search():
    while True:
        print('Search by ID or Name? 1-ID 2-Name')
        SearchBy = int(input('Please input your choice'))
        if SearchBy:
            if os.path.exists(filename):
                with open(filename,'r',encoding='UTF-8') as sfile:
                    student_list = sfile.readlines()
            else:
                student_list = []
            # print(student_list)
            d = []
            flag = False
            if student_list:
                for item in student_list:
                    d.append(dict(eval(item)))
                print(d)

                if SearchBy == 1:
                    searchId = input('Please input the Student ID for search:')
                    for item in d:
                        if item['id'] == searchId:
                            print('-------------------------------')
                            print('Student Found:')
                            print(item)
                            flag = False
                            break
                        else:
                            flag = True
                            # break
                    if flag:
                        print('-------------------------------')
                        print('Student Not Found')

                elif SearchBy == 2:
                    searchName = input('Please input the Student Name for search:')
                    for item in d:
                        if item['name'] == searchName:
                            print('----------------------------------')
                            print('Student Found:')
                            print(item)
                            flag = False
                            break
                        else:
                            flag = True
                            # break
                    if flag:
                        print('-------------------------------')
                        print('Student Not Found')
                else:
                    print('Invalid Input, please try again')
                    # break
            else:
                print('No any student info exsits')

        keepOnSearch = input('Keep on searching? y/n')
        if keepOnSearch == 'y':
            continue
        else:
            break

def delete():
    while True:
        delId = input('Please input the Student ID you want to delete:')
        if delId:
            if os.path.exists(filename):
                with open(filename,'r',encoding='UTF-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []

            flag = False

            if student_old:
                with open(filename,'w',encoding='UTF-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != delId:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'Student Id {delId} is deleted')
                    else:
                        print(f'Cannot find Student ID {delId}')
            else:
                print('No Student Info Found')
                break

        keepOnDel = input('Keep on deleting another Student? y/n')
        if keepOnDel == 'y':
            continue
        else:
            break

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