import os, datetime as dt
from flask import render_template, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import app
from app.classes.data import Review, Comment
from app.classes.forms import ReviewForm, CommentForm

@app.route('/reviews')
@login_required
def review_list():
    reviews = Review.objects()
    return render_template('reviews.html', reviews=reviews)

@app.route('/review/<review_id>')
@login_required
def review_detail(review_id):
    this_review   = Review.objects.get(id=review_id)
    these_comments = Comment.objects(review=this_review)
    return render_template('review.html', review=this_review, comments=these_comments)

@app.route('/review/new', methods=['GET','POST'])
@login_required
def review_new():
    form = ReviewForm()
    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename))

        r = Review(
            subject     = form.subject.data,
            content     = form.content.data,
            tag         = form.tag.data,
            author      = current_user._get_current_object(),
            modify_date = dt.datetime.utcnow(),
            image_path  = image_filename
        )
        r.save()
        return redirect(url_for('review_detail', review_id=r.id))
    return render_template('reviewform.html', form=form)

@app.route('/review/edit/<review_id>', methods=['GET','POST'])
@login_required
def review_edit(review_id):
    review = Review.objects.get(id=review_id)
    if review.author != current_user:
        flash("You don't own that review.")
        return redirect(url_for('review_detail', review_id=review_id))

    form = ReviewForm(obj=review)
    if form.validate_on_submit():
        image_filename = review.image_path
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename))

        review.update(
            subject     = form.subject.data,
            content     = form.content.data,
            tag         = form.tag.data,
            modify_date = dt.datetime.utcnow(),
            image_path  = image_filename
        )
        return redirect(url_for('review_detail', review_id=review.id))

    return render_template('reviewform.html', form=form)

@app.route('/review/delete/<review_id>')
@login_required
def review_delete(review_id):
    review = Review.objects.get(id=review_id)
    if review.author == current_user:
        review.delete()
        flash('Review deleted.')
    else:
        flash("Can't delete a review you don't own.")
    return redirect(url_for('review_list'))