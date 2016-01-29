import sqlite3


class Create_init_tables:
	def __init__(self):
		conn = sqlite3.connect('example.db')
		c = conn.cursor()

		c.execute(self.create_table_Movies())
		c.execute(self.create_table_Projections())
		c.execute(self.create_table_Reservations())
		conn.commit()

	def create_table_Movies(self):
		table = '''
		create table if not exists Movies(
			id int primary key,
			movie_name varchar(255),
			movie_rating float 
			)
		'''
		return table

	def create_table_Projections(self):
		
		table = '''
		create table if not exists Projections(
			id int primary key,
			projection_movie_ID int,
			projections_type text, 
			projection_date text,
			projection_time text,
			foreign key (projection_movie_ID) references Movies(id)
			)
		'''
		return table
		

	def create_table_Reservations(self):
		table = '''
		create table if not exists Reservations(
			id int primary key,
			username text,
			projection_id int,
			row int,
			col int,
			foreign key (projection_id) references Projections(id)
			)
		'''
		return table



	def populate_movies(self):
		some_movies = [(1, "The Hunger Games: Catching Fire", 7.9),\
						(2, "Wreck-It Ralph", 7.8),
						(3, "Her", 8.3)]
		conn = sqlite3.connect('example.db')
		c = conn.cursor()

		c.executemany("""insert into Movies(id, movie_name, movie_rating)
				values (?, ?,?) 
			""", some_movies)
		conn.commit()

	def populate_projections(self):
		proj = [(1,1,"3D","2014-04-01","19:10"),
				(2,1,"2D","2014-04-01","19:00"),
				(3,1,"4DX","2014-04-02","21:00"),
				(4,3,"2D","2014-04-05","20:20"),
				(5,2,"3D","2014-04-02","22:00"),
				(6,2,"2D","2014-04-02","19:30"),]
		conn = sqlite3.connect("example.db")
		c = conn.cursor()
		c.executemany("""insert into Projections 
			(id, projection_movie_ID, projections_type, projection_date, projection_time ) values(?,?,?,?,?)
			""", proj)
		conn.commit()

	def populate_reservations(self):
		res = [ (1,"RadoRado", 1, 2, 1),
				(2,"RadoRado", 1, 3, 5),
				(3,"RadoRado", 1, 7, 8),
				(4,"Ivo", 3, 1, 1),	
				(5,"Ivo", 3, 1, 2),
				(6,"Mysterious", 5, 2, 3),
				(7,"Mysterious", 5, 2, 4)]
		conn = sqlite3.connect("example.db")
		c = conn.cursor()
		c.executemany("""insert into Reservations(id, username, projection_id, row, col)
			values(?, ?, ?, ?, ?)
			""", res)
		conn.commit()


mydb = Create_init_tables()
# mydb.populate_movies()
# mydb.populate_projections()
mydb.populate_reservations()