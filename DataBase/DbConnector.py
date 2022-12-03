import pymysql

my_db= pymysql.connect(
    host="sql7.freesqldatabase.com",
    user="sql7582410",
    passwd="HwhEviA4ah",
    db="sql7582410"
)

def execute_query(query,val):
    cur = my_db.cursor()
    if val:
        cur.execute(query,val)
    else:
        cur.execute(query)
    my_db.commit()