package 구현;


import java.io.*;
import java.util.*;


public class 테트로미노 {

    int n, m, maxValue;
    int[] size;
    int[][] board, block_3_2, block_2_3, blockSize;
    boolean[][] piece;

    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        maxValue = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        block_3_2 = new int[][]{{0, 0, 1, 2}, {1, 0, 0, 2}, {0, 0, 0, 2}, {1, 0, 1, 2}, {0, 0, 0, 1}, {1, 0, 1, 1}, {0, 1, 0, 2}, {1, 1, 1, 2}};
        block_2_3 = new int[][]{{0, 1, 2, 0}, {0, 0, 2, 1}, {0, 0, 2, 0}, {0, 1, 2, 1}, {0, 0, 1, 0}, {0, 1, 1, 1}, {1, 0, 2, 0}, {1, 1, 2, 1}};
        blockSize = new int[][] {{3, 2}, {2, 3}, {4, 1}, {1, 4}, {2, 2}};

    }


    void select() {
        for (int i = 0; i < blockSize.length; i++) {
            int[] now = blockSize[i];
            piece = new boolean[now[1]][now[0]];

            size = now;
            if (i == 0) {
                for (int[] k : block_3_2) {
                    piece[k[0]][k[1]] = true;
                    piece[k[2]][k[3]] = true;
                    findMaxSum();
                    piece[k[0]][k[1]] = false;
                    piece[k[2]][k[3]] = false;
                }
            } else if (i == 1) {
                for (int[] k : block_2_3) {
                    piece[k[0]][k[1]] = true;
                    piece[k[2]][k[3]] = true;
                    findMaxSum();
                    piece[k[0]][k[1]] = false;
                    piece[k[2]][k[3]] = false;
                }
            } else {
                findMaxSum();
            }
        }

    }

    void findMaxSum() {
        for (int i = 0; i < n-size[1]+1; i++){
            for (int j = 0; j < m - size[0] + 1; j++) {
                int value = sumValue(i, j);
                if (maxValue < value) {
                    maxValue = value;
                }
            }
        }
    }

    int sumValue(int startX, int startY) {
        int value = 0;
        for (int i = startX; i < startX+size[1]; i++){
            for (int j = startY; j < startY + size[0]; j++) {
                if (piece[i-startX][j-startY]) continue;
                value += board[i][j];
            }
        }
        return value;
    }



    void solve() throws IOException {
        makeSettings();
        select();
        System.out.println(maxValue);
    }

    public static void main(String[] args) throws IOException {
        new 테트로미노().solve();
    }
}
