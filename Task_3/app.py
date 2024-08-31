import pymysql
from flask import Flask

app= Flask(__name__)

blog_list= [
        {
        "title": "Blog 1",
        "content" : "content 1",
        "author" : "author 1",
        },
        {
        "title": "Blog 2",
        "content" : "content 2",
        "author" : "author 2",
        },
        {
        "title": "Blog 3",
        "content" : "content 3",
        "author" : "author 3",
        },
        {
        "title": "Blog 4",
        "content" : "content 4",
        "author" : "author 4",
        }
    ]

@app.route('/')
def index():
    return "Hello, world"

@app.route('/about/')
def about_page():
    return "This is about page"

@app.route('/blogs/')
def blogs():
    return blog_list
@app.route('/blogs/<int:id>')
def blog_detail(id):
    if id > 0 and id <= len(blog_list):
        return blog_list[id-1]
    else:
        return "Blog not found!"
@app.route('/blogs/<string:blog_title>')
def blog_detail_with_string(blog_title):
    return f"Blog with title {blog_title}"

if __name__ == '__main__':
    app.run(debug=True)