from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer
from time import sleep
from param_input import SimulationParameterInput
        
class RugbySimulator(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"), # inherited from App
        ("q", "quit", "Quit the app"), # inherited from App
        ("r", "run_sim", "Run the simulation"),
        ("(","decrease_speed","Decrease the speed of simulation"),
        (")","increase_speed","Increase the speed of simulation"),
        ("shift+space","pause","Pause the simulation"),
        ("shift+enter","resume","Resume the simulation"),
        ("s", "stop", "Stop the simulation"),
        ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(SimulationParameterInput())

    def action_run_sim(self):
        """Run the simulation."""
        
    def action_increase_speed(self):
        """Increase the speed of the simulation."""
    
    def action_decrease_speed(self):
        """Decrease the speed of the simulation."""
    
    def action_pause(self):
        """Pause the simulation."""

    def action_resume(self):
        """Resume the simulation."""

    def action_stop(self):
        """Stop the simulation."""

if __name__ == "__main__":
    app = RugbySimulator()
    app.run()