package 구현;


import java.io.*;
import java.util.*;

public class 뱀 {
    int n, k, l, t, x, y, d, nx, ny, count;
    String[] order;
    int[][] board, dir;
    StringTokenizer st;
    Queue<int[]> snake;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        board = new int[n][n];
        order = new String[10001];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken())-1;
            y = Integer.parseInt(st.nextToken())-1;
            board[x][y] = 1;
        }
        l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            t = Integer.parseInt(st.nextToken());
            order[t] = st.nextToken();
        }

        dir = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        d = 0;
        snake = new LinkedList<>();
        snake.add(new int[]{0, 0});
        board[0][0] = 2;
        count =0;
        x = 0; y = 0;
    }

    void moveHead() {
        nx = x + dir[d][0];
        ny = y + dir[d][1];
        snake.add(new int[]{nx, ny});
    }

    boolean condition() {
        return nx >= 0 && nx < n && ny >= 0 && ny < n && board[nx][ny] != 2;
    }

    boolean isGrow() {
        return board[nx][ny] == 1;
    }

    void moveTail() {
        if (!isGrow()) {
            int[] tail = snake.poll();
            board[tail[0]][tail[1]] = 0;
        }
        board[nx][ny] = 2;
        x = nx; y = ny;
    }

    void moveDir() {
        if (order[count] != null) {
            String value = order[count];
            if (value.equals("D")) {
                d = (d+1)%4;
            } else {
                d = (d+3)%4;
            }
        }
    }

    void solve() throws IOException {
        makeSettings();

        while (true) {
            moveHead();
            if (!condition()) {
                break;
            }
            moveTail();
            count++;
            moveDir();
        }

        System.out.println(count+1);
    }


    public static void main(String[] args) throws IOException {
        new 뱀().solve();
    }
}
