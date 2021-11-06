
username = "arshia"
password = "123123"

while True:
    print("------------")
    input_username = input("username: ")
    input_password = input("password: ")
    print("------------")
    
    if username == input_username and input_password == password:
        print("Tebrikler! basariyla giris yaptiniz")
        break
    else :
        print("username veya password yanlis. Lutfen tekrar deneyiniz.")
        continue
    
