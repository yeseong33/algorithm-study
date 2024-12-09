package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 수학은체육과목입니다 {

    int n;
    long total;

    public static void main(String[] args) throws IOException {
        new 수학은체육과목입니다().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        fillNumber();

        System.out.println(total);

    }

    private void fillNumber() {
        for (int i = 2; i < n + 1; i++) {
            total = total - i + 1 + 3 + i;
        }
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        total = 4;

    }
}
