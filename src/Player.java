public class Player {
    private boolean hasBall;
    private boolean running;

    public boolean isRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    public boolean hasBall() {
        return hasBall;
    }

    public void setHasBall(boolean hasBall) {
        this.hasBall = hasBall;
    }

    public Player(boolean hasBall) {
        this.hasBall = hasBall;
    }

    public Player() {
        this(false);
    }
}