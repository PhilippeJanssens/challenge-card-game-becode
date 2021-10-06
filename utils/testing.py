class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, progr_lang):
        super().__init__(first, last, pay)
        self.progr_lang = progr_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_empl(self, empl):
        if empl not in self.employees:
            self.employees.append(empl)

    # removal does not work..
    def remove_empl(self, empl):
        if empl not in self.employees:
            self.employees.remove(empl)

    def print_empls(self):
        for empl in self.employees:
            print("-->", empl.fullname())


dev1 = Developer("Joelle", "Youtell", 50000, 'Python')
dev2 = Developer("Wanna", "Be", 60000, "Java")

mgr1 = Manager("sue", "smith", 90000, [dev1])

print(isinstance(mgr1, Employee))

print(mgr1.email)
mgr1.add_empl(dev2)
mgr1.remove_empl(dev1)

mgr1.print_empls()


# print(dev1.email)
# print(dev1.progr_lang)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)


def fill_deck():
    icon_color_tuple = ["♥ - Red", "♦ - Red", "♣ - Black", "♠ - Black"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards = []
    for item in range(len(icon_color_tuple)):
        for value in range(len(values)):
            cards.append(values[value] + " << " + icon_color_tuple[item] + " >>")
    print(len(cards),cards)
    return

fill_deck()
