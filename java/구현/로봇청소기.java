package 구현;

import java.io.*;
import java.util.*;


public class 로봇청소기 {

    int n, m, d, x, y, count, nx, ny;
    int[][] board, dir;
    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        count = 0;

        board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dir = new int[][] {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    }

    void clean() {
        if (board[x][y] == 0) {
            board[x][y] = 2;
            count++;
        }
    }

    boolean check4() {
        for (int i = 0; i < 4; i++) {
            nx = x + dir[i][0];
            ny = y + dir[i][1];
            if (board[nx][ny] == 0) {
                return true;
            }
        }
        return false;
    }

    boolean backMove() {
        nx = x + dir[(d+2)%4][0];
        ny = y + dir[(d+2)%4][1];
        if (board[nx][ny] != 1){
            x = nx;
            y = ny;
        } else {
            return false;
        }
        return true;
    }

    void rotation() {
        d = (d+3)%4;
    }

    void frontMove() {
        nx = x + dir[d][0];
        ny = y + dir[d][1];
        if (board[nx][ny] == 0) {
            x = nx;
            y = ny;
        }
    }

    void solve() throws IOException {
        makeSettings();

        while (true) {

            clean();
            if (!check4()){
                if (!backMove()) {
                    break;
                };
            } else {
                rotation();
                frontMove();
            }
        }

        System.out.println(count);
    }

    public static void main(String[] args) throws IOException {
        new 로봇청소기().solve();
    }
}
