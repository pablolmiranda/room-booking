from django.test import TestCase

from campus.models import Room
from campus.models import Attribute


class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="Gym", occupancy=10)

        Attribute.objects.create(name="Piano")
        Attribute.objects.create(name="Speakers")

    def test_room_name(self):
        r = Room.objects.get(pk=1)
        self.assertEquals(r.name, "Gym")

    def test_room_occupancy(self):
        r = Room.objects.get(pk=1)
        self.assertEquals(r.occupancy, 10)

    def test_room_attributes(self):
        rooms = Room.objects.all()
        attrs = Attribute.objects.all()

        r1 = rooms[0]

        a1 = attrs[0]
        a2 = attrs[1]

        r1.attributes.add(a1, a2)
        r1_attrs = r1.attributes.all()
        self.assertEquals("Piano", r1_attrs[0].name)
        self.assertEquals("Speakers", r1_attrs[1].name)
        self.assertEquals(len(r1_attrs), 2)

    def test_search_with_empty_parameters(self):
        rooms = Room().search(0, [])
        self.assertEquals(rooms[0].name, "Gym")

    def test_search_with_occupacy_greater_than_available(self):
        rooms = Room().search(20, [])
        self.assertEquals(len(rooms), 0)

    def test_search_with_occupacy_and_attributes(self):
        attrs = Attribute.objects.all()
        room = Room(name="Hall", occupancy="50")
        room.save()
        room.attributes.add(attrs[0])

        rooms = Room().search(30, ['Piano'])
        self.assertEquals(len(rooms), 1)
        self.assertEquals(rooms[0].name, "Hall")

class AttributeTestCase(TestCase):
    def setUp(self):
        Attribute.objects.create(name="Piano")

        Room.objects.create(name="Gym")
        Room.objects.create(name="Sanctuary")

    def test_attribute_name(self):
        a = Attribute.objects.get(pk=1)
        self.assertEquals(a.name, "Piano")

    def test_attributes_room(self):
        rooms = Room.objects.all()
        attrs = Attribute.objects.all()

        r1 = rooms[0]
        r2 = rooms[1]

        a1 = attrs[0]

        r1.attributes.add(a1)
        r2.attributes.add(a1)

        a1_rooms = a1.room_set.all()
        self.assertEquals("Gym", a1_rooms[0].name)
        self.assertEquals("Sanctuary", a1_rooms[1].name)
        self.assertEquals(len(a1_rooms), 2)


