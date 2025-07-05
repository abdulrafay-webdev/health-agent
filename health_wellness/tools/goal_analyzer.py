from agents import function_tool
from pydantic import BaseModel
import re

class GoalInput(BaseModel):
    raw_input: str

class GoalOutput(BaseModel):
    quantity: float
    metric: str
    duration: str

@function_tool(name_override="GoalAnalyzerTool")
async def goal_analyzer(input: GoalInput, context) -> GoalOutput:
    """
    Analyze user goals like 'lose 5kg in 2 months'.
    """
    text = input.raw_input.lower()
    pattern = r"(\d+(\.\d+)?)\s*(kg|pounds|lbs)\s*(in|within)\s*(\d+\s*(days?|weeks?|months?))"
    match = re.search(pattern, text)
    if not match:
        raise ValueError("Invalid format. Try: 'lose 5kg in 2 months'.")
    quantity = float(match.group(1))
    metric = match.group(3)
    duration = match.group(5)
    context.goal = {"quantity": quantity, "metric": metric, "duration": duration}
    return GoalOutput(quantity=quantity, metric=metric, duration=duration)
