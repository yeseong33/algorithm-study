package 구현;

import java.io.*;
import java.util.*;

public class puyopuyo {

    int total, x, y, nx, ny;
    int[][] dir;
    char[][] board;
    boolean[][] visited;
    Queue<int[]> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new char[12][6];
        for (int i = 0; i < 12; i++) {
            char[] value = br.readLine().toCharArray();
            for (int j = 0; j < 6; j++) {
                board[i][j] = value[j];
            }
        }
        que = new LinkedList<>();
        dir = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    }

    boolean makeChain() {
        visited = new boolean[12][6];
        boolean isPop = false;
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 6; j++) {
                if (board[i][j] != '.' && !visited[i][j]) {
                    visited[i][j] = true;
                    if (!pop(i, j)) continue;
                    isPop = true;
                }
            }
        }

        return isPop;
    }

    boolean pop(int i, int j) {
        int count = 1;
        List<int[]> record = new ArrayList<>();
        que.add(new int[] {i, j});
        record.add(new int[] {i, j});
        while (!que.isEmpty()) {
            int[] now = que.poll();
            x = now[0];
            y = now[1];
            for (int d = 0; d < 4; d++) {
                nx = x + dir[d][0];
                ny = y + dir[d][1];
                if (!condition()) continue;
                visited[nx][ny] = true;
                int[] value = new int[]{nx, ny};
                que.add(value);
                record.add(value);
                count++;
            }
        }
        if (count >= 4) {
//            System.out.println("passed");
            for (int[] now : record) {
                board[now[0]][now[1]] = '.';
            }
            return true;
        }
        return false;
    }

    boolean condition() {
        return nx >= 0 && nx < 12 && ny >= 0 && ny < 6 && !visited[nx][ny] && board[x][y] == board[nx][ny];
    }

    void counting() {
        total++;
    }

    boolean resetting() {
        boolean isChage = false;
        for (int j = 0; j < 6; j++) {
            int zeroCount = 0;
            for (int i = 11; i >= 0; i--) {
                if (board[i][j] == '.') {
                    zeroCount++;
                } else {
                    board[i+zeroCount][j] = board[i][j];
                    if (zeroCount > 0) {
                        board[i][j] = '.';
                        isChage = true;
                    }
                }
            }
        }
        return isChage;
    }

    void solve() throws IOException {
        makeSettings();

        while (true) {
            if (makeChain()) {
                counting();
            }
//            for (int i = 0; i < 12; i++) {
//                for (int j = 0; j < 6; j++) {
//                    System.out.print(board[i][j] + " ");
//                }
//                System.out.println();
//            }
//            System.out.println();
            if (!resetting()) {
                break;
            }
//
//            for (int i = 0; i < 12; i++) {
//                for (int j = 0; j < 6; j++) {
//                    System.out.print(board[i][j] + " ");
//                }
//                System.out.println();
//            }
//            System.out.println("this is");

        }
        System.out.println(total);
    }



    public static void main(String[] args) throws IOException {
        new puyopuyo().solve();
    }
}
