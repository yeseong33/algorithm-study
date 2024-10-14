package 구현;


import java.io.*;
import java.util.*;

public class 사다리조작 {

    int n, m, h, a, b, x, y, minValue;
    int[][] visited;

    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        visited = new int[h][n];
        minValue = h*n;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken())-1;
            b = Integer.parseInt(st.nextToken())-1;

            visited[a][b] = 1;
        }

    }

    void BT(int value, int count) {

        if (check()) {
            if (minValue > count) {
                minValue = count;
            }
            return;
        }

        if (count >= 3 || count >= minValue) {
            return;
        }


        for (int i = value; i < (n-1) * h; i++) {
            int x = i / (n-1);
            int y = i % (n-1);
            if (visited[x][y] == 0) {
                if (y > 0 && visited[x][y - 1] == 1) continue;
                if (y < n - 2 && visited[x][y + 1] == 1) continue;
                visited[x][y] = 1;
                BT(i + 1, count + 1);
                visited[x][y] = 0;
            }
        }
    }

    boolean selectCondition(int x, int y) {
        return visited[x][y] != 1;
    }


    boolean check() {
        for (int i = 0; i < n; i++) {
            int pos = i;
            for (int j = 0; j < h; j++) {
                if (pos > 0 && visited[j][pos - 1] == 1) pos--;
                else if (pos < n - 1 && visited[j][pos] == 1) pos++;
            }
            if (pos != i) return false;
        }
        return true;
    }



    void solve() throws IOException {
        makeSettings();
        BT(0, 0);
        if (minValue == n * h) {
            System.out.println(-1);
        } else {
            System.out.println(minValue);
        }
    }


    public static void main(String[] args) throws IOException {
        new 사다리조작().solve();
    }
}
