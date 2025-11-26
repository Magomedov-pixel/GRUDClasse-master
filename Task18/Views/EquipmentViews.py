from tkinter import *
from tkinter import ttk

from Task18.Controllers.EquipmentController import EquipmentController


class EquipmentView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных  Инвентарь компьютерной техник")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить компьютерной техники ')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите название техники")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # type
        self.type = ttk.Label(self.fram_add, text="введите тип")
        self.type.pack()
        # окна ввода type
        self.input_type = ttk.Entry(self.fram_add)
        self.input_type.pack()

        # serial
        self.serial = ttk.Label(self.fram_add, text="Введите серию")
        self.serial.pack()
        # Окна ввода данных serial
        self.input_serial = ttk.Entry(self.fram_add)
        self.input_serial.pack()

        # status
        self.status = ttk.Label(self.fram_add, text="Введите статус")
        self.status.pack()
        # Окна ввода данных status
        self.input_status = ttk.Entry(self.fram_add)
        self.input_status.pack()

        # user
        self.user = ttk.Label(self.fram_add, text="Введите имя пользователя")
        self.user.pack()
        # Окна ввода данных user
        self.input_user = ttk.Entry(self.fram_add)
        self.input_user.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_mel)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'type', 'serial', 'status','user')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        equipment = EquipmentController.get()
        list_equipment = []
        for equipment in equipment:
            list_equipment.append(
                (
                    equipment['id'],
                    equipment['name'],
                    equipment['type'],
                    equipment['serial'],
                    equipment['status'],
                    equipment['user'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='название')
        self.tree.heading('type',text='тип')
        self.tree.heading('serial', text='серия')
        self.tree.heading('status', text='статус')
        self.tree.heading('user', text='пользователь')

        for equipment in list_equipment:
            self.tree.insert('',END,values=equipment)

    # вывод
    def add_mel(self):
        EquipmentController.add(
            name=self.input_name.get(),
            type=self.input_type.get(),
            serial=self.input_serial.get(),
            status=self.input_status.get(),
            user=self.input_user.get(),
        )
        self.table()
