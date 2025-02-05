from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from programm_modules import CRUD

blog_post_file_path = "programm_database/blog_posts.json"
app = Flask(__name__)
blog_data = CRUD.Crud(blog_post_file_path)


@app.route('/')
def index():
    blog_posts = blog_data.get_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')  # Holt den Titel aus dem Formular
        author = request.form.get('author')  # Holt den Autor
        content = request.form.get('content')  # Holt den Inhalt

        if title and author and content:
            blog_posts = blog_data.get_posts()
            blog_posts.append({'id': blog_data.get_newest_id() + 1, 'title': title, 'author': author, 'content': content})

            blog_data.save_posts(blog_posts)

            return redirect(url_for('index'))

    return render_template('new_post.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    blog_posts = blog_data.get_posts()

    post_index, post = blog_data.get_post_by_id(post_id)

    del blog_posts[post_index]

    blog_data.save_posts(blog_posts)

    # reload index.html, cause the data has changed
    return redirect(url_for('index'))

# TODO route funktioniert nicht, wieso?
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """If methods = 'GET'-> update Blogpost, if methods = 'POST' save updated Blogpost"""
    # Fetch the blog posts from the JSON file
    blog_posts = blog_data.get_posts()
    post_index, post = blog_data.get_post_by_id(post_id)

    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        new_content = request.form.get('content')
        new_author = request.form.get('author')

        #changes data in dictionary
        post['content'] = new_content
        post['author'] = new_author

        #changes data in list
        blog_posts[post_index] = post

        # save changes to json
        blog_data.save_posts(blog_posts)

        # Redirect back to index
        return redirect(url_for('index'))

    # TODO route funktioniert nicht, wieso?
    else:
        # So display the update.html page
        return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)