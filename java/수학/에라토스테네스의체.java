package 수학;

import java.io.*;
import java.util.*;

public class 에라토스테네스의체 {

    int n, k, count, result;
    boolean[] filter;

    public static void main(String[] args) throws IOException {
        new 에라토스테네스의체().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        EratosthenesFilter();
        System.out.println(result);
    }

    private void EratosthenesFilter() {
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j * i <= n; j++) {
                int value = i * j;
                if (!filter[value]) {
                    filter[value] = true;
                    count++;
                }
                if (count == k) {
                    result = value;
                    return;
                }
            }
        }
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        filter = new boolean[n+1];
        count = 0;
        result = -1;
    }
}
