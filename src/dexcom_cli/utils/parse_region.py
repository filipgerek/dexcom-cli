from rich.console import Console

console = Console()

def parse_region(region: str) -> str:
    if region.lower() == "us":
        return "United States"
    elif region.lower() == "ous":
        return "Outside the United States (Europe, Australia, etc.)"
    elif region.lower() == "jp":
        return "Japan"
    else:
        console.print(f"[bold red]Invalid region: {region}[/]")
        raise ValueError(f"Invalid region: {region}")