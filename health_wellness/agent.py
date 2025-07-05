from agents import Agent
from tools.goal_analyzer import goal_analyzer as GoalAnalyzerTool
from tools.meal_planner import meal_planner as MealPlannerTool
from tools.workout_recommender import workout_recommender as WorkoutRecommenderTool
from tools.scheduler import schedule_checkin as CheckinSchedulerTool
from tools.tracker import track_progress as ProgressTrackerTool

# Specialized agents
from agents.injury_support_agent import injury_support_agent
from agents.nutrition_expert_agent import nutrition_expert_agent
from agents.escalation_agent import escalation_agent


wellness_agent = Agent(
    name="WellnessPlannerAgent",
    instructions="""
        You are a helpful Health & Wellness assistant.
        Your job is to understand user goals, suggest structured health plans,
        track progress, and hand off to other agents when needed.
    """,
    tools=[
        GoalAnalyzerTool,
        MealPlannerTool,
        WorkoutRecommenderTool,
        CheckinSchedulerTool,
        ProgressTrackerTool
    ],
    handoffs={
        "injury_support_agent": injury_support_agent,
        "nutrition_expert_agent": nutrition_expert_agent,
        "escalation_agent": escalation_agent
    }
)
