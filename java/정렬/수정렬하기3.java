package 정렬;


import java.io.*;
import java.util.*;

public class 수정렬하기3 {

    int n;
    BufferedReader br;
    BufferedWriter bw;
    int[] list;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());

        list = new int[10000001];

        for (int i = 0; i < n; i++) {
            Integer value = Integer.parseInt(br.readLine());
            list[value]++;
        }
    }


    void solve() throws IOException {
        makeSettings();

        for (int i = 1; i < 10000001; i++) {
            for (int j = 0; j < list[i]; j++) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 수정렬하기3().solve();
    }
}
