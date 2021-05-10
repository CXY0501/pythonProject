import os
import keyboard
filename = 'studentsys.txt'
def menu():
    print('======================Student Management System================================')
    print('---------------------------Function Menu---------------------------------------')
    print('|                      1.Insert Student Info                                   |')
    print('|                      2.Search Student Info                                   |')
    print('|                      3.Delete Student Info                                   |')
    print('|                      4.Modify Student Info                                   |')
    print('|                      5.Sort Student Scores                                   |')
    print('|                      6.Total Student Number                                  |')
    print('|                      7.Show all Student Info                                 |')
    print('|                      0.Log out System                                        |')
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
                # print(d)

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
    while True:
        modifyId = input('Please input the Student ID you want to modify:')
        if modifyId:
            if os.path.exists(filename):
                with open(filename,'r',encoding='UTF-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            d = []
            flag = False
            for item in student_old:
                d.append(dict(eval(item)))
            for item in d:
                if item['id'] == modifyId:
                    try:
                        item['name'] = input('Please input the name:')
                        item['Engligh'] = int(input('Please input the English Score:'))
                        item['Python'] = int(input('Please input the Python Score:'))
                        item['Java'] = int(input('Please input the Java Score:'))
                        flag = False
                        break
                    except:
                        print('Invalid Input, please try again')
                        break
                else:
                    flag = True
            if flag == True:
                print(f'Student ID {modifyId} is not found')

            with open(filename,'w',encoding='UTF-8') as mfile:
                for item in d:
                    mfile.write(str(item)+'\n')

        else:
            print('Invalid input, please try again')

        keepOnModify = input('Keep on Modifing?y/n')
        if keepOnModify == 'y':
            continue
        else:
            break


def sort():
    while True:
        if os.path.exists(filename):
            with open(filename,'r',encoding='UTF-8') as file:
                student_sort = file.readlines()
        else:
            student_sort = []
        d = []
        for item in student_sort:
            d.append(dict(eval(item)))

        for item in d:
            item['Total Score'] = item['English'] + item['Python'] + item['Java']

        sortType = int(input('Please choose sort type: 1. by Acsending 2. Decsending'))
        sortBy = int(input('Please choose sort by: 1. English Score 2. Python Score 3. Java Score 0. Total Scores'))
        if sortType == 1:
            if sortBy == 1:
                d.sort(key=lambda d:d['English'],reverse=False)
            elif sortBy == 2:
                d.sort(key=lambda d:d['Python'],reverse=False)
            elif sortBy == 3:
                d.sort(key=lambda d:d['Java'],reverse=False)
            elif sortBy == 0:
                d.sort(key=lambda d:d['Total Score'],reverse=False)
            else:
                print('Invalid input, please try again')
        elif sortType == 2:
            if sortBy == 1:
                d.sort(key=lambda d:d['English'],reverse=True)
            elif sortBy == 2:
                d.sort(key=lambda d:d['Python'],reverse=True)
            elif sortBy == 3:
                d.sort(key=lambda d:d['Java'],reverse=True)
            elif sortBy == 0:
                d.sort(key=lambda d:d['Total Score'],reverse=True)
            else:
                print('Invalid input, please try again')

        for item in d:
            print(item)

        keepOnSort = input('Keep on Sorting?y/n')
        if keepOnSort == 'y':
            continue
        else:
            break

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as file:
            student_total = file.readlines()
    else:
        student_total = []
    print('The total number of students is:')
    print(len(student_total))
    goBackMenu = input('Input any key to Go back to the Main Menu')

def show():
    while True:
        if os.path.exists(filename):
            with open(filename,'r',encoding='UTF-8') as file:
                student_all = file.readlines()
        else:
            student_all = []
        d=[]
        if student_all:
            for item in student_all:
                d.append(dict(eval(item)))
            for item in d:
                print(item)
        else:
            print('No Student Info Found')

        # keyboard.write('The quick brown fox jumps over the lazy dog.')
        goBackMenu = input('Input any key to Go back to the Main Menu')
        if goBackMenu:
            break


if __name__ == '__main__':
    main()