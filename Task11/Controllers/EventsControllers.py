from Task11.Models.Events import Event
class EventsController:
    obj = Event()
    @classmethod
    def get(cls):
        return cls.obj.events
    @classmethod
    def add(cls, title, date, time, description):
        cls.obj.events = {"title": title, "date": date, "time": time, "description": description}
    @classmethod
    def update_date(cls, id, new_date):
        for dict in cls.get():
            if dict['id'] == id:
                dict['date'] = new_date
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if __name__ == '__main__':
    print(EventsController.get())