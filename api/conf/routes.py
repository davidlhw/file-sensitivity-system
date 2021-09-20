from flask_restful import Api

from api.handlers.FileHandlers import UploadFile
from api.handlers.UserHandlers import (
    Index,
    Login,
    Logout,
    Register)


def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Index page.
    api.add_resource(Index, "/")

    # Register page.
    api.add_resource(Register, "/v1/auth/register")

    # Login page.
    api.add_resource(Login, "/v1/auth/login")

    # Logout page.
    api.add_resource(Logout, "/v1/auth/logout")

    # Get users page with admin permissions.
    api.add_resource(UploadFile, "/v1/upload")