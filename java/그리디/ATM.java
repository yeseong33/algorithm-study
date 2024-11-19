package 그리디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class ATM {

    List<Integer> numbers;

    public static void main(String[] args) throws IOException {
        new ATM().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        numbers.sort(Comparator.comparing(Integer::valueOf));
        stackSum();
        System.out.println(sumOfNumbers());
    }

    private void makeSettings() throws IOException {

        numbers = new ArrayList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(st.nextToken());
            numbers.add(value);
        }
    }

    private void stackSum() {
        for (int i = 1; i < numbers.size(); i++) {
            numbers.set(i, numbers.get(i - 1) + numbers.get(i));
        }
    }

    private Integer sumOfNumbers() {
        return numbers.stream()
                .mapToInt(Integer::valueOf)
                .sum();
    }
}
