import java.util.*;
public class Drill {
    private int numPlayers;
    private int numLines;
    private final ArrayList<LinkedList<Player>> lines = new ArrayList<>();

    public Drill(int numLines, int numPlayers) {
        this.numLines = numLines;
        this.numPlayers = numPlayers;
        buildLines();
    }

    /**
     * Adds the appropriate number of lines and players per line
     * to the global variable, lines.
     */
    public void buildLines() {
        for (int i = 0 ; i < numLines ; i++) {
            lines.add(new LinkedList<>());
        }
        int index = 0;
        int x = numPlayers;
        while (x > 0) {
            if (index == numLines)
                index = 0;
            lines.get(index).add(new Player());
            x--;
            index++;
        }
    }

    public ArrayList<LinkedList<Player>> getLines() {
        return lines;
    }

    public int getNumPlayers() {
        return numPlayers;
    }

    public void setNumPlayers(int numPlayers) {
        this.numPlayers = numPlayers;
    }

    public int getNumLines() {
        return numLines;
    }

    public void setNumLines(int numLines) {
        this.numLines = numLines;
    }
}
