from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Center, Vertical, ScrollableContainer
from textual.app import RenderResult, ComposeResult

class Player(Static):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, expand=True, **kwargs)

    def render(self) -> RenderResult:
        # 🏃‍➡️ 🏃 🏉
        return "🏃"
    
class Line(Static):
    def __init__(self, line_number: int, num_players: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line_number = line_number
        self.num_players = num_players
        self.line_id = ('line_' + str(self.line_number) if num_players > 0 
                        else 'space_' + str(self.line_number))

    def compose(self) -> ComposeResult:
        yield Vertical(id=self.line_id)

    async def on_mount(self):
        vertical_container = self.query_one(f'#{self.line_id}', Vertical)
        await vertical_container.mount_all([Player() for _ in range(self.num_players)])
    
class Field(Static):
    def __init__(self, num_lines: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_lines = num_lines

    def compose(self) -> ComposeResult:
        yield Center(id='display_space')

    async def on_mount(self):
        center_container = self.query_one('#display_space', Center)

        to_mount = []
        for i in range(self.num_lines):
            to_mount.append(Line(line_number=i, num_players=7))
            if i != self.num_lines - 1:
                to_mount.append(Line(line_number=i, num_players=0))

        await center_container.mount_all(to_mount)