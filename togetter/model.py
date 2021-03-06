from togetter.util import normalize
from google.appengine.ext import ndb


class Group(ndb.Model):  # Root entity
    label = ndb.StringProperty()
    default_store = ndb.KeyProperty(kind='Store')


class Ingredient(ndb.Model):  # Group as parent
    normalized = ndb.ComputedProperty(lambda self: normalize(self.key.id()))
    words = ndb.ComputedProperty(lambda self: [
        normalize(word) for word in self.key.id().split()], repeated=True)


class Store(ndb.Model):  # Group as parent
    label = ndb.StringProperty()
    location = ndb.GeoPtProperty()


class Ordering(ndb.Model):  # Store as parent
    position = ndb.IntegerProperty(default=0)


class List(ndb.Model):  # Group as parent
    label = ndb.StringProperty()
    store = ndb.KeyProperty(kind=Store)


class Item(ndb.Model):  # List as parent
    amount = ndb.IntegerProperty(default=1)
    position = ndb.IntegerProperty(default=0)
    collected = ndb.BooleanProperty(default=False)


class Listener(ndb.Model):  # Group as parent
    created = ndb.DateTimeProperty(auto_now_add=True)
