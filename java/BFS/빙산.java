package BFS;

// 1. 녹는다
//   만약 0이되면 -> 다음 que
//   아직 빙하라면 -> countque
// 2. 빙하 몇갠지 체크
//   countQue -> BFS


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class 빙산 {
    int n, m, x, y, nx, ny, count, cicle;
    int[] now;
    int[][] board, dir;
    boolean[][] visited;
    Queue<int[]> queue, countQueue, checkQueue;
    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        queue = new ArrayDeque<>();
        countQueue = new ArrayDeque<>();
        checkQueue = new ArrayDeque<>();
        dir = new int[][] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        count = 0;
        cicle = 0;
        visited= new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

    }

    void findEdge() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 첫 번째 행이나 마지막 행의 모든 열을 추가
                if (board[i][j] == 0) {
                    visited[i][j] = true;
                    queue.add(new int[]{i, j});
                }
            }
        }
    }

    void melt() {
        while(!queue.isEmpty()) {
            now = queue.poll();
            x = now[0];
            y = now[1];

            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (board[nx][ny] == 0 && !visited[nx][ny]) {
                        queue.add(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    } else if (board[nx][ny] != 0){
                        board[nx][ny] -= 1;
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }

    void counting() {
        while(!countQueue.isEmpty()) {
            now = countQueue.poll();
            x = now[0];
            y = now[1];

            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && board[nx][ny] != 0) {
                    visited[nx][ny] = true;
                    countQueue.add(new int[]{nx, ny});
                }
            }
        }
    }

    void findLandAndCounting() {
        while (!queue.isEmpty()) {
            now = queue.poll();
            x = now[0];
            y = now[1];
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];


                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {

                    visited[nx][ny] = true;
                    if(board[nx][ny] != 0) {
                        countQueue.add(new int[]{nx, ny});
                        queue.add(new int[]{nx, ny});
                        counting();
                        count++;
                    } else {
                        queue.add(new int[]{nx, ny});
                    }
                }
            }


        }
    }

    void solve() throws IOException {
        makeSettings();
        while (true) {
            cicle++;
            visited = new boolean[n][m];
            findEdge();
            melt();
            visited = new boolean[n][m];
            count = 0;
            findEdge();
            findLandAndCounting();

            if (count >= 2 ) {
                System.out.println(cicle);
                break;
            } else if (count == 0 ){
                System.out.println(0);
                break;
            }
        }

    }


    public static void main(String[] args) throws IOException {
        new 빙산().solve();
    }

}
