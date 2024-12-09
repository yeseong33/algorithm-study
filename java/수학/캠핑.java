package 수학;

import java.util.*;
import java.io.*;

public class 캠핑 {

    int l, p, v, step;
    BufferedReader br;

    public static void main(String[] args) throws IOException {
        new 캠핑().solve();
    }

    private void solve() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        step = 0;
        while (true) {
            makeSettings();
            if (isEnd()) break;
            int result = calculate();
            System.out.println("Case " + step + ": " + result);
        }
    }

    private boolean isEnd() {
        return l == 0;
    }

    private int calculate() {

        return ((v / p) * l) + Math.min(v%p, l);
    }

    private void makeSettings() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        l = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        step++;
    }

}
