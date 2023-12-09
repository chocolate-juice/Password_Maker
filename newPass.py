def enterNewPassword():
    nums = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    while True:
        password = input('Enter a password: ')
        for character in password:
            if character in nums:
                count += 1
        while count >= 1:
            if len(password) in range(8,16):
                return('Here is your new password: ' + password)
                break
            else:
                print('Your password must be 8-15 characters.')
                break
            continue
        while count == 0:
            if len(password) in range(8,16):
                print('Your password must contain at least one digit.')
                break
            else:
                print('Your password must be 8-15 characters and contain at least one digit.')
                break
            continue
        if len(password) in range(8,16):
            break
        else:
            continue
    
print(enterNewPassword())
