package 이분탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 세용액 {

    long result, a, b, c;
    long[] liquids;

    public static void main(String[] args) throws IOException {
        new 세용액().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        findComdi();
    }

    private void findComdi() {


        for (int i = 0; i < liquids.length; i++) {
            long liquidA = liquids[i];
            for (int j = i + 1; j < liquids.length; j++) {
                long liquidB = liquids[j];
                binarySearch(j + 1, liquids.length - 1, (liquidA + liquidB), liquidA, liquidB);
            }
        }

        System.out.println(a + " " + b + " " + c);


    }

    private void binarySearch(int left, int right, long target, long liquidA, long liquidB) {
        while (left <= right) {
            int mid = (left + right) / 2;
            long now = liquids[mid] + target;

            if (result >= Math.abs(now)) {
                result = Math.abs(now);
                a = liquidA;
                b = liquidB;
                c = liquids[mid];
            }

            if (now >= 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        liquids = new long[n];

        for (int i = 0; i < n; i++) {
            liquids[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(liquids);
        c = liquids[n - 1];

        result = Long.MAX_VALUE;
    }
}


