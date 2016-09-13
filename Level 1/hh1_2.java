package com.company.hh;

import java.util.ArrayList;

/**
 * Created by zobninatn on 06.09.16.
 */

/*
Задача 2

Рассмотрим спираль, в которой, начиная с 1 в центре, последовательно расставим числа по часовой стрелке,
пока не получится спираль 5 на 5

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
Можно проверить, что сумма всех чисел на диагоналях равна 101.

Чему будет равна сумма чисел на диагоналях, для спирали размером 1195 на 1195?
 */

public class hh1_2 {
    public int exec() {
        int sum = 1;
        int position = 0;
        int step = 2;
        int fieldSize = 1195 * 1195;
        int[] field = new int[fieldSize];

        for (int i = 0; i < fieldSize; i++) {
            field[i] = i + 1;
        }

        while (position < fieldSize - 1) {
            sum = sum + field[position + 1 * step] + field[position + 2 * step] +
                    field[position + 3 * step] + field[position + 4 * step];

            position += step * 4;
            step += 2;
        }
        return sum;
    }
}
