from datetime import datetime
import json
from notes import Note, get_next_id

notes = []

def add_note(title, body):
    note = Note(get_next_id(notes), title, body)
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

def get_note(identifier):
    if identifier.isdigit():
        for note in notes:
            if note.id == identifier:
                print_note_details(note)
                return
        print(f"Заметка с ID '{identifier}' не найдена.")
    else:
        found_notes = [note for note in notes if note.title == identifier]
        if found_notes:
            for note in found_notes:
                print_note_details(note)
                print()
        else:
            print(f"Заметки с заголовком '{identifier}' не найдены.")

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

def clear_notes():
    global notes
    notes = []
    save_notes()
    print("Все заметки были удалены.")

def print_note_details(note):
    print(f"ID: {note.id}")
    print(f"Заголовок: {note.title}")
    print(f"Содержимое: {note.body}")
    print(f"Дата создания: {note.created_at}")
    print(f"Дата обновления: {note.updated_at}")
