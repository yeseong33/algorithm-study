package 투포인터;

import java.io.*;
import java.util.*;

public class 소수의연속합 {

    int n, count = 0;
    List<Integer> primes;

    public static void main(String[] args) throws IOException {
        new 소수의연속합().solve();
    }

    void solve() throws IOException {

        makeSettings();

        if (n != 1) {
            makePrime();
            counting();
        }

        System.out.println(count);

    }

    private void counting() {

        int left = 0;
        int right = 0;
        long total = primes.get(left);

        while (right < primes.size() - 1 && primes.get(left) <= n) {
            if (total < n) {
                right++;
                total += primes.get(right);
            } else if (total > n) {
                total -= primes.get(left);
                left++;
            } else {
                count++;
                right++;
                total += primes.get(right);
            }
        }

    }

    private void makePrime() {
        boolean[] numbers = new boolean[n + 1];
        numbers[0] = true;
        numbers[1] = true;
        for (int i = 2; i < Math.sqrt(n) + 1; i++) {
            if (!numbers[i]) {
                for (int j = i * 2; j <= n; j += i) {
                    numbers[j] = true;
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            if (!numbers[i]) {
                primes.add(i);
            }
        }
        primes.add(0);
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        primes = new ArrayList<>();
    }
}
