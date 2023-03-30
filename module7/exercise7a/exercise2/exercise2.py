# Uriel Renteria
# 3/26/23

#Exercise 2
import login

def main():
    password = input('Enter your password: ')

    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password.')

    print('That is a valid password.')

if __name__ == '__main__':
    main()
