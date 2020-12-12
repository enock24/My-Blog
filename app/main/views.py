from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for, abort
from ..models import *
from .. import db,photos
from . import main
# from ..email import mail_message
# from .forms import BlogForm,CommentForm,UpdateProfile


@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Welcome to Blog Application!!"
    title= 'Blog-app!'
    return render_template('index.html', message=message,title=title)