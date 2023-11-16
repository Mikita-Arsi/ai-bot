import logging

import openai
import uvicorn
import time

from db import delete_comments
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from config import token, is_deploy, webhook_url, timeout, openai_key
from bot.commands import register_base_handlers
from init_db import metadata, engine, db
from aiogram.fsm.storage.memory import MemoryStorage


logger = logging.getLogger(__name__)
if is_deploy:
    logging_type = logging.INFO
    logging.basicConfig(
        level=logging_type,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s - %(name)s - %(message)s',
    )

else:
    logging_type = logging.INFO
    logging.basicConfig(
        level=logging_type,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
openai.api_key = openai_key
WEBHOOK_PATH = f"/bot{token}"
WEBHOOK_URL = webhook_url + WEBHOOK_PATH

app = FastAPI()
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

metadata.create_all(engine)
app.state.databade = db

start_time = time.time()


@app.on_event("startup")
async def on_startup():
    db_ = app.state.databade
    if not db_.is_connected:
        await db_.connect()
    register_base_handlers(dp)
    webhook_info = await bot.get_webhook_info()
    if webhook_info != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
    logger.info("App started")


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    global start_time
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)
    if time.time() - start_time > timeout:
        start_time = time.time()
        await delete_comments(259200)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    logger.info("App stopped")


def main():
    while True:
        try:
            uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    main()
