package 이분탐색;

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class 과자나눠주기 {

    int n, m, result;
    Deque<Integer> snacks;


    public static void main(String[] args) throws IOException {
        new 과자나눠주기().solve();
    }

    void solve() throws IOException {
        makeSettings();
        findMaxLen();
    }

    private void findMaxLen() {

        int left = 1;
        int right = snacks.getLast();

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canDivide(mid)) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(result);
    }

    private boolean canDivide(int mid) {

        int count = 0;

        for (int snack : snacks) {
            count += snack / mid;
        }

        return count >= n;
    }

    private void makeSettings() throws IOException {

        snacks = new ArrayDeque<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            snacks.add(Integer.parseInt(st.nextToken()));
        }

        sortSnacks();
    }

    private void sortSnacks() {
        snacks = new ArrayDeque<>(snacks.stream()
                .sorted()
                .collect(Collectors.toList()));
    }
}
