import aiohttp

from sanic.app import Sanic

from service_api.resources.movie_resource import MovieResource


def create_app():
    """Create our sanic application object."""
    app = Sanic()
    register_listeners(app)
    register_routes(app)
    return app


def register_listeners(app):
    """
    Register listeners for sanic application.
    :param app: sanic application
    """
    app.add_task(register_aiohttp_pool(app))


async def register_aiohttp_pool(app):
    """
    Setup session.
    :param app: sanic application
    """
    app.config["client_session"] = aiohttp.ClientSession()


def register_routes(app):
    """
    Add our resource objects to the sanic application.
    :param app: sanic application
    """
    app.add_route(
        MovieResource.as_view(),
        "/movies",
        methods=["GET"],
    )
