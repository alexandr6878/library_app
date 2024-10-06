import tkinter as tk
from tkinter import messagebox


class Book:

  def __init__(self, place, title, author):
    self.place = place
    self.title = title
    self.author = author
    self.is_borrowed = False

  def __str__(self):
    return self.title

class Library:

  def __init__(self):
    self.books = []
    self.borrowed_books = []

  def display_books(self):
    for book in self.books:
      print(f"Place: {book.place}, Title: {book.title}, Author: {book.author}")

  def add_book(self, book):
    self.books.append(book)


class Member(Library):

  def __init__(self, age, name):
    self.borrow_books = []
    self.age = age
    self.name = name

  def borrow_book(self, title, library):
    for book in library.books:
      if title == book.title:
        self.borrow_books.append(book)
        library.borrowed_books.append(book)
        library.book.is_borrowed = True
        print(f"You have borrowed {title}.")

  def see_books(self):
    for book in self.borrow_books:
      print(book.title)

  def return_book(self, title, library):
    for book in self.borrow_books:
      if title == book.title:
        self.borrow_books.remove(book)
        library.borrowed_books.remove(book)
        library.book.is_borrowed = False
        print(f"You have returned {title}.")


class Librarian():

  def __init__(self, library):
    self.library = library

  def add_book(self, place, title, author):
    book = Book(place, title, author)
    self.library.add_book(book)

  def view_borrowed(self):
    return [book for book in self.library.borrowed_books]


# kiev_lib = Library()
# odessa_lib = Library()
# alex = Member(16, "Alex")
# alex.borrow_book("Harry Potter", kiev_lib)


class LibraryApp:

  def __init__(self, root, library, librarian):
    self.root = root
    self.library = library
    self.librarians = librarian
    root.title('Library System')
    root.geometry("700x800")

    self.book_frame = tk.Frame(root)
    self.book_frame.pack(pady=10)
    tk.Label(self.book_frame, text="Add the book").grid(row=1, column=0)
    tk.Label(self.book_frame, text="Author").grid(row=2, column=0)
    tk.Label(self.book_frame, text="Title").grid(row=3, column=0)
    tk.Label(self.book_frame, text="Place").grid(row=4, column=0)
    # add_BOOK
    self.autor_entry = tk.Entry(self.book_frame)
    self.autor_entry.grid(row=5, column=0)
    self.title_entry = tk.Entry(self.book_frame)
    self.title_entry.grid(row=6, column=0)
    self.place_entry = tk.Entry(self.book_frame)
    self.place_entry.grid(row=7, column=0)

    tk.Button(self.book_frame, text="Add",
              command=self.add_book).grid(row=1, column=1)


    # BORROW BOOK UI
    self.borrow_frame = tk.Frame(root)
    self.borrow_frame.pack(pady=10)
    tk.Label(self.borrow_frame, text="Borrow the book").grid(row=8, column=0)
    tk.Label(self.borrow_frame, text="Title").grid(row=9, column=0)
    self.borrow_entry = tk.Entry(self.borrow_frame)
    self.borrow_entry.grid(row=11, column=0)
    tk.Button(self.borrow_frame, text="Borrow",
              command=self.borrow_book).grid(row=8, column=1)


    # RETURN BOOK UI
    self.return_frame = tk.Frame(root)
    self.return_frame.pack(pady=10)
    tk.Label(self.return_frame, text="Return the book").grid(row=12, column=0)
    tk.Label(self.return_frame, text="Title").grid(row=13, column=0)
    self.return_entry = tk.Entry(self.return_frame)
    self.return_entry.grid(row=14, column=0)
    tk.Button(self.return_frame, text="Return",
              command=self.return_book).grid(row=12, column=1)

    # BORROWED BOOKS'
    self.borrowed_frame = tk.Frame(root)
    self.borrowed_frame.pack(pady=10)
    tk.Label(self.borrowed_frame, text="View borrowed books").grid(row=15,
                                                                   column=0)
    tk.Button(self.borrowed_frame, text="View",
              command=self.view_books).grid(row=15, column=1)
    self.borrowed_books_label = tk.Label(self.borrowed_frame, text="")
    self.borrowed_books_label.grid(row=15, column=0)

  def view_books(self):
    borrowed_book = [str(book) for book in self.library.borrowed_books]
    # print(borrowed_book)
    if (borrowed_book):
      self.borrowed_books_label.config(text='Borrowed books: ' +
                                       ', '.join(borrowed_book))
      self.borrow_entry.delete(0, tk.END)
    else:
      messagebox.showwarning("Error",  "Something goes wrong.")

  def return_book(self):
    title = self.title_entry.get()
    for book in self.library.borrowed_books:
      if (book.title == title):
        self.library.borrowed_books.remove(book)
        book.is_borrowed = False
        messagebox.showinfo("Success", f"You have returned '{title}'.")
      else:
        messagebox.showwarning("Error", f"'{title}' is not available.")

  def add_book(self):
    title = self.title_entry.get()
    place = self.place_entry.get()
    author = self.autor_entry.get()
    book = Book(place, title, author)
    self.library.add_book(book)
    messagebox.showinfo("Success", f"You have add '{title}'.")


  def borrow_book(self):
    title = self.borrow_entry.get()
    if len(self.library.books) == 0:
      self.borrow_entry.delete(0, tk.END)
      messagebox.showwarning("Error", f"'{title}' is not available or already borrowed.")
    for book in self.library.books:
      if (book.title == title and not book.is_borrowed):
        self.library.borrowed_books.append(book)
        book.is_borrowed = True
        self.borrow_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"You have borrowed '{title}'.")
      else:
        self.borrow_entry.delete(0, tk.END)
        messagebox.showwarning("Error", f"'{title}' is not available or already borrowed.")


root = tk.Tk()
library = Library()
librarian = Librarian(library)
app = LibraryApp(root, library, librarian)

root.mainloop()