public class FibonacciCache {

    public static void main(String[] args) {
        reset();
        store();
        System.out.println(get(200));

    }
    public static long[] fib = new long[20];


    public static void store() {
        fib[0] = 0;
        fib[1] = 1;
        for (int i=2; i<fib.length; i++)
            fib[i] = fib[i-2] + fib[i-1];
    }
    public static void reset() {
        for (int i =0; i<fib.length; i++)
            fib[i] = 0;
    }
    public static int get(int i) {
        int getvariable = -1;
        if (i<fib.length) {
            if (i>-1) {
                getvariable = (int) fib[i];
            }
        }
        return getvariable;
    }

}
