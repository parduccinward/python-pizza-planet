from app.controllers import BeverageController
from app.services.base import BaseService
from app.services.factory import ServiceFactory


class BeverageService(BaseService):
    controller_class = BeverageController
    blueprint_name = 'beverage'

    @staticmethod
    def create_blueprint():
        return ServiceFactory.create_blueprint(BeverageService)
