from flask import render_template, Blueprint

blog = Blueprint('blog', __name__)

@blog.route("/blog")
def blog_main():
    return render_template('blog.html')
