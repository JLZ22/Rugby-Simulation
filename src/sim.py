from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer
from time import sleep
from param_input import SimulationParameterInput
from field import Field, Player
        
class RugbySimulator(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("r", "run_sim", "Run"),
        ("-","decrease_speed","Slower"),
        ("+","increase_speed","Faster"),
        ("shift+space","pause_or_resume","Pause/Resume"),
        ("s", "stop", "Stop"),
        ("d", "toggle_dark", "Dark mode"), # inherited from App
        ("q", "quit", "Quit"), # inherited from App
        ]
    
    CSS_PATH = "sim.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield SimulationParameterInput()
        yield ScrollableContainer(Field(num_lines=0, num_players=0))
        yield Footer()

    def action_run_sim(self):
        """Run the simulation."""
        
    def action_increase_speed(self):
        """Increase the speed of the simulation."""
    
    def action_decrease_speed(self):
        """Decrease the speed of the simulation."""
    
    def action_pause_or_resume(self):
        """Pause the simulation."""

    def action_stop(self):
        """Stop the simulation."""

if __name__ == "__main__":
    app = RugbySimulator()
    app.run()