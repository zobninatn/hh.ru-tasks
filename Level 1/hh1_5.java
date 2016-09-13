package com.company.hh;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by zobninatn on 07.09.16.
 */

/*
Рассмотрим все возможные числа a**b для 1<a<6 и 1<b<6:
2**2=4, 2**3=8, 2**4=16, 2**5=32 3**2=9, 3**3=27, 3**4=81, 3**5=243 4**2=16,
 4**3=64, 4**4=256, 4**5=1024, 5**2=25, 5**3=125, 5**4=625, 5**5=3125
Если убрать повторения, то получим 15 различных чисел.
Сколько различных чисел a**b для 2<a<114 и 2<b<131?
 */

public class hh1_5 {
    public int exec() {
        List<Double> container = new ArrayList<>();
        List<Double> sortedContainer = new ArrayList<>();

        for (double n = 3; n < 114; n++) {
            for (double m = 3; m < 131; m++) {
                container.add(Math.pow(n, m));
            }
        }

        for (Double i: container) {
            if (!sortedContainer.contains(i)) {
                sortedContainer.add(i);
            }
        }
        return sortedContainer.size();
    }
}
