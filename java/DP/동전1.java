package DP;


import java.io.BufferedReader;
import java.io.Console;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class 동전1 {


    Integer n, k;
    List<Integer> coinType, dp;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        coinType = new ArrayList<>();

        IntStream.range(0, n)
                .forEach(i -> {
                    try {
                        coinType.add(Integer.parseInt(br.readLine()));
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                });

        dp = new ArrayList<>();
        dp.add(1);

        IntStream.range(1, k + 1)
                .forEach(i -> dp.add(0));
    }


    public void solve() throws IOException {
        makeSettings();
        coinType.forEach(this::counting);
        System.out.println(dp.get(dp.size() - 1));
    }

    private void counting(Integer coin) {
        IntStream.range(coin, k + 1)
                .forEach(i -> {
                    dp.set(i, dp.get(i) + dp.get(i - coin));
                });

    }


    public static void main(String[] args) throws IOException {
        new 동전1().solve();
    }


}
