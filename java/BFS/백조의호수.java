package BFS;

import java.io.*;
import java.util.*;

public class 백조의호수 {
    int n, m, x, y, nx, ny, count;
    int[] now, startSwan, endSwan;
    boolean[][] visited, visited2;
    int[][]dir;
    char[][] board;
    Deque<int[]> que, newQue, nextQue, nextNewQue;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new boolean[n][m];
        visited2 = new boolean[n][m];
        que = new ArrayDeque<>();
        nextQue = new ArrayDeque<>();
        newQue = new ArrayDeque<>();
        nextNewQue = new ArrayDeque<>();
        count = 0;
        dir = new int[][]{new int[]{1, 0}, new int[]{0, 1}, new int[]{-1, 0}, new int[]{0, -1}};
        board = new char[n][m];
        for (int i = 0; i < n; i++) {
            char[] arr = br.readLine().toCharArray();
            char value;
            for (int j = 0; j < m; j++) {
                value = arr[j];
                board[i][j] = value;
                if (value == 'L') {
                    board[i][j] = '.';
                    if (startSwan == null) {
                        startSwan = new int[]{i, j};
                        visited[i][j] = true;
                    } else {
                        endSwan = new int[]{i, j};
                    }
                }
                if (board[i][j] == '.') {
                    newQue.offer(new int[]{i, j});
                }
            }
        }
        que.offer(startSwan);
    }

    boolean find() {
        while (!que.isEmpty()) {
            now = que.removeFirst();
            x = now[0];
            y = now[1];
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    if (nx == endSwan[0] && ny == endSwan[1]){
                        return true;
                    }
                    if (board[nx][ny] == 'X') {
                        board[nx][ny] = '.';
                        nextQue.offer(new int[]{nx, ny});
                    } else  {
                        que.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        Deque<int[]> temp = que;
        que = nextQue;
        nextQue = temp;
        nextQue.clear();
        return false;
    }

    void melt() {
        while (!newQue.isEmpty()) {
            now = newQue.poll();
            x = now[0];
            y = now[1];
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && !visited2[nx][ny]) {
                    visited2[nx][ny] = true;
                    if (board[nx][ny] == 'X') {
                        board[nx][ny] = '.';
                        nextNewQue.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        Deque<int[]> temp = newQue;
        newQue = nextNewQue;
        nextNewQue = temp;
        nextNewQue.clear();
    }

    void solve() throws IOException {

        makeSettings();
        while(true){
            if (find()) {
                break;
            }
            melt();
            count++;
        }
        System.out.print(count);
    }


    public static void main(String[] args) throws IOException {
        new 백조의호수().solve();
    }
}
