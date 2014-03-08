from app import app
from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, login_user, logout_user, current_user
from forms import UserLoginForm
from models import User



@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserLoginForm()
    all = User.query.all()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return render_template('user_page.html', user=user)
    return render_template('home.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
