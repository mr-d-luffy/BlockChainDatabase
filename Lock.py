
def PasswordChack(Key):
    with open("passwd.key", 'r') as File:
        Passwd = File.read()
        if Key == Passwd:
            pass
        else:
            exit()
        File.close()

def ChangePasswd(Key):
    with open("passwd.key", 'w') as File:
        File.write(Key)
        File.close()
