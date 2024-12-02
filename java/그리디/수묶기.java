package 그리디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class 수묶기 {
    int total;
    List<Integer> numbers, minus, plus;


    public static void main(String[] args) throws IOException {
        new 수묶기().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        tied();
        System.out.println(total);
    }

    private void tied() {
        for (int i = 1; i < minus.size(); i += 2) {
            total += minus.get(i) * minus.get(i - 1);
        }
        if (minus.size() % 2 == 1) {
            total += minus.get(minus.size() - 1);
        }

        for (int i = 1; i < plus.size(); i += 2) {
            if (plus.get(i) == 1 || plus.get(i - 1) == 1) {
                total += plus.get(i) + plus.get(i - 1);
            } else {
                total += plus.get(i) * plus.get(i - 1);
            }
        }
        if (plus.size() % 2 == 1) {
            total += plus.get(plus.size() - 1);
        }
    }

    private void makeSettings() throws IOException {

        total = 0;

        numbers = new ArrayList<>();
        minus = new ArrayList<>();
        plus = new ArrayList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(br.readLine());
            if (value <= 0) {
                minus.add(value);
            } else {
                plus.add(value);
            }
        }

        minus.sort((a, b) -> Integer.compare(a, b));
        plus.sort((a, b) -> Integer.compare(b, a));

    }
}
