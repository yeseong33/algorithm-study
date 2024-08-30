package BFS;

import java.io.*;
import java.util.*;

public class 텀프로젝트 {


    BufferedReader br;
    BufferedWriter bw;
    StringTokenizer st;
    int n, t;
    Deque<Integer> que;
    boolean[] visited;
    int[] board, path;
    
    void startSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        t = Integer.parseInt(br.readLine());
    }


    void BFS() {
        Stack<Integer> stack = new Stack<>();
        while (!que.isEmpty()) {
            int now = que.pollFirst();

            if (path[now] == -2) {
                while (!stack.isEmpty()) {
                    int value = stack.pop();
                    visited[value] = false;
                    path[value] = -2;
                }
                return;
            }

            if (!visited[now]){
                visited[now] = true;
                que.add(board[now]);
                stack.add(now);
            } else {
                int value;
                while (visited[now]) {
                    value = stack.pop();
                    visited[value] = false;
                    path[value] = now;
                }
                while (!stack.isEmpty()) {
                    value = stack.pop();
                    visited[value] = false;
                    path[value] = -2;

                }
            }
        }
    }

    void makeTeam() throws IOException {
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        visited = new boolean[n];

        path = new int[n];
        Arrays.fill(path, -1);
        board = new int[n];
        que = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(st.nextToken())-1;
            board[i] = value;
            if (board[i] == i) {
                path[i] = i;
            }
        }

        for (int i = 0; i < n; i++) {
            if (path[i] == -1){
                que.add(i);
                BFS();
            }
        }
        bw.write(Arrays.stream(path).filter(value -> value == -2).count()+"\n");
    }



    void solve() throws IOException {
        startSettings();
        for (int i = 0; i < t; i++) {
            makeTeam();
        }
        bw.flush();
        bw.close();

    }


    public static void main(String[] args) throws IOException {
        new 텀프로젝트().solve();
    }
}
//
//1 2 3 4 5
//2 3 4 5 42
//7
//3 1 3 7 3 4 6
//8
//1 2 3 4 5 6 7 8

//0  1  2 3 4 5 6
//-2 -2 2 6 2 3 5