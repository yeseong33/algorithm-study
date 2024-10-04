package 구현;


import java.io.*;
import java.util.*;

public class 연구소 {

    int n, m, baseCoun, x, y, nx, ny, baseCount, maxCount;
    int[][] board, dir;
    boolean[] wallVisited;
    StringTokenizer st;
    Queue<int[]> que;
    List<int[]> gas;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        que = new LinkedList<>();
        maxCount = 0;
        wallVisited = new boolean[n*m];
        baseCount = 0;
        gas = new ArrayList<>();
        dir = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(st.nextToken());
                board[i][j] = value;
                if (value != 0) {
                    baseCount++;
                    int t = i * m + j % m;
                    wallVisited[t] = true;
                }
                if (value == 2) {
                    gas.add(new int[]{i, j});
                }
            }
        }
    }

    void wall(int start, int d) {

        if (d == 3) {
            baseCount += 3;
            int result = spared();
            if (result > maxCount) {
                maxCount = result;
            }
            baseCount -= 3;
            return;
        }

        for (int i = start; i < n*m; i++) {
            if (!wallVisited[i]) {
                int x = i / m;
                int y = i % m;
                wallVisited[i] = true;
                board[x][y] = 1;
                wall(start+1, d+1);
                board[x][y] = 0;
                wallVisited[i] = false;
            }
        }
    }


    int spared() {
        boolean[][] visited = new boolean [n][m];
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int value = board[i][j];
                if (value != 0) {
                    visited[i][j] = true;
                    count++;
                }
                if (value == 2) {
                    que.add(new int[]{i, j});
                }
            }
        }
        while (!que.isEmpty()) {
            int[] now = que.poll();
            x = now[0];
            y = now[1];
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                if (condition(visited)) {
                    visited[nx][ny] = true;
                    que.add(new int[]{nx, ny});
                    count++;
                }
            }
        }
        return n*m - count;
    }

    boolean condition(boolean[][] visited) {
        return nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny];
    }

    void solve() throws IOException {
        makeSettings();
        wall(0, 0);
        System.out.println(maxCount);

    }


    public static void main(String[] args) throws IOException {
        new 연구소().solve();
    }
}
