import pytest
from classShop import Product, ShoppingCart, ElemCount, Exc_Product

array = []
iphone = Product("123", "Iphone 16", 60000, 200)
array.append(iphone)
sumsung = Product("124", "Sumsung Galaxy S8", 55000, 300)
array.append(sumsung)
coffee_mach = Product("125", "Coffee machine", 20000, 150)
array.append(coffee_mach)
disk = Product("126", "disk R18", 8000, 1000)
array.append(disk)


def test_add():
    cart = ShoppingCart()
    result = cart.add("123", 100, array)
    result = cart.add("124", 100, array)
    result = cart.add("124", 50, array)

    assert result == {"123": 100, "124": 150}
    assert array[0].stock == 100
    assert array[1].stock == 150

    with pytest.raises(ElemCount) as ctx:
        cart.add("125", 200, array)
    assert "Количество добавляемых товаров больше, чем есть на складе." in str(ctx.value)

    with pytest.raises(ElemCount) as ctx:
        cart.add("125", 0, array)
    assert "Нельзя добавить 0 единиц товара" in str(ctx.value)

    with pytest.raises(Exc_Product) as ctx:
        cart.add("127", 200, array)
    assert "Данный товар отсутсвует на складе." in str(ctx.value)

    cart.del_product("123", array)
    cart.del_product("124", array)



def test_less():
    cart = ShoppingCart()
    result = cart.add("123", 100, array)
    result = cart.add("126", 300, array)

    result = cart.less_count("123", 50, array)
    result = cart.less_count("126", 100, array)

    assert result == {"123": 50, "126": 200}
    assert array[0].stock == 150
    assert array[3].stock == 800

    with pytest.raises(ElemCount) as ctx:
        cart.less_count("123", 100, array)
    assert "В корзине нет такого количества товаров." in str(ctx.value)

    result = cart.less_count("123", 50, array)
    assert result == {"126": 200}

    with pytest.raises(Exc_Product) as ctx:
        cart.less_count("127", 200, array)
    assert "Данного товара нет в корзине." in str(ctx.value)

    cart.del_product("126", array)

def test_del():
    cart = ShoppingCart()
    result = cart.add("123", 100, array)
    result = cart.add("126", 300, array)

    result = cart.del_product("123", array)
    result = cart.del_product("126", array)

    assert result == {}
    assert array[0].stock == 200
    assert array[3].stock == 1000

    with pytest.raises(Exc_Product) as ctx:
        cart.del_product("123", array)
    assert "Данного товара нет в корзине" in str(ctx.value)

def test_cost():
    cart = ShoppingCart()

    with pytest.raises(Exc_Product) as ctx:
        cart.all_cost(array)
    assert "Корзина пуста!" in str(ctx.value)

    result = cart.add("123", 100, array)
    result = cart.add("124", 200, array)
    result = cart.add("125", 100, array)
    result = cart.add("126", 200, array)

    assert cart.all_cost(array) == 20600000

