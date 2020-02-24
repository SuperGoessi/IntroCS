import re

def main():
    username = input('Please input name: ')
    qq = input('Please input ypur qq: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6, 20}$', username)
    if not m1:
        print('Please input valid name')
    
    m2 = re.match(r'^[1-9]\d{4, 11}$', qq)
    if not m2:
        print("Please input valid qq")
    if m1 and m2:
        print("We got it")

if __name__ == '__main__':
    main()