package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 암호코드 {

    String code;
    int[] dp;
    boolean flag = false;


    public static void main(String[] args) throws IOException {
        new 암호코드().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        deCode();
        if (flag) {
            System.out.println(0);
        } else {
            System.out.println(dp[dp.length-1]);
        }
    }

    private void deCode() {
        for (int i = 2; i < dp.length; i++) {
            String c = String.valueOf(code.charAt(i-1)) + String.valueOf(code.charAt(i));
            int count = 0;
            int count2 = dp[i - 1];
            if (Integer.parseInt(c) <= 26 && code.charAt(i-1) != '0') {
                count = dp[i-2];
            }
            if (Integer.parseInt(c) == 0) {
                flag = true;
            }
            if (code.charAt(i) == '0') {
                count2 = 0;
            }
            dp[i] = (count2 + count) % 1000000;
        }
    }

    private void makeSettings() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        code = br.readLine();
        dp = new int[code.length()];
        dp[0] = 1;
        if (code.length() != 1) {
            int count = 0;
            int count2 = dp[0];
            if (Integer.parseInt(String.valueOf(code.charAt(0)) + String.valueOf(code.charAt(1))) <= 26 ) {
                count = 1;
            }
            if (Integer.parseInt(String.valueOf(code.charAt(0)) + String.valueOf(code.charAt(1))) == 0 || code.charAt(0) == '0') {
                flag = true;
            }
            if (code.charAt(1) == '0') {
                count2 = 0;
            }
            dp[1] = count2 + count;
        }
        if (code.charAt(0) == '0') {

            flag = true;
        }

    }
}
