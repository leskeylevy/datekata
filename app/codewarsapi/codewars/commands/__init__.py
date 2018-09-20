"""
Need to load all the commands when package is imported in order for sublime to
register all the commands
"""
from flask import Blueprint
commands = Blueprint('commands',__name__)

from . import insert_kata,start_kata,submit_kata



