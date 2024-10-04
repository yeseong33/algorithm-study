package 구현;

import java.io.*;
import java.util.*;


public class 구슬탈출2 {

    boolean redFirst;
    boolean[][][][] visited;
    int n, m, count, rx, ry, bx, by, nrx, nry, nbx, nby, d;
    int[] start, goal, moveSet;
    int[][] dir;
    char[][] board;
    PriorityQueue<int[]> que;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        count = 0 ;
        visited = new boolean[n][m][n][m];
        que = new PriorityQueue<>((a, b) -> {
            return Integer.compare(a[0], b[0]);
        });
        start = new int[5];
        goal = new int[2];
        dir = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        redFirst = true;

        for (int i = 0; i < n; i++) {
            char[] values = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                char value = values[j];
                board[i][j] = values[j];
                if (value == 'B') {
                    start[3] = i;
                    start[4] = j;
                    board[i][j] = '.';
                } else if (value == 'R') {
                    start[1] = i;
                    start[2] = j;
                    board[i][j] = '.';
                } else if (value == 'O') {
                    goal[0] = i;
                    goal[1] = j;
                    board[i][j] = '.';
                }
            }
        }
        visited[start[1]][start[2]][start[3]][start[4]] = true;
        que.add(start);
    }


    boolean play() {

        while (!que.isEmpty()) {
            int[] now = que.poll();
            count = now[0];
            rx = now[1];
            ry = now[2];
            bx = now[3];
            by = now[4];
            for (int i = 0; i < 4; i++) {
                d = i;
                if (i == 0) {
                    up();
                } else if (i == 1) {
                    down();
                } else if (i == 2) {
                    left();
                } else {
                    right();
                }
                move(rx, ry, bx, by);
                if (gameOver()) continue;
                if (gameClear()) {
                    return true;
                }

                if (visited[nrx][nry][nbx][nby]) continue;
                visited[nrx][nry][nbx][nby] = true;
                que.add(new int[]{count + 1, nrx, nry, nbx, nby});
            }
        }
        return false;
    }

    void up() {
        redFirst = bx >= rx;
    }

    void down() {
        redFirst = bx <= rx;
    }

    void left() {
        redFirst = by >= ry;
    }

    void right() {
        redFirst = by <= ry;
    }

    void move(int rx, int ry, int bx, int by) {
        nrx = 0; nry = 0; nbx =0; nby = 0;
        if (redFirst) {
            int[] newR = moving(rx, ry);
            nrx = newR[0]; nry = newR[1];
            int[] newB = moving(bx, by);
            nbx = newB[0]; nby = newB[1];
        } else {
            int[] newB = moving(bx, by);
            nbx = newB[0]; nby = newB[1];
            int[] newR = moving(rx, ry);
            nrx = newR[0]; nry = newR[1];
        }

    }

    int[] moving(int x, int y) {
        int nx = x;
        int ny = y;

        while (true) {
            if (!condition(nx, ny)) {
                nx -= dir[d][0];
                ny -= dir[d][1];
                break;
            }
            nx = nx + dir[d][0];
            ny = ny + dir[d][1];
            if (isGoal(nx, ny)) {
                break;
            }
        }

        return new int[]{nx, ny};
    }

    boolean condition(int nx, int ny) {
        return board[nx][ny] != '#' && !(nx == nbx && ny == nby) && !(nx == nrx && ny == nry);
    }

    boolean isGoal(int x, int y) {
        return x == goal[0] && y == goal[1];
    }

    boolean gameOver() {
        return goal[0] == nbx && goal[1] == nby || count >= 10;
    }

    boolean gameClear() {
//        System.out.println(nrx + " " + nry);
        return goal[0] == nrx && goal[1] == nry;
    }

    void solve() throws IOException {
        makeSettings();
        if (play()) {
            System.out.println(count + 1);
        } else {
            System.out.println(-1);

        }
    }

    public static void main(String[] args) throws IOException {
        new 구슬탈출2().solve();
    }
}
