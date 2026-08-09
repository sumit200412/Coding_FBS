admin = 1234
Password = "sumit"
captcha = 3459
attempt = 1
while(attempt <= 3):
    Id = int(input("Enter the ID: "))
    Pass = input("Enter the Password: ")
    print(f"Captcha: {captcha}")
    cap = int(input("Enter the captcha: "))
    if(admin == Id and Password == Pass and captcha == cap):
        print("Login Successful")
        break
    else:
        print("Login Failed")
        attempt += 1
if(attempt > 3):
    print("Maximum attempts reached")