"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpvpvdvk4rjsv8kqm0-a.oregon-postgres.render.com",
        database="todo_fhwe",
        user="root",
        password="DmSSqG7bULZ2G6y5gGaXcszdrq6Egx6T")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
