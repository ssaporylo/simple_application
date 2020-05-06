import asyncio

from aiocache import cached

from sanic.views import HTTPMethodView

from service_api.constants import CACHE_TTL, URL
from service_api.services.decorators import catch_exceptions
from service_api.services.http_client import get_http_request


class MovieResource(HTTPMethodView):

    @cached(ttl=CACHE_TTL, key=__name__)
    @catch_exceptions
    async def get(self, request):
        futures = [
            get_http_request(request, f"{URL}/people"),
            get_http_request(request, f"{URL}/films")
        ]
        people, films = await asyncio.gather(*futures)
        film_cache = {}
        for person in people:
            people_films = person.pop('films', [])
            for film in people_films:
                key = film.split('/')[-1]
                if film_cache.get(key):
                    film_cache[key].append(person)
                else:
                    film_cache[key] = [person]
        for film in films:
            film['people'] = film_cache.get(film["id"])
        return films
