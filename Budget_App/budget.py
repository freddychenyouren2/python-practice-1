class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = [] #instance variable

    def deposit(self, amount, description=""):
        #Use a dictionary to create the object
        new_object = {"amount": amount, "description": description}
        self.ledger.append(new_object)
        
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            withdraw_amount = -1 * amount
            self.deposit(withdraw_amount, description)
            return True
        else:
            return False
        
    def get_balance(self):
        #Sum all deposit/withdrawal entries from ledger
        balance = 0
        for log in self.ledger:
            balance += log['amount']
        return balance
    
    def transfer(self, amount, another_budget):
        if self.check_funds(amount):
            withdraw_text = f'Transfer to {another_budget.category}'
            self.withdraw(amount, withdraw_text)

            deposit_text = f'Transfer from {self.category}'
            another_budget.deposit(amount, deposit_text)
            return True
        else:
            return False

    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    #Printing Budget Object
    def __str__(self):
        title_line = f'{self.category.center(30, "*")}\n'
        items_line = '' #empty string initialize
        total = 0

        #Get up till 23rd character in description. Make it left-justified
        #Format amount to 2dp. Get up till 7th character in amount. Make it right-justified
        for log in self.ledger:
            item_description = log['description'][:23].ljust(23)
            item_amount = "{:.2f}".format(log['amount']).rjust(7)
            items_line += f'{item_description}{item_amount}\n' #Keep adding new line
            total += log['amount']

        result = title_line + items_line + f'Total: {total:.2f}'
        return result


def create_spend_chart(categories):
    # Calculate total withdrawals for each category
    category_withdrawals = {} #Dictionary: (key=category.category, value=withdrawal)
    total_withdrawals = 0

    for category in categories:
        #Only sum up the withdrawals. USE abs() to make every calculation involve positive values.
        #Negative values very tricky
        withdrawals = abs(sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0))
        category_withdrawals[category.category] = withdrawals
        total_withdrawals += withdrawals
    #print(total_withdrawals)


    # Calculate percentage spent for each category
    percentages = []
    for category in categories:
        percentage = category_withdrawals[category.category] * 100 // total_withdrawals if total_withdrawals > 0 else 0 #Account for the case if there is no withdrawals
        percentages.append(percentage)

    #print(f"Percentages {percentages}")

    #Start creating the bar chart
    chart = "Percentage spent by category\n"
    #range(start(incl), end(excl), increment)
    for percentage in range(100, -10, -10): #Going down by 10 each
        chart += f'{str(percentage).rjust(3)}| '
        for category_percentage in percentages:
            #Up to nearest 10 percentage points
            if category_percentage >= percentage:
                chart += "o  "
            else:
                chart += "   "
        #After filling for one level, must add \n for a new line before the next outer for loop runs
        chart += "\n"
    #Create the dash lines, note the triple dashes for every category and then one extra dash at the end
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    #Start contructing the vertical names if the categories
    longest_category_length = max(len(category.category) for category in categories)

    #Recall each category is a string, where each letter can be accesed like a list
    for pos in range(longest_category_length):
        chart += " " * 5 #Before start of any names due to "100| "
        # Check if a category still has characters at this position to be written
        for category in categories:
            if pos < len(category.category):
                chart += category.category[pos] + "  " #Extra two spaces before next possible letter
            else:
                chart += "   " #Three empty spaces for the next possible letter
        
        if pos < longest_category_length - 1:
            chart += "\n" #New line for the next character for every category EXCEPT LAST LINE

    #Final output
    return chart