# Uriel Renteria
# 4/10/23

def main():
    list2D = [[1, 2], [3,4], [5,6], [7,8], [9,10]]

    found = 0

    for row in list2D:
        for element in row:
            if element == 7:
                found = element
                break
    

    print(list2D)
    print('The lucky number is: ', found)

if __name__ == '__main__':
    main()
