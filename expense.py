from PyInquirer import prompt
import csv
from user import userList


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":userList
    },

]


def new_expense(*args):
    infos = prompt(expense_questions)
    with open('expense_report.csv', 'a', newline='') as csvfile:
        tmp = csv.writer(csvfile)
        tmp.writerow([infos['amount'], infos['label'], infos['spender']])
    print("Expense Added !")
    return True