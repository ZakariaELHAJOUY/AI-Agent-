import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

llm = ChatOpenAI(
    model="phi3.5:3.8b",
    base_url="http://localhost:11434/v1"
)

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        You love to know information.  People love and hate you for it.  You win most of the
        quizzes at your local pub.
    """,
    llm=llm
)

# Get task description from the console
task_description = input("Enter the task description: ")
expected_output = "Give me a quick summary and then also give me 7 bullet points describing it."

task1 = Task(
    description=task_description,
    expected_output=expected_output,
    agent=info_agent
)
crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=2
)

result = crew.kickoff()

print("############")
print(result)

