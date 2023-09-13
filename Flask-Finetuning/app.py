import openai
from flask import Flask, jsonify, request

app = Flask(__name__)

# OpenAI APIキーを設定
openai.api_key = "YOUR_API_KEY"


@app.route("/generate", methods=["POST"])
def generate_response():
    # リクエストからテキストメッセージを取得
    user_message = request.json["user_message"]

    # OpenAIのAPIを使用してテキスト生成
    response = openai.Completion.create(
        model="ft:gpt-3.5-turbo-0613:org-3rODLwkcbvK5spUe147VVARU::7WDiAH8m",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    # 応答からassistantのメッセージを抽出
    assistant_response = response.choices[0].message["content"]

    # 応答をJSON形式で返す
    return jsonify({"assistant_response": assistant_response})


if __name__ == "__main__":
    app.run()
