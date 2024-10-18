package DP;


import java.io.*;
import java.util.*;


public class 가장큰증가하는부분수열 {

    int n, maxValue;
    int[] nums, dp;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        nums = new int[n];
        dp = new int[n];
        maxValue = 0;

        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(st.nextToken());
            nums[i] = value;
            dp[i] = value;
        }

    }

    void findMaxValue(int value) {
        if (maxValue < value) {
            maxValue = value;
        }
    }


    void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < n; i++) {
            for (int j = i; j >= 0; j--) {
                if (dp[j] > 0 && nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[j] + nums[i], dp[i]);
                }
                findMaxValue(dp[i]);
            }
        }

        System.out.println(maxValue);


    }


    public static void main(String[] args) throws IOException {
        new 가장큰증가하는부분수열().solve();
    }
}
