class Projects:
    def __init__(self):
        self.__list_projects = [
            {"id": 1, "name": "Веб-сайт", "status": "в процессе", "deadline": "2024-03-01", "priority": "высокий"}
        ]
        self.id = 2

    @property
    def projects(self):
        return self.__list_projects

    @projects.setter
    def projects(self, dict):
        dict['id'] = self.id
        self.projects.append(dict)
        self.id += 1


if __name__ == '__main__':
    pr = Projects()
    print(pr.projects)
