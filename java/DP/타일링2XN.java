package DP;

import java.io.*;
import java.util.*;

public class 타일링2XN {
    int n;
    long [] nums;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        nums = new long[n+1];
        if (n == 1) {
            nums[1] = 1;
        } else {
            nums[1] = 1;
            nums[2] = 3;
        }

    }

    void solve() throws IOException {
        makeSettings();

        for (int i = 3; i <= n; i++) {
            nums[i] = nums[i - 1] + 2 * nums[i - 2];
            nums[i] %= 10007;  // 매번 모듈러 연산 적용
        }
        System.out.println(nums[n]);
    }


    public static void main(String[] args) throws IOException {
        new 타일링2XN().solve();
    }
}
