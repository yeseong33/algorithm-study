package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 돌게임 {

    int n;
    boolean[] dp;

    public static void main(String[] args) throws IOException {
        new 돌게임().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        play();
        if (dp[n]) {
            System.out.println("SK");
        } else {
            System.out.println("CY");
        }
    }

    private void play() {
        for (int i = 4; i < n+1; i++) {
            dp[i] = !(dp[i - 1] && dp[i - 3]);
        }
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dp = new boolean[n + 1];
        dp[1] = true;
        if (n >= 3) {
            dp[3] = true;
        }
    }

}
