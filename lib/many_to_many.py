class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        """Returns a list of contracts related to this author"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Returns a list of books related to this author through contracts"""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Creates a new contract for this author and the given book"""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Returns the sum of all royalties from this author's contracts"""
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    def __init__(self, title):
        self.title = title
    
    def contracts(self):
        """Returns a list of contracts related to this book"""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Returns a list of authors related to this book through contracts"""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        # Validate inputs
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        # Add to all contracts list
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts with the given date"""
        return [contract for contract in cls.all if contract.date == date]