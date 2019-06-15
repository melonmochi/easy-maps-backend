import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from .models import UserModel, RoleModel


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode


class RoleNode(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class RoleConnection(relay.Connection):
    class Meta:
        node = RoleNode


class Query(graphene.ObjectType):

    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_users = SQLAlchemyConnectionField(UserConnection)
    # Disable sorting over this field
    all_roles = SQLAlchemyConnectionField(RoleConnection, sort=None)

    def resolve_user(self, args, context, info):
        query = UserNode.get_query(context)
        id = args.get('id')
        return query.get(id)


schema = graphene.Schema(query=Query)
