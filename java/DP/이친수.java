package DP;


import java.io.*;
import java.util.*;

public class 이친수 {

    int n;
    long[] nums;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        nums = new long[n + 1];
        nums[1] = 1;
        if (n > 1) {
            nums[2] = 1;
        }
    }


    void solve() throws IOException {
        makeSettings();

        for (int i = 3; i < n + 1; i++) {
            nums[i] = nums[i - 2] + nums[i - 1];
        }

        System.out.println(nums[n]);
    }



    public static void main(String[] args) throws IOException {
        new 이친수().solve();
    }
}
