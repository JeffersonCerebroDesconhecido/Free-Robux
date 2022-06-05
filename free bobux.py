print('To get free bobux you need login in your account roblox')

user = ['daviwnl1']

password = ['bobux']

archive = ['1']

login_user = input('user: ')
while not login_user in user:
    print('to get robux you need login corretly')
    login_user = input('user: ')
else:
    print('user corretly')
    login_password = input('password: ')
    while not login_password in password:
        print('PLS LOGIN CORRETLY')
        login_password = input('password: ')
    else:
        print('='*20)
        print('1(secret archive)')
        option = input('option: ')
        while not option in archive:
            print('this option not exist')
            option = input('option: ')
        else:
            print('to get free bobux enter in https://robuxfacil.com')
            leave = input('to leave press enter')
