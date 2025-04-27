from libMgmtSys import LibraryManagementSystem

if __name__ == "__main__":
    lms = LibraryManagementSystem()

    # Adding Books
    lms.add_book("The Secret of Everything","Rhonda Byrne","9780316769488","Spiritual",5)
    lms.add_book("To kill a Mockingbird","Harper Lee","9780061120084","Fiction",3)
    lms.add_book("1984","George Orwell","9780451524935","Dystopian",4)

    # Adding Members
    lms.add_member(1, "Sumit")
    lms.add_member(2, "Bunty")

    # Borrow Books
    lms.borrow_book(1,"9780316769488")
    lms.borrow_book(2,"9780061120084")
    
    # Show each member's borrowed books
    print("\n Borrowed Books")
    lms.show_member_borrowed_books(1)
    lms.show_member_borrowed_books(2)
    
    # Return Books
    lms.return_book(1,"9780316769488")
    lms.return_book(2,"9780061120084")

    # show all library books
    print("\n All Library books")
    lms.show_library_books()


    # Show transaction log
    print("\n Transaction log")
    lms.show_transactions()
    




    
