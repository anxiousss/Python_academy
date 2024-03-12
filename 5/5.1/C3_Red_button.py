class RedButton:

    def __init__(self, n_req=0, alert='Тревога!'):
        self.n_req = n_req
        self.alert = alert

    def click(self):
        self.n_req += 1
        print(self.alert)

    def count(self):
        return self.n_req
