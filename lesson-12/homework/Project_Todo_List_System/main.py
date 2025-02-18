name = 'Aza'
hi = 'Todo List System'
bye = 'Thanks for using'
only = 'Enter the numbers from 1 to 8'
menu = {
    '1': 'Tasks list',
    '2': 'Upcoming Tasks list',
    '3': 'Ongoing Tasks list',
    '4': 'Success Tasks list',
    '5': 'Create Task',
    '6': 'Set Status Task',
    '7': 'Delete Task',
    '8': 'Exit',
}
status = {
    '1': 'Upcoming',
    '2': 'Ongoing',
    '3': 'Success',
}

i_n_f_i = '4'
i_n_f_t = ['1,Create App,Ongoing\n', '2,Upgrade Ap,Upcoming\n', '3,Status App,Success\n', '4,Delete App,Upcoming']
start = True


def open_file(fn='id'):
    try:
        with open(fn + '.csv') as file:
            content = file.readlines()
        if fn == 'id':
            return content
        result = []
        for i in content:
            id, title, stat = tuple(i.replace('\n', '').split(','))
            result.append({'id': id, 'title': title, 'status': stat})
        return result
    except Exception:
        w_a_f(fn, i_n_f_i if fn == 'id' else i_n_f_t)
        return i_n_f_i if fn == 'id' else open_file(fn)


# write append file
def w_a_f(fn, val, mode='w'):
    with open(fn + '.csv', mode) as file:
        file.write(''.join(val))


def show_tasks(action=0):
    for i in tasks:
        if action == 0 or i['status'] == status[str(action)]:
            print(f'{i['id']}: Title: {i['title']} Status:{i['status']}')


tasks = open_file('tasks')
id_task_global = open_file()[0]


def create_task():
    global id_task_global, tasks

    title = input('Enter Title Task: ')
    stat = set_status(5)
    id_task_global = str(int(id_task_global) + 1)
    tasks.append({'id': id_task_global, 'title': title, 'status': status[stat]})
    w_a_f('tasks', f'{id_task_global},{title},{status[stat]}\n', 'a')
    w_a_f('id', id_task_global)
    print('Task Created Successfully')


def check_task_id():
    while True:
        task_id = input('Enter Task Id: ')
        if task_id in [task['id'] for task in tasks]:
            return task_id
        print('Not found task id. Re-enter')


def set_status(action=6, task_id='1'):
    valid_status = status
    if action == 6:
        print(task_id)
        t_i_s = {task['id']: task['status'] for task in tasks}
        valid_status = {i: j for i, j in status.items() if t_i_s[task_id] != j}

    count = 0
    while True:
        if count > 0:
            print('Enter only numbers', [int(i) for i in valid_status.keys()])
        print('Set Status Task:')
        for i, j in valid_status.items():
            print('\t', f'{i}: {j}')
        stat = input('Enter Status Task: ')
        count = 1
        if stat in valid_status.keys():
            return stat


# delete update task
def d_u_t(action=7):
    global tasks
    show_tasks()
    task_id = check_task_id()
    stat = -1
    if action == 6:
        stat = set_status(6, task_id)
    for i in tasks:
        if i['id'] == task_id:
            if action == 6:
                i['status'] = status[stat]
            else:
                tasks.remove(i)
            break
    w_a_f('tasks', [f'{i['id']},{i['title']},{i['status']}\n' for i in tasks])
    print('Task', 'Deleted' if action == 7 else 'Updated', 'Successfully')


while start:
    print(hi)
    for i, k in menu.items():
        print(f'{i}. {k}')
    num = input()
    match num:
        case '1':
            show_tasks()
        case '2':
            show_tasks(1)
        case '3':
            show_tasks(2)
        case '4':
            show_tasks(3)
        case '5':
            create_task()
        case '6':
            d_u_t(6)
        case '7':
            d_u_t()
        case '8':
            print(bye)
            break
        case _:
            print(only)
    print()
