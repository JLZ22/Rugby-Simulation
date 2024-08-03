from textual.widgets import Static
from textual.containers import Center, Vertical
from textual.app import RenderResult, ComposeResult
from textual.reactive import Reactive

class Tile(Static):
    text = Reactive("🏃")
    EMPTY = 0
    PLAYER = 1
    BALL = 2
    BALL_CARRIER = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, expand=True, **kwargs)

    def render(self) -> RenderResult:
        # 🏃 🏉
        return self.text

    def set_state(self, state: int):
        assert state >= 0 and state <= 3, 'Must be a number between 0 and 3 inclusive. Use class constants.'
        if state == self.EMPTY:
            self.text = ''
        elif state == self.PLAYER:
            self.text = '🏃'
        elif state == self.BALL:
            self.text = '🏉'
        elif state == self.BALL_CARRIER:
            self.text = '🏃🏉'
    
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
            [Tile(id=id) 
             for id in self.player_ids])
    
class Field(Static):
    '''
    Uses a grid to represent the playing field. The grid will have 
    num_lines columns and num_lines // num_players + 2 rows
    TODO: Change from making each player a widget, maintain an array and update a grid
    '''

    def __init__(self, num_lines: int, num_players: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_lines = num_lines
        self.num_players = num_players
        self.ball_carrier = 'tile_0'

    def compose(self) -> ComposeResult:
        yield Center(id='display_space')

    async def on_mount(self):
        center_container = self.query_one('#display_space', Center)
        if center_container is None:
            return

        # Display the field of players
        await center_container.mount_all(self.init_lines())

        self.query_one('#tile_0', Tile).set_state(Tile.BALL_CARRIER)

    def init_lines(self):
        '''
        Build an array of lines with num_players/num_lines players per line. 
        Assigns one remainder player to each line until no more remainders. 
        Adds empty columns to simulate space. 
        '''
        to_mount = []
        num_players_created = 0
        remainder = self.num_players % self.num_lines
        players_per_line = self.num_players // self.num_lines
        for i in range(self.num_lines):

            # add line to the field
            to_mount.append(
                Line(line_number=i, 
                    player_ids=self.init_players(num_players_created, remainder),
                    id=f'line_{i}',
                    classes='column'))
            
            # update the remainder 
            remainder-=1
            
            # update the number of players created
            num_players_created += players_per_line
            
            # add empty space between lines unless it's the last line
            if i != self.num_lines - 1:
                to_mount.extend([Vertical(classes='column') for _ in range(3)])

        return to_mount
    
    def init_players(self, num_players_created, remainder):
        '''
        Create an array of tiles representing one line
        '''
        tile_ids = []
        players_per_line = self.num_players // self.num_lines
        for p in range(num_players_created, 
                        num_players_created + 
                        players_per_line + 
                        (1 if remainder > 0 else 0)):
            tile_ids.append(f'tile_{p}')
        return tile_ids