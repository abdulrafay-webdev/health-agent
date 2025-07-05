from agents import function_tool
from pydantic import BaseModel

class ScheduleInput(BaseModel):
    day_of_week: str

class ScheduleOutput(BaseModel):
    message: str

@function_tool(name_override="CheckinSchedulerTool")
async def schedule_checkin(input: ScheduleInput, context) -> ScheduleOutput:
    """Schedule weekly check-in reminders."""
    msg = f"Progress check scheduled every {input.day_of_week.title()}."
    return ScheduleOutput(message=msg)
