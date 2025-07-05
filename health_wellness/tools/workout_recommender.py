from agents import function_tool
from pydantic import BaseModel
from typing import List

class WorkoutPlanInput(BaseModel):
    experience_level: str

class WorkoutPlanOutput(BaseModel):
    exercises: List[str]

@function_tool(name_override="WorkoutRecommenderTool")
async def workout_recommender(input: WorkoutPlanInput, context) -> WorkoutPlanOutput:
    """Generate a weekly workout plan based on experience_level."""
    level = input.experience_level.lower()
    plan = [f"{level.title()} Workout Day {i+1}" for i in range(5)]
    context.workout_plan = {"level": level, "plan": plan}
    return WorkoutPlanOutput(exercises=plan)
