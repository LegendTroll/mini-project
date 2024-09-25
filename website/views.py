from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Task
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/add-task', methods=['POST'])
@login_required
def add_task():
    task_data = request.form.get('task')
    
    if len(task_data) < 1:
        flash('Task is too short!', category='error')
    else:
        new_task = Task(data=task_data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added!', category='success')
    
    return redirect(url_for('views.home'))

@views.route('/delete-task/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted!', category='success')
    else:
        flash('Task does not exist or you do not have permission to delete it.', category='error')
    
    return redirect(url_for('views.home'))
