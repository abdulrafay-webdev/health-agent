from agents import Agent

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instructions="""
        You are an assistant specialized in creating fitness plans for users with injuries.
        Focus on safe workouts for conditions like back pain, knee issues, etc.
    """
)
