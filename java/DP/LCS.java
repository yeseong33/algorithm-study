package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class LCS {

    String l1, l2;
    int[] counts;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        l1 = br.readLine();
        l2 = br.readLine();

        counts = new int[Math.max(l2.length()+1, l1.length()+1)];
    }

    void countLCS() {
        int[] pre = counts.clone();
        for (int i = 1; i < l1.length()+1; i++) {
            for (int j = 1; j < l2.length()+1 ; j++) {
                if (l1.charAt(i-1) == l2.charAt(j-1)) {
                    counts[j] = pre[j-1]+ 1;
                } else {
                    counts[j] = Math.max(pre[j], counts[j-1]);
                }
            }
           pre = counts.clone();
        }
    }

    void solve() throws IOException {
        makeSettings();
        countLCS();
        System.out.println(counts[l2.length()]);
    }

    public static void main(String[] args) throws IOException {
        new LCS().solve();
    }
}

