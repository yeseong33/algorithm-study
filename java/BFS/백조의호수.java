//package BFS;
//
//import java.io.*;
//import java.util.*;
//
//public class 백조의호수 {
//    int n, m, x, y, nx, ny, count;
//    int[] now, startSwan, endSwan;
//    boolean[][] visited, visited2;
//    int[][]dir;
//    char[][] board;
//    Deque<int[]> que, newQue, nextQue, nextNewQue;
//
//    void makeSettings() throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        n = Integer.parseInt(st.nextToken());
//        m = Integer.parseInt(st.nextToken());
//        visited = new boolean[n][m];
//        visited2 = new boolean[n][m];
//        que = new ArrayDeque<>();
//        nextQue = new ArrayDeque<>();
//        newQue = new ArrayDeque<>();
//        nextNewQue = new ArrayDeque<>();
//        count = 0;
//        dir = new int[][]{new int[]{1, 0}, new int[]{0, 1}, new int[]{-1, 0}, new int[]{0, -1}};
//        board = new char[n][m];
//        for (int i = 0; i < n; i++) {
//            char[] arr = br.readLine().toCharArray();
//            char value;
//            for (int j = 0; j < m; j++) {
//                value = arr[j];
//                board[i][j] = value;
//                if (value == 'L') {
//                    board[i][j] = '.';
//                    if (startSwan == null) {
//                        startSwan = new int[]{i, j};
//                        visited[i][j] = true;
//                    } else {
//                        endSwan = new int[]{i, j};
//                    }
//                }
//                if (board[i][j] == '.') {
//                    newQue.offer(new int[]{i, j});
//                }
//            }
//        }
//        que.offer(startSwan);
//    }
//
//    boolean find() {
//        while (!que.isEmpty()) {
//            now = que.removeFirst();
//            x = now[0];
//            y = now[1];
//            for (int i = 0; i < 4; i++) {
//                nx = x + dir[i][0];
//                ny = y + dir[i][1];
//                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
//                    visited[nx][ny] = true;
//                    if (nx == endSwan[0] && ny == endSwan[1]){
//                        return true;
//                    }
//                    if (board[nx][ny] == 'X') {
//                        board[nx][ny] = '.';
//                        nextQue.offer(new int[]{nx, ny});
//                    } else  {
//                        que.offer(new int[]{nx, ny});
//                    }
//                }
//            }
//        }
//        Deque<int[]> temp = que;
//        que = nextQue;
//        nextQue = temp;
//        nextQue.clear();
//        return false;
//    }
//
//    void melt() {
//        while (!newQue.isEmpty()) {
//            now = newQue.poll();
//            x = now[0];
//            y = now[1];
//            for (int i = 0; i < 4; i++) {
//                nx = x + dir[i][0];
//                ny = y + dir[i][1];
//                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && !visited2[nx][ny]) {
//                    visited2[nx][ny] = true;
//                    if (board[nx][ny] == 'X') {
//                        board[nx][ny] = '.';
//                        nextNewQue.offer(new int[]{nx, ny});
//                    }
//                }
//            }
//        }
//        Deque<int[]> temp = newQue;
//        newQue = nextNewQue;
//        nextNewQue = temp;
//        nextNewQue.clear();
//    }
//
//    void solve() throws IOException {
//
//        makeSettings();
//        while(true){
//            if (find()) {
//                break;
//            }
//            melt();
//            count++;
//        }
//        System.out.print(count);
//    }
//
//
//    public static void main(String[] args) throws IOException {
//        new 백조의호수().solve();
//    }
//}

// version 2
package BFS;

import java.io.*;
import java.util.*;

public class 백조의호수 {

    int n, m, ni, nj, x, y, nx, ny, count;
    int [] now;
    int[][] visited, dir, swanVisited ;
    char[][] board;
    StringTokenizer st;
    Deque<int[]> swan, water, nSwan, nWater;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        count = 0;

        board = new char[n][m];
        swan = new ArrayDeque<>();
        nSwan = new ArrayDeque<>();
        water = new ArrayDeque<>();
        nWater = new ArrayDeque<>();

        boolean flag = false;
        swanVisited = new int[n][m];

        for (int i = 0; i < n; i++) {
            char[] in = br.readLine().toCharArray();
            for (int j = 0; j < in.length; j++) {
                char value = in[j];
                board[i][j] = value;
                if (value == 'L') {
                    board[i][j] = '.';
                    swanVisited[i][j] = 2;
                    if (flag) continue;
                    swanVisited[i][j] = 1;
                    swan.add(new int[]{i, j});
                    flag = true;
                }
            }
        }

        dir = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == '.') {
                    for (int t = 0; t < 4; t++) {
                        ni = i + dir[t][0];
                        nj = j + dir[t][1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
                            if (visited[ni][nj] == 0) {
                                if (board[ni][nj] == 'X') {
                                    visited[ni][nj] = 1;
                                    water.add(new int[] {ni, nj});
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    boolean waterCondition() {
        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (visited[nx][ny] == 0 && board[nx][ny] == 'X') {
                return true;
            }
        }
        return false;
    }


    void nextWater() {
        for (int i = 0; i < 4; i++) {
            nx = x + dir[i][0];
            ny = y + dir[i][1];
            if (waterCondition()) {
                visited[nx][ny] = 1;
                nWater.add(new int[]{nx, ny});
            }
        }
    }


    void day() {
        while (!water.isEmpty()) {
            now = water.poll();
            x = now[0];
            y = now[1];
            board[x][y] = '.';
            nextWater();
        }
        water = new ArrayDeque<>(nWater);
        nWater.clear();

    }

    boolean swanCondition() {
        if (swanVisited[nx][ny] == 0 && board[nx][ny] == '.') {
            return true;
        }
        return false;
    }

    boolean isEdge() {
        if (swanVisited[nx][ny] == 0  && board[nx][ny] == 'X') {
            return true;
        }
        return false;
    }

    boolean isEnd() {
        if (swanVisited[nx][ny] == 2) {
            return true;
        }
        return false;
    }

    boolean baseCondition() {
        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            return true;
        }
        return false;
    }


    boolean nextSwan() {
        for (int i = 0; i < 4; i++) {
            nx = x + dir[i][0];
            ny = y + dir[i][1];
            if (!baseCondition()) continue;
            if (isEnd()) {
                return true;
            }
            if (swanCondition()) {
                swanVisited[nx][ny] = 1;
                swan.add(new int[]{nx, ny});
            }
            if (isEdge()) {
                swanVisited[nx][ny] = 1;
                nSwan.add(new int[]{nx, ny});
            }
        }
        return false;
    }


    boolean swanMeet() {
        while (!swan.isEmpty()) {
            now = swan.poll();
            x = now[0];
            y = now[1];
            if (nextSwan()){
              return true;
            };
        }
        swan = new ArrayDeque<>(nSwan);
        nSwan.clear();
        return false;
    }


    void solve() throws IOException {
        makeSettings();
        if (swanMeet()) {
            System.out.println(count);
            return;
        }
        while (true) {
            count++;
            day();
            if (swanMeet()) {
                System.out.println(count);
                return;
            }
        }
    }


    public static void main(String[] args) throws IOException {
        new 백조의호수().solve();
    }
}