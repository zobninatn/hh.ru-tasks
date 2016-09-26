import hh1.*;

public class Main {

    public static void main(String[] args) {
        System.out.println("- - - - - - - - - - - - - - -");
        hh1_1 hh1 = new hh1_1();
        int result6 = hh1.exec();
        System.out.println("Task 1 value is " + result6);

        System.out.println("- - - - - - - - - - - - - - -");
        hh1_2 hh2 = new hh1_2();
        int result2 = hh2.exec();
        System.out.println("Task 2 value is " + result2);

        System.out.println("- - - - - - - - - - - - - - -");
        hh1_3 hh3 = new hh1_3();
        long result3 = hh3.exec(500000000, 510000000);
        System.out.println("Task 3 value is " + result3);

        System.out.println("- - - - - - - - - - - - - - -");
        hh1_4 hh4 = new hh1_4();
        int result4 = hh4.exec(1, 4600000);
        System.out.println("Task 4 value is " + result4);

        System.out.println("- - - - - - - - - - - - - - -");
        hh1_5 hh5 = new hh1_5();
        int result5 = hh5.exec();
        System.out.println("Task 5 value is " + result5);

    }
}
