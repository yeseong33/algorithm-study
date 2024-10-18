package DP;


import java.io.*;
import java.util.*;


public class 가장긴증가하는부분수열 {

    int n, maxValue;
    int[] nums, dp;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        dp = new int[n];
        maxValue = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] =  Integer.parseInt(st.nextToken());
            dp[i] = 1;
        }
    }

    void setMaxLength(int value) {
        if (maxValue < value) {
            maxValue = value;
        }
    }

    void findMaxLength() {
        for (int i = 0; i < n; i++) {
            for (int j = i; j >= 0; j--) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                setMaxLength(dp[i]);
            }
        }
    }


    void solve() throws IOException {
        makeSettings();
        findMaxLength();
        System.out.println(maxValue);
    }




    public static void main(String[] args) throws IOException {
        new 가장긴증가하는부분수열().solve();
    }
}
