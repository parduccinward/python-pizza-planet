from app.controllers import IngredientController
from app.services.base import BaseService
from app.services.factory import ServiceFactory


class IngredientService(BaseService):
    controller_class = IngredientController
    blueprint_name = 'ingredient'

    @staticmethod
    def create_blueprint():
        return ServiceFactory.create_blueprint(IngredientService)
