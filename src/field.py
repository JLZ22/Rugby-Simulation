from textual.widgets import Static
from textual.containers import Center, Vertical
from textual.app import RenderResult, ComposeResult
from textual.reactive import Reactive

class Player(Static):
    text = Reactive("🏃")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, expand=True, **kwargs)

    def render(self) -> RenderResult:
        # 🏃‍➡️ 🏃 🏉
        return self.text

    def add_ball(self):
        self.text += '🏉'
    
    def remove_ball(self):
        self.text = self.text[:-1] if len(self.text) > 1 else self.text
    
class Line(Static):
    def __init__(self, line_number: int, 
                 player_ids: list[str], 
                 *args, 
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.line_number = line_number
        self.player_ids = player_ids

    def compose(self) -> ComposeResult:
        yield Vertical(id=f'line_{self.line_number}')

    async def on_mount(self):
        vertical_container = self.query_one(f'#line_{self.line_number}', Vertical)

        await vertical_container.mount_all(
            [Player(id=id) 
             for id in self.player_ids])
    
class Field(Static):

    def __init__(self, num_lines: int, num_players: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_lines = num_lines
        self.num_players = num_players

    def compose(self) -> ComposeResult:
        yield Center(id='display_space')

    async def on_mount(self):
        center_container = self.query_one('#display_space', Center)
        if center_container is None:
            return

        to_mount = []
        num_players_created = 0
        for i in range(self.num_lines):
            if i == 0:
                players_per_line = (self.num_players // self.num_lines + 
                                    self.num_players % self.num_lines)
            else:
                players_per_line = self.num_players // self.num_lines

            # add line to the field
            to_mount.append(
                Line(line_number=i, 
                    player_ids=[f'player_{p}' 
                    for p in range(num_players_created, 
                    num_players_created + players_per_line)],
                    id=f'line_{i}',
                    classes='column'))
            
            # update the number of players created
            num_players_created += players_per_line
            
            # add empty space between lines unless it's the last line
            if i != self.num_lines - 1:
                to_mount.extend([Vertical(classes='column') for _ in range(3)])

        await center_container.mount_all(to_mount)

        self.query_one('#player_0', Player).add_ball()