package BFS;


import java.io.*;
import java.util.*;

public class 말이되고픈원숭이 {

    int k, n, m, t, count, x, y, nx, ny;
    int[] now;
    int[][] board, monkeyMove, horseMove;
    int[][][] visited;
    StringTokenizer st;
    PriorityQueue<int[]> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        visited = new int[k+1][n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(st.nextToken());
                board[i][j] = value;
            }
        }
        que = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        que.add(new int[]{0, k, 0, 0});
        monkeyMove = new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        horseMove = new int[][] {{-2, 1}, {-2, -1}, {2, 1}, {2, -1}, {1 ,-2}, {-1, -2}, {1, 2}, {-1, 2}};
    }


    void solve() throws IOException {
        makeSettings();
        if (!BFS()) {
            System.out.print(-1);
        }
    }

    boolean passCondition(int type) {
        if (nx >= 0 && nx < n && ny >= 0 && ny < m){
            if ( visited[count-type][nx][ny] == 0) {
                if (board[nx][ny] != 1) {
                    return true;
                }
            }
        }
        return false;
    }

    void next(int type) {
        que.add(new int[] {t+1, count-type, nx, ny});
    }

    void mMove() {
        for (int i = 0; i < 4; i++) {
            nx = x + monkeyMove[i][0];
            ny = y + monkeyMove[i][1];
            if (passCondition(0)) {
                visited[count-0][nx][ny] = 1;
                next(0);
            }
        }

    }

    void hMove() {
        for (int i = 0; i < 8; i++) {
            nx = x + horseMove[i][0];
            ny = y + horseMove[i][1];
            if (passCondition(1)) {
                visited[count- 1][nx][ny] = 1;
                next(1);
            }
        }

    }


    boolean isEnd(){
        if (x == n-1 && y == m-1) {
            System.out.println(t);
            return true;
        }
        return false;
    }

    boolean BFS() {

        while (!que.isEmpty()) {
            now = que.poll();
            t = now[0];
            count = now[1];
            x = now[2];
            y = now[3];
            if (isEnd()) {
                return true;
            }
            mMove();
            if (count > 0) {
                hMove();
            }
        }
        return false;
    }


    public static void main(String[] args) throws IOException {
        new 말이되고픈원숭이().solve();
    }
}
