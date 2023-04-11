# Uriel Renteria
# 4/10/23

def main():
    list = [20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30]

    found = 0
 
    for index in list:
        if index == 27:
            found = index
            break
    print(list)
    print('Lucky number is: ', found)

if __name__ == '__main__':
    main()
