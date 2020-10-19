import sqlite3

create_str = ('''CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, 
                pin TEXT, balance INTEGER DEFAULT 0);''')

insert_str = "INSERT INTO card (number, pin) VALUES"

login_str = "SELECT * FROM card WHERE number="
login_str2 = " AND pin="

balance_str = "SELECT balance FROM card WHERE id="

income_str = "UPDATE card SET balance="
income_str2 = " WHERE id="

delete_str = "DELETE FROM card WHERE id="


class BankDB:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS card")
        self.cur.execute(create_str)
        self.conn.commit()

    def insertCard(self, acc):
        execute_str = f'{insert_str}({acc.card}, {acc.pin});'
        self.cur.execute(execute_str)
        self.conn.commit()

    def checkAcc(self, card, pin):
        execute_str = f'{login_str}{card}'
        execute_str += f'{login_str2}{pin}'
        self.cur.execute(execute_str)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return -1

    def checkCard(self, card):
        execute_str = f'{login_str}{card}'
        self.cur.execute(execute_str)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return -1

    def checkBalance(self, acc_id):
        execute_str = f'{balance_str}{acc_id}'
        self.cur.execute(execute_str)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return 0

    def addIncome(self, acc_id, income):
        current = int(self.checkBalance(acc_id))
        current += income
        execute_str = f'{income_str}{current}'
        execute_str += f'{income_str2}{acc_id}'
        self.cur.execute(execute_str)
        self.conn.commit()

    def deleteAcc(self, acc_id):
        execute_str = f'{delete_str}{acc_id}'
        self.cur.execute(execute_str)
        self.conn.commit()
