from dao import DAO


class DTO:
    db_conn = None

    def __init__(self):
        self.db_conn = DAO.get_connection()

    def insert_episode(self, episode_name):
        str_episode = episode_name.replace('"', '')
        sql_select = f"SELECT COUNT(*) FROM EPISODE WHERE NAME='{str_episode}'"
        cursor = self.db_conn.cursor().execute(sql_select)
        result = cursor.fetchone()[0]
        if result > 0:
            return
        else:
            sql_insert = f"INSERT INTO EPISODE VALUES (SEQ_EPISODE.nextval, '{str_episode}')"
            self.db_conn.cursor().execute(sql_insert)
            self.db_conn.commit()

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

    def insert_season(self, season):
        sql_select = f"SELECT COUNT(*) FROM SEASON WHERE NAME='{season}'"
        cursor = self.db_conn.cursor().execute(sql_select)
        result = cursor.fetchone()[0]
        if result > 0:
            return
        else:
            sql_insert = f"INSERT INTO SEASON VALUES (SEQ_DIRECTOR.nextval, '{season}')"
            self.db_conn.cursor().execute(sql_insert)
            self.db_conn.commit()

    def insert_time(self, year, month):
        sql_select = f"SELECT COUNT(*) FROM TIME WHERE YEAR={year} AND MONTH={month}"
        cursor = self.db_conn.cursor().execute(sql_select)
        result = cursor.fetchone()[0]
        if result > 0:
            return
        else:
            sql_insert = f"INSERT INTO TIME VALUES (SEQ_TIME.nextval, {year}, {month})"
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
