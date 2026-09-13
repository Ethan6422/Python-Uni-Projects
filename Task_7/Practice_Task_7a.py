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

# Add new book
new_book = Book("Animal Farm", "George Orwell", "Secker & Warburg", 112, 7.50)
print(f"\nAdding: {new_book}")

with open('book_info.txt', 'a') as file:
    file.write(f"\n{new_book.title},{new_book.author},{new_book.publisher},{new_book.page_count},{new_book.price}")
