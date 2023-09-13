public class Player {
    private boolean hasBall;

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