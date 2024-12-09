package 수학;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class 분수찾기 {

    int n;
    List<Integer> numbers;

    public static void main(String[] args) throws IOException {
        new 분수찾기().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        findValue();
    }

    private void findValue() {
        int count = 0;
        int now = 0;
        for (int i = 1; i <= numbers.size(); i++) {
            count = i + 1;
            now = numbers.get(i);
            if (now > n) {
                count = i;
                break;
            }
        }

        int num = n - numbers.get(count-1) + 1;
        int top, bottom;
        if (count % 2 == 0) {
            top = count - num;
            bottom = num;
        } else {
            top =  num;
            bottom = count-num
            ;
        }

        System.out.println(top + "/" + bottom);


    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        numbers = new ArrayList<>();

        numbers.add(0);
        numbers.add(1);
        int idx = 1;
        while (true) {
            int value = idx + numbers.get(idx);
            if (value > 10000001) {
                numbers.add(value);
                break;
            }
            numbers.add(value);
            idx++;
        }
    }
}
