# Uriel Renteria
# 3/26/23

# Exercise 4
def main():
    csv_file = open('test_scores.csv', 'r')

    lines = csv_file.readlines()

    csv_file.close()

    for line in lines:
        tokens = line.split(',')
        total = 0.0
        for token in tokens:
            total += float(token)

        average = total / len(token)
        print(f'Average : {average}')

if __name__ == '__main__':
    main()
