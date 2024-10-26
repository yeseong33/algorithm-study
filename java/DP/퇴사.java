package DP;

import java.io.BufferedReader;


import java.io.*;
import java.util.*;


public class 퇴사 {

    int n;
    StringTokenizer st;
    long[] cost, value, sums;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        cost = new long[n + 1];
        value = new long[n + 1];
        sums = new long[n + 1];

        for (int i = 1; i < n + 1; i++) {
            String s = br.readLine();
            st = new StringTokenizer(s);
            cost[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

    }


    void cul() {
        for (int i = 1; i <= n; i++) {
            if (i + (int) cost[i] - 1 <= n) {
                sums[i + (int) cost[i] - 1] = Math.max(value[i] + sums[i - 1], sums[i + (int) cost[i] - 1]);
            }
            sums[i] = Math.max(sums[i - 1], sums[i]);

        }
    }


    void printResult() {
        System.out.println(sums[n]);
    }

    void solve() throws IOException {
        makeSettings();
        cul();
        printResult();
    }


    public static void main(String[] args) throws IOException {
        new 퇴사().solve();
    }
}
