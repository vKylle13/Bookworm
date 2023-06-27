import sqlite3

conn = sqlite3.connect('database/Bookworm.db')

cursor = conn.cursor()

create_book_table_query = '''
    CREATE TABLE IF NOT EXISTS bookTable (
        bookAuthor VARCHAR(100),
        bookTitle VARCHAR(100),
        bookDate DATE,
        bookGenre VARCHAR(100),
        bookPath VARCHAR(255),
        PRIMARY KEY (bookTitle)
    )
'''
cursor.execute(create_book_table_query)

create_user_table_query = '''
    CREATE TABLE IF NOT EXISTS userTable (
        userName VARCHAR(100),
        userEmail VARCHAR(100),
        userPassword VARCHAR(200),
        userLevel VARCHAR(10),
        PRIMARY KEY (userName)
    )
'''
cursor.execute(create_user_table_query)

create_borrowed_books_table_query = '''
    CREATE TABLE IF NOT EXISTS borrowedBooks (
        userName VARCHAR(100),
        bookTitle VARCHAR(100),
        userBorrow VARCHAR(100),
        PRIMARY KEY (userBorrow)
    )
'''
cursor.execute(create_borrowed_books_table_query)

conn.commit()
conn.close()
