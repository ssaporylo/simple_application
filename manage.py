import logging

import click

from service_api.app import create_app


logger = logging.getLogger(__name__)


@click.group()
def command_group():
    """Works as a command group."""
    pass


@command_group.command(help="Run server")
@click.option("-h", "--host", default="0.0.0.0")
@click.option("-p", "--port", default="5000")
def runserver(host, port):
    app = create_app()
    app.run(host, port)


if __name__ == "__main__":
    try:
        command_group()
    except Exception as e:
        logger.critical(
            f"Unexpected exception occurred. Service is going to shutdown. Error message: {e}",
            extra={"error_message": e},
        )
        exit(1)
    finally:
        logger.info("Service stopped.")
