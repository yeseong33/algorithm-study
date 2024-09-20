package BFS;

import java.io.*;
import java.util.*;

public class 다리만들기 {
    int n, x, y, nx, ny, count, group, nowG, maxc;
    int [] now;
    int[][] dir, board, visited;

    PriorityQueue<int[]> que, newQue;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        maxc = 1000000000;
        n = Integer.parseInt(br.readLine());
        group = -1;
        board = new int[n][n];
        visited = new int[n][n];
        que = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dir = new int[][] {{0,1}, {1,0}, {0,-1}, {-1,0}};

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int value = Integer.parseInt(st.nextToken());
                board[i][j] = value;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(board[i][j] == 1) {
                    findGroup(i, j);
                }
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] < 0) {
                    que.add(new int[]{0 ,i, j, board[i][j]});
                }
            }
        }

    }

    void findGroup(int i, int j) {
        que.add(new int[]{i, j});
        board[i][j] = group;
        while (!que.isEmpty()) {
            now = que.poll();
            x = now[0]; y = now[1];

            for (int k = 0; k < 4; k++) {
                nx = x + dir[k][0]; ny = y + dir[k][1];
                if (condition()) {
                    if (board[nx][ny] == 1) {
                        board[nx][ny] = group;
                        que.add(new int[]{nx, ny});
                    }
                }
            }
        }
        group--;
    }


    boolean condition() {
        if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
            return true;
        }
        return false;
    }

    boolean isEnd() {
        if (board[nx][ny] < 0 &&  board[nx][ny] != nowG) {
            maxc = Math.min(count + visited[nx][ny], maxc);
            return true;
        }
        return false;
    }


    void firstVisited() {
        visited[nx][ny] = count + 1;
        board[nx][ny] = nowG;
        que.add(new int[]{count + 1, nx, ny, nowG});
    }

    boolean isOcean() {
        if (board[nx][ny] == 0) {
            firstVisited();
            return false;
        }
        if (isEnd()) {
            return true;
        }
        return false;
    }

    void findLand() {
        int size = que.size();
        for (int t = 0; t < size; t++) {
            now = que.poll();
            x = now[1]; y = now[2]; nowG = now[3];
            count = now[0];

            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0]; ny = y + dir[i][1];
                if (condition()) {
//                    for (int k = 0; k < n; k++) {
//                        for (int l = 0; l < n; l++) {
//                            System.out.print(board[k][l] + " ");
//                        }
//                        System.out.println();
//                    }
//                    System.out.println();R
//                    for (int k = 0; k < n; k++) {
//                        for (int l = 0; l < n; l++) {
//                            System.out.print(visited[k][l] + " ");
//                        }
//                        System.out.println();
//                    }
//                    System.out.println();

                    isEnd();
                    isOcean();
                }
            }
        }
    }



    void solve() throws IOException {
        makeSettings();
        while (true){
            findLand();
            if (maxc != 1000000000) {
                System.out.println(maxc);
                return;

            }
        }
    }



    public static void main(String[] args) throws IOException {
        new 다리만들기().solve();
    }
}
