class RedButton:

    def __init__(self, n_req=0, alert='Тревога!'):
        self.n_req = n_req
        self.alert = alert

    def click(self):
        self.n_req += 1
        print(self.alert)

    def count(self):
        return self.n_req


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
