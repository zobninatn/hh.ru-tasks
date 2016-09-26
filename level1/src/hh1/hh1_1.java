package hh1;
import java.util.Arrays;

/**
 * Created by zobninatn on 11.09.16.
 */

/*
Задача 1

Число 125874 и результат умножения его на 2 — 251748 можно получить друг из друга перестановкой цифр.
Найдите наименьшее положительное натуральное x такое, что числа 2*x, 3*x можно получить друг из друга перестановкой цифр.
 */

public class hh1_1 {

    public int exec() {
        for (int i = 1; i < 100000; i++) {
            String x2 = Integer.toString(i*2);
            String x3 = Integer.toString(i*3);

            char[] x2Char = x2.toCharArray();
            char[] x3Char = x3.toCharArray();

            Arrays.sort(x2Char);
            Arrays.sort(x3Char);

            if (Arrays.equals(x2Char, x3Char)) {
                return i;
            }
        }
        return 0;
    }
}
