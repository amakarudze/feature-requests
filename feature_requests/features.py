import functools

from flask import Blueprint, flash, g, render_template, request, session, url_for

bp = Blueprint('features', __name__, url_prefix='/features')