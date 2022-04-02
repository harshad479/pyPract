# TS 19 19-03-2022
'''
Design a simple database application that 
stores the records and retrieve the same'''
import sqlite3
con=sqlite3.connect('population.db')
cur=con.cursor()

cur.execute('CREATE Table PopbyRegion(Region TEXT,Population INTEGER)')

cur.execute('INSERT INTO PopbyRegion VALUES ("Central Africa",330993)') 
cur.execute('INSERT INTO PopbyRegion VALUES ("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopbyRegion VALUES ("Northern Africa", 1037463)') 
cur.execute('INSERT INTO PopbyRegion VALUES ("Southern Asia",2051941)')
cur.execute('INSERT INTO PopbyRegion VALUES ("Asia Pacific", 785468)')
cur.execute('INSERT INTO PopbyRegion VALUES ("Middle East",687630)') 
cur.execute('INSERT INTO PopbyRegion VALUES ("Eastern Asia", 1362955) ')
cur.execute('INSERT INTO PopbyRegion VALUES ("Southern America", 593121)')
cur.execute('INSERT INTO PopbyRegion VALUES ("Eastern Europe",222437)')
cur.execute('INSERT INTO PopbyRegion VALUES ("North America", 661157)') 
cur.execute('INSERT INTO PopbyRegion VALUES ("Western Europe",387933)')
cur.execute('INSERT INTO PopbyRegion VALUES ("Japan", 100562)')

con.commit()

#con.close()