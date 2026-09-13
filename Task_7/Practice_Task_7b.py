class Book:
    def __init__(self, title, author, publisher, page_count, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.price = price

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, \
                Pages: {self.page_count}, Price: {self.price}")

class EBook(Book):
    def __init__(self, title, author, publisher, page_count, price, file_size, file_format):
        super().__init__(title, author, publisher, page_count, price)
        self.file_size = file_size
        self.file_format = file_format

    def __str__(self):
        return (F"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, \
                Pages: {self.page_count}, Price: {self.price}, File size: {self.file_size} \
                File format: {self.file_format}")


books = []
with open('book_info.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 5:
            book = Book(data[0], data[1], data[2], int(data[3]), float(data[4]))
            books.append(book)

# Display books
print("Books in collection:")
for book in books:
    print(book)

# Add new ebooks
ebooks = []

while True:
    title = input("Title (or 'done' to finish): ")
    if title.lower() == 'done':
        break

    author = input("Author: ")
    publisher = input("Publisher: ")
    page_count = int(input("Page count: "))
    price = float(input("Price: "))
    file_size = float(input("File size (MB): "))
    file_format = input("File format: ")

    ebooks.append(EBook(title, author, publisher, page_count, price, file_size, file_format))

print("\nEBooks entered:")
for ebook in ebooks:
    print(ebook)
