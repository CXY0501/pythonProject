import time

def show_info():
    print('Please input the number to execute the coresponding step：0 Quit 1 Check Login Information:')

def write_loginInfo(username):
    with open('login.txt','a+') as file:
        s = f'username:{username} log in at {time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}\n'
        file.write(s)

def read_loginInfo():
    with open('login.txt','r') as file:
        while True:
            line = file.readline()
            if line:
                print(line,end='')
            else:
                break

if __name__ == '__main__':
    while True:
        name = input('please input username:')
        psw = input('please input password:')
        if name == 'admin' and psw == '1234admin':
            print('log in successfully!')
            write_loginInfo(name)
            show_info()
            num = int(input('please input number:'))
            while True:
                if num == 0:
                    print('log out successfully')
                    break
                elif num == 1:
                    print('show log in information:')
                    read_loginInfo()
                    show_info()
                    num = int(input('please input number:'))
                else:
                    print('your input is invalid, please try again')
                    show_info()
                    num = int(input('please input number:'))
            break
        else:
            print('wrong user name or wrong password, please try again')



