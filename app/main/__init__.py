from flask import Blueprint
main = Blueprint('main',__name__)

from . import views,errors,forms

from .insert_kata import InsertProblemViewCommand, InsertTestFixtureCommand
from .start_kata import StartKataCommand
from .submit_kata import SubmitProblemCommand
