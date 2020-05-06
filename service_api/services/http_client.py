from sanic.log import logger

from service_api.services.decorators import setup_aiohttp_session


@setup_aiohttp_session
async def get_http_request(session, url):
    """
    Make get api call
    :param session: Session instance
    :param url: string
    :return: json
    """
    logger.info(f"Get request: {url}")
    async with session.get(url) as resp:
        try:
            resp_json = await resp.json()
        except Exception as e:
            logger.exception(f"Request: {url} failed. Error: {str(e)}")
            raise
        if resp.status not in [200, 204]:
            logger.error(f"Service unavailable. Status code:{resp.status}")
        return resp_json
