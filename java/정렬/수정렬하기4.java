package 정렬;


import java.io.*;
import java.util.*;

public class 수정렬하기4 {

    int n;
    BufferedReader br;
    BufferedWriter bw;
    List<Integer> list;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());

        list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            Integer value = Integer.parseInt(br.readLine());
            list.add(value);
        }

        list.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return Integer.compare(b, a);
            }
        });

    }


    void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < n; i++) {
            bw.write(list.get(i) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 수정렬하기4().solve();
    }
}
