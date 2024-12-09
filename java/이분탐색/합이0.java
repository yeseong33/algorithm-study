package 이분탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 합이0 {

    long count;
    long[] players;

    public static void main(String[] args) throws IOException {
        new 합이0().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        for (int a = 0; a < players.length; a++) {
            long player1 = players[a];
            for (int b = a + 1; b < players.length; b++) {
                long player2 = players[b];
                long target = -(player1 + player2);
                int lb = binarySearchLowerBound(b + 1, players.length - 1, target);
                int ub = binarySearchUpperBound(b + 1, players.length - 1, target);
                count += (ub - lb);
            }
        }

        System.out.println(count);
    }

    private int binarySearchLowerBound(int left, int right, long target) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (players[mid] >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int binarySearchUpperBound(int left, int right, long target) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (players[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        players = new long[n];

        for (int i = 0; i < n; i++) {
            players[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(players);
        count = 0;
    }
}
