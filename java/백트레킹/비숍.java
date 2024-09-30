package 백트레킹;

import java.io.*;
import java.util.*;

public class 비숍 {
    int n, mCount, mCount2;  // 짝수 칸과 홀수 칸 각각의 최대 비숍 수
    int[][] board;           // 체스판
    boolean[] visited1, visited2; // 두 대각선에 대한 방문 기록

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        visited1 = new boolean[2 * n];  // "/" 방향 대각선
        visited2 = new boolean[2 * n];  // "\" 방향 대각선
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        mCount = 0;
        mCount2 = 0;
    }

    void BT(int x, int y, int count, boolean isOdd) {
        if (y >= n) {
            x++;
            y = (y % 2 == 0) ? 1 : 0;  // 다음 행에서는 다른 시작점에서 탐색
        }
        if (x >= n) {
            if (isOdd) {
                mCount = Math.max(mCount, count);  // 홀수 칸의 최댓값 업데이트
            } else {
                mCount2 = Math.max(mCount2, count);  // 짝수 칸의 최댓값 업데이트
            }
            return;
        }

        // 비숍을 놓을 수 있는지 확인
        if (board[x][y] == 1 && !visited1[x + y] && !visited2[x - y + n]) {
            // 비숍을 놓고 대각선 방문 처리
            visited1[x + y] = true;
            visited2[x - y + n] = true;
            BT(x, y + 2, count + 1, isOdd);  // 다음 칸 탐색
            // 방문 처리 해제
            visited1[x + y] = false;
            visited2[x - y + n] = false;
        }

        // 비숍을 놓지 않는 경우 다음 칸 탐색
        BT(x, y + 2, count, isOdd);
    }

    void solve() throws IOException {
        makeSettings();
        // 짝수 칸 탐색 (0, 0부터 시작)
        BT(0, 0, 0, false);
        // 홀수 칸 탐색 (0, 1부터 시작)
        BT(0, 1, 0, true);
        // 두 경우의 합이 최종 답
        System.out.println(mCount + mCount2);
    }

    public static void main(String[] args) throws IOException {
        new 비숍().solve();
    }
}
