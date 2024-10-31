package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

public class 제곱수의합 {

    int n;
    List<Integer> dp;

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dp = new ArrayList<>();
        dp.add(0);
        dp.add(1);
    }

    void makeSumOf() {

        IntStream.rangeClosed(2, n).forEach(i -> {
            dp.set(i, IntStream.rangeClosed(1, (int) Math.sqrt(i))
                    .map(j -> {
                        int square = j * j;
                        if (square == i) {
                            return 1;
                        } else {
                            return dp.get(i - square) + 1;
                        }
                    })
                    .min()
                    .orElse(100001));
        });

    }

    void solve() throws IOException {
        makeSettings();
        makeSumOf();
        System.out.println(dp.get(n));
    }

    public static void main(String[] args) throws IOException {
        new 제곱수의합().solve();
    }
}
