package 구현;


import java.io.*;
import java.util.*;

public class 연산자끼워넣기 {

    int n, minValue, maxValue;
    int[] nums, request;
    StringTokenizer st;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        minValue = 1000000000;
        maxValue = -1000000000;
        request = new int[4];

        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            request[i] = Integer.parseInt(st.nextToken());
        }
    }

    void cul(int total, int now) {

        if (now == n) {
            if (total > maxValue) {
                maxValue = total;
            }
            if (total < minValue) {
                minValue = total;
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (request[i] > 0) {
                request[i] -= 1;
                int nextTotal = makeValue(i, total, now);
                cul(nextTotal, now + 1);
                request[i] += 1;
            }
        }
    }

    int makeValue(int c, int total, int now) {
        int nextTotal = 0;
        if (c == 0) {
            nextTotal = total + nums[now];
        } else if (c == 1) {
            nextTotal = total - nums[now];
        }else if (c == 2) {
            nextTotal = total * nums[now];
        }else if (c == 3) {
            nextTotal = Math.abs(total) / nums[now];
            if (total <= 0) {
                nextTotal = -nextTotal;
            }
        }
        return nextTotal;
    }

    void solve() throws IOException {
        makeSettings();
        cul(nums[0], 1);
        System.out.println(maxValue);
        System.out.println(minValue);
    }

    public static void main(String[] args) throws IOException {
        new 연산자끼워넣기().solve();
    }
}
