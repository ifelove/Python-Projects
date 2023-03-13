def main():
    #while(True):
        print("You are welcome to email slicer app")
        print("...............................")
        email_adress = input("Enter your email adress :")
        (username, domain) = email_adress.split("@")
        (domain, extention) = domain.split('.')

        print(f"Your username is {username}")
        print(f"Your domain is {domain}")
        print(f"Your extention is {extention}")



if __name__=='__main__':
    main()