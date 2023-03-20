from app.controllers import OrderController
from app.services.base import BaseService
from app.services.factory import ServiceFactory


class OrderService(BaseService):
    controller_class = OrderController
    blueprint_name = 'order'

    @staticmethod
    def create_blueprint():
        return ServiceFactory.create_blueprint(OrderService)
