import random


def main():
    char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

    length = int(input('Password Length?: '))
    num = int(input('How many to generate? (suggest more than 3): '))

    for i in range(num):
      pass_gen = generate_pass(length)
      print (pass_gen)


def generate_pass(pwd_length):
    char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    return ''.join(random.choice(char) for i in range(pwd_length))


if  __name__ == '__main__':
    main()
