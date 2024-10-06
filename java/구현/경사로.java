package 구현;


import java.io.*;
import java.util.*;


public class 경사로 {

    int n, l, x, y, nx, ny, d, count, result, bx, by, step;
    boolean nowB;
    int[][] board, dir;
    boolean[][] visited;

    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        result = 0;
        board = new int[n][n];
        dir = new int[][]{{1, 0}, {0, 1}};
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }


    void BT() {
        if (count == n) {
            visited[x][y] = true;
            result++;
            return;
        }

        if (runwayUp()) {
            BT();
        } else if (runwayDown()) {
            BT();
        } else if (next()) {
            BT();
        }
    }

    boolean runwayUp() {
        nx = x + dir[d][0];
        ny = y + dir[d][1];
        if (condition()) {
            if (board[nx][ny] == step + 1) {
                for (int t = 0; t < l; t++) {
                    nx = x - dir[d][0] * t;
                    ny = y - dir[d][1] * t;
                    if (!condition() || step != board[nx][ny] || visited[nx][ny]) {
                        return false;
                    }
                    visited[nx][ny] = true;
                }
                x += dir[d][0];
                y += dir[d][1];
                count++;
                step++;
                return true;
            }
        }
        return false;
    }

    boolean runwayDown() {
        nx = x + dir[d][0];
        ny = y + dir[d][1];
        if (condition()) {
            if (board[nx][ny] == step - 1) {
                for (int t = 1; t < l+1; t++) {
                    nx = x + dir[d][0] * t;
                    ny = y + dir[d][1] * t;
                    if (!condition() || step-1 != board[nx][ny] || visited[nx][ny]) {

                        return false;
                    }
                    visited[nx][ny] = true;
                }
                x += dir[d][0] * (l);
                y += dir[d][1] * (l);
                count += l;
                step--;
                return true;
            }
        }
        return false;
    }

    boolean next() {
        nx = x + dir[d][0];
        ny = y + dir[d][1];
        if (condition()) {
            if (board[nx][ny] == step) {
                x = nx;
                y = ny;
                count++;
                nowB = false;
                return true;
            }
        }
        return false;
    }



    boolean condition() {
        return nx >= 0 && nx < n && ny >= 0 && ny < n;
    }


    void solve() throws IOException {
        makeSettings();
        int i = 0;
        for (int j = 0; j < n; j++) {
            visited =  new boolean[n][n];
            step = board[i][j];
            x = i; y = j; count = 1;
            d = 0;
            BT();
        }
        int j = 0;
        for (i = 0; i < n; i++) {
            visited =  new boolean[n][n];
            step = board[i][j];
            x = i; y = j; count = 1;
            d = 1;
            BT();
        }
        System.out.println(result);
    }



    public static void main(String[] args) throws IOException {
        new 경사로().solve();
    }
}


//9 2
//2 2 2 1 1 1 2 2 2
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5
//5 5 5 5 5 5 5 5 5

//4 1
//3 2 1 2
//3 2 2
//2 1 3