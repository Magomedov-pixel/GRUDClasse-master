class Expenses:
    def __init__(self,):
        self.__list_expenses = [
            {"id": 1, "amount": 1500, "category": "Еда", "date": "2024-01-20","description": "Продукты"}
        ]
        self.id = 2
    @property
    def expense(self):
        return self.__list_expenses
    @expense.setter
    def expense(self, dict):
        dict['id'] = self.id
        self.expense.append(dict)
        self.id += 1
#
if __name__ == '__main__':
    exp = Expenses()
    print(exp.expense)
    exp.expense = {"amount": 1500, "category": "Еда", "date": "2024-01-20","description": "Продукты"}
    print(exp.expense)