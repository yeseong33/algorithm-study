package 그리디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 잃어버린괄호 {

    int total, minus, plus;
    int[] numbers;
    List<Character> orders;
    boolean state;


    public static void main(String[] args) throws IOException {
        new 잃어버린괄호().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        play();
        System.out.println(total);
    }

    private void play() {
        total = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (orders.get(i) == '-') {
                state = true;
            }
            if (state) {
                total -= numbers[i];
            } else {
                total += numbers[i];
            }
        }
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String origin = br.readLine();

        orders = new ArrayList<>();
        orders.add('s');

        numbers = Arrays.stream(origin.replace('-', ' ')
                .replace('+', ' ')
                .split(" "))
                .mapToInt(Integer::valueOf)
                .toArray();

        for (char c : origin.toCharArray()) {
            if (c == '+' || c == '-') {
                orders.add(c);
            }
        }

        minus = 0;
        plus = 0;
        state = false;
    }


}
