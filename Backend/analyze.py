import requests
import json
import asyncio
import aiohttp
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

def analyze_paragraph(paragraph):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the given paragraph and provide a summary and insights."},
            {"role": "user", "content": f"Analyze this paragraph:\n\n{paragraph}\n\nProvide:\n1. A concise summary of the main points\n2. Additional insights and analysis"}
        ],
        temperature=0.2,
        max_tokens=1000
    )
    cleaned_response = response.choices[0].message.content.replace('*', '')
    with open("summarize.txt", 'w') as f:
        f.write(cleaned_response)
    return cleaned_response

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    paragraph = data.get('paragraph', '')
    result = analyze_paragraph(paragraph)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(port=5003, debug=True)
