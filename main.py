from csv_handler import HandlerCSV
from dto import DTO

dto = DTO()
data = HandlerCSV.read_csv('dataset.csv')


def episode():
    for row in data['Title']:
        dto.insert_episode(row)


def director():
    for row in data['Directed by']:
        dto.insert_director(row)


def season():
    for row in data['Season']:
        dto.insert_season(row)


def format_time():
    for row in data['Original air date']:
        print(row)
        date_array = str(row).split('-')
        year = date_array[0]
        month = date_array[1]
        dto.insert_time(year, month)


def exhibition():
    for row in data.values:
        episode_id = dto.get_episode_id(row[3])
        director_id = dto.get_director_id(row[4])
        time_id = dto.get_time_id(row[6])
        season_id = dto.get_season_id(row[9])
        viewers = row[8]
        dto.insert_exhibition(episode_id, director_id, time_id, season_id, viewers)


episode()
director()
season()
format_time()
exhibition()
