from Task18.Models.Equipment import Equipment


class EquipmentController:
    obj = Equipment()

    @classmethod
    def add(cls, name, type, serial, status, user):
        cls.obj.equipment = {
            "name": name,
            "type": type,
            "serial": serial,
            "status": status,
            "user": user
        }
        return True

    # прокси метод
    @classmethod
    def get(cls):
        return cls.obj.equipment

    # поставить прививку,
    @classmethod
    def genre(cls, id):

        for dict in cls.get():
            if dict['id'] == id:
                dict['genre'] = True
                return dict
            else:
                return f'питомца с id {id} нет в базе данных'

    @classmethod
    def list_album(cls, album):
        list = []
        for dict in cls.get():
            if dict['album'] == album:
                list.append(dict['name'])
        return list

    # найти по типу
    @classmethod
    def type_artist(cls, artist):
        result = f"нет {artist}"
        for dict in cls.get():
            if dict['artist'] == artist:
                result = f"есть {artist}"
        return result


if __name__ == "__main__":
    print(EquipmentController.get())