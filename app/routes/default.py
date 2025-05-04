from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

# Here's the basics for making any new route
# It's a good idea to use the same name/word, and same capitalization conventions
# Add a route name, function name, and html template name 
# (then go make that html template)
@app.route('/projectaboutus')
def projectaboutus():
    return render_template('projectaboutus.html')

@app.route('/projectpage')
def projectpage():
    return render_template('projectpage.html')

@app.route('/projectquiz')
def projectquiz():
    return render_template('projectquiz.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/review/new', methods=['GET', 'POST'])
def reviewform():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Review submitted!', 'success')
        return redirect(url_for('reviewform')) 
    return render_template('reviewform.html', form=form)

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/blogform')
def blogform():
    return render_template('blogform.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/blog/new')
def blogsnew():
           return render_template('blog.html')

# In your routes file (e.g., forum.py or wherever the blog routes are defined)

from flask import render_template, redirect, url_for, request
from app import app  # Ensure app is imported correctly

@app.route('/blog/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Get the form data
        title = request.form['title']
        content = request.form['content']
        
        # Here, you can add code to save the new post to the database
        # For example:
        # new_blog_post = BlogPost(title=title, content=content)
        # db.session.add(new_blog_post)
        # db.session.commit()
        
        # Redirect to the list of posts after submission
        return redirect(url_for('view_blog'))  # Adjust 'view_blog' to your actual route for viewing posts

    return render_template('newblogpost.html')  # Create a new template for the form
