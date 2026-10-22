class ElemCount(Exception):
    pass


class ExcProduct(Exception):
    pass

class PromoError(Exception):
    pass

promos = ["DISCOUNT10", "DISCOUNT20", "DISCOUNT50"]

class Product:

    def __init__(self, id: str, name: str, price: int, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock




class ShoppingCart:
    array: dict[str, int]

    def __init__(self):
        self.array: dict[str, int] = {}
        self.discount: float = 0.0

    ##добавление товара в корзину
    def add(self, id: str, stock: int, data):
        if stock == 0:
            raise ElemCount(f'Нельзя добавить 0 единиц товара')
        for y in data:
            if y.id == id:
                if y.stock >= stock:
                    if id in self.array:
                        self.array[id] += stock
                    else:
                        self.array[id] = stock
                    y.stock -= stock
                    return self.array
                else:
                    raise ElemCount(f'Количество добавляемых товаров больше, чем есть на складе.')

        raise ExcProduct(f'Данный товар отсутсвует на складе.')



    ##уменьшение количества товара в корзине
    def less_count(self, id: str, stock: int, data):
        if id in self.array:
            if self.array[id] >= stock:
                self.array[id] -= stock

                if self.array[id] == 0:
                    del self.array[id]

                for x in data:
                    if x.id == id:
                        x.stock += stock
                        break

                return self.array
            else:
                raise ElemCount(f'В корзине нет такого количества товаров.')

        else:
            raise ExcProduct(f'Данного товара нет в корзине.')


    ##удаление товара из корзины
    def del_product(self, id: str, data):
        if id in self.array:
            for x in data:
                if x.id == id:
                    x.stock += self.array[id]
                    del self.array[id]
                    return self.array

            return self.array
        else:
            raise ExcProduct(f'Данного товара нет в корзине')

    ##полная стоимость товаров в корзине
    def all_cost(self, array):


        if len(self.array) > 0:
            cost = 0
            for x in array:
                if x.id in self.array:
                    cost += self.array[x.id] * x.price

            return cost - cost * self.discount
        else:
            raise ExcProduct(f'Корзина пуста!')


    ##метод для применения скидки
    def promo_dis(self, promo: str):
        if promo in promos:
            self.discount = float(promo[8:])/100
        else:
            raise PromoError(f'Неверный промокод.')