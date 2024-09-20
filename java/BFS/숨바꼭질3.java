package BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 숨바꼭질3 {

    int n, k, x, t, nx, nt, jj;
    int[] visited, now, dir;
    PriorityQueue<int[]> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        visited = new int[100001];
        que = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dir = new int[] {1, -1};
    }

    boolean passCondition() {
        if (nx >= 0 && nx < 100001 && visited[nx] == 0) {
            return true;
        }
        return false;
    }

    boolean move() {
        for (int i = 0 ; i < dir.length ; i++) {
            nx = x + dir[i];
            if (passCondition()) {
                if (isEnd(nx)) {
                    return true;
                }
                visited[nx] = 1;
                que.add(new int[] {t+1, nx});
                if (nx == 0) continue;
                while (true) {
                    nx *= 2;
                    if (nx >= 100001) break;
                    if (isEnd(nx)) return true;
                    que.add(new int[]{t+1, nx});
                    visited[nx] = 1;
                }
            }
        }
        return false;
    }

    boolean isEnd(int value) {
        return value == k;
    }

    void BFS() {
        que.add(new int[] {0, n});
        visited[n] = 1;

        if (n != 0) {
            while (true) {
                n *= 2;
                if (n >= 100001) break;
                if (isEnd(n)) {
                    t = -1;
                    return;
                }
                que.add(new int[]{0, n});
                visited[n] = 1;
            }
        }

        while (!que.isEmpty()) {
            now = que.poll();
            t = now[0];
            x = now[1];
            if (move()){
                return;
            };
        }
    }



    public void solve() throws IOException {
        makeSettings();
        if (n == k) {
            System.out.println(0);
        } else {
            BFS();
            System.out.println(t+1);
        }
    }



    public static void main(String[] args) throws IOException {
        new 숨바꼭질3().solve();
    }
}
