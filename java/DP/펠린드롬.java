package DP;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class 펠린드롬 {

    BufferedReader br;
    BufferedWriter bw;
    Integer n;
    int[] numbers;
    boolean[][] dp;


    public static void main(String[] args) throws IOException {
        new 펠린드롬().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        play();

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (dp[a][b]) {
                bw.write("1\n");
            } else {
                bw.write("0\n");
            }
        }

        bw.flush();
        bw.close();

    }

    private void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        numbers = new int[n+1];
        dp = new boolean[n+1][n+1];

        for (int i = 1; i < n+1; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i <= n; i++) {
            dp[i][i] = true; // 길이 1은 항상 팰린드롬
        }
        for (int i = 1; i < n; i++) {
            if (numbers[i] == numbers[i + 1]) {
                dp[i][i + 1] = true; // 길이 2 처리
            }
        }
    }

    private void play() {
        // DP 갱신
        for (int len = 3; len <= n; len++) { // 길이 3 이상
            for (int i = 1; i <= n - len + 1; i++) {
                int j = i + len - 1; // 끝점
                if (numbers[i] == numbers[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                }
            }
        }
    }
}


