class Elevator:

    def __init__(self, number_of_storages=5, current_age=3):
        self.number_of_storages = number_of_storages
        self.current_age = current_age

    def up(self):
        if self.current_age >= self.number_of_storages:
            print('Лифт не может подняться выше')
        else:
            self.current_age = self.current_age + 1
            print('Лифт поднимается на ' + str(self.current_age) + ' этаж')

    def down(self):
        if self.current_age <= 1:
            print('Лифт не может опуститься ниже')
        else:
            self.current_age = self.current_age - 1
            print('Лифт опускается на ' + str(self.current_age) + ' этаж')

a = Elevator(10, 1)

a.down()
a.up()

