package 그리디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 주식 {

    int testCount, n;
    long[] maxis;
    BufferedReader br;
    List<Long> numbers;

    public static void main(String[] args) throws IOException {
        new 주식().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < testCount; i++) {
            makeStockSettings();
            stock();
        }
    }

    private void stock() {
        long maxValue = 0;

        for (int i = numbers.size() - 1; i >= 0; i--) {
            if (numbers.get(i) > maxValue) {
                maxValue = numbers.get(i);
            }
            maxis[i] = maxValue;
        }

        long total = 0;
        for (int i = 0; i < numbers.size(); i++) {
            total += maxis[i] - numbers.get(i);
        }
        System.out.println(total);
    }

    private void makeStockSettings() throws IOException {
        numbers = new ArrayList<>();

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers.add(Long.parseLong(st.nextToken()));
        }
        maxis = new long[n];
    }

    private void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        testCount = Integer.parseInt(br.readLine());
    }
}
