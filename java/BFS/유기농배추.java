package BFS;

import java.io.*;
import java.util.*;

public class 유기농배추 {

    BufferedReader br;
    BufferedWriter bw;
    StringTokenizer st;
    int t, m, n, k, count;
    int[][] board, visited, dir;
    Queue<int[]> que;
    List<int[]> req;


    void makeSettings() throws IOException {
        br =  new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        t = Integer.parseInt(br.readLine());
        dir = new int[][]{new int[] {1, 0},  new int[] {0, 1},  new int[] {-1, 0},  new int[] {0, -1}};
    }


    void counting() throws IOException {
        int x, y, nx, ny;
        int[] now;
        boolean isFirst;

        count = 0;
        st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        visited = new int[n][m];
        req = new ArrayList<>();

        que = new LinkedList<>();

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            y = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());
            board[x][y] = 1;
            req.add(new int[]{x, y});
        }

        for (int[] q : req) {
            que.add(q);
            visited[q[0]][q[1]] = 1;
            while (!que.isEmpty()) {
                now = que.poll();
                isFirst = true;
                for (int i = 0; i < 4; i++) {
                    nx = now[0] + dir[i][0];
                    ny = now[1] + dir[i][1];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                        if (board[nx][ny] == 1) {
                            if (visited[nx][ny] == 1) {
                                isFirst = false;
                            } else {
                                visited[nx][ny] = 1;
                                que.add(new int[] {nx, ny});
                            }
                        }
                    }
                }
                if (isFirst) {
                    count++;
                }
            }
        }

    }


    void solve() throws IOException {
        makeSettings();
        for (int i = 0; i < t; i++) {
            counting();
            bw.write(count+"\n");
        }
        bw.flush();
        bw.close();
    }



    public static void main(String[] args) throws IOException {
        new 유기농배추().solve();
    }
}

