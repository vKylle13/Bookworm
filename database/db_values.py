import sqlite3

conn = sqlite3.connect('database/Bookworm.db')

cursor = conn.cursor()

book_data = [
    ('Large Deployable Satellite Antennas: Design Theory, Methods and Applications', 'Baoyan Duan, Yiqun Zhang, Jingli Du', '2020-06-29', 'Non-fiction', 'book1.json'),
    ('Black Lies, White Lies: The Truth According to Tony Brown', 'Tony Brown', '2009', 'Fiction', 'book2.json'),
    ('Everything Sad Is Untrue: A True Story', 'Daniel Nayeri', '2022', 'Non-fiction', 'book3.json'),
    ('How Successful People Think: Change Your Thinking, Change Your Life', 'John C. Maxwell', '2011', 'Non-fiction', 'book4.json'),
    ('Violets', 'Kyung-Sook Shin', '1999', 'Fiction', 'book5.json'),
    ('Advanced Software Engineering', 'Milton Cash', 'Unknown', 'Non-fiction', 'book6.json'),
    ('11th Hour', 'James Patterson', '2015', 'Fiction', 'book7.json'),
    ('Robin Sharma The Greatness Guide', 'Robin Sharma', '2015', 'Non-fiction', 'book8.json'),
    ('The Four: The Hidden DNA of Amazon, Apple, Facebook, and Google', 'Scott Galloway', '2015', 'Non-fiction', 'book9.json'),
    ('Van Start', 'Wim Tersteeg', '2015', 'Fiction', 'book10.json'),
    ('100M Offers', 'Alex Hormozi', '2015', 'Non-fiction', 'book11.json'),
    ('Brother Dear', 'R. Phoenix', '2012', 'Fiction', 'book12.json'),
    ('Woven by Gold (Beasts of the Briar #2)', 'Elizabeth Helen', '2022-10-02', 'Fiction', 'book13.json'),
    ('How to Be a People Magnet: Finding Friends and Lovers and Keeping Them for Life', 'Leil Lowndes', '2012', 'Non-fiction', 'book14.json'),
    ('Lost in London', 'Cindy Callaghan', '2012', 'Fiction', 'book15.json'),
    ('Music and Movement: A Way of Life for the Young Child', 'Linda Carol Edwards', '2012', 'Non-fiction', 'book16.json'),
    ('Prahlad', 'Kevin Missal', '2012', 'Fiction', 'book17.json'),
    ('Savage Hearts', 'J.T. Geissinger', '2004', 'Fiction', 'book18.json'),
    ('The Cruel Prince', 'Holly Black', '2004', 'Fiction', 'book19.json'),
    ('Afterwar: Healing the Moral Wounds of Our Soldiers', 'Nancy Sherman', '2004', 'Non-fiction', 'book20.json'),
    ('Thinking, Fast and Slow', 'Daniel Kahneman', '2004', 'Non-fiction', 'book21.json'),
    ('For Whom the Bell Tolls', 'Ernest Hemingway', '2003', 'Fiction', 'book22.json'),
    ('I Will Teach You to Be Rich, Second Edition: No Guilt. No Excuses. No BS. Just a 6-Week Program That Works', 'Ramit Sethi', '2001', 'Non-fiction', 'book23.json'),
    ('Love and Other Words', 'Christina Lauren', '2003', 'Fiction', 'book24.json'),
    ('My Fault, Culpable', 'Mercedes Ron', '2003', 'Fiction', 'book25.json'),
    ('Destined to Reign', 'Joseph Prince', '2001', 'Non-fiction', 'book26.json'),
    ('Secret Sin: A Byrne Brothers Novella', 'Jill Ramsower', '2021', 'Fiction', 'book27.json'),
    ('The Immeasurable Depth of You', 'Maria Ingrande Mora', '2001', 'Fiction', 'book28.json'),
    ('A Little Life', 'Hanya Yanagihara', '2023', 'Fiction', 'book29.json'),
    ('Aristotle and Dante Dive into the Waters of the World', 'Benjamin Alire Saenz', '2005', 'Fiction', 'book30.json'),
    ('Dark Psychology Secrets', 'William Cooper', '2005', 'Non-fiction', 'book31.json'),
    ('Happy Place', 'Emily Henry', '2003', 'Fiction', 'book32.json'),
    ('The Best of Everything', 'Rona Jaffe', '2003', 'Fiction', 'book33.json'),
    ('Practical Guide to Diagnostic Parasitology', 'Lynne Shore Garcia', '2021', 'Non-fiction', 'book34.json'),
    ("Daddy's Home: A Memoir of Fatherhood and Laughter", 'Alan Thicke', '2003', 'Non-fiction', 'book35.json'),
    ('The Color Purple', 'Alice Walker', '1982', 'Fiction', 'book36.json'),
    ('The Success Principles: How to Get from Where You Are to Where You Want to Be', 'Jack Canfield', '2004', 'Non-fiction', 'book37.json'),
    ('The Alchemist', 'Paulo Coelho', '1988', 'Fiction', 'book38.json'),
    ('The Power of Now: A Guide to Spiritual Enlightenment', 'Eckhart Tolle', '1997', 'Non-fiction', 'book39.json'),
    ('To Kill a Mockingbird', 'Harper Lee', '1960', 'Fiction', 'book40.json')
]

insert_book_query = '''
    INSERT INTO bookTable (bookTitle, bookAuthor, bookDate, bookGenre, bookPath)
    VALUES (?, ?, ?, ?, ?)
'''

user_info = [
    ('TadaMacky', 'tadamacky@gmail.com', 'niggas in my butthole', 'Peasant'),
    ('zofx', 'zofiashannelle@gmail.com', 'FR E SH A VOCA DO', 'Noble')
]

insert_user_query = '''
    INSERT INTO userTable (userName, userEmail, userPassword, userLevel)
    VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_book_query, book_data)
# cursor.executemany(insert_user_query, user_info)

conn.commit()
conn.close()
