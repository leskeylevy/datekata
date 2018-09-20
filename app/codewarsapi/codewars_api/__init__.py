from flask import Blueprint
codewars_api = Blueprint('codewars_api',__name__)

from . import codewarsapi, codewarsession, consts,setup
