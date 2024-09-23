import java.io.*;
import java.util.*;


public class Main {

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

        for (int i = 1; i < n+1; i++) {
            visited[i] = 1;
            que.add(i);
            BT();
            que.pop();
            visited[i] = 0;
        }
    }


    void solve() throws IOException {
        makeSettings();
        BT();
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}
