# Uriel Renteria
# 3/26/23

# Exercise 3
def main():
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
    print()

def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')

if __name__ == '__main__':
    main()

