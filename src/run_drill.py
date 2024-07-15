from Drill import Drill
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run a drill.')
    parser.add_argument('--num-lines', type=int, help='Number of lines', default=3)
    parser.add_argument('--num-players', type=int, help='Number of players', default=9)
    parser.add_argument('--num-passes', type=int, help='Number of passes', default=20)
    args = parser.parse_args()

    drill = Drill(args.num_lines, args.num_players)
    drill.runDrill(args.num_passes)
    drill.printOsicllations()

if __name__ == '__main__':
    main()