package 백트레킹;

import java.io.*;
import java.util.*;



public class N과M3 {

    int n,m;
    BufferedWriter bw;
    Stack<Integer> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        que = new Stack<>();
    }


    boolean isFull() {
        if (que.size() == m)  {
            return true;
        }
        return false;
    }

    void BT() throws IOException {
        if (isFull()) {
            for (int c : que) {
                bw.write(c + " ");
            }
            bw.newLine();
            return;
        }

        for (int i = 0; i < n+1; i++) {
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
        new N과M3().solve();
    }
}
