from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

# Veritabanı bağlantısını kurma
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    db='movie',
    port=3308,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
@app.route('/movies/')
def index():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Movie_info")
        movies = cursor.fetchall()
    return render_template('index.html', movies=movies)

@app.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Movie_info WHERE id = %s", (movie_id,))
        movie = cursor.fetchone()
    if movie is None:
        return "Movie not found", 404
    return render_template('movie.html', movie=movie)