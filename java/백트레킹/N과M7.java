package 백트레킹;

import java.io.*;
import java.util.*;

public class N과M7 {


    int n, m;
    int[] visited, intValues;
    BufferedWriter bw;
    Stack<Integer> que;
    StringTokenizer st;
    String[] values;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        values = br.readLine().split(" ");
        intValues = new int[values.length];
        for (int i = 0; i < values.length; i++) {
            intValues[i] = Integer.parseInt(values[i]);  // 문자열을 int로 변환
        }
        Arrays.sort(intValues);
        visited = new int[n];
        que = new Stack<>();
    }


    boolean isFull() {
        if (que.size() == m) {
            return true;
        }
        return false;
    }


    void BT() throws IOException {
        if (isFull()) {
            for (int value : que) {
                bw.write(intValues[value] + " ");
            }
            bw.newLine();
            return;
        }

        for (int i = 0; i < n; i++) {
            que.add(i);
            BT();
            que.pop();
        }
    }


    void solve() throws IOException {
        makeSettings();
        BT();
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new N과M7().solve();
    }
}
