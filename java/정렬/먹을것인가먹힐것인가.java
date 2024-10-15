package 정렬;


import java.io.*;
import java.util.*;

public class 먹을것인가먹힐것인가 {

    int t, n, m, start, end, count;
    BufferedReader br;
    StringTokenizer st;
    int[] numsA, numsB;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
    }

    void setting() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        numsA = new int[n];
        numsB = new int[m];
        count = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(st.nextToken());
            numsA[i] = value;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int value = Integer.parseInt(st.nextToken());
            numsB[i] = value;
        }

        Arrays.sort(numsA);
        Arrays.sort(numsB);

    }

    void counting() {
        int cn = n;
        int a = 0;
        int b = 0;
        while (a < n && b < m) {
            int valueA = numsA[a];
            int valueB = numsB[b];
            if (valueA > valueB) {
                count += cn;
                b++;
            } else {
                a++;
                cn--;
            }
        }

    }

    void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < t; i++) {
            setting();
            counting();
            System.out.println(count);

        }

    }

    public static void main(String[] args) throws IOException {
        new 먹을것인가먹힐것인가().solve();
    }
}
