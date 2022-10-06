public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        number();
        hello(args[1]);
        goodbye(args[0]);
    }
    public static void number () {
        int firstNumber;
        firstNumber = 5;
        System.out.println(firstNumber);
    }

    public static void hello (String hello) {
        System.out.println("I SAID " + hello);
    }

    public static void goodbye (String bye) {
        System.out.println(bye);
    }

    public static void calculate (String calc1, String calc2) {
        Integer.parseInt(calc1);
        Integer.parseInt(calc2);
        System.out.println(calc1 + calc2);

    }

}
