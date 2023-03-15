from app.plugins import ma
from .models import Beverage, BeverageDetail, Ingredient, Size, Order, IngredientDetail


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price', 'size')


class IngredientDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )


class BeverageDetailSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeverageDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredient_detail = ma.Nested(IngredientDetailSerializer, many=True)
    beverage_detail = ma.Nested(BeverageDetailSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'ingredient_detail',
            'beverage_detail'
        )
