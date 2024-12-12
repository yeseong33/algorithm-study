package 이분탐색;

import java.io.*;
import java.util.*;


public class 합이0인네정수 {

    long count;
    long[] firstSet;
    long[][] numbers;

    public static void main(String[] args) throws IOException {
        new 합이0인네정수().solve();
    }


    private void solve() throws IOException {

        makeSettings();
        findSumIsZero();

    }

    private void findSumIsZero() {

        int idx = -1;
        for (int i = 0; i < numbers[0].length; i++) {
            for (int j = 0; j < numbers[0].length; j++) {
                idx++;
                firstSet[idx] = numbers[0][i] + numbers[1][j];
            }
        }

        Arrays.sort(firstSet);


        for (int i = 0; i < numbers[0].length; i++) {
            for (int j = 0; j < numbers[0].length; j++) {
                long target = numbers[2][i] + numbers[3][j];
                int lower = binarySearchLower(0, firstSet.length, target);
                int upper = binarySearchUpper(0, firstSet.length, target);
                count += upper - lower;
            }
        }

        System.out.println(count);
    }

    private int binarySearchLower(int left, int right, long target) {

        while (left < right) {
            int mid = (left + right) / 2;

            long now = firstSet[mid];

            if (now + target >= 0) {
                right = mid;
            } else if (now + target < 0) {
                left = mid + 1;
            }
        }

        return left;
    }

    private int binarySearchUpper(int left, int right, long target) {

        while (left < right) {
            int mid = (left + right) / 2;

            long now = firstSet[mid];

            if (now + target > 0) {
                right = mid;
            } else if (now + target <= 0) {
                left = mid + 1;
            }
        }
        return left;
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        numbers = new long[4][n];

        firstSet = new long[n * n];

        count = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 4; j++) {
                numbers[j][i] = Long.parseLong(st.nextToken());
            }
        }

        for (int i = 0; i < 4; i++) {
            Arrays.sort(numbers[i]);
        }
    }
}
