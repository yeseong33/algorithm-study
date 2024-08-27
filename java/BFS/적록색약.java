package BFS;

import java.io.*;
import java.util.*;

import static java.lang.Integer.sum;


public class 적록색약 {

    char[][] board;
    char color;
    int[][] dir;
    boolean[][]visited;
    int[] now, counts;
    int n, x, y, nx, ny;
    Deque<int[]> que;
    Map<Character, Integer> colorMap;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        visited = new boolean[n][n];
        dir = new int[][]{new int[]{0, -1}, new int[]{-1, 0}, new int[]{0, 1}, new int[]{1, 0}};
        que = new ArrayDeque<>();
        char[] cs;
        counts = new int[3];
        colorMap = new HashMap<>();
        colorMap.put('R', 0);
        colorMap.put('G', 2);
        colorMap.put('B', 1);
        for (int i = 0; i < n; i++) {
            cs = br.readLine().toCharArray();
            for (int j = 0; j < n; j++) {
                board[i][j] =cs[j];
            }
        }
    }


    void BFS() {
        que.add(new int[]{x, y});

        while (!que.isEmpty()) {
            now = que.pollFirst();
            x = now[0];
            y = now[1];

            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (!visited[nx][ny] && board[nx][ny] == color) {
                        visited[nx][ny] = true;
                        que.add(new int[] {nx, ny});
                    }
                }
            }

        }

    }


    void solve() throws IOException {
        makeSettings();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                x = i;
                y = j;
                color = board[x][y];
                if (!visited[x][y]){
                    visited[x][y] = true;
                    BFS();
                    counts[colorMap.get(color)]++;
                }

            }
        }
        int value2 = counts[0]+counts[2];
        int value1 = Arrays.stream(counts).sum();

        System.out.print(value1 + " ");

        visited = new boolean[n][n];
        counts = new int[2];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'G') {
                    board[i][j] = 'R';
                }
            }
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                x = i;
                y = j;
                color = board[x][y];
                if (!visited[x][y]){
                    visited[x][y] = true;
                    BFS();
                    counts[colorMap.get(color)]++;
                }

            }
        }
        value2 = counts[0];
        value1 = Arrays.stream(counts).sum();

        System.out.println(value1);

    }


    public static void main(String[] args) throws IOException {
        new 적록색약().solve();
    }
}
