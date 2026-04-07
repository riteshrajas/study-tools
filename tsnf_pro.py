import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
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
            ],
            "Intermolecular Forces (IMFs)": [
                {"q": "Which IMF is the weakest?", "a": "London Dispersion"},
                {"q": "Which IMF is the strongest?", "a": "ion-dipole"},
                {"q": "What happens to boiling and melting points as IMFs increase?", "a": "increase"},
                {"q": "H-bonds occur between a hydrogen and which three elements (e.g. X, Y, Z)?", "a": "N, O, F", "tip": "Nitrogen, Oxygen, Fluorine (NOF)"}
            ],
            "Kinetics": [
                {"q": "What are the units for the rate constant (k) of a 1st order reaction?", "a": "s-1"},
                {"q": "What is the formula for the half-life of a 1st order process?", "a": "0.693/k", "tip": "t1/2 = 0.693/k"}
            ],
            "General Equilibrium": [
                {"q": "Does a large Keq mean more products or reactants at equilibrium?", "a": "products"},
                {"q": "According to Le Chatelier's Principle, if Q > Keq, which way does the reaction shift?", "a": "left", "tip": "Shifts towards the reactants"}
            ],
            "Acid-Base Equilibrium": [
                {"q": "Do acids donate or accept [H+]?", "a": "donate"},
                {"q": "Is the pH of pure water always 7?", "a": "no", "tip": "Only at 25 degrees Celsius"},
                {"q": "What is the formula for pH?", "a": "-log[H+]"}
            ],
            "Thermodynamics": [
                {"q": "Do thermodynamically favorable reactions have a positive or negative delta G?", "a": "negative"},
                {"q": "What is the value of delta G at equilibrium?", "a": "0"}
            ],
            "Electrochemistry": [
                {"q": "Does oxidation occur at the anode or cathode?", "a": "anode", "tip": "An Ox, Red Cat"},
                {"q": "In a battery, do electrons flow from anode to cathode or cathode to anode?", "a": "anode to cathode"},
                {"q": "In a salt bridge, do cations flow to the anode or cathode?", "a": "cathode"}
            ]
        }
        self.score = 0
        self.total = 0

    def display_welcome(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Panel.fit(
            "[bold cyan]AP Chemistry: 'Thou Shalt Not Forget'[/bold cyan]\n"
            "[yellow]The Official Study Tool for Ritesh Raj[/yellow]",
            border_style="blue",
            padding=(1, 2)
        ))
        console.print("\n[bold]Welcome![/bold] Let's review some key AP Chemistry concepts.\n")

    def run_quiz(self, practice_mode=False):
        categories = list(self.rules.keys())
        random.shuffle(categories)

        total_questions = sum(len(self.rules[c]) for c in categories)
        incorrect_pool = []

        for cat in categories:
            questions = self.rules[cat].copy()
            random.shuffle(questions)
            
            console.print(Panel(f"[bold magenta]{cat}[/bold magenta]", expand=False, border_style="magenta"))
            
            for q_data in questions:
                progress_text = f"[cyan]({self.total + 1}/{total_questions})[/cyan]"
                user_ans = Prompt.ask(f"{progress_text} [white]{q_data['q']}[/white]")
                
                if user_ans.lower() == q_data['a'].lower():
                    console.print("[bold green]✓ Correct![/bold green]\n")
                    self.score += 1
                else:
                    console.print(f"[bold red]✗ Incorrect.[/bold red] Answer: [bold green]{q_data['a']}[/bold green]")
                    if 'tip' in q_data:
                        console.print(f"[italic blue]Hint: {q_data['tip']}[/italic blue]")
                    console.print()
                    if practice_mode:
                        incorrect_pool.append(q_data)
                
                self.total += 1

        if practice_mode and incorrect_pool:
            console.print(Panel("[bold yellow]Practice Mode: Reviewing Incorrect Questions[/bold yellow]", expand=False, border_style="yellow"))

            round_num = 2
            while incorrect_pool:
                console.print(f"\n[bold underline]Practice Round {round_num}[/bold underline]")
                next_pool = []
                random.shuffle(incorrect_pool)

                for i, q_data in enumerate(incorrect_pool):
                    progress_text = f"[yellow](Practice {i + 1}/{len(incorrect_pool)})[/yellow]"
                    user_ans = Prompt.ask(f"{progress_text} [white]{q_data['q']}[/white]")

                    if user_ans.lower() == q_data['a'].lower():
                        console.print("[bold green]✓ Correct![/bold green]\n")
                    else:
                        console.print(f"[bold red]✗ Incorrect.[/bold red] Answer: [bold green]{q_data['a']}[/bold green]")
                        if 'tip' in q_data:
                            console.print(f"[italic blue]Hint: {q_data['tip']}[/italic blue]")
                        console.print()
                        next_pool.append(q_data)

                incorrect_pool = next_pool
                round_num += 1

            console.print("[bold green]All questions mastered![/bold green]\n")

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

    mode = Prompt.ask("[bold cyan]Choose mode[/bold cyan] (1: Standard Quiz, 2: Practice Mode)", choices=["1", "2"], default="1")
    is_practice = (mode == "2")

    app.run_quiz(practice_mode=is_practice)
