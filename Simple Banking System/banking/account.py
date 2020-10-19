import random


class BankAccount:
    def __init__(self):
        self.card = self.generateCardNumber()
        self.pin = self. generateCardPin()
        self.balance = 0
        random.seed()

    @staticmethod
    def generateCardNumber():
        number_str = "400000"
        for _ in range(9):
            number_str += str(random.randint(0, 9))
        number = list(map(int, number_str))
        for index in range(15):
            if index % 2 == 0:
                number[index] *= 2
                if number[index] > 9:
                    number[index] -= 9
        total_sum = sum(number)
        check_sum = (10 - total_sum + int(total_sum / 10) * 10) % 10
        number_str += str(check_sum)
        return number_str

    @staticmethod
    def generateCardPin():
        number = str(random.randint(0, 9))
        for _ in range(3):
            number += str(random.randint(0, 9))
        return number

    @staticmethod
    def luhnAlgorithm(number_str):
        number = list(map(int, number_str))
        for index in range(16):
            if index % 2 == 0:
                number[index] *= 2
                if number[index] > 9:
                    number[index] -= 9
        total_sum = sum(number)
        if total_sum % 10 == 0:
            return True
        return False
