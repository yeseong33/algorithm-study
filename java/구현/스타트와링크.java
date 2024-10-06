package 구현;


import java.io.*;
import java.util.*;

public class 스타트와링크 {

    int n, minValue;
    boolean[] visited;
    int[][] board;
    StringTokenizer st;
    Stack<Integer> stack;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new boolean[n];
        minValue = 1000000000;
    }

    void makeTeam(int d, int idx) {
        if (d == n/2) {
            int result = score();
            if (minValue > result) {
                minValue = result;
            }
            return;
        }

        for (int i = idx; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                makeTeam(d+1, i+1);
                visited[i] = false;
            }
        }
    }

    int score() {
        int total1 = 0;
        int total2 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (i == j) continue;
                if (visited[i] && visited[j]) {
                    total1 += board[i][j] + board[j][i];
                } else if (!visited[i] && !visited[j]) {
                    total2 += board[i][j] + board[j][i];
                }
            }
        }
        return Math.abs(total1 - total2);
    }



    void solve() throws IOException {
        makeSettings();
        makeTeam(0, 0);
        System.out.println(minValue);
    }

    public static void main(String[] args) throws IOException {
        new 스타트와링크().solve();
    }
}
