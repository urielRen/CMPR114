# Uriel Renteria
# 4/10/23

def main():
    list = [20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30]

    count = 0

    for index in list:
        count += index

    average = count / len(list)
    print(list)
    print(f'Sum = {count: .0f}')
    print(f'AVerage = {average: .2f}')

if __name__ == '__main__':
    main()