from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def display_reduced_form(equation_str: str):
    """ Display the reduced form of the equation
        as it is MANDATORY """
    
    console = Console()
    text = Text("Reduced form: ", style="bold cyan")
    text.append(equation_str, style="yellow")
    console.print(text)


def display_polynomial_degree(degree: int):
    """ Display the polynomial degree """
    
    console = Console()
    text = Text("Polynomial degree: ", style="bold cyan")
    text.append(str(degree), style="yellow")
    console.print(text)


def display_discriminant(delta: float):
    """ Display the discriminant with a proper Delta character """
    
    console = Console()
    text = Text("Δ = ", style="bold cyan")
    
    # Add value with appropriate color based on sign
    if delta > 0:
        text.append(str(delta), style="green")
        console.print(text)
        console.print("Discriminant is [bold green]positive[/], the equation has [bold]two distinct real solutions[/].")
    elif delta == 0:
        text.append(str(delta), style="yellow")
        console.print(text)
        console.print("Discriminant is [bold yellow]zero[/], the equation has [bold]one real solution[/] (a double root).")
    else:
        text.append(str(delta), style="red")
        console.print(text)
        console.print("Discriminant is [bold red]negative[/], the equation has [bold]two complex solutions[/].")


def display_str(str_value: str):
    """ Display a simple string """
    
    console = Console()
    console.print(str_value)


def display_solution(solutions: any):
    """ Display the solution(s) to the equation """
    
    console = Console()
    panel = Panel(
        title="Solution(s)",
        renderable=format_solutions(solutions),
        border_style="green"
    )
    console.print(panel)


def format_solutions(solutions):
    """ Format the solutions for display """

    if solutions is None:
        return Text("No solution", style="red")
    
    if isinstance(solutions, str):
        # Special case for all real numbers being solutions
        if "All real numbers" in solutions:
            return Text(solutions, style="green")
        return Text(solutions, style="yellow")
    
    if isinstance(solutions, (int, float)):
        return Text(f"The solution is: {solutions}", style="yellow")
    
    if isinstance(solutions, list):
        if len(solutions) == 0:
            return Text("No solution", style="red")
        
        if len(solutions) == 1:
            return Text(f"The solution is: {solutions[0]}", style="yellow")
        
        text = Text("The solutions are:", style="yellow")
        for i, sol in enumerate(solutions):
            if isinstance(sol, complex):
                real_part = sol.real
                imag_part = abs(sol.imag)
                if sol.imag >= 0:
                    text.append(f"\nx{i+1} = {real_part} + {imag_part}i", style="yellow")
                else:
                    text.append(f"\nx{i+1} = {real_part} - {imag_part}i", style="yellow")
            else:
                text.append(f"\nx{i+1} = {sol}", style="yellow")
        return text
    
    return Text(str(solutions), style="yellow")