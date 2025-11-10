from Task6_peewee.Models.Expenses import *

class ExpensesController:
    '''
    CRUD
    добавить расход,
    сумма по категории,
    расходы за период,
    '''
    @classmethod
    def add(cls,amount,category,date,description):
        # добавить расход
        Expenses.create(
            amount = amount,
            category = category,
            date = date,
            description = description
        )
    @classmethod
    def grade_update(cls,amount,category):
        #сумма по категории
        Expenses.update({Expenses.category:category}).where(Expenses.amount==amount).execute()

    @classmethod
    def get_name(cls,date):
        #расходы за период
        return Expenses.select().where(Expenses.date==date)

if __name__ == '__main__':
    ExpensesController.add(
        1500,
        "Еда",
        "2024-01-20",
        "Продукты"
    )