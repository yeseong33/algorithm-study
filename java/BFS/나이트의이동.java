package BFS;

import java.io.*;
import java.util.*;

public class 나이트의이동 {
    BufferedReader br;
    BufferedWriter bw;
    StringTokenizer st;
    int t, n, x, y, nx, ny, rx, ry, count;
    int[] now;
    int[][] visited, move;
    boolean isEnd;
    Deque<int[]> que, newQue;


    void makeSettings() throws IOException {
        n = Integer.parseInt(br.readLine());
        visited = new int[n][n];
        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        rx = Integer.parseInt(st.nextToken());
        ry = Integer.parseInt(st.nextToken());
        visited[x][y] = 1;
        isEnd = false;
        count = 0;
        que = new LinkedList<>();
        newQue = new LinkedList<>();
        que.add(new int[]{x, y});
    }

    void BFS() {
        while (!que.isEmpty()) {
            now = que.poll();
            x = now[0];
            y = now[1];
            for (int i = 0; i < 8; i++) {
                nx = x + move[i][0];
                ny = y + move[i][1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (nx == rx && ny == ry) {
                        isEnd = true;
                        return;
                    }
                    if (visited[nx][ny] == 0) {
                        visited[nx][ny] = 1;
                        newQue.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }

    void solve() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        t = Integer.parseInt(br.readLine());
        move = new int[][]{new int[] {-2, -1}, new int[] {-2, 1}, new int[] {2, -1}, new int[] {2, 1}, new int[] {-1, -2}, new int[] {1, -2}, new int[] {-1, 2}, new int[] {1, 2}};

        for (int i = 0; i < t; i++) {
            makeSettings();
            if (x == rx && x == ry) {
                isEnd = true;
            }
            while (!isEnd) {
                count++;
                BFS();
                que = newQue;
                newQue = new LinkedList<>();

            }
            bw.write(count + "\n");
        }
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new 나이트의이동().solve();
    }
}
