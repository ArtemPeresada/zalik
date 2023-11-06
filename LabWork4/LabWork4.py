class Книга:
    def __init__(self, назва, кількість_сторінок):
        self.назва = назва
        self.кількість_сторінок = кількість_сторінок
        self.прочитано_сторінок = 0

    def обрахунок_відсотків_прочитаного(self):
        if self.кількість_сторінок > 0:
            return (self.прочитано_сторінок / self.кількість_сторінок) * 100
        else:
            return 0

    def прочитати(self, сторінки):
        if сторінки > 0:
            self.прочитано_сторінок += сторінки
            if self.прочитано_сторінок > self.кількість_сторінок:
                self.прочитано_сторінок = self.кількість_сторінок

class Бібліотека:
    def __init__(self):
        self.список_книг = []

    def додати_книгу(self, назва, кількість_сторінок):
        книга = Книга(назва, кількість_сторінок)
        self.список_книг.append(книга)

    def редагувати_книгу(self, назва, прочитано_сторінок):
        for книга in self.список_книг:
            if книга.назва == назва:
                книга.прочитати(прочитано_сторінок)
                print(f'Відсоток прочитаних сторінок для книги "{книга.назва}": {книга.обрахунок_відсотків_прочитаного()}%')
                break

    def видалити_книгу(self, назва):
        for книга in self.список_книг:
            if книга.назва == назва:
                self.список_книг.remove(книга)
                break

    def вивести_список_книг(self):
        for книга in self.список_книг:
            print(f'Назва: {книга.назва}, Прочитано: {книга.обрахунок_відсотків_прочитаного()}%')

# Приклад використання класів:
бібліотека = Бібліотека()

while True:
    дія = input("Оберіть дію (додати/редагувати/видалити/вивести/вийти): ")
    
    if дія == 'додати':
        назва = input("Введіть назву книги: ")
        кількість_сторінок = int(input("Введіть кількість сторінок: "))
        бібліотека.додати_книгу(назва, кількість_сторінок)
        
    if дія == 'редагувати':
        назва = input("Введіть назву книги: ")
        прочитано_сторінок = int(input("Введіть кількість прочитаних сторінок: "))
        бібліотека.редагувати_книгу(назва, прочитано_сторінок)
    
    elif дія == 'видалити':
        назва = input("Введіть назву книги для видалення: ")
        бібліотека.видалити_книгу(назва)
    
    elif дія == 'вивести':
        бібліотека.вивести_список_книг()
    
    elif дія == 'вийти':
        break
