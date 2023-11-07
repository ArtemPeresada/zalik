class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.pages_read = 0

    def calculate_percentage_read(self):
        if self.page_count > 0:
            return (self.pages_read / self.page_count) * 100
        else:
            return 0

    def read(self, pages):
        if pages > 0:
            self.pages_read += pages
            if self.pages_read > self.page_count:
                self.pages_read = self.page_count

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, title, page_count):
        book = Book(title, page_count)
        self.book_list.append(book)

    def edit_book(self, title, pages_read):
        for book in self.book_list:
            if book.title == title:
                while pages_read > book.page_count:
                    print(f'Ви ввели більше сторінок, ніж у книзі "{book.title}".')
                    pages_read = input(f'Введіть кількість прочитаних сторінок для книги "{book.title}": ')
                    
                    try:
                        pages_read = int(pages_read)
                    except ValueError:
                        print("Будь ласка, введіть ціле число.")
                book.read(pages_read)
                print(f'Відсоток прочитаних сторінок для книги "{book.title}": {book.calculate_percentage_read()}%')
                break

    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)
                break

    def list_books(self):
        for book in self.book_list:
            print(f'Назва: {book.title}, Прочитано: {book.calculate_percentage_read()}%')

library = Library()

while True:
    action = input("Оберіть дію (add/edit/remove/list/exit): ")
    
    if action == 'add':
        title = input("Введіть назву книги: ")
        
        while True:
            page_count = input("Введіть кількість сторінок: ")
            try:
                page_count = int(page_count)
                break
            except ValueError:
                print("Будь ласка, введіть ціле число.")
        library.add_book(title, page_count)
        
    if action == 'edit':
        title = input("Введіть назву книги: ")
        
        while True:
            pages_read = input(f'Введіть кількість прочитаних сторінок для книги "{title}": ')
            try:
                pages_read = int(pages_read)
                break
            except ValueError:
                print("Будь ласка, введіть ціле число.")
        library.edit_book(title, pages_read)
    
    elif action == 'remove':
        title = input("Введіть назву книги для видалення: ")
        library.remove_book(title)
    
    elif action == 'list':
        library.list_books()
    
    elif action == 'exit':
        break
