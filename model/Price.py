class Price(object):

    def __init__(self):
        super(Price, self).__init__()

    def get_date(self):
        return self._date

    def set_date(self,new_date):
        self._date = new_date

    def get_price(self):
        return self._price

    def set_price(self,new_price):
        self._price = new_price