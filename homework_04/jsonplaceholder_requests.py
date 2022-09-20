"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> list[dict]:
    async with session.get(url) as response:
        data = await response.json()
        return data


async def fetch_users_data(users_data_url) -> list[dict]:
    async with aiohttp.ClientSession(trust_env=True) as session:
        data = await fetch_json(session, users_data_url)
        return data


async def fetch_posts_data(posts_data_url) -> list[dict]:
    async with aiohttp.ClientSession(trust_env=True) as session:
        data = await fetch_json(session, posts_data_url)
        return data
