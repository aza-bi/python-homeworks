name = 'Aza'
hi = 'Library Management System'
bye = 'Thanks for using'
menu = {
    '1': 'List all books',
    '2': 'Search book',
    '3': 'Borrow book',
    '4': 'Return book',
    '5': 'Patron info',
    '6': 'Exit',
}
start = True
i_n_f_b = ['1,Harry Potter\n', '2,The Hobbit\n', '3,T-SQL Querying\n', '4,Data Pipelines with Airflow']


def w_f(fn, val):
    with open(fn + '.csv', 'w') as file:
        file.write(val)


def open_file(fn='patron_info'):
    try:
        with open(fn + '.csv') as file:
            content = file.readlines()
        if fn == 'patron_info':
            return content[0].split(',') if len(content) > 0 else content
        return {i: j for i, j in tuple(i.replace('\n', '').split(',') for i in content)}
    except Exception:
        w_f(fn, ''.join(i_n_f_b) if fn == 'books' else '')
        return open_file(fn)


books = open_file('books')
p_i = open_file()

def b_n_f(count = 0, text = ''):
    if count == 0:
        print('Book not found', text)
        return True
    return False

def print_books(action=1):
    count = 0
    text = None
    if action == 2:
        text = input('Enter the title book: ')

    for i, j in books.items():
        if text is not None:
            if text.lower() not in j.lower():
                continue
        count = 1
        print(f'{i}: Title: {j} |', 'Not Available' if i in p_i else 'Available')
    b_n_f(count)

def get_id(action=3):
    count = 1
    while True:
        b_n_f(count, 'enter only numbers: ' + str([int(i) for i in books.keys() if (action == 3 and i not in p_i) or (action == 4 and i in p_i)]))
        count = 0
        for i, j in books.items():
            if (action == 3 and i not in p_i) or (action == 4 and i in p_i):
                print(f'{i}: Title: {j}')
        id = input('Book id: ')
        if id in books.keys() and (action == 3 and id not in p_i) or (action == 4 and id in p_i):
            return id

def borrows_return(action=3):
    global p_i

    id = get_id(action)
    if action == 3:
        p_i.append(id)
        print(f'The borrowed book, {books[id]}, was successful\nHappy reading =)')
    else:
        p_i.remove(id)
        print(f'The return of the book, {books[id]}, was successful\nThanks for reading =)')
    w_f('patron_info', ','.join(p_i))


def action_5():
    print('Name:', name)
    for i in p_i:
        print(books[i])


while start:
    print(hi)
    for i, k in menu.items():
        print(f'{i}. {k}')
    num = input()
    match num:
        case '1':
            print_books()
        case '2':
            print_books(2)
        case '3':
            borrows_return()
        case '4':
            borrows_return(4)
        case '5':
            action_5()
        case '6':
            print(bye)
            break
        case _:
            print('Enter the numbers from 1 to 6 only')
    print()
