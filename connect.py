''' соединение с бд'''
from peewee import Model, MySQLDatabase, AutoField, IntegerField, CharField, \
                   DateField, DateTimeField, ForeignKeyField

db = MySQLDatabase('prodi_poluf_2023', user='root', password='lenok',
                   host='localhost', port=3306)


class DateBase(Model):
    class Meta:
        database = db


class Project(DateBase):
    id = AutoField()
    full_title = CharField()
    short_title = CharField()
    icon = CharField()
    created_time = DateTimeField()
    delete_time = DateTimeField()
    start_scheduled_date = DateField()
    finish_sheduled_date = DateField()
    description = CharField()
    creator_employee_id = IntegerField()
    responsible_employe_id = IntegerField()


class TaskStatus(DateBase):
    ''' статус задач'''
    id = AutoField()
    name = CharField()
    color_hex = CharField()


class Task(DateBase):
    ''' задача'''
    id = AutoField()
    project_id = ForeignKeyField(Project, backref='task')
    full_title = CharField()
    short_title = CharField()
    description = CharField()
    executive_employeel_id = IntegerField()
    status_id = ForeignKeyField(TaskStatus, backref='task')
    created_time = DateTimeField()
    update_time = DateTimeField()
    daleted_time = DateTimeField()
    deadline = CharField()
    start_actual_time = DateTimeField()
    finish_actual_time = DateTimeField(null=True)
    previous_task_id = CharField()
    icon = CharField()


class TaskTask(DateBase):
    ''' задача краткая'''
    id = AutoField()
    idtask = ForeignKeyField(Task, backref='tasktask')
    nubver = CharField()
    vaib = CharField()
    opinasin = CharField()
    name = CharField()
    dedline = DateTimeField()


db.connect()
db.create_tables([Project, Task, TaskStatus, TaskTask], safe=True)
db.close()
