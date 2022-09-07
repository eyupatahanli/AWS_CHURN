import mysql.connector

mydb = mysql.connector.connect(
  host="18.133.241.81",
  user="eyup",
  password="churn123"
)

print(mydb)

mycursor = mydb.cursor(buffered=True)

mycursor = mydb.cursor()


mycursor.execute("select * from churndb.churntable")

a = mycursor.fetchone()
b = list(a)

"""
get_data = 'INSERT INTO weather (max_temp, min_temp, avg_temp) VALUES (%s, %s, %s);'


def lambda_handler(event, context):
    cnx = mysql.connector.connect(host=os.environ['RDS_HOSTNAME'], user=os.environ['RDS_USERNAME'], passwd=os.environ['RDS_PASSWORD'],
                                      database=os.environ['RDS_DB_NAME'], port=os.environ['RDS_PORT'], charset='utf8')
    cur = cnx.cursor()
    cur.execute(get_data, (1, 2, 5))
    cnx.commit()
    cnx.close()
    return {'statusCode': 200,'headers': {"content-type": "application/json"}, 'body': json.dumps("hi", indent=0, sort_keys=True, default=str)}
    # return controller(event,action)"""