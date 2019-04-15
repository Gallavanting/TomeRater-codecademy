class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "User {username}, email: {email}, books read: {amount}".format(username = self.name, email = self.email, amount = len(self.books))

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email has been updated.")

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        counter = 0
        sum = 0
        for value in self.books.values():
            if value != None:
                counter += 1
                sum += value
        return sum/counter

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return self.title

    # DO NOT MODIFY! Makes instances of the class Hashable.
    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def add_rating(self, rating):
        if rating == None:
            return None
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        counter = 0
        sum = 0
        for value in self.ratings:
                counter += 1
                sum += value
        return sum/counter

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "TomeRater Application."

    def __eq__(self, other):
        if self.users == user.users and self.books == other.books:
            return True
        else:
            return False

    def create_book(self, title, isbn):
        return Book(title, isbn)

    # Creates fiction object
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    # Creates non-fiction object
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    # Checks to see if user exists. If user exists, adds book to user and rating to book, iterates book read count.
    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            return "No user with email {email}!".format(email = email)
        else: user = self.users.get(email)
        user.read_book(book, rating)
        book.add_rating(rating)
        if book in self.books.keys():
            self.books[book] += 1
        if book not in self.books.keys():
            self.books[book] = 1

    # Adds user to dictionary and appends books to user if applicable
    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    # Compares read counters for books in sequence, records highest and returns it. Keeps current book in case of tie.
    def most_read_book(self):
        most_read_key = None
        most_read_value = 0
        for key, value in self.books.items():
            if value > most_read_value:
                most_read_key = key
                most_read_value = value
        return most_read_key

    # Cycles through books, compares each book to its recorded highest average rating. Keeps book it had in case of tie.
    def highest_rated_book(self):
        highest_rated = None
        book_rating = 0
        for books in self.books.keys():
            comparison = books.get_average_rating()
            if comparison > book_rating:
                highest_rated = books
                book_rating = books.get_average_rating()
        return "{title} at {rating}".format(title = highest_rated, rating = book_rating)

    # Cycles through users, compares each user to the recorded highest_average. Keeps user it had in case of tie.
    def most_positive_user(self):
        most_positive = None
        highest_average = 0
        for users in self.users.values():
            average = users.get_average_rating()
            if average > highest_average:
                most_positive = users
                highest_average = users.get_average_rating()
        return "{user} is the most positive user with an average rating of {rating}".format(user = most_positive.name, rating = highest_average)
