from . import controller
from app import db, lm
from flask import render_template, request, url_for, redirect, flash
from app.models.forms import Adm_form, New_adm_form, New_video_form
from app.models.tables import Adm, Video
from flask_login import login_user,logout_user,current_user

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@controller.route('/admin/', methods=['GET','POST'])
def admin():
    form = Adm_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Adm.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('new_movie'))
            else:
                #add a flash message
                return redirect(url_for('controller.admin'))
    else:
        return render_template("admin_login.html",form=form)

@controller.route('/logout/')
def logout():
    if is_authenticated:
        logout_user()
        return redirect(url_for("index"))


@controller.route('/new_admin/',methods=['GET','POST'])
def new_admin():
    form = New_adm_form()
    if request.method == 'Post':
        if form.validate_on_submit():
            NewAdmData = Adm(form.user.data, form.password.data, form.power.data)
            db.session.add(NewAdmData)
            db.session.commit()
            return redirect(url_for('index')) #add a flash message
        else:
            pass #add a flash message
    else:
        return render_template("new_admin.html", form=form)


@controller.route('/new_movie/', methods=['GET','POST'])
def new_movie():
    form = New_video_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            NewVideoData = Video(form.title.data,form.genre.data,form.link.data,form.image.data)
            db.session.add(NewVideoData)
            db.session.commit()
            #add a flash message
            return redirect(url_for('new_movie'))
        else:
            pass#add a flash message
    else:
        return render_template('new_movie.html',form=form)

@controller.route('/edit/<int:id>/', methods=['GET','POST'])
def edit(id):
    form = New_video_form()
    video = Video.query.filter_by(id=id).first()
    if request.method == "POST":
        video.title = form.title.data
        video.link = form.link.data
        video.image = form.image.data
        video.genre = form.genre.data
        video.description = form.description.data
        db.session.commit()
        #add a flash message
        return redirect(url_for('index'))
    else:
        return render_template('edit.html',form=form, video=video)
