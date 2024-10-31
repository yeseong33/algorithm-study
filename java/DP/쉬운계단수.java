package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class 쉬운계단수 {

    int n, rest, count;
    List<Deque<Integer>> dps;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dps = new ArrayList<>(10);
        rest = 1000000000;
        count = n - 1;

        // 0~9까지의 Deque 초기화
        IntStream.range(0, 10)
                .forEach(i -> dps.add(new ArrayDeque<>()));

        // 설정 초기화
        dps.get(0).add(0);
        IntStream.range(1, 10).forEach(i -> dps.get(i).add(1));
    }

    void isStairsNum() {
        if (count == 0) {
            return;
        }

        List<Deque<Integer>> results = IntStream.range(0, 10)
                .mapToObj(i -> {
                    Deque<Integer> newQ = new ArrayDeque<>();
                    if (i == 0) {
                        if (!dps.get(i + 1).isEmpty()) {
                            int next = dps.get(i + 1).peek();
                            newQ.add(next % rest);
                        }
                    } else if (i == 9) {
                        if (!dps.get(i - 1).isEmpty()) {
                            int prev = dps.get(i - 1).peek();
                            newQ.add(prev % rest);
                        }
                    } else {
                        int next = dps.get(i + 1).peek();
                        int prev = dps.get(i - 1).peek();
                        newQ.add((prev + next) % rest);
                    }
                    return newQ;
                })
                .collect(Collectors.toList()); // Java 11에서는 Collectors.toList()를 사용해야 함.

        count--;
        dps = results;
        isStairsNum();
    }

    void result() {
        int total = dps.stream()
                .map(dp -> dp.isEmpty() ? 0 : dp.peek())
                .reduce(0, (sum, value) -> (sum + value) % rest);
        System.out.println(total);
    }

    void solve() throws IOException {
        makeSettings();
        isStairsNum();
        result();
    }

    public static void main(String[] args) throws IOException {
        new 쉬운계단수().solve();
    }
}
