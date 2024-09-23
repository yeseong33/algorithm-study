package 백트레킹;

import java.io.*;
import java.util.*;

public class N과M2 {


    int n, m;
    int[] visited;
    BufferedWriter bw;
    Stack<Integer> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new int[n+1];
        que = new Stack<>();
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
                bw.write(value + " ");
            }
            bw.newLine();
            return;
        }

        for (int i = start; i < n+1; i++) {
            que.add(i);
            BT(i+1);

            que.pop();
        }
    }


    void solve() throws IOException {
        makeSettings();
        BT(1);
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new N과M2().solve();
    }
}
