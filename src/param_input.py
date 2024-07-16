from textual import on
from textual.app import ComposeResult
from textual.widgets import Static, Label, Input, Pretty
from textual.validation import Number, Function

class SimulationParameterInput(Static):
    def __init__(self):
        super().__init__()
        self.players = 5
        self.lines = 4
        self.iterations = 10

    def compose(self) -> ComposeResult:
        yield Label("Enter the number of players (pos int): ")
        yield Input(type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Number(minimum=2)
                    ],
                    id="players")
        
        yield Label("Enter the number of lines (less than num players): ")
        yield Input(type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Function(self.validate_lines, "Number of lines must be less than number of players")
                    ],
                    id="lines")
        
        yield Label("Enter the number of iterations (pos int): ")
        yield Input(type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Number(minimum=1)
                    ],
                    id="iterations")
        
        yield Pretty("Players: 5, Lines: 4, Iterations: 10", id="vals")
        
    @on(Input.Changed, "#players")
    def set_players(self, event: Input.Changed):
        try:
            val = int(event.value)
        except ValueError:
            return
        self.players = val
        
    @on(Input.Changed, "#lines")
    def set_lines(self, event: Input.Changed):
        try:
            val = int(event.value)
        except ValueError:
            return
        self.lines = val
        
    @on(Input.Changed, "#iterations")
    def set_iterations(self, event: Input.Changed):
        try:
            val = int(event.value)
        except ValueError:
            return
        self.iterations = val

    @on(Input.Changed)
    def show_vals(self, event: Input.Changed):
        self.query_one("#vals", Pretty).update(f"Players: {self.players}, Lines: {self.lines}, Iterations: {self.iterations}")

    def validate_lines(self, value: str) -> bool:
        try:
            return int(value) < self.players
        except ValueError:
            return False