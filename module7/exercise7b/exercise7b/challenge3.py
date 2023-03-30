# Uriel Renteria
# 3/27/28

# Challenge 3
def main():
    names = ['Howard', 'Jamie', 'Jill']

    print('The list before the insert or remove.')
    print(names)

    NameRemove = input('ENter a the name to remove: ')

    names.insert(0, 'Jose')
    names.remove(NameRemove)
    print('The list after the insert')
    
    print(names)

main()

def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value

    average = sum / len(numbers)
    print('the total is ', sum, ' the average is ', average)

    output = open('numbers.txt', 'w')
    output.writelines(str(numbers) + '\n')
    output.writelines('The total is: ' + str(sum) + '\n')
    output.writelines('The average is : ' + str(average) + '\n')
    print('Open the file and wrote to it.')

total()