from agents import function_tool
from pydantic import BaseModel
from typing import List

class MealPlanInput(BaseModel):
    diet_type: str

class MealPlanOutput(BaseModel):
    meals: List[str]

@function_tool(name_override="MealPlannerTool")
async def meal_planner(input: MealPlanInput, context) -> MealPlanOutput:
    """
    Suggest a 7-day meal plan based on diet_type.
    """
    diet = input.diet_type.lower()
    plan = [f"{diet.title()} Meal Day {i+1}" for i in range(7)]
    context.meal_plan = plan
    context.diet_preferences = diet
    return MealPlanOutput(meals=plan)
