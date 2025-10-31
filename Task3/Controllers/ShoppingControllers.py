from Task3.Models.Shopping import Shopping


class ShoppingControllers:
    '''
    добавить продукт,
    отметить купленным,
    показать некупленное,
    удалить
    '''

    obj = Shopping()

    @classmethod
    # прокси
    def get(cls):
        return cls.obj.shoppings

    # добавить продукт
    @classmethod
    def add(cls, product):
        cls.obj.shoppings = {"product": product}

    # отметить купленным
    @classmethod
    def bought(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                dict['bought'] = True
                return dict
            else:
                return f'продукта не {id} в базе'

    # удалить продукт
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if  __name__ == '__main__':
    print(ShoppingControllers.bought(1))
    print(ShoppingControllers.get())
    print(ShoppingControllers.add("бананы",))
    print(ShoppingControllers.get())
    print(ShoppingControllers.delete(1))
    print(ShoppingControllers.get())