import datetime


class Table:
    def __init__(self, table_id: int, seat_num: int, time_limit=datetime.timedelta(minutes=90)):
        self.table_id = table_id
        self.seat_num = seat_num
        self.time_limit = time_limit
        self.is_occupied = False
        self.occupied_seats = 0
        self.location = None
        self.start_time = None

    def is_available(self):
        return self.is_occupied

    def reserve_a_table(self, guest_num) -> bool:
        if not self.is_occupied:
            return False
        if self.seat_num < guest_num:
            return False
        self.occupied_seats = guest_num
        self.start_time = datetime.datetime.utcnow()
        self.is_occupied = True
        print("Table is reserved")
        return True

    def release_a_table(self) -> bool:
        if self.is_occupied:
            self.occupied_seats = 0
            self.is_occupied = False
            self.start_time = None
            print("Released Table")
            return True
        else:
            return False

    def _get_end_time(self):
        return self.start_time + self.time_limit

    def time_left(self) -> datetime.timedelta:
        if not self.start_time:
            return datetime.timedelta()
        return self._get_end_time() - self.start_time

    def get_available_hour(self) -> datetime.datetime:
        if not self.start_time:
            return datetime.datetime.utcnow()
        return self.start_time + self.time_limit

    def __str__(self):
        return f"Table id: {self.table_id}, seats: {self.seat_num}, is_available: {self.is_occupied}"

    def __repr__(self):
        return f"Table {self.table_id} ({self.seat_num})"


class TableReservationSystem:
    def __init__(self, tables_list: list, restaurant_name: str, max_time_limit=datetime.timedelta(minutes=90)):
        self.restaurant_name = restaurant_name
        self.max_time_limit = max_time_limit
        self.tables: list[Table] = []
        for table_id, seats in enumerate(tables_list):
            self.tables.append(Table(table_id, seats, max_time_limit))

    def reserve_a_table(self, guest_num, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                return table.reserve_a_table(guest_num)
        return False

    def release_a_table(self, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                table.release_a_table()
        return False

    def get_available_tables(self, guest_num) -> list[Table]:
        available_tables = []
        for table in self.tables:
            if table.seat_num >= guest_num and table.is_available():
                available_tables.append(table)
        available_table_length = len(available_tables)
        sorted_tables = []
        for i in range(available_table_length):
            min_table = available_tables[0]
            min_table_idx = 0
            for table_idx, table in enumerate(available_tables):
                if table.seat_num > min_table.seat_num:
                    min_table = table
                    min_table_idx = table_idx
            sorted_tables.append(min_table)
            available_tables.pop(min_table_idx)
        return sorted_tables

    def get_soonest_available_tables(self, guest_num: int) -> list[Table]:
        suitable_tables: list[Table] = []
        for table in self.tables:
            if table.seat_num >= guest_num:
                suitable_tables.append(table)
        sorted_tables: list[Table] = []
        suitable_tables_length = len(suitable_tables)
        for i in range(suitable_tables_length):
            min_table = suitable_tables[0]
            min_table_idx = 0
            for idx, table in suitable_tables:
                if (table.get_available_hour(), table.seat_num) < (min_table.get_available_hour(), min_table.seat_num):
                    min_table = table.get_available_hour()
                    min_table_idx = idx
            sorted_tables.append(min_table)
            suitable_tables.pop(min_table_idx)
        return sorted_tables

    # def get_tables_with_less_than_x_minutes_left(self, guest_num: int, minutes: datetime.timedelta) -> list[Table]:


if __name__ == "__main__":
    table1 = Table(1111, 4)
    table2 = Table(2222, 2)
    table3 = Table(3333, 5)
    table4 = Table(4444, 7)
    table_list = [table1, table2, table3, table4]
    system = TableReservationSystem(table_list, "Kharasho")
    system.get_available_tables(5)
