'''Реализовать консольное приложение заметки, с сохранением,
чтением, добавлением, редактированием и удалением заметок.

Заметка должна содержать идентификатор, заголовок, тело заметки
и дату/время создания или последнего изменения заметки.
'''
import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

# notes = []

def get_next_id():
    if not notes:
        return "1"
    else:
        return str(int(notes[-1].id) + 1)

def add_note(title, body):
    note = Note(get_next_id(), title, body)
    notes.append(note)
    save_notes()
    print(f"Заметка '{note.title}' успешно сохранена.")


def edit_note(note_id, new_title, new_body):
    for note in notes:
        if note.id == note_id:
            note.title = new_title
            note.body = new_body
            note.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print(f"Заметка '{note.title}' успешно обновлена.")
            return
    print(f"Заметка с ID '{note_id}' не найдена.")


def delete_note(note_id):
    for i, note in enumerate(notes):
        if note.id == note_id:
            del notes[i]
            save_notes()
            print(f"Заметка '{note.title}' успешно удалена.")
            return
    print(f"Заметка с ID '{note_id}' не найдена.")

def list_notes(filter_date=None):
    if filter_date:
        filtered_notes = [note for note in notes if note.created_at.startswith(filter_date)]
    else:
        filtered_notes = notes
    
    if filtered_notes:
        print("Список заметок:")
        for note in filtered_notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Дата: {note.created_at}")
    else:
        print("Нет сохраненных заметок.")

def save_notes():
    with open("notes.json", "w") as f:
        json.dump([note.__dict__ for note in notes], f, indent=4)


def load_notes():
    global notes
    try:
        with open("notes.json", "r") as f:
            note_dicts = json.load(f)
            notes = []
            for note_dict in note_dicts:
                note = Note(note_dict["id"], note_dict["title"], note_dict["body"])
                note.created_at = note_dict["created_at"]
                note.updated_at = note_dict["updated_at"]
                notes.append(note)
    except FileNotFoundError:
        print("Файл с заметками не найден. Создается новый файл.")
    except json.JSONDecodeError:
        print("Ошибка в формате файла с заметками. Создается новый файл.")
    except Exception as e:
        print(f"Произошла ошибка при загрузке заметок: {e}")
        print("Создается новый файл с заметками.")
    finally:
        if not notes:
            save_notes()


def main():
    load_notes()
    
    print("Выберите действие: ")
    print("1. Добавить заметку")
    print("2. Изменить заметку")
    print("3. Удалить заметку")
    print("4. Показать заметки")
    print("0. Выход из программы")
    
    while True:
        command = input()

        if command == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add_note(title, body)
        elif command == "2":
            note_id = input("Введите ID заметки: ")
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое тело: ")
            edit_note(note_id, new_title, new_body)
        elif command == "3":
            note_id = input("Введите ID заметки: ")
            delete_note(note_id)
        elif command == "4":
            filter_date = input("Введите дату для фильтрации (YYYY-MM-DD, оставьте пустым для показа всех): ")
            list_notes(filter_date)
        elif command == "0":
            save_notes()
            break
        else:
            print("Неизвестная команда. Попробуйте еще раз.")
        
        print()
        print("Выберите действие: ")
        print("1. Добавить заметку")
        print("2. Изменить заметку")
        print("3. Удалить заметку")
        print("4. Показать заметки")
        print("0. Выход из программы")

if __name__ == "__main__":
    main()
