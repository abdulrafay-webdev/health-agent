import os
import asyncio
from dotenv import load_dotenv
# from agents import Runner
from agents import Runner
from agent import wellness_agent
from context import UserSessionContext

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment")

async def main():
    context = UserSessionContext(
        name="Abdulrafay",
        uid=1,
        goal=None,
        diet_preferences=None,
        workout_plan=None,
        meal_plan=[],
        injury_notes=None,
        handoff_logs=[],
        progress_logs=[]
    )

    print("\n💬 Type your health goal (e.g., 'I want to lose 5kg in 2 months'):")
    user_input = input("👉 ")

    runner = Runner(api_key=api_key)
    result = await runner.run(wellness_agent, user_input, context=context)
    print("\n🧠 Agent Response:")
    print(result.final_output)

asyncio.run(main())
