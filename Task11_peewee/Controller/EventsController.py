from Task11_peewee.Model.Events import *

class EventsController:
    '''
    добавить событие,
    события на дату,
    предстоящие события
    '''
    @classmethod
    def add(cls, title, date, time, description):
        # добавить книгу
        Events.create(
            title=title,
            date=date,
            time=time,
            description=description
        )
    @classmethod
    def get_author(cls, date):
        # события на дату
        return Events.select().where(Events.date == date)


if __name__ == '__main__':
    EventsController.add(
        "sfs",
        '12.12.2222',
        '12:12',
        'dfjkk'
    )