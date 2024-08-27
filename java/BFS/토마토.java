package BFS;

import java.io.*;
import java.util.*;

public class 토마토 {
    int n, m, h, x, y, z, nx, ny, nz, tomato, total;
    int[][][] board;
    int[][] dir;
    int[] now;
    boolean[][][] visited;
    boolean isEnd;
    Queue<int[]> que, nextQue;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        isEnd = false;
        tomato = 0;
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        total = 0;
        board = new int[h][n][m];
        visited = new boolean[h][n][m];
        que = new LinkedList<>();
        nextQue = new LinkedList<>();
        dir = new int[][]{new int[]{1, 0, 0}, new int[]{-1, 0, 0}, new int[]{0, 1, 0}, new int[]{0, -1, 0}, new int[]{0, 0, 1}, new int[]{0, 0, -1}};
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                String[] s = br.readLine().split(" ");
                for (int k = 0; k < m; k++) {
                    board[i][j][k] = Integer.parseInt(s[k]);
                    if (Integer.parseInt(s[k]) == 1) {
                        que.add(new int[]{i, j, k});
                        visited[i][j][k] = true;
                        tomato++;
                        total++;
                    } else if (Integer.parseInt(s[k]) == 0) {
                        total++;
                    }
                }
            }
        }
    }


    void BFS() {
        if (que.isEmpty()) {
            isEnd = true;
        }
        while (!que.isEmpty()) {
            now = que.poll();
            z = now[0];
            x = now[1];
            y = now[2];

            for (int i = 0; i < 6; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                nz = z + dir[i][2];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && nz >= 0 && nz < h) {
                    if (!visited[nz][nx][ny] && board[nz][nx][ny] ==0) {
                        tomato++;
                        visited[nz][nx][ny] = true;
                        nextQue.add(new int[]{nz, nx, ny});
                    }
                }
            }
        }
    }

    void solve() throws IOException {
        makeSettings();
        int count = -2;
        while (!isEnd) {
            BFS();
            que = nextQue;
            nextQue = new LinkedList<>();
            count++;
        }
        if (tomato == total) {
            System.out.print(count);
        } else {
            System.out.print(-1);
        }

    }


    public static void main(String[] args) throws IOException {
        new 토마토().solve();
    }
}