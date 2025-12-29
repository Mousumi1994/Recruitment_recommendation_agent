from crewai import Agent, Crew, Task, Process, LLM
from crewai.tools import tool

# Initialize LLM
llm = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")


# ---- TOOLS ----

@tool
def analyze_resume_skills(candidate_data: str) -> str:
    """
    Analyzes a candidate's resume text to extract key skills and experience.
    """
    return (
        "Skills: Python, SQL, Machine Learning, Communication; "
        "Experience: 3 years in data science"
    )


@tool
def match_job_description(job_description: str, skills_analysis: str) -> str:
    """
    Compares extracted skills to a job description to determine fit.
    """
    return "The skills and experience have been compared to the job requirements."


# ---- AGENT ----

recruiter_agent = Agent(
    role="Expert Recruitment Analyst",
    goal="Recommend the top candidate for a specific job opening based on their profile, skills, and experience",
    backstory=(
        "An AI agent specialized in recruitment, known for meticulous analysis "
        "of job descriptions and candidate resumes. It provides objective, "
        "data-driven recommendations to human hiring managers."
    ),
    tools=[analyze_resume_skills, match_job_description],
    verbose=True,              # ✅ MUST be boolean
    llm=llm,
    allow_delegation=False
)


# ---- TASK ----

job_desc = """
Job Title: Data Scientist
Requirements: 5+ years experience, strong Python, SQL, and Machine Learning skills.
Must have excellent communication.
"""

candidate_profile = """
Candidate Name: Alex
Summary: Alex has 3 years of experience in data science, skilled in Python, SQL, and ML.
Holds a Master's degree. Good soft skills.
"""

recommendation_task = Task(
    description=f"""
    Analyze the following Job Description and Candidate Profile:

    Job Description:
    {job_desc}

    Candidate Profile:
    {candidate_profile}

    Use the available tools to first analyze the skills, then match them
    to the job description.

    Your final output MUST be a detailed recommendation report for a human
    hiring manager.

    Include:
    - Match Score (1–10)
    - Strengths
    - Gaps
    - Final hiring recommendation
    """,
    agent=recruiter_agent,
    expected_output=(
        "A detailed hiring recommendation with a match score (1–10) "
        "and clear justification."
    )
)


# ---- CREW ----

crew = Crew(
    agents=[recruiter_agent],
    tasks=[recommendation_task],
    process=Process.sequential,
    verbose=True     # ✅ FIXED (boolean only)
)


# ---- RUN ----

result = crew.kickoff()
print(result)
