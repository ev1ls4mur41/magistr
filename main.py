class Magistr:
    def __init__(self, name: str, rating: int, age: float):
        self.name = name
        self.rating = rating
        self.age = age

    def rating_change(self, value: int):
        if 1 <= self.rating + value <= 100:
            self.rating += value
            if value > 0:
                self.age -= abs(value) // 10
                if self.age < 14.5:
                    self.age = 14.5
            else:
                self.age += abs(value) // 10

    def __iadd__(self, string: str):
        length = len(string)
        self.rating += length
        self.age -= length // 10
        if self.age < 14.5:
            self.age = 14.5
        return self

    def __call__(self, number: int):
        return (number - self.age) * self.rating

    def __str__(self):
        return f"Mag {self.name} with {self.rating} rating looks {self.age} years old"

    def __lt__(self, other):
        if (self.rating, -self.age, self.name) < (other.rating, -other.age, other.name):
            return True
        return False

    def __gt__(self, other):
        if (self.rating, -self.age, self.name) > (other.rating, -other.age, other.name):
            return True
        return False

    def __le__(self, other):
        if (self.rating, -self.age, self.name) <= (other.rating, -other.age, other.name):
            return True
        return False

    def __ge__(self, other):
        if (self.rating, -self.age, self.name) >= (other.rating, -other.age, other.name):
            return True
        return False

    def __eq__(self, other):
        if (self.rating, -self.age, self.name) == (other.rating, -other.age, other.name):
            return True
        return False

    def __ne__(self, other):
        if (self.rating, -self.age, self.name) != (other.rating, -other.age, other.name):
            return True
        return False


name = input("Введите имя магистра: ")
rating = int(input("Введите рейтинг магистра: "))
age = float(input("Введите возраст магистра: "))

magistr = Magistr(name=name,rating=rating ,age=age)
print(magistr)