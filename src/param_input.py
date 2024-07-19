from textual import on
from textual.app import ComposeResult
from textual.widgets import Static, Label, Input, Pretty
from textual.containers import Center
from textual.validation import Number, Function

class SimulationParameterInput(Static):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.players = 12
        self.lines = 5
        self.iterations = 10

    def compose(self) -> ComposeResult:
        yield Label("Enter the number of players (pos int): ")
        yield Input(value=str(self.players),
                    type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Number(minimum=2)
                    ],
                    id="players")
        
        yield Label("Enter the number of lines (less than num players): ")
        yield Input(value=str(self.lines),
                    type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Function(self.validate_lines, "Number of lines must be less than number of players")
                    ],
                    id="lines")
        
        yield Label("Enter the number of iterations (pos int): ")
        yield Input(value=str(self.iterations),
                    type="integer",
                    placeholder="Enter an integer: ",
                    validators=[
                        Number(minimum=1)
                    ],
                    id="iterations")
        
        yield Center(Static(id="vals"))
        
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
        self.query_one("#vals", Static).update(f"Players: {self.players}\nLines: {self.lines}\nIterations: {self.iterations}")

    def validate_lines(self, value: str) -> bool:
        try:
            return int(value) < self.players
        except ValueError:
            return False