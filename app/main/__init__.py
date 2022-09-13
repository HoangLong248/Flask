from flask import Flask, Blueprint

main = Blueprint('main', __name__)

from . import views, errors

