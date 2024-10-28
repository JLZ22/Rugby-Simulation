from Drill import Drill
import utils

if __name__ == "__main__":
    num_iterations = 1000    
    save = ""

    for num_lines in range(2, 101):
        contains_success = False
        player_range = range(num_lines + 1, num_lines * 10 + 1)
        txt = f'{num_lines} lines | {num_iterations:,} iterations' + '-' * 25 + '\n'
        save += txt
        print(txt, end="")
        for num_players in player_range:
            drill = Drill(num_lines, num_players)
            r = drill.run(num_iterations, verbose=False)
            del drill 

            if not r:
                contains_success = True
                txt = f"No oscillations for {num_players:>3} players.\n"
                save += txt
                utils.printGreen(txt, end="")
        
        if not contains_success:
            txt = f"No successful runs for {num_lines:>3} lines over following range of players: {player_range}.\n"
            save += utils.formatRed(f"No successful runs for {num_lines:>3} lines over following range of players: {player_range}.\n")
            utils.printRed(txt, end="")

    from pathlib import Path

    with open(Path(f"results/Lines-{num_lines}_Players-{num_players}_Iterations-{num_iterations}.txt"), "w") as f:
        f.write(save)