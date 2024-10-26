package DP;

import java.io.BufferedReader;


import java.io.*;
import java.util.*;


public class 퇴사2 {

    long[] cost, value, sums;
    int n;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        cost = new long[n + 1];
        value = new long[n + 1];
        sums = new long[n + 1];

        for (int i = 1; i < n+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            cost[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

    }


    void findBestCombi() {
        for (int i = 1; i < n + 1; i++) {
            if (i + (int) cost[i] - 1 <= n) {
                sums[i+(int)cost[i]-1] = Math.max(sums[i-1] + value[i], sums[i+(int)cost[i]-1]);
            }
            sums[i] = Math.max(sums[i], sums[i - 1]);

        }
    }

    void printResult() {
        System.out.println(sums[n]);
    }



    void solve() throws IOException {
        makeSettings();
        findBestCombi();
        printResult();
    }

    public static void main(String[] args) throws IOException {
        new 퇴사2().solve();
    }
}
