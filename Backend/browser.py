from flask import Flask, request, jsonify
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use import Agent
from langchain_openai import ChatOpenAI
from playwright.async_api import async_playwright
from flask_cors import CORS
import asyncio

app = Flask(__name__)
CORS(app)

async def init_browser():
     p = await async_playwright().start()
     browser = await p.chromium.launch(
         executable_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
         headless=False
     )
     return browser

async def open_tabs(links):
    browser_instance = await init_browser()
    context = await browser_instance.new_context()
    
    for i in links:
        page = await context.new_page()
        await page.goto(i)
        print(f"Tab 1 opened: {i}")

async def create_doc(links):
    with open('summarize.txt', 'r') as file:
        summarize_content = file.read()
    browser_config = BrowserConfig(
        chrome_instance_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        headless=False,
        disable_security=True,
    )
    browser_ag = Browser(config=browser_config)
    b_context = await browser_ag.new_context()
    model = ChatOpenAI(model='gpt-4o')


    agent = Agent(
        task='In docs.google.com, open a new document, then first copy and paste ' + summarize_content + 
        ' then add each link in:\n' + '\n'.join(links) + 
        ' to the document and indicate spacing and an area to take notes about each link, which you will leave blank for someone else to fill out. So after each link just write Notes with a colon',
        llm=model,
        browser_context=b_context,
    )

    await agent.run()

@app.route('/api/browser', methods=['POST'])
async def browser_api():
    data = request.get_json()
    links = data.get('links', [])
    try:
        await open_tabs(links)
        await create_doc(links)
        return '', 204  # Return no content with 204 status code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5002, debug=True)
