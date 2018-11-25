###USER should be able to edit password

## assume dictionary of password for each user

mydict ={}
mydict["Tvisha"] ="password"
mydict["Tynan"] = "password123"
mydict["Krish"] = "Lion123"

name = input("please enter your first name:")


if name not in mydict.keys():
    print("User does not exist try again")

else:
    pss = input("Please enter your old password:")
    #print(pss)
    #print(mydict[name])
    if pss == mydict[name]:

        newpss= input("Please input your new password:")
        #update password in database
        mydict[name] = newpss
        print("password updated")

    else:
        print("incorrect password, please try again")

