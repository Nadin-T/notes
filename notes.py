'''Реализовать консольное приложение заметки, с сохранением,
чтением, добавлением, редактированием и удалением заметок.

Заметка должна содержать идентификатор, заголовок, тело заметки
и дату/время создания или последнего изменения заметки.
'''

from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

def get_next_id(notes):
    if not notes:
        return "1"
    else:
        return str(int(notes[-1].id) + 1)
