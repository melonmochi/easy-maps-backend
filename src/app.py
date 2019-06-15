from flask import Flask
from flask_graphql import GraphQLView
from .database import db_session
from .schema import schema


def create_app():
    app = Flask(__name__)
    app.debug = True

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            chema=schema,
            graphiql=True,  # for having the GraphiQL interface
            context={'session': db_session}))

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
