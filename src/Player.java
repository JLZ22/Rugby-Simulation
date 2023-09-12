public class Player {
    private boolean hasBall;

    public boolean isHasBall() {
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