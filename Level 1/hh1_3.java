package com.company.hh;

/**
 * Created by zobninatn on 06.09.16.
 */

/*
Задача 3

Наименьшее число m, такое, что m! делится без остатка на 10 — это m=5 (5! = 120).
Аналогично, наименьшее число m, такое, что m! делится без остатка на 25 — это m=10.
В общем случае, значение функции s(n) равно наименьшему числу m, такому что m! без
остатка делится на n. Определим функцию S(M, N) = ∑s(n) для всех n ∈ [M, N].
К примеру, S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25. Найдите S(500000000, 510000000).
 */

public class hh1_3 {
    public long exec(long m, long n) {

        long sum = 0;
        for (long i = m; i <= n; i++) {
            sum += findDiv(i);
        }
        return sum;
    }

    private long findDiv(long k) {
        for (long i = 0; i <= k; i++) {
            if (factorial(i) % k == 0) {
                return i;
            }
        }
        return k;
    }

    private long factorial(long k) {
        int y = 1;
        for (int i = 1; i <= k; i++){
            y = y * i;
        }
        return y;
    }
}
