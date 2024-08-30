package BFS;

import java.io.*;
import java.util.*;


public class 벽부수고이동하기 {
    int n, m, x, y, nx, ny, count, breakCount;
    int[] now;
    int[][] board, dir;
    boolean[][][] visited;
    PriorityQueue<int[]> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        visited = new boolean[2][n][m];
        visited[0][0][0] = true;
        visited[1][0][0] = true;
        for (int i = 0; i < n; i++) {
            char[] arr  = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                 board[i][j] = arr[j]-'0';
            }
        }
        que = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                // 0번째 인덱스 기준으로 오름차순 정렬
                return Integer.compare(o1[0], o2[0]);
            }
        });
        que.add(new int[]{1, 1, 0, 0});
        dir = new int[][] {new int[] {1, 0}, new int[] {-1, 0}, new int[] {0, 1}, new int[] {0, -1} };
    }


    boolean condition() {
        if (nx >= 0 && nx < n && ny >= 0 && ny < m){
            if(!visited[breakCount][nx][ny]) {
                visited[breakCount][nx][ny] = true;
                return true;
            }
        }
        return false;
    }

    boolean isEnd() {
        return nx == n - 1 && ny == m - 1;
    }

    int BFS() {
        while (!que.isEmpty()) {
            now = que.poll();
            count = now[0];
            breakCount = now[1];
            x = now[2];
            y = now[3];
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                if (condition()) {
                    if (isEnd()) {
                        return count+1;
                    }
                    if (board[nx][ny] == 1) {
                        if (breakCount == 1) {
                            que.add(new int[]{count + 1, breakCount-1, nx, ny});
                        }
                    } else {
                        que.add(new int[]{count + 1, breakCount, nx, ny});
                    }
                }
            }
        }
        return -1;
    }

    void solve() throws IOException {
        makeSettings();
        if (n== 1 && m==1){
            System.out.print(1);
            return;
        };
        System.out.print(BFS());
    }




    public static void main(String[] args) throws IOException {
        new 벽부수고이동하기().solve();
    }
}
