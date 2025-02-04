from flask import Flask
from flask import render_template
from programm_modules import CRUD

blog_post_file_path = 'programm_database/blog_posts.json'
app = Flask(__name__)
blog_data = CRUD.Crud(blog_post_file_path)



@app.route('/p')
def index():
    blog_posts = blog_data.get_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)