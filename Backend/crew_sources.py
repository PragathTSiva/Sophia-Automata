from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import EXASearchTool
from pydantic import BaseModel, Field, ValidationError
from typing import List
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)

class ResearchRequest(BaseModel):
    topic: str = Field(..., description="Research topic to search for")

class MySources(BaseModel):
    article_links: List[str] = Field(..., description="links to research articles")
    video_links: List[str] = Field(..., description="links to video content")

@CrewBase
class ResearchCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def article_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['article_research_agent'],
            tools=[EXASearchTool()],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def video_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['video_research_agent'],
            tools=[EXASearchTool()],
            verbose=True,
            allow_delegation=False,
        )

    @task
    def article_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['article_research_task'],
            agent=self.article_research_agent(),
            output_json=MySources
        )

    @task
    def video_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['video_research_task'],
            agent=self.video_research_agent(),
            output_json=MySources
        )

    @crew
    def crew(self) -> Crew:
        """Creates a Research Crew with separate agents for articles and videos"""
        return Crew(
            agents=[
                self.article_research_agent(),
                self.video_research_agent()
            ],
            tasks=[
                self.article_research_task(),
                self.video_research_task()
            ],
            process=Process.sequential,
            verbose=True,
        )

@app.route('/api/research', methods=['POST'])
def research_topic():
    data = request.get_json()
    research_request = ResearchRequest(**data)
    research = {'topic': research_request.topic}
    crew = ResearchCrew()
    result = crew.crew().kickoff(inputs=research)
    crew_output = result.to_dict()
    return jsonify(crew_output)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Research API is running'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
