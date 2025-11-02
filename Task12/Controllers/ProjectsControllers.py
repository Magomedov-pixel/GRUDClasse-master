from Task12.Models.Projects import Projects


class ProjectsController:
    obj = Projects()

    @classmethod
    def get(cls):
        return cls.obj.projects

    # дрбавить проект
    @classmethod
    def add(cls, name, status, deadline, priority):
        cls.obj.projects = {"name": name, "status": status, "deadline": deadline, "priority": priority}

    # обновление приоритета
    @classmethod
    def update_priority(cls, id, new_priority):
        for dict in cls.get():
            if dict['id'] == id:
                dict['priority'] = new_priority


if __name__ == '__main__':
    print(ProjectsController.get())
    ProjectsController.add("ggg", "ggg", "2024-02-15", "djjdjd")
    print(ProjectsController.get())
