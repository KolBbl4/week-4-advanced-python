from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author:str

book = Book(title="Fahrenheit 451", author="Bradbury")

print(book.author)
