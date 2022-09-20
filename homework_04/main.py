"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from .models import async_engine, Base, Session, User, Post
from .jsonplaceholder_requests import fetch_users_data, fetch_posts_data, USERS_DATA_URL, POSTS_DATA_URL


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_main():

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(USERS_DATA_URL),
        fetch_posts_data(POSTS_DATA_URL),
    )

    async with Session() as session:
        async with session.begin():
            for user in users_data:
                user_to_add = User(id=user["id"], name=user["name"], username=user["username"], email=user["email"])
                session.add(user_to_add)
            for post in posts_data:
                post_to_add = Post(user_id=post["userId"], title=post["title"], body=post["body"])
                session.add(post_to_add)
            await session.commit()


def main():

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
