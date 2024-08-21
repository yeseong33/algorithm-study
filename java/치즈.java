import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 치즈 {

    int n, m, count;
    int[][] board, visited;
    Deque<int[]> que = new LinkedList<>();
    ArrayList<int[]> dir = new ArrayList<>(Arrays.asList(
            new int[]{0, 1},
            new int[]{1, 0},
            new int[]{0, -1},
            new int[]{-1, 0}
    ));


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        count = 0;
        board = new int[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (!(i > 0 && i < n - 1 && j > 0 && j < m - 1)) {
                    que.add(new int[]{i, j});
                    visited[i][j] = 1;
                }
            }
        }
    }

    void melt() {
        while (!que.isEmpty()) {
            int[] now = que.removeLast();
            for (int[] dir : dir) {
                int x = now[0] + dir[0];
                int y = now[1] + dir[1];
                if (x >= 0 && x < n && y >= 0 && y < m) {
                    if (visited[x][y] == 0) {
                        if (board[x][y] == 0) {
                            visited[x][y] = 1;
                            que.add(new int[]{x, y});
                        } else {
                            board[x][y] += 1;
                        }
                    }

                }
            }
        }
    }

    boolean isEnd() {
        int oneCount = 0;
        if (count == 0) return true;
        int[][] newVisited = new int[n][m];
        LinkedList<int[]> newQue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] >= 3){
                    board[i][j] = 0;
                    newVisited[i][j] = 1;
                    newQue.add(new int[]{i, j});
                } else if (board[i][j] == 2){
                    board[i][j] = 1;
                    oneCount++;
                } else if(board[i][j] == 1){
                    oneCount++;
                }
            }
        }
        visited = newVisited;
        que = newQue;
        return oneCount != 0;
    }

    void run() throws IOException {
        makeSettings();
        while (isEnd()) {
            melt();
            count++;
        }
        System.out.println(count);
    }


    public static void main(String[] args) throws IOException {
        new 치즈().run();
    }

}
