class Category:
    def __init__(self,_name):
        self.name = _name
        self.ledger = []
        self.balance = 0
        self.expense = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.expense += amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_c):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+other_c.name)
            other_c.deposit(amount, "Transfer from "+self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount

    def __str__(self):
        lines = []
        left = int((30-len(self.name))/2)
        right = 30-len(self.name)-left
        lines.append("*"*left+self.name+"*"*right)
        for item in self.ledger:
            amount_str = str(item["amount"])
            if amount_str.find(".") == -1:
                amount_str += ".00"

            if len(item["description"]) > 23 :
                lines.append(item["description"][0:23] + " " * (7 - len(amount_str)) + amount_str)
            else :
                lines.append(item["description"]+" "*(30-len(item["description"])-len(amount_str))+amount_str)

        balance_str = str(self.balance)
        if balance_str.find(".") == -1:
            balance_str += ".00"
        lines.append("Total: "+balance_str)

        show = ""
        for line in lines:
            show += line + "\n"

        show = show[0:len(show)-1]
        return show

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15,"groceries")
food.withdraw(15.89, "restaurant and more food for dessert")


clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)



def create_spend_chart(categories):
    expense = []
    total = 0
    bar = []
    percent = ["  0"," 10"," 20"," 30"," 40"," 50"," 60"," 70"," 80"," 90","100",]
    len_names = []
    for category in categories:
        total += category.expense
        len_names.append(len(category.name))

    for category in categories:
        expense.append(int(category.expense/total*10))

    for i in range(11):
        bar.append(percent[i]+"| ")
        for j in range(len(categories)):
            if expense[j] >= i:
                bar[i] += "o  "
            else:
                bar[i] += "   "

    bar.reverse()
    bar.append(" "*4+"-"*(len(bar[0])-4))

    for i in range(max(len_names)):
        bar.append(" "*5)
        for category in categories:
            try:
                bar[12+i] +=  category.name[i]+" "*2
            except:
                bar[12 + i] += " " * 3
    result = "Percentage spent by category\n"
    for i in range(len(bar)):
        result += bar[i] + "\n"
    result = result[0:len(result)-1]


    return result

print(create_spend_chart([food,clothing,auto]))









