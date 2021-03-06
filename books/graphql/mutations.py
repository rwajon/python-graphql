import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Mutation(ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()