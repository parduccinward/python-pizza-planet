

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, IngredientDetail, Size, Beverage


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test', '--cov=./app', '--cov-report', 'term-missing', '--cov-fail-under=100'])


if __name__ == '__main__':
    manager()
