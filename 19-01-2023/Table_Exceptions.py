class TableException(Exception):
    pass

class InvalidGuestNum(TableException):
    def __init__(self, received_guests_num, table_guests_num): 
        super().__init__()
        self.table_guests_num = table_guests_num
        self.received_guests_num = received_guests_num

class TableAlreadyReserved(TableException):
    pass