class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    def getBookInfo(self):
        return f'{self.title},{self.author},{self.price}'
a = Book('파이썬 정복', '김상형', 22000)
b = Book('이것이 MariaDB다', '우재남', 30000)
c = Book('생활코딩! HTML+CSS+자바스크립트', '이고잉', 27000)
d = Book('파이썬 웹프로그래밍', '김석훈', 22000)
e = Book('맛있는 MongoDB', '정승호', 28000)
books = [a, b, c, d, e]
for i in books:
    for j in i.getBookInfo().split(','):
        print(j)
    print('-' * 9)
# print(a.getBookInfo())
# print(b.getBookInfo())