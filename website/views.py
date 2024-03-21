from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Note, session

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('home.html', user=current_user)

    elif request.method == 'POST':
        # if we want to add note
        if 'note' in request.form:
            note_text = request.form['note']

            if len(note_text) < 1:
                flash('Note is too short!', category='error')
                return redirect(url_for('views.index', user=current_user))

            new_note = Note(note_text, user_id=current_user.id)
            session.add(new_note)
            session.commit()
            flash('Note added!', category='success')

            return redirect(url_for('views.index', user=current_user))

        # if we want delete note
        elif 'delete_note' in request.form:
            note_id_to_delete = request.form['delete_note']
            print(note_id_to_delete)
            note_to_delete = session.query(Note).filter_by(id=note_id_to_delete).one_or_none()
            session.delete(note_to_delete)
            session.commit()
            flash('Note deleted!', category='success')
            return redirect(url_for('views.index', user=current_user))


