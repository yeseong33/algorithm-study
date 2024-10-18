package DP;

import java.io.*;
import java.util.*;


public class 연속합 {

    int n, head, tail, maxValue;
    int[] nums, numSum;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new int[n+1];
        numSum = new int[n+1];
        maxValue = -1001;
        head = 0;
        tail = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i < n+1; i++) {
            int value = Integer.parseInt(st.nextToken());
            nums[i] = value;
        }

        int total = 0;
        for (int i = 0; i < n + 1; i++) {
            total += nums[i];
            numSum[i] = total;
        }


    }


    void findMaxSum() {
        int total = 0;
        for (int i = 1; i < n + 1;i++ ) {
            total += nums[i];

            if (total > maxValue) {
                maxValue = total;
            }
            if (total < 0) {
                total = 0;
            }
        }
    }


    void solve() throws IOException {
        makeSettings();
        findMaxSum();
        System.out.println(maxValue);

    }


    public static void main(String[] args) throws IOException {
        new 연속합().solve();
    }
}
