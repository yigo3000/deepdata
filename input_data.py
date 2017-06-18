import pymysql
import tensorflow as ts
DB_HOST = 'db_host'

DB_USER = 'root'

DB_PASS = 'm7227510'

DB_NAME = 'morning'


def get_data(ticker="", date=""):
    db_name = _get_db_name(ticker)

    pass


def _get_db_name(name):
    u"""Returns a new (cleaned) name that can be used in a MySQL database.



    :param name: Original name.

    :return Name that can be used in a MySQL database.

    """

    name = (name.lower()

            .replace(u'/', u' per ')

            .replace(u'&', u' and ')

            .replace(u'%', u' percent '))

    name = re.sub(ur'[^a-z0-9]', u' ', name)

    name = re.sub(ur'\s+', u' ', name).strip()

    return name.replace(u' ', u'_')

def _db_execute(query, conn):

    u"""Helper method for executing the given MySQL non-query.



    :param query: MySQL query to be executed.

    :param conn: MySQL connection.

    """

    cursor = conn.cursor()

    cursor.execute(query)

    cursor.close()

def matrixer():
    pass

def data_valide():
    #检验数据的有效性
    pass

def main():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER,
                           passwd=DB_PASS, db=DB_NAME)
    with open() as xxx:
        ticker = xxx.readline()
    date = "201503"
    data = get_data(ticker, date)




if __name__ == '__main__':
    main()
