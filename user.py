from PyInquirer import prompt
import csv

userList = []
with open('users.csv', 'r', newline='') as csvfile:
        tmp = csv.reader(csvfile)
        for i in tmp:
            userList.append(i[0])

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        tmp = csv.writer(csvfile)
        tmp.writerow([infos['username']])
    print("User added !")
    return True