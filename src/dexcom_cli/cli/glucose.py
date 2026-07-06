
from dexcom_cli.services.glucose import GlucoseService

from rich.console import Console

console = Console()

def glucose():
    service = GlucoseService()

    reading = service.get_current_glucose()
    
    console.print(f"[bold green]: {reading.value} {reading.unit}")
    console.print(f"Updated at: {reading.timestamp}")