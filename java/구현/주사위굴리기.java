package 구현;


import java.io.*;
import java.util.*;

public class 주사위굴리기 {

    int n, m, x, y, k;
    int[][] board, dir;
    BufferedWriter bw;
    BufferedReader br;
    StringTokenizer st;
    List<Integer> requests;
    Dice dice;



    class Dice {

        int top, bottom, right, left, front, back, nx, ny, request;
        int[] now;

        public Dice(int i, int j) {
            this.now = new int[]{i, j};
        }

        void setRequest(int value) {
            this.request = value;
        }

        void move() {
            if (request == 1) {
                moveRight();
            } else if (request == 2) {
                moveLeft();
            } else if (request == 3) {
                moveTop();
            } else if (request == 4) {
                moveBottom();
            }
        }

        void moveRight() {
            int start = top;
            top = left;
            left = bottom;
            bottom = right;
            right = start;
        }

        void moveLeft() {
            int start = top;
            top = right;
            right = bottom;
            bottom = left;
            left = start;
        }

        void moveTop() {
            int start = top;
            top = front;
            front = bottom;
            bottom = back;
            back = start;
        }

        void moveBottom() {
            int start = top;
            top = back;
            back = bottom;
            bottom = front;
            front = start;
        }

        void check() {
            if (board[now[0]][now[1]] == 0) {
                board[now[0]][now[1]] = bottom;
            } else {
                bottom = board[now[0]][now[1]];
                board[now[0]][now[1]] = 0;
            }

        }

        boolean canMove() {
            nx = now[0] + dir[request][0];
            ny = now[1] + dir[request][1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                now = new int[]{nx, ny};
                return true;
            }
            return false;
        }

    }


    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        dir = new int[][]{{0, 0}, {0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        requests = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            String value = st.nextToken();
            requests.add(Integer.parseInt(value));
        }


        dice = new Dice(x, y);
    }



    void solve() throws IOException {

        makeSettings();


        for (int request : requests) {
            dice.setRequest(request);
            if (dice.canMove()) {
                dice.move();
                dice.check();
                bw.write(String.valueOf(dice.top) + "\n");
            }
        }

        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new 주사위굴리기().solve();
    }
}
