package 큐;

import java.io.*;
import java.util.*;

public class 큐 {
    BufferedReader br;
    BufferedWriter bw;
    int n;
    Deque<Integer> que;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        que = new LinkedList<>();
    }

    void solve() throws IOException {
        makeSettings();
        String line = "";
        String[] req;
        String method;
        for (int i = 0; i < n; i++) {
            line = br.readLine();
            req = line.split(" ");
            method = req[0];
            if (method.equals("push")) {
                que.add(Integer.parseInt(req[1]));
            } else if (method.equals("pop")) {
                if (que.isEmpty()){
                    bw.write("-1\n");
                    continue;
                }
                bw.write(que.removeFirst() + "\n");
            } else if (method.equals("size")) {
                bw.write(que.size() + "\n");
            } else if (method.equals("empty")) {
                if (que.isEmpty()) {
                    bw.write(1 + "\n");
                } else {
                    bw.write(0 + "\n");
                }
            } else if (method.equals("front")) {
                if (que.isEmpty()){
                    bw.write("-1\n");
                    continue;
                }
                bw.write(que.getFirst()+"\n");
            } else {
                if (que.isEmpty()){
                    bw.write("-1\n");
                    continue;
                }
                bw.write(que.getLast()+"\n");
            }
        }
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new 큐().solve();
    }
}
