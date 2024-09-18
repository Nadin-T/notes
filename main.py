from note_manager import add_note, clear_notes, edit_note, delete_note, list_notes, get_note, load_notes

def main():
    load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Список заметок")
        print("5. Просмотр заметки")
        print("6. Очистить список заметок")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите содержимое заметки: ")
            add_note(title, body)
        elif choice == "2":
            note_id = input("Введите ID заметки для редактирования: ")
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое содержимое: ")
            edit_note(note_id, new_title, new_body)
        elif choice == "3":
            note_id = input("Введите ID заметки для удаления: ")
            delete_note(note_id)
        elif choice == "4":
            filter_date = input("Введите дату для фильтрации (ГГГГ-ММ-ДД, оставьте пустым для показа всех): ")
            list_notes(filter_date)
        elif choice == "5":
            identifier = input("Введите ID или заголовок заметки: ")
            get_note(identifier)
        elif choice == "6":
            clear_notes()
        elif choice == "0":
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
