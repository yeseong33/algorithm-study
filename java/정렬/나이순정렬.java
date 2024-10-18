package 정렬;


import java.io.*;
import java.util.*;


public class 나이순정렬 {

    int n;
    StringTokenizer st;
    BufferedWriter bw;
    List<int[]> list;
    String[][] users;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        users = new String[201][n];

        list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            users[age][i] = name;
            list.add(new int[]{age, i});
        }


        list.sort(Comparator.comparingInt((int[] a) -> a[0])
                .thenComparingInt(a -> a[1]));
    }


    void solve() throws IOException {
        makeSettings();

        for (int[] value : list) {
            bw.write( value[0] + " "+ users[value[0]][value[1]]+"\n");
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 나이순정렬().solve();
    }
}
