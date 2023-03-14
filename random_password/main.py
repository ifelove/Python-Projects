import string,random

characters=list(string.ascii_letters + string.digits + "@!#$%&*()")
print(characters)
def generate_password():

    password_length=int(input("Enter thr length of password you want to generate:  "))
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password="".join(password)
    print(password)


if __name__=="__main__":
    generate_password()
