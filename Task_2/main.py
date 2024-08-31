import requests, pymysql





connection = pymysql.connect(   
    host = 'localhost',
    user = 'root',
    password='12345',
    db='movie',
    port = 3308,
    charset = 'utf8mb4', 
    cursorclass= pymysql.cursors.DictCursor 
)


MOVIE = input("Enter the name of the film: ")

API_KEY = "5d9df2b8"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"



response = requests.get(url)

my_movie = {}
if response.status_code == 200:
    data = response.json()
    title = data.get('Title')
    released = data.get('Released')
    genre = data.get('Genre')
    director = data.get('Director')
    my_movie["title"] = title
    my_movie["released"] = released
    my_movie["genre"] = genre
    my_movie["director"] = director


    print(f"Title: {title}")
    print(f"Released: {released}")
    print(f"Genre: {genre}")
    print(f"Director: {director}")
else:
    print("Failed to fetch data from OMDB API")


def insert_into_movie(title, released, genre, director):
    with connection.cursor() as cursor:
        sql = "INSERT INTO movie.Movie_info (title, released, genre, director) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, released, genre, director))
        connection.commit()


insert_into_movie(
    my_movie.get("title"),
    my_movie.get("released"),
    my_movie.get("genre"),
    my_movie.get("director")
)