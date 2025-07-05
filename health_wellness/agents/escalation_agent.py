from agents import Agent

escalation_agent = Agent(
    name="EscalationAgent",
    instructions="""
        You are an escalation agent that connects the user to a human trainer.
        Politely inform the user that a real coach will follow up soon.
    """
)
