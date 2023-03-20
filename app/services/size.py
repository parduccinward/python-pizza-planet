from app.controllers import SizeController
from app.services.base import BaseService
from app.services.factory import ServiceFactory


class SizeService(BaseService):
    controller_class = SizeController
    blueprint_name = 'size'

    @staticmethod
    def create_blueprint():
        return ServiceFactory.create_blueprint(SizeService)
