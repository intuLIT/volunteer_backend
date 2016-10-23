import graphene

import cookbook.ingredients.schema


class Query(volunteer_backend.volunteer_backend.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
