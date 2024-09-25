package 백트레킹;

import java.io.*;
import java.util.*;

public class 소문난칠공주 {

    int rCount, x, y, nx, ny, vCount;
    int[][] base;
    char[][] board;
    boolean[][] visited, copyVisited;
    Stack<Integer> que, stack;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new char[5][5];
        base = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        rCount = 0;
        for (int i = 0; i < 5; i++) {
            char[] in = br.readLine().toCharArray();
            for (int j = 0; j < 5; j++) {
                board[i][j] = in[j];
            }
        }
        visited = new boolean[5][5];
        que = new Stack<>();
    }


    boolean isOverS(int count) {
        if (count >= 4) {
            return true;
        }
        return false;
    }

    boolean isFull(int total) {
        if (total == 7) {
            return true;
        }
        return false;
    }

    boolean condition() {
        if (nx >= 0 && nx < 5 && ny >=0 && ny < 5) {
            return true;
        }
        return false;
    }

    int isNotSom(int value) {
        int xv = value / 5;
        int yv = value % 5;
        if (board[xv][yv] == 'Y') {
            return 1;
        }
        return 0;
    }

    void checkAround() {
        for (int i = 0; i < 4; i++) {
            nx = x + base[i][0];
            ny = y + base[i][1];
            if (condition()) {
                if (copyVisited[nx][ny]) {
                    vCount++;
                    copyVisited[nx][ny] = false;
                    stack.add(nx * 5 + ny % 5);
                }
            }
        }
    }

    boolean isConnected() {
        vCount = 0;
        copyVisited = new boolean[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                copyVisited[i][j] = visited[i][j];
            }
        }

        stack = new Stack<>();
        stack.add(que.peek());

        while (!stack.isEmpty()) {
            int now = stack.pop();
            x = now / 5;
            y = now % 5;
            checkAround();
        }
        if (vCount == 7) {
            return true;
        }
        return false;
    }


    void nextPerson(int total, int count, int start)  {
        for (int i = start; i < 25; i++) {
            que.add(i);
            visited[i/5][i%5] = true;
            BT(total+1, count+isNotSom(i), i+1);
            visited[i/5][i%5] = false;
            que.pop();
        }
    }


    void BT(int total, int count, int start) {
        if (isOverS(count)) {
            return;
        }

        if (isFull(total)) {
            if (isConnected()) {
                rCount++;
            }
            return;
        }
        nextPerson(total, count, start);
    }

    void solve() throws IOException {
        makeSettings();
        BT(0, 0, 0);
        System.out.println(rCount);
    }

    public static void main(String[] args) throws IOException {
        new 소문난칠공주().solve();
    }
}




