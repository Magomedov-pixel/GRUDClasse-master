class Event:
    def __init__(self):
        self.__list_events = [
            {"id": 1, "title": "Встреча", "date": "2024-02-15", "time": "14:00","description": "С коллегами"}
        ]
        self.id = 2
    @property
    def events(self):
        return self.__list_events
    @events.setter
    def events(self,dict):
        dict['id'] = self.id
        self.events.append(dict)
        self.id += 1
if __name__ == '__main__':
    ev = Event()
    print(ev.events)