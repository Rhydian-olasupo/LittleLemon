from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_post_item(self):
        item = Menu.objects.create(Title="IceCream",Price = 80.0,Inventory=100)
        expected_value = str(item)
        self.assertEqual(expected_value,str(item))
