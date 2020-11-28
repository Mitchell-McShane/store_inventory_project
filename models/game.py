class Game:
    def __init__(self, name, worker, genre, price, buying_cost, stock, studio, id=None):
        self.name = name
        self.worker = worker
        self.genre = genre
        self.price = price
        self.buying_cost = buying_cost
        self.stock = stock
        self.studio = studio
        self.id = id