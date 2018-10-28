import random



def main():
    char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

    try:
        pwd_length = int(input('Password Length?: '))
        if pwd_length < 5:
            raise Exception("Please specify at least 5 for password length.")

        num = int(input('How many to generate? (suggest more than 3): '))

        for i in range(num):
            pass_gen = ''

        for j in range(pwd_length):
            pass_gen += random.choice(char)
        
        print (pass_gen)
    
    except Exception as e:
        print("Error: {}".format(e))
  
  
if  __name__ == '__main__':
    main()
