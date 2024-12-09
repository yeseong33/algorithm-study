package 이분탐색;

import java.io.*;
import java.util.StringTokenizer;

public class 용액 {

    long[] liquid;
    long result, prev, a, b;

    public static void main(String[] args) throws IOException {
        new 용액().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < liquid.length; i++) {
            binarySearch(i+1, liquid.length-1, liquid[i]);
        }
        System.out.println(a + " " + b);
    }

    private void binarySearch(int left, int right, long target) {

        while (left <= right) {
            int mid = (left + right) / 2;

            long now = liquid[mid] + target;

            if (result >= Math.abs(now)) {
                result = Math.abs(now);
                a = target;
                b = liquid[mid];
            }

            if (liquid[mid] >= -target) {
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

        liquid = new long[n];

        for (int i = 0; i < n; i++) {
            liquid[i] = Integer.parseInt(st.nextToken());
        }


        a = liquid[0];
        b = liquid[n - 1];
        result = Math.abs(a + b);

    }
}

