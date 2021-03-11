import psycopg2
from psycopg2 import 

import os

con = psycopg2.connect(
		user = 'postgres',
		password = '',
		host = 'localhost',
		port = '5432',
		database = 'perpustakaan'
	)

def main(db):
	print('=================================')
	print('CRUD USING PostgreSQL | psycopg2')
	print('=================================')
	print('''
	1) Insert Data
	2) Show Data
	3) Update Data
	4) Delete Data
	0) Exit
	---------------------''')
	choice = input('choose menu(1/2/3/4/0)> ')

	os.system('clear')

	if choice == '1': insert_buku(db)
	elif choice == '2': 
		show_buku(db)
	elif choice == '3': 
		update_buku(db)
	elif choice == '4': 
		delete_buku(db)
	elif choice == '0':
		db.close()
		print('\nPostgreSQL connection is closed')
		exit()
	else : print('Menu salah')

def insert_buku(db):
	try:
		cur = db.cursor()

		# id_buku = input('ID buku : ')
		judul = input('Judul : ')
		penulis = input('Penulis : ')
		tahun = input('Tahun : ')

		cur.execute('INSERT INTO buku VALUES (DEFAULT, %s, %s, %s)', (judul, penulis, tahun))
		db.commit()
		print('{} record inserted successfully into buku table'.format(cur.rowcount))

	except (Exception, psycopg2.Error) as error:
		print('Failed to insert record into buku table', error)
	finally:
		if db:
			cur.close()

def show_buku(db):
	try:
		cur = db.cursor()

		# https://fle.github.io/reset-a-postgresql-sequence-and-recompute-column-values.html
		# Set temporary values intentionally far of existing values to avoid conflicts when we recompute the column
		cur.execute("UPDATE buku SET id_buku=10000+nextval('buku_id_buku_seq');")
		# restart sequence to 1
		cur.execute('ALTER SEQUENCE buku_id_buku_seq RESTART WITH 1')
		# rewwrite all column values
		cur.execute("UPDATE buku SET id_buku=nextval('buku_id_buku_seq')")
		cur.execute('SELECT * FROM buku ORDER BY id_buku ASC')
		result = cur.fetchall()

		if cur.rowcount < 0:
			print('No data')
		else:
			for data in result:
				print(data)
	except (Exception, psycopg2.Error) as error:
		print('Oops! an exception has occured: ', error)
		print('Exception TYPE: ', type(error))
	finally:
		if db:
			cur.close()

def update_buku(db):
	try:
		cur = db.cursor()
		show_buku(db)

		id_buku = input('Pilih id buku> ')
		judul = input('Judul Baru : ')
		penulis = input('Penulis Baru : ')
		tahun = input('Tahun Baru : ')

		cur.execute('UPDATE buku SET judul=%s, penulis=%s, tahun=%s WHERE id_buku=%s', (judul, penulis, tahun, id_buku))
		db.commit()
		print(f'{cur.rowcount} record updated successfully')
	except (Exception, psycopg2.Error) as error:
		print('Error in update operation', error)
	finally:
		if db:
			cur.close()

def delete_buku(db):
	try:
		cur = db.cursor()
		show_buku(db)

		id_buku = input('Pilih ID buku> ')
		cur.execute('DELETE FROM buku WHERE id_buku=%s',(id_buku))
		db.commit()
		print(f'{cur.rowcount} record deleted successfully')
	except(Exception, psycopg2.Error) as error:
		print('Error in delete operation', error)
	finally:
		if db:
			cur.close()

if __name__=='__main__':
	while True:
		main(con)
		
