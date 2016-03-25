import sqlite3
from prettytable import PrettyTable


class MagicReservtions:
    def __init__(self):
        self.conn = sqlite3.connect("example.db")
        self.cursor = self.conn.cursor()
        # self.conn.row_factory = sqlite3.Row

    def show_movies(self):
        data = self.cursor.execute("""SELECT id, movie_name, movie_rating FROM Movies
								order by movie_rating DESC""")
        pretty = PrettyTable(["ID", "Name", "Rating"])
        for item in data:
            pretty.add_row([item[0], item[1], item[2]])
        print(pretty)
        return data.fetchall()

    def show_movie_projections(self, movie_id, date=None):
        if date:
            proj_data = self.cursor.execute("""select Projections.id, Projections.projection_date,\
										 Projections.projection_time, Projections.projections_type \
									from Projections
									join Movies
									on Projections.projection_movie_ID = Movies.id
									where projection_movie_ID=?
									and projection_date=?
									ORDER BY projection_date""", (movie_id, date))
        else:
            proj_data = self.cursor.execute("""select Projections.id, Projections.projection_date,\
										 Projections.projection_time, Projections.projections_type \
									from Projections
									join Movies
									on Projections.projection_movie_ID = Movies.id
									where projection_movie_ID=?
									ORDER BY projection_date""", str(movie_id))

        nice_table = PrettyTable(
            ["Proj_ID", "Proj_Date", "Proj_Time", "Proj_Type"])
        for i in proj_data:
            nice_table.add_row([i[0], i[1], i[2], i[3]])
        print(nice_table)
        return proj_data.fetchall()

    def make_reservation(self):
        user_name = "Goshko"  # input("Pls enter your name")
        number_of_tickets = 3  # input("select the number of tickets you want")
        print(">>>select a movie by ID:<<<")
        self.show_movies()
        user_movie_ID = 1  # input("the system expects your input")
        self.show_movie_projections(user_movie_ID)
        user_projection_ID = 1  # input("projection ID from the list Please")
        self.take_available_seats()
        self.select_seat(
            user_name, number_of_tickets, user_movie_ID, user_projection_ID)
        # return 1

    def select_seat(self, user_name, number_of_tickets, user_movie_ID, user_projection_ID, attempts=0):
        while number_of_tickets > 0:
            user_row = input("select row")
            user_col = input("select place")
            if attempts > 3:
                return ("pls request offline assitance. Good buy!")
            if self.seat_taken_check(user_row, user_col):
                attempts += 1
                self.select_seat(
                    user_name, number_of_tickets, user_movie_ID, user_projection_ID, attempts)
            else:
                self.cursor.execute("""
					INSERT INTO Reservations(username, projection_id, row, col)
					VALUES(?,?, ?, ?)""", (user_name, user_projection_ID, user_row, user_col))
                self.conn.commit()
                print(str(number_of_tickets) + "before")
                number_of_tickets -= 1
                print(str(number_of_tickets) + "after")

                nice_table = PrettyTable(
                    ["Name", "projection_ID", "row", "seat"])
                # print("your reservation: {} projection ID:{} on row {} seat {} ".format(user_name, user_projection_ID, user_row, user_col))
                nice_table.add_row(
                    [user_name, user_projection_ID, user_row, user_col])

                print(nice_table)

    def seat_taken_check(self, user_row, user_col):
        user_row = int(user_row)
        # print(user_row)
        user_col = int(user_col)
        # print(user_col)
        check_reservations = """
			SELECT row, col from Reservations
		"""
        check_seat = self.cursor.execute(check_reservations)
        for seat in check_seat:
            if seat[0] + 1 == user_row and seat[1] + 1 == user_col:
                print("seat already taken")
                return True

    def cancel_reservation(self, name):
        self.cursor("""
			DELETE FROM Reservations
			WHERE username = ?""", (name))
        self.conn.commit()

    def exit(self):
        pass

    def help_with_commands(self):
        pass

    def take_available_seats(self):
        seats = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
        take_row_col = """
	    SELECT row, col FROM Reservations
	    """
        res_list = self.cursor.execute(take_row_col)

        for item in res_list:
            seats_row = item[0]
            seats_col = item[1]
            seats[seats_row][seats_col] = 'X'

        # print("  1    2    3    4    5    6    7    8    9    10")
        # for i in range(0, len(seats)):
        #     print(seats[i])

        pretty = PrettyTable(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        for i in range(0, len(seats)):

            pretty.add_row([seats[i][0], seats[i][1], seats[i][2], seats[i][3],
                            seats[i][4], seats[i][5], seats[i][6], seats[i][7],
                            seats[i][8], seats[i][9]])
        print(pretty)

    def UI(self):
        commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "make_reservation": self.make_reservation,
            "cancel_reservation": self.cancel_reservation,
            "exit": self.exit,
            "help": self.help_with_commands
        }
        user_command = input("select command>>>")
        user_command_first_part = user_command.split()[0]
        try:
            user_command_second_part = user_command.split()[1]
            if type(user_command_second_part) != type(1):
                print("projection argumanet is not valid")
        except:
            pass

        if user_command_first_part not in commands:
            print("command invalid. Consider using help")
        else:
            try:
                commands[user_command_first_part](user_command_second_part)
            except:
                commands[user_command_first_part]()


panda = MagicReservtions()
panda.UI()
# print(panda.show_movies())
# print(panda.show_movie_projections(3))
# print(panda.make_reservation())
# print(panda.take_available_seats())
