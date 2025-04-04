''' fastapi'''
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from connect import Project, TaskStatus, Task, TaskTask
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', response_class=HTMLResponse)
async def main_str(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})


@app.get('/dashbord', response_class=HTMLResponse)
async def str_dashbord(request: Request):
    return templates.TemplateResponse('dashpord.html',
                                      {'request': request})


@app.get('/taskstr', response_class=HTMLResponse)
async def str_task(request: Request):
    tata = TaskTask.select()
    tass = [{'id': tt.id,
             'idtask': tt.idtask,
             'nubver': tt.nubver,
             'vaib': tt.vaib,
             'opinasin': tt.opinasin,
             'name': tt.name,
             'dedline': tt.dedline}
            for tt in tata]
    return templates.TemplateResponse('task.html',
                                      {'request': request,
                                       'tata': tass})


@app.get('/calendar', response_class=HTMLResponse)
async def str_calendar(request: Request):
    return templates.TemplateResponse('calendar.html',
                                      {'request': request})


@app.get('/project')
async def get_progect():
    proj = Project.select()
    return [{'id': pro.id, 'full_title': pro.full_title,
             'short_title': pro.short_title,
             'icon': pro.icon, 'created_time': pro.created_time,
             'delete_time': pro.delete_time,
             'start_scheduled_date': pro.start_scheduled_date,
             'finish_schedule_date': pro.finish_schedule_date,
             'description': pro.description,
             'creator_employee_id': pro.creator_employee_id,
             'responsible_employe_id': pro.responsible_employe_id}
            for pro in proj]


@app.get('/taskstatus')
async def get_tast_status():
    status = TaskStatus.select()
    return [{'id': st.id,
             'name': st.name,
             'color_hex': st.color_hex}
            for st in status]


@app.get('/task')
async def get_task():
    task = Task.select()
    return [{'id': ta.id,
             'project_id': ta.project_id,
             'full_title': ta.full_title,
             'short_title': ta.short_title,
             'description': ta.description,
             'executive_employeel_id': ta.executive_employeel_id,
             'status_id': ta.status_id,
             'created_time': ta.created_time,
             'update_time': ta.update_time,
             'daleted_time': ta.daleted_time,
             'deadline': ta.deadline,
             'start_actual_time': ta.start_actual_time,
             'finish_actual_time': ta.finish_actual_time,
             'previous_task_id': ta.previous_task_id,
             'icon': ta.icon}
            for ta in task]


@app.get('/tasktask')
async def crop_task():
    tata = TaskTask.select()
    return [{'id': tt.id,
             'idtask': tt.idtask,
             'nubver': tt.nubver,
             'vaib': tt.vaib,
             'opinasin': tt.opinasin,
             'name': tt.name,
             'dedline': tt.dedline}
            for tt in tata]
