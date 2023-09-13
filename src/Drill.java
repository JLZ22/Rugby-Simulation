import java.util.*;
public class Drill {
    private int currLine;
    private boolean goingRight;
    private int numPlayers;
    private int numLines;
    private final ArrayList<LinkedList<Player>> lines = new ArrayList<>();

    /**
     * Constructor
     * @param numLines > 1
     * @param numPlayer >= numLines
     * @param goingRight Direction the ball is going
     * @param startingLine < numLines
     */
    public Drill(int numLines, int numPlayer, boolean goingRight, int startingLine) {
        this.numLines = numLines;
        this.numPlayers = numPlayers;
        this.goingRight = goingRight;
        currLine = startingLine;
        buildLines();
    }

    /**
     * Runs drill where players pass the ball numPlayer
     * number of times. (eventually until every player
     * goes through every line)
     */
    public void runDrill() throws InterruptedException {
        int temp = numPlayers;
        while (numPlayers!=0) {
            try {
                passBall();
            } catch (NoBallException e) {
                e.printStackTrace();
            }
            Thread.sleep(100);
            printDrill();
        }
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
        lines.get(0).getFirst().setHasBall(true);
    }

    /**
     * Passes the ball from the first player of one line to
     * the first player of the adjacent line in the given direction.
     * If there are no more lines in the given direction, switch
     * the direction.
     *
     * @throws NoBallException
     */
    public void passBall() throws NoBallException{
        if (!lines.get(currLine).getFirst().hasBall())
            throw new NoBallException();
        LinkedList<Player> curr = lines.get(currLine);
        LinkedList<Player> next;
        if (goingRight) {
            if (currLine+1 == lines.size()) {
                flipDirection();
                passBall();
            }
            next = lines.get(currLine+1);
        } else {
            if (currLine == 0) {
                flipDirection();
                passBall();
            }
            next = lines.get(currLine-1);
        }
        next.add(curr.remove());
        next.getFirst().setHasBall(true);
    }

    public void flipDirection() {
        goingRight = !goingRight;
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
