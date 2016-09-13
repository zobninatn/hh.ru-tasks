package com.company.hh;

import java.util.Arrays;

/**
 * Created by zobninatn on 06.09.16.
 */

/*
Задача 4

В некоторых числах можно найти последовательности цифр, которые в сумме дают 10.
К примеру, в числе 3523014 целых четыре таких последовательности:
352 3014
3 523 014
3 5230 14
35 23014

Можно найти и такие замечательные числа, каждая цифра которых входит в по крайней мере одну такую
последовательность. Например, 3523014 является замечательным числом, а 28546 — нет (в нём нет
последовательности цифр, дающей в сумме 10 и при этом включающей 5).

Найдите количество этих замечательных чисел в интервале [1, 4600000] (обе границы — включительно).
 */

public class hh1_4 {
    public int exec(int a, int b) {
        int count = 0;
        for (int i = a; i <= b; i++) {
            String var = Integer.toString(i);
            int[] controlArray = new int[var.length()];
            Arrays.fill(controlArray, 0);

            for (int n = 0; n <= var.length(); n++) {
                for (int m = n; m <= var.length(); m++) {
                    String slice = var.substring(n, m);
                    if (verify(slice)) {
                        for (int z = n; z < m; z++) {
                            controlArray[z] = 1;
                        }
                    }
                }
            }
            int buffer = 0;
            for (int k: controlArray) {
                buffer += k;
            }
            if (buffer == var.length()) {
                count += 1;
            }
        }
        return count;
    }

    private boolean verify(String slice) {
        char[] charSlice = slice.toCharArray();
        int buffer = 0;
        for (char k: charSlice) {
            int intChar = Integer.parseInt(String.valueOf(k));
            buffer += intChar;
        }
        if (buffer == 10) {
            return true;
        } else {
            return false;
        }
    }
}
