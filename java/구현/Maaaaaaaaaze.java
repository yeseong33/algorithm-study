package 구현;


import java.io.*;
import java.util.*;

public class Maaaaaaaaaze {

    int minCount;
    int[][] plate, dir;
    boolean[] select;
    boolean[][] visitedPlate;
    int[][][] origin, board;
    boolean[][][] originVisited, visited, V;
    StringTokenizer st;
    Stack<Integer> stack;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new int[5][5][5];
        V = new boolean[5][5][5];
        visited = new boolean[5][5][5];
        stack = new Stack<>();
        minCount = 9999999;
        for (int z = 0; z < 5; z++) {
            for (int x = 0; x < 5; x++) {
                st = new StringTokenizer(br.readLine());
                for (int y = 0; y < 5; y++) {
                    int value = Integer.parseInt(st.nextToken());
                    board[z][x][y] = value;
                    if (value == 0) {
                        V[z][x][y] = true;
                    }
                }
            }
        }
        select = new boolean[5];
        dir = new int[][] {{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}};

    }


    void makeBoard(int d) {
        if (d == -1) {
            if (!checkEntranceAndExit()) return;
            for (int z = 0; z < 5; z++) {
                for (int x = 0; x < 5; x++) {
                    for (int y = 0; y < 5; y++) {
                        visited[z][x][y] = originVisited[z][x][y];
                    }
                }
            }

            findRoute();
            return;
        }

        for (int i = 0; i < 4; i++) {
            rotation(d);
            makeBoard(d-1);
        }
    }

    boolean checkEntranceAndExit() {
        return origin[0][0][0] == 1 && origin[4][4][4] == 1;
    }

    void rotation(int d) {
        plate = origin[d];
        visitedPlate = originVisited[d];
        int[][] newPlate = new int[5][5];
        boolean[][] newVisitedPlate = new boolean[5][5];

        for (int j = 0; j < 5; j++) {
            for (int i = 0; i < 5; i++) {
                newPlate[i][j] = plate[4 - j][i];  // 90도 시계 방향 회전
                newVisitedPlate[i][j] = visitedPlate[4 - j][i];  // visited 배열도 함께 회전
            }
        }

        origin[d] = newPlate;
        originVisited[d] = newVisitedPlate;
    }


    void findRoute() {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 0, 0}); // {z, x, y, count}

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int z = current[0], x = current[1], y = current[2], count = current[3];

            // 현재 카운트가 최소 카운트보다 크면 반환
            if (minCount <= count) {
                continue;
            }

            // 목표 지점에 도달한 경우
            if (z == 4 && x == 4 && y == 4) {
                minCount = count;
                return;
            }

            // 모든 방향으로 탐색
            for (int i = 0; i < 6; i++) {
                int nz = z + dir[i][0];
                int nx = x + dir[i][1];
                int ny = y + dir[i][2];

                if (condition(nz, nx, ny)) {
                    visited[nz][nx][ny] = true; // 방문 표시
                    queue.add(new int[]{nz, nx, ny, count + 1}); // 다음 위치와 카운트
                }
            }
        }
    }

    boolean condition(int nz, int nx, int ny) {
        return nz >= 0 && nz < 5 && nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && !visited[nz][nx][ny] && origin[nz][nx][ny] == 1;
    }

    void selectOrder() {


        if (stack.size() == 5) {
            makeOrigin();
            makeBoard(4);
            return;
        }

        for (int i = 0; i < 5; i++) {
            if (select[i]) continue;
            select[i] =true;
            stack.add(i);
            selectOrder();
            stack.pop();
            select[i] =false;
        }

    }

    void makeOrigin() {
        origin = new int[5][5][5];
        originVisited = new boolean[5][5][5];

        for (int z = 0; z < 5 ;z++) {
            int k = stack.get(z);
            int[][] tmp = board[k];
            boolean[][] tmp2 = V[k];
            origin[z] = tmp;
            originVisited[z] = tmp2;
        }
    }

    void solve() throws IOException {
        makeSettings();


        selectOrder();


        if (minCount == 9999999) {
            minCount = -1;
        }
        System.out.println(minCount);

    }


    public static void main(String[] args) throws IOException {
        new Maaaaaaaaaze().solve();
    }
}
