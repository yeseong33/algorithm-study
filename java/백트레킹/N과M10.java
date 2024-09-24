package 백트레킹;

import java.io.*;
import java.util.*;

public class N과M10 {


    int n, m;
    int[] visited, intValues;
    BufferedWriter bw;
    Stack<Integer> que;
    StringTokenizer st;
    String[] values;
    Set<Integer> duplicate;

    boolean makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        values = br.readLine().split(" ");
        intValues = new int[values.length];
        for (int i = 0; i < values.length; i++) {
            intValues[i] = Integer.parseInt(values[i]);
        }
        Arrays.sort(intValues);


        que = new Stack<>();
        visited = new int[1000001];
        return false;
    }


    boolean isFull() {
        if (que.size() == m) {
            return true;
        }
        return false;
    }


    void BT(int start) throws IOException {
        if (isFull()) {
            for (int value : que) {
                bw.write(value+ " ");
            }
            bw.newLine();
        }
        int before = 0;
        for (int i = start; i < n; i++) {
            if (visited[i] == 0) {
                if (before != intValues[i]) {
                    visited[i] += 1;
                    que.add(intValues[i]);
                    before = intValues[i];
                    BT(i+1);
                    que.pop();
                    visited[i] -= 1;
                }
            }
        }
    }


    void solve() throws IOException {
        if (makeSettings()) {
            return;
        }
        BT(0);
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new N과M10().solve();
    }
}


