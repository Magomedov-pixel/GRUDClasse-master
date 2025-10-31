from Task6.Models.Expenses import Expenses
class ExpensesController:
    '''
    добавить расход,
    сумма по категории,
    расходы  за период
    '''
    obj = Expenses()

    @classmethod
    def get(cls):
        return cls.obj.expense

    @classmethod
    def set(cls, amount, category, date, description,):
        cls.obj.expense = {"amount": amount, "category": category, "date": date, "description": description}
    @classmethod
    def update(cls,id,new_amound):
        for dict in cls.get():
            if dict['id'] == id:
                dict['amount'] = new_amound
if __name__ == '__main__':
    ExpensesController.set(1,"<ddd>","<ddd>","<ddd>")
    print(ExpensesController.get())