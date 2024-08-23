package 배열;

import java.io.*;
import java.util.*;

public class 두수의합 {
    int n, x, count;
    int[] num;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        num = new int[2000001];
        while (st.hasMoreTokens()) {
            String tmp = st.nextToken();
            num[Integer.parseInt(tmp)] = 1;
        }

        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        count = 0;
    }

    private void counting() {
        int fx, bx;
        fx = x;
        bx = 0;
        while (fx > bx) {
            if (num[fx] == 1 && num[bx] == 1) {
                count++;
            }
            fx -= 1;
            bx += 1;
        }
    }

    void solve() throws IOException {
        makeSettings();
        counting();
        System.out.println(count);
    }




    public static void main(String[] args) throws IOException {
        new 두수의합().solve();
    }
}
