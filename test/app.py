import os

import openai
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# OPENAI_API_KEYを取得
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}]
)
