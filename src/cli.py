"""
Command-line interface for the fact checker
"""

import sys
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich.markdown import Markdown
from src.simple_model import SimpleFactChecker


class FactCheckerCLI:
    """Interactive CLI for fact verification"""
    
    def __init__(self):
        self.console = Console()
        self.fact_checker: Optional[FactChecker] = None
    
    def display_welcome(self):
        """Display welcome message"""
        welcome_text = """
# 🔍 Journalism Fact Verification System

Welcome to the AI-powered fact checker! This tool helps verify factual claims
using advanced language models.

Enter any factual claim, and the system will analyze its accuracy.
        """
        self.console.print(Panel(Markdown(welcome_text), border_style="cyan", box=box.DOUBLE))
    
    def setup_provider(self):
        """Setup the ML model"""
        self.console.print("\n[bold cyan]Loading trained fact-checking model...[/bold cyan]")
        
        try:
            self.fact_checker = SimpleFactChecker()
            self.console.print(f"✓ [green]Model loaded successfully![/green]\n")
        except Exception as e:
            self.console.print(f"[red]Error loading model: {e}[/red]")
            sys.exit(1)
    
    def display_result(self, result: dict, claim: str):
        """Display the verification result in a formatted way"""
        # Determine color based on verdict
        verdict = result["verdict"]
        if verdict == "TRUE":
            verdict_color = "green"
            emoji = "✓"
        elif verdict == "FALSE":
            verdict_color = "red"
            emoji = "✗"
        elif verdict == "PARTIALLY_TRUE":
            verdict_color = "yellow"
            emoji = "⚠"
        elif verdict == "ERROR":
            verdict_color = "red"
            emoji = "⚠"
        else:  # UNVERIFIABLE
            verdict_color = "blue"
            emoji = "?"
        
        # Create result table
        table = Table(show_header=False, box=box.ROUNDED, border_style=verdict_color)
        table.add_column("Field", style="bold cyan", width=15)
        table.add_column("Value", style="white")
        
        table.add_row("Claim", claim)
        table.add_row("Verdict", f"[{verdict_color}]{emoji} {verdict}[/{verdict_color}]")
        table.add_row("Confidence", f"{result['confidence']}%")
        table.add_row("Explanation", result['explanation'])
        
        if result.get('sources'):
            sources_text = "\n• " + "\n• ".join(result['sources'])
            table.add_row("Key Areas", sources_text)
        
        self.console.print("\n")
        self.console.print(Panel(table, title="[bold]Verification Result[/bold]", border_style=verdict_color))
    
    def run(self):
        """Main CLI loop"""
        self.display_welcome()
        self.setup_provider()
        
        while True:
            self.console.print("\n" + "="*60 + "\n")
            
            # Get claim from user
            claim = Prompt.ask("[bold cyan]Enter a factual claim to verify[/bold cyan]")
            
            if not claim.strip():
                self.console.print("[yellow]Please enter a valid claim.[/yellow]")
                continue
            
            # Show processing message
            with self.console.status("[bold green]Verifying claim...", spinner="dots"):
                result = self.fact_checker.verify_fact(claim)
            
            # Display result
            self.display_result(result, claim)
            
            # Ask if user wants to continue
            self.console.print("\n")
            if not Confirm.ask("[bold cyan]Check another fact?[/bold cyan]", default=True):
                self.console.print("\n[bold green]Thank you for using the Fact Checker! Stay informed! 📰[/bold green]\n")
                break


def main():
    """Entry point for the CLI"""
    try:
        cli = FactCheckerCLI()
        cli.run()
    except KeyboardInterrupt:
        console = Console()
        console.print("\n\n[yellow]Fact checking session ended.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console = Console()
        console.print(f"\n[red]Unexpected error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
