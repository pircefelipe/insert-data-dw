from dao import DAO


class DTO:
    db_conn = None

    def __init__(self):
        self.db_conn = DAO.get_connection()

    def insert(self, table_data, data):
        old_data = ''
        for row_data in data:
            str_data = str(row_data).replace('"', '')
            if str_data == old_data:
                continue
            sql = f"INSERT INTO {table_data['table_name']} VALUES ({table_data['seq_name']}.nextval, '{str_data}')"
            self.db_conn.cursor().execute(sql)
            self.db_conn.commit()
            old_data = str_data

    def insert_director(self, director_name):
        sql_select = f"SELECT COUNT(*) FROM DIRECTOR WHERE NAME='{director_name}'"
        cursor = self.db_conn.cursor().execute(sql_select)
        result = cursor.fetchone()[0]
        if result > 0:
            return
        else:
            sql_insert = f"INSERT INTO DIRECTOR VALUES (SEQ_DIRECTOR.nextval, '{director_name}')"
            self.db_conn.cursor().execute(sql_insert)
            self.db_conn.commit()

    def insert_time(self, year, month):
        sql_select = f"SELECT COUNT(*) FROM TIME WHERE YEAR={year} AND MONTH={month}"
        cursor = self.db_conn.cursor().execute(sql_select)
        result = cursor.fetchone()[0]
        if result > 0:
            return
        else:
            sql_insert = f"INSERT INTO TIME (ID_TIME, YEAR, MONTH) VALUES (SEQ_TIME.nextval, {year}, {month})"
            self.db_conn.cursor().execute(sql_insert)
            self.db_conn.commit()

    def get_episode_id(self, episode_name):
        name = str(episode_name).replace('"', '')
        sql_select = f"SELECT ID_EPISODE FROM EPISODE WHERE NAME='{name}'"
        cursor = self.db_conn.cursor().execute(sql_select)
        return cursor.fetchone()[0]

    def get_director_id(self, director_name):
        name = str(director_name).replace('"', '')
        sql_select = f"SELECT ID_DIRECTOR FROM DIRECTOR WHERE NAME='{name}'"
        cursor = self.db_conn.cursor().execute(sql_select)
        return cursor.fetchone()[0]

    def get_time_id(self, date):
        date_array = date.split('-')
        sql_select = f"SELECT ID_TIME FROM TIME WHERE YEAR={date_array[0]} AND MONTH={date_array[1]}"
        cursor = self.db_conn.cursor().execute(sql_select)
        return cursor.fetchone()[0]

    def get_season_id(self, season):
        sql_select = f"SELECT ID_SEASON FROM SEASON WHERE SEASON={season}"
        cursor = self.db_conn.cursor().execute(sql_select)
        return cursor.fetchone()[0]

    def insert_exhibition(self, episode_id, director_id, time_id, season_id, viewers):
        sql_insert = f"INSERT INTO EXHIBITION (ID_EPISODE, ID_DIRECTOR, ID_TIME, ID_SEASON, VIEWERS_IN_MILLIONS) VALUES ({episode_id}, {director_id}, {time_id}, {season_id}, {viewers})"
        self.db_conn.cursor().execute(sql_insert)
        self.db_conn.commit()
