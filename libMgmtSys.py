"""This will have following classes:
1. Book
2. Member
3. Library
4. Transaction
5. TrasnactionLogger
6. LibraryManagementSystem
"""

from datetime import datetime

# Abstract base class for common interface
from abc import ABC, abstractmethod

# Book Class: represents a single book in the library
class Book:

    def __init__(self, title, author, isbn, genre, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.copies_available = copies_available

    def borrow_book(self):
        """Decreases the number of available copies of the book when borrowed"""
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        else:
            return False
        
    def return_book(self):
        """Increases the number of available copies of the book when returned"""
        self.copies_available += 1

    def get_details(self):
        """Returns the details of the book"""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}"
    
    
# Member Class: represents a library user

class Member:

    def __init__(self, member_id,name):
            self.member_id = member_id
            self.name = name
            self.borrowed_books = []

    def borrow_book(self, book):
            """Allows a member to borrow a book"""
            if book.borrow_book():
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book.title}")
            else:
                print(f"Sorry, {book.title} is currently unavialble")

    def return_book(self, book):
            """Allows a member to return a book"""
            if book in self.borrowed_books:
                book.return_book()
                self.borrowed_books.remove(book)
            else:
                print(f"{self.name} didn't borrow {book.title}")

    def get_borrowed_books(self):
            """Returns a list of borrowed books"""
            return [book.title for book in self.borrowed_books]
    

# Library Class: represents the library and manages books and members

class Library:
     
    def __init__(self):
       self.books = []
       self.members = []

    def add_book(self, book):
         """Adds a book to the library"""
         self.books.append(book)

    def add_member(self, member):
         """Adds a member to the library"""
         self.members.append(member)

    def find_book_by_isbn(self, isbn):
         """Finds a book by ISBN"""
         for book in self.books:
              if book.isbn == isbn:
                   return book
         return None
    
    def get_all_books(self):
         """Returns all books details"""
         return [book.get_details() for book in self.books]
    


# Transaction Class: represents a borrowing/returning transaction

class TransactionLogger:
     
     def __init__(self):
          self.transactions = []

     def log_transaction(self, transaction):
          """Logs a new transaction"""
          self.transactions.append(transaction)
          print(f" Transaction logged: {transaction}")

     def show_transactions(self):
          """Display all transactions"""
          for transaction in self.transactions:
               print(transaction)


# Transaction Class: for representing a transaction

class Transaction:

     def __init__(self, member, book, transaction_type):
          self.member = member
          self.book = book
          self.trasaction_type = transaction_type
          self.timestamp = datetime.now()

     def __str__(self):
          """Returns a string representing a transaction"""
          return f"{self.member.name} {self.trasaction_type} {self.book.title} at {self.timestamp}"


# Library Management System: integrates everything

class LibraryManagementSystem:
     
     def __init__(self):
          self.library = Library()
          self.transaction_logger = TransactionLogger()

     def add_book(self, title, author, isbn, genre, copies_available):
          """Adds a book to the library"""
          book = Book(title, author, isbn, genre, copies_available)
          self.library.add_book(book)

     def add_member(self, member_id, name):
          """Adds a member to borrow a book"""
          member = Member(member_id, name)
          self.library.add_member(member)

     def borrow_book(self, member_id, isbn):
          """Allows a member to borrow a book"""
          member = next((p for p in self.library.members if p.member_id == member_id),None)
          book = self.library.find_book_by_isbn(isbn)
          if member and book:
               member.borrow_book(book)
               transaction = Transaction(member, book, "borrowed")
               self.transaction_logger.log_transaction(transaction)

     def return_book(self, member_id, isbn):
          """Allows a member to return a book"""
          member = next((p for p in self.library.members if p.member_id == member_id),None)
          book = self.library.find_book_by_isbn(isbn)
          if member and book:
               member.return_book(book)
               transaction = Transaction(member, book, "returned")
               self.transaction_logger.log_transaction(transaction)

     def show_library_books(self):
          """Show all books in the library"""
          for book in self.library.get_all_books():
               print(book)


     def show_member_borrowed_books(self, member_id):
          """Show all books borrowed by a member"""
          member = next((p for p in self.library.members if p.member_id == member_id),None)
          if member:
               print(f"{member.name} has borrowed: {','.join(member.get_borrowed_books())}")
          else:
               print(f"Member with id {member_id} not found")

     def show_transactions(self):
          """Show all logged transactions"""
          self.transaction_logger.show_transactions()


          


          


          

    

        
        




