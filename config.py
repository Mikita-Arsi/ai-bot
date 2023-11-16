import os


db_name = 'mgr.sqlite'

is_deploy = bool(int(os.getenv("IS_DEPLOY")))
token = os.getenv("TOKEN_N")
openai_key = os.getenv("OPENAI_KEY")

if is_deploy:
    token = os.getenv("TOKEN")
    webhook_url = 'gleb-ai-v2-bot.kz'
else:
    token = os.getenv("TOKEN_N")
    webhook_url = 'https://a4dd-85-143-224-20.ngrok-free.app'


DB = "postgresql://postgres:5432@176.119.147.78:5432/bot"

timeout = 86400