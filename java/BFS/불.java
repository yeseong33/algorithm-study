package BFS;

import java.io.*;
import java.util.*;

public class 불 {

    BufferedReader br;
    BufferedWriter bw;
    StringTokenizer st;
    int n, m, count, fCount, x, y, nx, ny, t;
    int[] now;
    int[][] visited, dir;
    boolean isEnd, everEnd;
    HashMap<Character, Integer> mapping;
    Deque<int[]> que, fQue, newQue;



    void makeSettings() throws IOException {
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        visited = new int[n][m];
        dir = new int[][] {new int[]{1, 0}, new int[]{0, 1},new int[]{0, -1},new int[]{-1, 0}};
        count = 0;
        isEnd = false;
        everEnd = false;
        que = new LinkedList<>();
        fQue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            char[] arr = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                visited[i][j] = mapping.get(arr[j]);
                if (arr[j] == '*') {
                    visited[i][j] = 1;
                    fQue.add(new int[]{i, j});
                } else if (arr[j] == '@') {
                    que.add(new int[]{i, j});
                }
            }
        }
    }

    Deque<int[]> BFS(Deque<int[]> que, Boolean isFire) {
        newQue = new LinkedList<>();
        if (que.isEmpty() && !isFire) {
            everEnd = true;
            return newQue;
        }
        while (!que.isEmpty()) {
            now = que.poll();
            x = now[0];
            y = now[1];

            for (int i = 0; i < 4; i++) {
                nx = x + dir[i][0];
                ny = y + dir[i][1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (isFire) {
                        if (visited[nx][ny] != 1) {
                            visited[nx][ny] = 1;
                            newQue.add(new int[]{nx, ny});
                        }
                    } else {
                        if (visited[nx][ny] == 0) {
                            visited[nx][ny] = 3;
                            newQue.add(new int[]{nx, ny});
                        }
                    }
                } else {
                    if (!isFire) {
                        isEnd = true;
                        return newQue;
                    }
                }
            }
        }
        return newQue;
    }

    void solve() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        t = Integer.parseInt(br.readLine());
        mapping = new HashMap<>();
        mapping.put('.', 0);
        mapping.put('#', 1);
        mapping.put('*', 2);
        mapping.put('@', 3);

        for (int i = 0; i < t; i++) {
            makeSettings();
            while (!isEnd && !everEnd) {
                count++;
                fQue = BFS(fQue, true);
                que = BFS(que, false);

            }
            if (isEnd) {
                bw.write(count + "\n");
            } else {
                bw.write("IMPOSSIBLE\n");
            }
        }
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new 불().solve();
    }
}
