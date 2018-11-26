from datetime import datetime

from flask import Blueprint, flash, render_template, request
from sqlalchemy import and_

from .models import db, FeatureRequest, Customer, Priority, ProductArea
from .auth import login_required


bp = Blueprint('features', __name__)


@bp.route('/', methods=['GET'])
# @login_required
def index():
    return render_template('index.html')


@bp.route('/create',  methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        customer_id = request.form['customer_id']
        priority_id = request.form['priority_id']
        product_area = request.form['product_area']
        target_date = request.form['target_date']

        error = None

        if not title:
            error = 'Title is required.'
        elif not description:
            error = 'Description is required.'
        elif not customer_id:
            error = 'Client ID is required.'
        if not priority_id:
            error = 'Priority is required.'
        elif not target_date:
            error = 'Target date is required.'
        # elif target_date > datetime.utcnow() or target_date == datetime.utcnow():
            # error = 'Target date should be in the future.'
        elif FeatureRequest.query.filter(and_(FeatureRequest.customer_id == customer_id,
                                              FeatureRequest.priority_id == priority_id,
                                              FeatureRequest.closed == False)).all():
            error = 'Customer already has feature request with same priority. Please assign another priority.'

        flash(error)

        if error is None:
            feature_request = FeatureRequest(title=title, description=description, customer_id=customer_id,
                                             priority_id=priority_id, product_area=product_area,
                                             target_date=target_date)
            db.session.add(feature_request)
            db.session.commit()
            flash('Feature request added successfully.')

    clients = Customer.query.all()
    priority_list = Priority.query.all()
    product_areas = ProductArea.query.all()

    return render_template('create.html', clients=clients, priority_list=priority_list, product_areas=product_areas)


@bp.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Client name is required.'
            flash(error)

        if error is None:
            client_name = Customer(name=name)
            db.session.add(client_name)
            db.session.commit()
            flash('Client added successfully.')

    return render_template('client.html')


@bp.route('/add_priority', methods=['GET', 'POST'])
def add_priority():
    if request.method == 'POST':
        priority_level = request.form['priority_level']
        error = None

        if not priority_level:
            error = 'Priority level is required.'
            flash(error)

        if error is None:
            priority = Priority(priority_level=priority_level)
            db.session.add(priority)
            db.session.commit()
            flash('Priority added successfully.')

    return render_template('priority.html')


@bp.route('/add_product_area', methods=['GET', 'POST'])
def add_product_area():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Product area is required.'
            flash(error)

        if error is None:
            product_area = ProductArea(name=name)
            db.session.add(product_area)
            db.session.commit()
            flash('Product area added successfully.')

    return render_template('product_area.html')
