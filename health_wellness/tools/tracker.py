from agents import function_tool
from pydantic import BaseModel
from datetime import datetime

class ProgressInput(BaseModel):
    update: str

class ProgressOutput(BaseModel):
    status: str

@function_tool(name_override="ProgressTrackerTool")
async def track_progress(input: ProgressInput, context) -> ProgressOutput:
    """Log and store user progress updates."""
    entry = {"timestamp": datetime.utcnow().isoformat(), "note": input.update}
    context.progress_logs.append(entry)
    return ProgressOutput(status="Progress updated ✅")
