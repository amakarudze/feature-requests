from datetime import datetime

from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from .models import db, FeatureRequest
from .auth import login_required


bp = Blueprint('features', __name__)


@bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html')


@bp.route('/create',  methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        client_id= request.form['client_id']
        priority_id = request.form['priority_id']
        target_date = request.form['email']
        error = None

        if not title:
            error = 'Title is required.'
        elif not description:
            error = 'Description is required.'
        elif not client_id:
            error = 'Client ID is required.'
        if not priority_id:
            error = 'Priority is required.'
        elif not target_date:
            error = 'Target date is required.'
        elif target_date > datetime.utcnow() or target_date == datetime.utcnow():
            error = 'Target date should be in the future.'
        elif FeatureRequest.query.filter_by(client_id=client_id, priority_id=priority_id).first() is not None:
            error = '{} already has feature request with same priority. Please assign another priority.'

        if error is None:
            user = FeatureRequest(title=title, description=description, client_id=client_id, priority_id=priority_id,
                                  target_date=target_date)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

        flash(error)

    return render_template('create.html')


