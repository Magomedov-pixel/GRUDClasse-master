from itertools import product


class Shop:
    def __init__(self):
        self.__shopping_list = [
            {"id": 1, "product": "Хлеб", "quantity": 1, "bought": False},
            {"id": 2, "product": "Молоко", "quantity": 2, "bought": True}
        ]
        self.id = 3
    def add(self,product):
        self.shopping_list.append(
            {
                "id": 1,
                "product": product,
                "quantity": 1,
                "bought": False
            }
        )
        self.id +=1
        return True
    @property
    def shopping_list(self):
        return self.__shopping_list
    def completed(self,id):
        for dict in self.__shopping_list:
            if dict['id'] == id:
                dict['completed'] = True
                return dict
        # удалить
    def delete(self, id):
        for dict in self.__shopping_list:
            if dict['id'] == id:
                self.__shopping_list.remove(dict)

if __name__ == "__main__":
    product = Shop()
    print(product.shopping_list)