import oracledb


class DAO:

    def __init__(self):
        return

    @staticmethod
    def get_connection():
        return oracledb.connect(user='projeto', password='Proj310', dsn='192.168.15.102:1521/oracle')

    @staticmethod
    def close_connection(connection):
        connection.close()
