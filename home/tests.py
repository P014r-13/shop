from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Product, Category, Order, OrderItem, Address
from user.models import Code, User
class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Test Product', price=100, count=10, disc='Test Description', category=Category.objects.create(name='Test Category'))

    def test_product_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_product_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_product_count_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('count').verbose_name
        self.assertEqual(field_label, 'count')

    def test_product_disc_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('disc').verbose_name
        self.assertEqual(field_label, 'disc')

    def test_product_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_product_image_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_product_discount_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('discount').verbose_name
        self.assertEqual(field_label, 'discount')

    def test_product_string_representation(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), product.name)

    def create_product(self, name, price, count, disc, category):
        return Product.objects.create(
            name=name,
            price=price,
            count=count,
            disc=disc,
            category=category
        )

    def read_product(self, id):
        return Product.objects.get(id=id)

    def update_product(self, product, name=None, price=None, count=None, disc=None, category=None):
        if name:
            product.name = name
        if price:
            product.price = price
        if count:
            product.count = count
        if disc:
            product.disc = disc
        if category:
            product.category = category
        product.save()
        return product

    def delete_product(self, product):
        product.delete()


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_category_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_category_parent_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('parent').verbose_name
        self.assertEqual(field_label, 'parent')

    def test_category_string_representation(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), category.name)

    def create_category(self, name, parent=None):
        return Category.objects.create(name=name, parent=parent)

    def read_category(self, id):
        return Category.objects.get(id=id)

    def update_category(self, category, name=None, parent=None):
        if name:
            category.name = name
        if parent:
            category.parent = parent
        category.save()
        return category

    def delete_category(self, category):
        category.delete()


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Address.objects.create(user=User.objects.create(email='testuser@example.com', password='testpassword'), address='123 Test St', city=Address.City.Tehran)

    def test_address_user_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_address_address_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_address_city_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_address_string_representation(self):
        address = Address.objects.get(id=1)
        self.assertEqual(str(address), address.address)

    def create_address(self, user, address, city):
        return Address.objects.create(
            user=user,
            address=address,
            city=city
        )

    def read_address(self, id):
        return Address.objects.get(id=id)

    def update_address(self, user=None, address=None, city=None):
        if user:
            address.user = user
        if address:
            address.address = address
        if city:
            address.city = city
        address.save()
        return address

    def delete_address(self, address):
        address.delete()



class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(user=User.objects.create(email='testuser@example.com', password='testpassword'), date='2024-04-19 12:00:00', status=True, code=Code.objects.create(code=12345, time='12:00'))

    def test_order_user_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_order_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_order_status_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_order_code_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_order_string_representation(self):
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), f'Order {order.id}')

class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        OrderItem.objects.create(order=Order.objects.create(user=User.objects.create(email='testuser@example.com', password='testpassword'), date='2024-04-19 12:00:00', status=True, code=Code.objects.create(code=12345, time='12:00')), product=Product.objects.create(name='Test Product', price=100, count=10, disc='Test Description', category=Category.objects.create(name='Test Category')), quantity=2)

    def test_order_item_order_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order')

    def test_order_item_product_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('product').verbose_name
        self.assertEqual(field_label, 'product')

    def test_order_item_quantity_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_order_item_string_representation(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertEqual(str(order_item), order_item.product.name)

class CodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Code.objects.create(code=12345, time='12:00')

    def test_code_code_label(self):
        code = Code.objects.get(id=1)
        field_label = code._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_code_time_label(self):
        code = Code.objects.get(id=1)
        field_label = code._meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'time')

    def test_code_string_representation(self):
        code = Code.objects.get(id=1)
        self.assertEqual(str(code), f'Code {code.code}')
