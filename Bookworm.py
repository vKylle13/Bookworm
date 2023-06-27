# =================================================================================================================================
# Imports
# =================================================================================================================================

import os
import json
import sqlite3
import tkinter as tk
import sys
import PyPDF2
import customtkinter as ctk
from PIL import Image

# =================================================================================================================================
# Register Window
# =================================================================================================================================

class registerWindow:

    def __init__(self):
        self.register = ctk.CTk()
        self.register.title("Bookworm: Register")
        self.register.geometry("500x650")
        self.register.resizable(False, False)
        self.register.iconbitmap("resources\logcon.ico")

        # color variables
        self.main_color = '#282C34'
        self.widget_color = '#383E4A'
        self.button_hover = '#AF87E9'

        # Temporary Colors
        colorpink = '#FF6666'
        coloryellow = '#FF9900'
        coloraqua = '#7755A7'

        # font variables
        self.entry_font = ctk.CTkFont(family="Arial", size=20)

        # frame skeleton > frame 1
        self.frame1 = tk.Frame(self.register, width=500, height=177, bg=self.main_color)
        self.frame1.pack_propagate(False)
        self.frame1.pack()

        # frame skeleton > frame 2
        self.frame2 = tk.Frame(self.register, width=500, height=270, bg=self.main_color)
        self.frame2.pack_propagate(False)
        self.frame2.pack()

        # frame skeleton > frame 3
        self.frame3 = tk.Frame(self.register, width=500, height=203, bg=self.main_color)
        self.frame3.pack_propagate(False)
        self.frame3.pack()

        # frame 1 widgets > container for image title
        self.image_logo = ctk.CTkImage(light_image=Image.open("resources/bookworm.png"), dark_image=Image.open("resources/bookworm.png"), size=(244, 31))
        self.label_logo = ctk.CTkLabel(self.frame1, image=self.image_logo, text="")
        self.label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # frame 2 widgets > user id frame
        self.frame_userID = ctk.CTkFrame(self.frame2, width=425, height=60, fg_color=self.widget_color)
        self.frame_userID.pack_propagate(False)
        self.frame_userID.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # frame 2 widgets > user id icon
        self.image_userIcon = ctk.CTkImage(light_image=Image.open("resources/usericon.png"), dark_image=Image.open("resources/usericon.png"), size=(29, 29))
        self.label_userIcon = ctk.CTkLabel(self.frame_userID, image=self.image_userIcon, text="")
        self.label_userIcon.pack(side="left", padx=(15, 0))

        # frame 2 widgets > user id entry
        self.entry_userID = ctk.CTkEntry(self.frame_userID, placeholder_text="User ID", width=350, height=60, fg_color=self.widget_color, border_width=0, placeholder_text_color='#a6a8ae', font=self.entry_font)
        self.entry_userID.pack(side="left", padx=(15, 0))

        # frame 2 widgets > password frame
        self.frame_password = ctk.CTkFrame(self.frame2, width=425, height=60, fg_color=self.widget_color)
        self.frame_password.pack_propagate(False)
        self.frame_password.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # frame 2 widgets > password icon
        self.image_passIcon = ctk.CTkImage(light_image=Image.open("resources/passicon.png"), dark_image=Image.open("resources/passicon.png"), size=(26, 31))
        self.label_passIcon = ctk.CTkLabel(self.frame_password, image=self.image_passIcon, text="")
        self.label_passIcon.pack(side="left", padx=(15, 0))

        # frame 2 widgets > password entry
        self.entry_password = ctk.CTkEntry(self.frame_password, placeholder_text="Key Phrase", width=350, height=60, fg_color=self.widget_color, border_width=0, placeholder_text_color='#a6a8ae', font=self.entry_font)
        self.entry_password.pack(side="left", padx=(15, 0))

        # frame 2 widgets > email frame
        self.frame_email = ctk.CTkFrame(self.frame2, width=425, height=60, fg_color=self.widget_color)
        self.frame_email.pack_propagate(False)
        self.frame_email.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # frame 2 widgets > email icon
        self.image_emailIcon = ctk.CTkImage(light_image=Image.open("resources/mail.png"), dark_image=Image.open("resources/mail.png"), size=(29, 21))
        self.label_emailIcon = ctk.CTkLabel(self.frame_email, image=self.image_emailIcon, text="")
        self.label_emailIcon.pack(side="left", padx=(15, 0))

        # frame 2 widgets > email entry
        self.entry_email = ctk.CTkEntry(self.frame_email, placeholder_text="Email Adress", width=350, height=60, fg_color=self.widget_color, border_width=0, placeholder_text_color='#a6a8ae', font=self.entry_font)
        self.entry_email.pack(side="left", padx=(15, 0))

        # frame 3 widgets > login button
        self.button_login = ctk.CTkButton(self.frame3, width=290, height=50, fg_color=self.widget_color, text="LOGIN", font=self.entry_font, hover_color=self.button_hover, command=self.to_login)
        self.button_login.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # frame 3 widgets > sign up button
        self.button_signup = ctk.CTkButton(self.frame3, width=290, height=50, fg_color=self.widget_color, text="REGISTER", font=self.entry_font, hover_color=self.button_hover, command=self.insert_information)
        self.button_signup.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def to_login(self):
        self.register.destroy()
        login_window = loginWindow()
        login_window.login.mainloop()

    def insert_information(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        userID = self.entry_userID.get()

        conn = sqlite3.connect("database\Bookworm.db")
        c = conn.cursor()

        c.execute("INSERT INTO userTable (userName, userEmail, userPassword, userLevel) VALUES (?, ?, ?, ?)",
                  (userID, email, password, "Peasant"))
        
        conn.commit()
        conn.close()

        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_userID.delete(0, tk.END)

        print("Pushed")
        self.to_login()

# =================================================================================================================================
# User Window
# =================================================================================================================================

class userWindow:

    def __init__(self, username):
        # user window properties
        self.userwindow = ctk.CTk()
        self.userwindow.title("Bookworm: User Window")
        self.userwindow.geometry('1280x720')
        self.userwindow.resizable(False, False)
        self.userwindow.iconbitmap("resources\logcon.ico")
        self.theusername = username

        # color variables
        main_color = '#282C34'
        secondary_color = '#21252B'
        thirdary_color = '#383E4A'
        button_hover = '#7755A7'

        # font variables
        buttonfont = ctk.CTkFont(family="Arial", size=15, weight="bold")

        # frame skeleton > frame 1
        self.frame_topbar = tk.Frame(self.userwindow, width=1280, height=55)
        self.frame_topbar.pack_propagate(False)
        self.frame_topbar.pack()

        # frame skeleton > frame 2
        self.frame_leftmain = tk.Frame(self.userwindow, width=641, height=665, bg=main_color)
        self.frame_leftmain.pack_propagate(False)
        self.frame_leftmain.pack(side="left")

        # frame skeleton > frame 3
        self.frame_rightmain = tk.Frame(self.userwindow, width=640, height=665, bg=main_color)
        self.frame_rightmain.pack_propagate(False)
        self.frame_rightmain.pack(side="right")

        # topbar widgets > container for image title
        self.frame_tbleftcontainer = tk.Frame(self.frame_topbar, width=228, height=55, bg=secondary_color)
        self.frame_tbleftcontainer.pack_propagate(False)
        self.frame_tbleftcontainer.pack(side="left")

        # topbar widgets > the image title
        self.image_bookworm = ctk.CTkImage(light_image=Image.open("resources/bookworm.png"), dark_image=Image.open("resources/bookworm.png"), size=(199, 25))
        self.label_bookworm = ctk.CTkLabel(self.frame_tbleftcontainer, image=self.image_bookworm, text="")
        self.label_bookworm.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # topbar widgets > container for app drag function
        self.frame_tbcentercontainer = tk.Frame(self.frame_topbar, width=878, height=55, bg=secondary_color)
        self.frame_tbcentercontainer.pack_propagate(False)
        self.frame_tbcentercontainer.pack(side="left")

        # topbar widgets > container for signed in
        self.frame_tbrightcontainer = tk.Frame(self.frame_topbar, width=174, height=55, bg=secondary_color)
        self.frame_tbrightcontainer.pack_propagate(False)
        self.frame_tbrightcontainer.pack(side="left")

        # topbar widgets > signed in
        self.label_signedin = ctk.CTkLabel(self.frame_tbrightcontainer, text="User: " + self.theusername, font=buttonfont)
        self.label_signedin.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # left side widgets > top container
        self.frame_topcontainer = tk.Frame(self.frame_leftmain, width=603, height=91, bg=main_color)
        self.frame_topcontainer.pack_propagate(False)
        self.frame_topcontainer.pack()

        # left side widgets > frame for search box
        self.frame_searchboxbg = ctk.CTkFrame(self.frame_topcontainer, width=603, height=52, fg_color=thirdary_color, corner_radius=11)
        self.frame_searchboxbg.pack_propagate(False)
        self.frame_searchboxbg.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # left side widgets > magnifying glass icon
        self.image_searchicon = ctk.CTkImage(light_image=Image.open("resources/searchicon.png"), dark_image=Image.open("resources/searchicon.png"), size=(18, 18))
        self.label_searchicon = ctk.CTkLabel(self.frame_searchboxbg, image=self.image_searchicon, text="")
        self.label_searchicon.pack(side="left", padx=(20, 0))

        # left side widgets > search entry
        self.entry_search = ctk.CTkEntry(self.frame_searchboxbg, placeholder_text="SEARCH BOOKS", width=500, height=42, fg_color='#383E4A', border_width=0, placeholder_text_color='#a6a8ae')
        self.entry_search.pack(side="left", padx=(20, 0))

        # left side widgets > search button
        self.image_arrowentericon = ctk.CTkImage(light_image=Image.open("resources/arrowenter.png"),dark_image=Image.open("resources/arrowenter.png"), size=(20, 20))
        self.button_arrowentericon = ctk.CTkButton(self.frame_searchboxbg, image=self.image_arrowentericon, width=0, height=0,fg_color="transparent", text="", hover_color=thirdary_color, command=self.search_function)
        self.button_arrowentericon.pack(side="left", padx=(5, 0))

        # left side widgets > center frame HEREHRHEHREHHREHRE
        self.frame_centercontainer = tk.Frame(self.frame_leftmain, width=641, height=496, bg=main_color)
        self.frame_centercontainer.pack_propagate(False)
        self.frame_centercontainer.pack()

        # left side widgets > display box center
        self.frame_displaybox = ctk.CTkFrame(self.frame_centercontainer, width=603, height=496, fg_color=thirdary_color, corner_radius=11)
        self.frame_displaybox.pack_propagate(False)
        self.frame_displaybox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # left side widgets > bottom buttons container
        self.frame_bottomcontainer = tk.Frame(self.frame_leftmain, width=641, height=78, bg=main_color)
        self.frame_bottomcontainer.pack_propagate(False)
        self.frame_bottomcontainer.pack()

        # left side widgets > refresh button
        self.frame_refreshbuttoncontainer = tk.Frame(self.frame_bottomcontainer, width=110, height=78, bg=main_color)
        self.frame_refreshbuttoncontainer.pack_propagate(False)
        self.frame_refreshbuttoncontainer.pack(side="left", padx=(20, 10))
        self.button_refresh = ctk.CTkButton(self.frame_refreshbuttoncontainer, width=110, height=33, fg_color=thirdary_color, corner_radius=11, text="REFRESH", font=buttonfont, hover_color=button_hover, command=self.convert_pdf_to_json)
        self.button_refresh.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # left side widgets > Profile Button
        self.frame_profilebuttoncontainer = tk.Frame(self.frame_bottomcontainer, width=110, height=78, bg=main_color)
        self.frame_profilebuttoncontainer.pack_propagate(False)
        self.frame_profilebuttoncontainer.pack(side="left", padx=(5, 5))
        self.button_profile = ctk.CTkButton(self.frame_profilebuttoncontainer, width=110, height=33, fg_color=thirdary_color, corner_radius=11, text="PROFILE", font=buttonfont, hover_color=button_hover)
        self.button_profile.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # right side widgets > book display
        self.frame_bookdisplay = ctk.CTkScrollableFrame(self.frame_rightmain, width=599, height=618, fg_color=thirdary_color)
        self.frame_bookdisplay.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.search_function()
        self.display_borrowed()
    
    def search_function(self):
        for child in self.frame_bookdisplay.winfo_children():
            child.destroy()
        keyword = self.entry_search.get()
        results = []

        for filename in os.listdir("books\JSONBooks"):
            if filename.endswith(".json"):
                with open(os.path.join("books\JSONBooks", filename), "r") as file:
                    json_data = json.load(file)
                    json_text = " ".join(json_data.values())
                    if keyword.lower() in json_text.lower():
                        conn = sqlite3.connect("database\Bookworm.db")
                        cursor = conn.cursor()
                        cursor.execute(
                            "SELECT bookTitle, bookAuthor, bookDate, bookGenre, bookPath FROM bookTable WHERE bookPath = ?",
                            (filename,))
                        book_info = cursor.fetchone()
                        conn.close()

                        if book_info:
                            results.append(book_info)
        
        if results:
            for i, book_info in enumerate(results):
                
                self.booknametemp = book_info[0]

                self.EntryTrial = ctk.CTkFrame(self.frame_bookdisplay, height=60, width=580, fg_color='#282c34', corner_radius=11)
                self.EntryTrial.pack_propagate(False)
                self.EntryTrial.pack(padx=10, pady=(5, 5))

                self.titlecontainer = ctk.CTkFrame(self.EntryTrial, width=490, height=60, fg_color='#282c34')
                self.titlecontainer.pack_propagate(False)
                self.titlecontainer.pack(side="left")

                self.Titlelabel = tk.Label(self.titlecontainer, text=" " + book_info[0] + " by " + book_info[1], bg='#282c34', fg='#DBDBDB', font=("Arial", 15))
                self.Titlelabel.pack(side="left", padx=(10, 0))

                self.buttoncontainer = ctk.CTkFrame(self.EntryTrial, width=90, height=60, fg_color='#282c34')
                self.buttoncontainer.pack_propagate(False)
                self.buttoncontainer.pack(side="left")

                self.image_play = ctk.CTkImage(light_image=Image.open("resources/play-circle.png"),dark_image=Image.open("resources/play-circle.png"), size=(20, 20))
                self.button_play = ctk.CTkButton(self.buttoncontainer, image=self.image_play, width=0, height=0,fg_color="transparent", text="", hover_color='#AF87E9')
                self.button_play.pack(side="left", padx=(5, 0))

                self.image_add = ctk.CTkImage(light_image=Image.open("resources/plusfile.png"),dark_image=Image.open("resources/plusfile.png"), size=(22, 22))
                self.button_add = ctk.CTkButton(self.buttoncontainer, image=self.image_add, width=0, height=0,fg_color="transparent", text="", hover_color='#AF87E9', command=lambda: self.push_to_database(book_info[0]))
                self.button_add.pack(side="left", padx=(5, 0))
        else:
            print("No matching books found.")

    def convert_pdf_to_json(self):
        os.makedirs("Books/JSONBooks", exist_ok=True)
        words_to_remove = ["word1", "word2", "word3"]

        # Iterate through all files in the directory
        for filename in os.listdir("Books/PDFBooks"):
            if filename.endswith(".pdf"):
                file_path = os.path.join("Books/PDFBooks", filename)
                print(f"Processing file: {filename}")

                # Extract text from the PDF
                text = self.extract_text_from_pdf(file_path)

                # Remove Duplicate Words
                text = self.remove_duplicate_words(text)

                # Remove Words From Text
                for word in words_to_remove:
                    text = text.replace(word, "")

                # Create the output JSON file path and save the file
                output_path = os.path.join("Books/JSONBooks", os.path.splitext(filename)[0] + ".json")
                self.save_as_json(text, output_path)

    def extract_text_from_pdf(self, file_path):
            with open(file_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                num_pages = len(reader.pages)

                text = ""
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text += page.extract_text()

                return text
            
    def save_as_json(self, text, output_path):
            # Create a dictionary with the text content
            data = {
                "text": text
            }

            # Save the data as JSON
            with open(output_path, "w") as output_file:
                json.dump(data, output_file, indent=4)

    def remove_duplicate_words(self, text):

        word_list = text.split()
        unique_words = list(set(word_list))
        cleaned_text = " ".join(unique_words)
        return cleaned_text

    def push_to_database(self, book):
        usernametopush = self.theusername
        booktopush = book

        print(usernametopush + " " + booktopush)

    def display_borrowed(self):
        conn = sqlite3.connect('database/Bookworm.db')
        cursor = conn.cursor()

        name = self.theusername

        select_query = f"SELECT borrowTitle FROM borrowedBooks WHERE borrowName LIKE '%{name}%'"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        conn.close()

        for rows in rows:
            self.EntryContainer = tk.Frame(self.frame_displaybox, width=580, height=60, bg='#282c34')
            self.EntryContainer.pack_propagate(False)
            self.EntryContainer.pack(padx=10, pady=(5, 5))

            self.titlecon = ctk.CTkLabel(self.EntryContainer, width=490, height=60, fg_color='#282c34')
            self.titlecon.pack_propagate(False)
            self.titlecon.pack(side="left")

            self.borrowedtitle = tk.Label(self.titlecon, text=" " + rows[0], bg='#282c34', fg='#DBDBDB', font=("Arial", 15))
            self.borrowedtitle.pack(side="left", padx=(10, 0))

# =================================================================================================================================
# Login Window
# =================================================================================================================================

class loginWindow:

    def __init__(self):
        
        # login window properties
        self.login = ctk.CTk()
        self.login.geometry('500x650')
        self.login.protocol("WM_DELETE_WINDOW", sys.exit)
        self.login.title("Bookworm: Login")
        self.login.resizable(False, False)
        self.login.iconbitmap("resources\logcon.ico")

        # color variables
        self.main_color = '#282C34'
        self.widget_color = '#383E4A'
        self.button_hover = '#AF87E9'

        # font variables
        self.entry_font = ctk.CTkFont(family="Arial", size=20)

        # frame skeleton > frame 1
        self.frame1 = tk.Frame(self.login, width=500, height=177, bg=self.main_color)
        self.frame1.pack_propagate(False)
        self.frame1.pack()

        # frame skeleton > frame 2
        self.frame2 = tk.Frame(self.login, width=500, height=164, bg=self.main_color)
        self.frame2.pack_propagate(False)
        self.frame2.pack()

        # frame skeleton > frame 3
        self.frame3 = tk.Frame(self.login, width=500, height=309, bg=self.main_color)
        self.frame3.pack_propagate(False)
        self.frame3.pack()

        # frame 1 widgets > logo
        self.image_logo = ctk.CTkImage(light_image=Image.open("resources/bookworm.png"), dark_image=Image.open("resources/bookworm.png"), size=(244, 31))
        self.label_logo = ctk.CTkLabel(self.frame1, image=self.image_logo, text="")
        self.label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # frame 2 widgets > user id frame
        self.frame_userID = ctk.CTkFrame(self.frame2, width=425, height=60, fg_color=self.widget_color)
        self.frame_userID.pack_propagate(False)
        self.frame_userID.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # frame 2 widgets > user id icon
        self.image_userIcon = ctk.CTkImage(light_image=Image.open("resources/usericon.png"), dark_image=Image.open("resources/usericon.png"), size=(29, 29))
        self.label_userIcon = ctk.CTkLabel(self.frame_userID, image=self.image_userIcon, text="")
        self.label_userIcon.pack(side="left", padx=(15, 0))

        # frame 2 widgets > user id entry
        self.entry_userID = ctk.CTkEntry(self.frame_userID, placeholder_text="User ID", width=350, height=60, fg_color=self.widget_color, border_width=0, placeholder_text_color='#a6a8ae', font=self.entry_font)
        self.entry_userID.pack(side="left", padx=(15, 0))

        # frame 2 widgets > password frame
        self.frame_password = ctk.CTkFrame(self.frame2, width=425, height=60, fg_color=self.widget_color)
        self.frame_password.pack_propagate(False)
        self.frame_password.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # frame 2 widgets > password icon
        self.image_passIcon = ctk.CTkImage(light_image=Image.open("resources/passicon.png"), dark_image=Image.open("resources/passicon.png"), size=(26, 31))
        self.label_passIcon = ctk.CTkLabel(self.frame_password, image=self.image_passIcon, text="")
        self.label_passIcon.pack(side="left", padx=(15, 0))

        # frame 2 widgets > password entry
        self.entry_password = ctk.CTkEntry(self.frame_password, placeholder_text="Key Phrase", width=350, height=60, fg_color=self.widget_color, border_width=0, placeholder_text_color='#a6a8ae', font=self.entry_font)
        self.entry_password.pack(side="left", padx=(15, 0))

        # frame 3 widgets > login button
        self.button_login = ctk.CTkButton(self.frame3, width=290, height=50, fg_color=self.widget_color, text="LOGIN", font=self.entry_font, hover_color=self.button_hover, command=lambda: self.login_function(self.entry_userID, self.entry_password))
        self.button_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # frame 3 widgets > sign up button
        self.button_signup = ctk.CTkButton(self.frame3, width=290, height=50, fg_color=self.widget_color, text="SIGN UP", font=self.entry_font, hover_color=self.button_hover, command=self.to_signup)
        self.button_signup.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def login_function(self, entry_userID, entry_password):
        username = entry_userID.get()
        password = entry_password.get()
        conn = sqlite3.connect("database/Bookworm.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userTable WHERE userName = ? AND userPassword = ?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            user_level = result[3]
            if user_level == "Noble":
                print("Welcome Your Majesty")
            elif user_level == "Peasant":
                print("Welcome Peasant")
                self.login.destroy()
                user_window = userWindow(username)
                user_window.userwindow.mainloop()
        else:
            print("Invalid credentials")

    def run(self):
        self.login.mainloop()

    def on_closing(self, event=0):
        sys.exit()

    def to_signup(self):
        self.login.destroy()
        signup_window = registerWindow()
        signup_window.register.mainloop()

# =================================================================================================================================
# Initiator
# =================================================================================================================================

login_window = loginWindow()
login_window.run()