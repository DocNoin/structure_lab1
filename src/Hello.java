public class Hello {
    public static void main(String[] args) throws Exception {
        cls();
        System.out.println("Hello, World!");
    }

    public static void cls() {
        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        }
        catch(Exception e) {
            System.out.println("Exception");
        }
    }
}
