package 백트레킹;


import java.io.*;
import java.util.*;

public class Graaaaarden {

    int n, m, g, r, greenCount, redCount, count, x, y, nx, ny, nc, twoCount, origin, time;
    int[][] board, checkBoard, dir, times;
    boolean[] visited;
    boolean[][] greenVisited, redVisited;

    Stack<int[]> potions, nextQue;
    ArrayList<int[]>  grounds;

    PriorityQueue<int[]> que;

    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        grounds = new ArrayList<>();
        board = new int[n][m];
        twoCount = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (value == 2) {
                    twoCount++;
                    grounds.add(new int[]{i, j});
                }
                board[i][j] = value;
            }
        }


        potions = new Stack<>();
        visited = new boolean[twoCount];


        greenCount = g;
        redCount = r;
        dir = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        que = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[3], b[3]); // 우선순위: a[0]과 b[0]의 크기 비교
            }
        });
    }

    boolean isCheck() {
        return redCount == 0 && greenCount == 0;
    }

    void green(int[] ground, int next) {
        if (greenCount < 1) return;
        potions.add(new int[] {ground[0], ground[1], 1});
        greenCount -= 1;
        BT(next);
        greenCount += 1;
        potions.pop();
    }

    void red(int[] ground, int next) {
        if (redCount < 1) return;
        potions.add(new int[] {ground[0], ground[1], 2});
        redCount -= 1;
        BT(next);
        redCount += 1;
        potions.pop();
    }

    void nextPotion(int start) {
        for (int i = start; i < twoCount; i++) {
            int[] ground = grounds.get(i);
            if (!visited[i]) {
                visited[i] = true;
                green(ground, i+1);
                red(ground, i+1);
                visited[i] = false;
            }
        }
    }

    void BT(int start) {
        if (isCheck()) {
            check();
            if (nc > count) {
                count = nc;
            }
            return;
        }

        nextPotion(start);
    }


    void checkSettings() {

        checkBoard = new int[n][m];
        greenVisited = new boolean[n][m];
        redVisited = new boolean[n][m];
        times = new int[n][m];

        for (int[] now : potions) {
            checkBoard[now[0]][now[1]] = now[2];
            if (now[2] == 1) {
                greenVisited[now[0]][now[1]] = true;
            } else {
                redVisited[now[0]][now[1]] = true;
            }
            times[now[0]][now[1]] = 1;
            que.add(new int[]{now[2], now[0], now[1], 1});
        }
    }

    boolean condition() {
        // 기존에 이미 도달했을 때의 처리 및 타임스탬프 확인 추가
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && board[nx][ny] != 0) {
            if (checkBoard[nx][ny] == 0) {
                return true; // 아직 방문하지 않은 경우
            } else if (checkBoard[nx][ny] == 1 && origin == 2 && times[nx][ny] == time+1) {
                // 초록색 배양액이 먼저 도달했고, 빨간색 배양액이 다음 시간에 도달한 경우 꽃이 핌
                return true;
            } else if (checkBoard[nx][ny] == 2 && origin == 1 && times[nx][ny] == time+1) {
                // 빨간색 배양액이 먼저 도달했고, 초록색 배양액이 다음 시간에 도달한 경우 꽃이 핌
                return true;
            }
        }
        return false;
    }

    void check() {
        checkSettings();
        nc = 0;
        while (!que.isEmpty()) {
            int[] now = que.poll();
            origin = now[0];
            x = now[1];
            y = now[2];
            time = now[3];
            if (checkBoard[x][y] == 4) continue;
            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];
                if (condition()) {
                    if (origin == 1) { // Green 배양액
                        if (redVisited[nx][ny] && checkBoard[nx][ny] != 4) {
                            // 꽃이 이미 핀 곳이 아니라면 꽃을 핌
                            checkBoard[nx][ny] = 4; // 꽃이 핌
                            nc++;
                        } else if (checkBoard[nx][ny] == 0) {
                            checkBoard[nx][ny] = 1;
                            greenVisited[nx][ny] = true;
                            times[nx][ny] = time + 1; // 방문 시간 기록
                            que.add(new int[]{origin, nx, ny, time + 1});
                        }
                    } else if (origin == 2) { // Red 배양액
                        if (greenVisited[nx][ny] && checkBoard[nx][ny] != 4) {
                            checkBoard[nx][ny] = 4; // 꽃이 핌
                            nc++;
                        } else if (checkBoard[nx][ny] == 0) {
                            checkBoard[nx][ny] = 2;
                            redVisited[nx][ny] = true;
                            times[nx][ny] = time + 1; // 방문 시간 기록
                            que.add(new int[]{origin, nx, ny, time + 1});
                        }
                    }
                }
            }
        }
    }


    void solve() throws IOException {
        makeSettings();
        BT(0);
        System.out.println(count);
    }

    public static void main(String[] args) throws IOException {
        new Graaaaarden().solve();
    }
}
