from graphene import AbstractType, Field, Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from volunteer_backend.user.models import User



# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node, )
        filter_fields = ['id', 'name', 'email', 'phone', 'location']
        # filter_fields = {
        #     'id': ['exact'],
        #     'name': ['exact', 'icontains', 'istartswith'],
        #     'email': ['exact'],
        #     'phone': ['exact', 'icontains', 'istartswith'],
        #     'location': ['exact']
        # }
        # filter_order_by = ['id']



# class NonProfitNode(DjangoObjectType):
#     class Meta:
#         model = NonProfit
#         # Allow for some more advanced filtering here
#         filter_fields = {
#             'id': ['exact'],
#             'name': ['exact', 'icontains', 'istartswith'],
#             'description': ['icontains'],
#             'user': ['exact'],
#             'location': ['exact'],
#         }
#         filter_order_by = ['id',]
#         interfaces = (relay.Node, )

# class EventNode(DjangoObjectType):
#     class Meta:
#         model = Event
#         # Allow for some more advanced filtering here
#         filter_fields = {
#             'id': ['exact'],
#             'name': ['exact', 'icontains', 'istartswith'],
#             'start_date': ['icontains'],
#             'end_date': ['icontains'],
#             'address': ['icontains', 'exact'],
#             'location': ['exact'],
#             'description': ['icontains'],
#             'photo': ['exact'],
#             'min_volunteers': ['exact'],
#             'max_volunteers': ['exact'],
#             'organization': ['exact', 'icontains', 'istartswith'],
#         }
#         filter_order_by = ['organization',]
#         interfaces = (relay.Node, )

# class CategoryNode(DjangoObjectType):
#     class Meta:
#         model = Category
#         filter_fields = {
#             'id': ['exact'],
#             'name': ['exact', 'icontains', 'istartswith'],
#         }
#         filter_order_by = ['name',]
#         interfaces = (relay.Node, )


class Query(AbstractType):
    name = "Model"
    user = Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    
    
    # nonprofit = relay.Node.Field(NonProfitNode)
    # all_nonprofits = DjangoFilterConnectionField(NonProfitNode)

    # event = relay.Node.Field(EventNode)
    # all_events = DjangoFilterConnectionField(EventNode)

    # category = relay.Node.Field(CategoryNode)
    # all_categories = DjangoFilterConnectionField(CategoryNode)

