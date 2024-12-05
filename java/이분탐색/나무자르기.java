package 이분탐색;

import java.io.*;
import java.util.*;

public class 나무자르기 {
    int n, m;
    long maxLen, minLen, result;
    long[] tree;

    public static void main(String[] args) throws IOException{
        new 나무자르기().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        cutTree();
        System.out.println(result);
    }

    private void cutTree() {

        while (minLen <= maxLen) {
            long mid = (maxLen + minLen) / 2;
            if (isE(mid)) {
                result = Math.max(result, mid);
                minLen = mid+1;
            } else {
                maxLen = mid-1;
            }
        }

    }

    private boolean isE(long mid) {
        long count = 0;

        for (int i = 0; i < n; i++) {
            long value = tree[i] - mid;
            if (value > 0) {
                count += value;
            }
        }

        return count >= m;
    }

    private void makeSettings() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        tree = new long[n];
        maxLen = 0;
        minLen = 0;
        result = 0;

        tokenizer = new StringTokenizer(reader.readLine());

        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(tokenizer.nextToken());
            tree[i] = value;
            maxLen = Math.max(value, maxLen);

        }

    }
}
