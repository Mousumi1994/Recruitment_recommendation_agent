**📌 Project Overview**

This project demonstrates a basic Recruitment Recommendation AI Agent built using CrewAI and a local Large Language Model (LLM).
The agent simulates how AI can assist HR and hiring teams by analyzing a candidate’s profile against a job description and generating a structured hiring recommendation.

The focus of this project is to understand:

How to design a single AI agent

How to use tools for task-specific reasoning

How AI agents can support real-world recruitment workflows

**🧠 What This AI Agent Does**

The AI agent:

Analyzes a candidate’s resume/profile to extract skills and experience

Compares those skills with a given job description

Produces a human-readable recommendation report, including:

Match score (1–10)

Candidate strengths

Skill/experience gaps

Final hiring recommendation

This system is intended as a decision-support tool, not a replacement for human recruiters.

**⚙️ Technology Stack**

Python

CrewAI – AI agent framework

Ollama (Llama 3.1) – Local LLM inference

Prompt Engineering

Tool-based agent reasoning

**🏗️ Code Architecture & Explanation**
**1️⃣ LLM Initialization**

llm = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")


A local LLM (Llama 3.1) is used via Ollama, enabling offline experimentation and avoiding external API dependencies.

**2️⃣ Tool Definitions**

Two tools are created to simulate modular recruitment logic:

🔹 Resume Skill Analysis Tool
@tool
def analyze_resume_skills(candidate_data: str) -> str:


Extracts key skills and experience from candidate data

In this prototype, returns a predefined analysis (can be extended later)

🔹 Job Matching Tool
@tool
def match_job_description(job_description: str, skills_analysis: str) -> str:


Compares extracted skills against job requirements

Simulates evaluation logic for candidate-job fit

**3️⃣ AI Agent Definition**



recruiter_agent = Agent(
    role="Expert Recruitment Analyst",
    
    goal="Recommend the top candidate for a specific job opening",
    
    tools=[analyze_resume_skills, match_job_description],
    
    allow_delegation=False
)




This single AI agent:

Acts as an expert recruitment analyst

Uses defined tools for structured reasoning

Generates objective, data-informed recommendations

Does not delegate tasks (kept simple by design)

**4️⃣ Task Configuration**


recommendation_task = Task(
    description=...,
    
    agent=recruiter_agent
)



The task:

Provides a job description and candidate profile

Instructs the agent to use tools

Requires a structured output including:

Match score

Strengths

Gaps

Hiring recommendation

**5️⃣ Crew Setup & Execution**

crew = Crew(
    agents=[recruiter_agent],
    
    tasks=[recommendation_task],
    
    process=Process.sequential
)


The crew contains one agent and one task

Tasks run sequentially

Final output is printed as a recommendation report

**🎯 Why This Project Matters**

This project showcases:

Practical application of AI agents in HR tech

Understanding of agent design, tools, and prompts

Ability to translate AI concepts into business-relevant solutions

It also serves as a foundation for future enhancements such as:

Multi-agent collaboration

Real resume parsing

Scoring models using data science techniques

ATS or HR system integration

**🚀 Future Improvements**

Add real resume parsing using NLP

Introduce multiple agents (e.g., Skill Evaluator, Culture Fit Agent)

Integrate scoring logic using ML models

Build a UI or API layer

**👤 Author**

Aspiring Data Scientist
Passionate about applying AI and data science to solve real-world problems in recruitment, HR tech, and decision support systems.
