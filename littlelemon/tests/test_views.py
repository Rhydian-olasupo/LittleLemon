from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title='Amala',Price=10.60,Inventory=20)
        self.menu2 = Menu.objects.create(Title='Sharwama',Price=20.50,Inventory=500)
        # Add more test instances of the Menu model if needed

    def test_getall(self):
        url = reverse('menu')
        print(url)
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)