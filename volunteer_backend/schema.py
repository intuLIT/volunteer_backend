import graphene

import volunteer_backend.user.schema


class Query(volunteer_backend.user.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
