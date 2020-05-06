import functools

from sanic.log import logger
from sanic.response import json, text


def catch_exceptions(func):
    """Catch exceptions."""

    @functools.wraps(func)
    async def decorated(request, *args, **kwargs):
        try:
            res = await func(request, *args, **kwargs)
        except Exception as e:
            logger.exception(str(e))
            return text(body='Invalid request', status=400)
        return json(body=res)
    return decorated


def setup_aiohttp_session(func):
    """Setup session."""

    @functools.wraps(func)
    async def decorated(request, *args, **kwargs):
        return await func(request.app.config["client_session"], *args, **kwargs)
    return decorated
