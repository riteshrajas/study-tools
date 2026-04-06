import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress

console = Console()

class TSNFApp:
    def __init__(self):
        self.rules = {
            "Solubility": [
                {"q": "Are Group 1 elements soluble?", "a": "yes", "tip": "Li, Na, K, Rb, Cs, Fr"},
                {"q": "Are Nitrates (NO3-) soluble?", "a": "yes", "tip": "Always soluble!"},
                {"q": "Are Ammonium (NH4+) salts soluble?", "a": "yes", "tip": "Always soluble!"},
                {"q": "Is AgCl soluble?", "a": "no", "tip": "Silver chloride is a classic precipitate."},
                {"q": "Is BaSO4 soluble?", "a": "no", "tip": "Sulfate of Barium is a white solid."}
            ],
            "Strong Acids/Bases": [
                {"q": "Is HCl a strong acid?", "a": "yes"},
                {"q": "Is HF a strong acid?", "a": "no", "tip": "HF is weak due to strong H-F bond."},
                {"q": "Is NaOH a strong base?", "a": "yes", "tip": "Group 1 hydroxides are strong."},
                {"q": "Is Ca(OH)2 a strong base?", "a": "yes", "tip": "Group 2 hydroxides are strong bases."}
            ],
            "Flame Colors": [
                {"q": "Flame color for Lithium (Li+)?", "a": "crimson"},
                {"q": "Flame color for Sodium (Na+)?", "a": "yellow"},
                {"q": "Flame color for Potassium (K+)?", "a": "violet"},
                {"q": "Flame color for Copper (Cu2+)?", "a": "blue-green"}
            ],
            "Periodic Trends": [
                {"q": "Electronegativity increases up and to the ____?", "a": "right"},
                {"q": "Atomic radius increases down and to the ____?", "a": "left"}
            ]
        }
        self.score = 0
        self.total = 0

    def display_welcome(self):
        console.print(Panel.fit(
            "[bold cyan]AP Chemistry: 'Thou Shalt Not Forget'[/bold cyan]\n"
            "[yellow]The Official Study Tool for Ritesh Raj[/yellow]",
            border_style="blue"
        ))

    def run_quiz(self):
        categories = list(self.rules.keys())
        random.shuffle(categories)

        for cat in categories:
            questions = self.rules[cat]
            random.shuffle(questions)
            
            console.print(f"\n[bold magenta]Category: {cat}[/bold magenta]")
            
            for q_data in questions:
                user_ans = Prompt.ask(f"[white]{q_data['q']}[/white]")
                
                if user_ans.lower() == q_data['a'].lower():
                    console.print("[bold green]✓ Correct![/bold green]")
                    self.score += 1
                else:
                    console.print(f"[bold red]✗ Incorrect.[/bold red] Answer: [bold green]{q_data['a']}[/bold green]")
                    if 'tip' in q_data:
                        console.print(f"[italic blue]Hint: {q_data['tip']}[/italic blue]")
                
                self.total += 1

        self.display_summary()

    def display_summary(self):
        table = Table(title="Study Session Summary")
        table.add_column("Stat", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Correct Answers", str(self.score))
        table.add_row("Total Questions", str(self.total))
        table.add_row("Percentage", f"{(self.score/self.total)*100:.1f}%")
        
        console.print("\n")
        console.print(table)
        
        if self.score / self.total >= 0.8:
            console.print("[bold green]🌟 Excellent! You're dominating the basics.[/bold green]")
        else:
            console.print("[bold yellow]📖 Keep practicing. These are the free points![/bold yellow]")

if __name__ == "__main__":
    app = TSNFApp()
    app.display_welcome()
    app.run_quiz()
