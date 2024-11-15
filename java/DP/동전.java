package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.StringTokenizer;

public class 동전 {

    int n, coinTypeNum, value;
    BufferedReader br;
    StringTokenizer st;
    List<Integer> coinType, dp;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        coinType = new ArrayList<>();
        dp = new ArrayList<>();

    }

    private void counting() throws IOException {
        coinTypeNum = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        value = Integer.parseInt(br.readLine());
        IntStream.range(0, coinTypeNum)
                .forEach(i -> {
                    coinType.add(Integer.parseInt(st.nextToken()));
                });
        dp.add(1);
        IntStream.range(1, value + 1)
                .forEach(i -> dp.add(0));
        coinType.forEach(this::writeDp);
        System.out.println(dp.get(dp.size() - 1));
        coinType.clear();
        dp.clear();
    }

    private void writeDp(Integer coin) {
        IntStream.range(coin, value + 1)
                .forEach(i -> {
                    dp.set(i, dp.get(i) + dp.get(i - coin));
                });
    }

    void solve() throws IOException {
        makeSettings();
        IntStream.range(0, n)
                .forEach(i -> {
                    try {
                        counting();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                });
    }


    public static void main(String[] args) throws IOException {
        new 동전().solve();
    }
}
