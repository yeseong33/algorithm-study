package 정렬;


import java.io.*;
import java.util.*;

public class 수정렬하기5 {

    int n;
    BufferedReader br;
    BufferedWriter bw;
    int[] list1, list2;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());

        list1 = new int[1000001];
        list2 = new int[1000001];

        for (int i = 0; i < n; i++) {
            Integer value = Integer.parseInt(br.readLine());
            if (value < 0) {
                list1[-value]++;
            } else {
                list2[value]++;
            }
        }
    }


    void solve() throws IOException {
        makeSettings();
        for (int i = 1000000; i > 0; i--) {
            for (int j = 0; j < list1[i]; j++) {
                bw.write(-i + "\n");
            }
        }
        for (int i = 0; i < 1000001; i++) {
            for (int j = 0; j < list2[i]; j++) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 수정렬하기5().solve();
    }
}
