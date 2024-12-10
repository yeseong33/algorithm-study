package 이분탐색;

import java.io.*;
import java.util.*;


public class 공유기설치 {

    long m;
    long[] x;

    public static void main(String[] args) throws IOException {
        new 공유기설치().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        binarySearch();

    }

    private void binarySearch() {

        long left = 1;
        long right = x[x.length-1] - x[0];

        while (left <= right) {

            long mid = (left + right) / 2;

            if (canInstall(mid) < m) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(left-1);

    }

    private long canInstall(long mid) {

        long count = 1;
        long prev = x[0];

        for (int i = 1; i < x.length; i++) {
            long now = x[i];

            if (now - prev >= mid) {
                count++;
                prev = now;
            }
        }

        return count;
    }

    private void makeSettings() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        m = Long.parseLong(st.nextToken());

        x = new long[n];

        for (int i = 0; i < n; i++) {
            x[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(x);
    }
}
