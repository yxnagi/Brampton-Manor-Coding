public class Lesson2 {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        yesloop();
        carloop();
        DayProgram();
        DayProgramCase();
        arrayerror();
    }

    public static void yesloop () {
        for (int i = 0; i < 5; i++) {
            System.out.println("yes");
        }
    }

    public static void carloop () {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String each : cars) {
            System.out.println(each);
        }
    }

    public static void DayProgram () {
        int day = 2;
        if (day == 6) {
            System.out.println("Today is saturday");
            }
        else if (day == 7) {
            System.out.println("Today is sunday");
            }
        else {
            System.out.println("looking forward to the weekend");
            }
        }

    public static void DayProgramCase() {
        int day = 6;
        switch (day) {
            case 6:
                System.out.println("Today is saturday");
                break;
            case 7:
                System.out.println("Today is sunday");
                break;
            default:
                System.out.println("looking forward to the weekend");
        }
    }

    public static void arrayerror() {
        int[] MyNumbers = {1, 2, 3};
        try {
            System.out.println(MyNumbers[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("The 10th element in the array does not exist! " + e);
        }
    }
}

