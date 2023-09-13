public class Main {
    public static void main(String[] args) {
        Drill d = new Drill(5, 17, true, 0);
//        d.printDrill();
        try {
            d.runDrill();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}