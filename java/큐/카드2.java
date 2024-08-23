package 큐;

import java.io.*;
import java.util.*;

public class 카드2 {
    int n;
    Queue<Integer> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        que = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            que.add(i);
        }

    }

    void solve() throws IOException {
        makeSettings();

        while (que.size() > 1) {
            que.poll();
            que.add(que.poll());
        }

        System.out.println(que.peek());
    }

    public static void main(String[] args) throws IOException {
        new 카드2().solve();

    }
}
