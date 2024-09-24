package 백트레킹;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class 로또 {

    int k, choiceSize;
    int[] visited, nums;
    BufferedReader br;
    BufferedWriter bw;
    StringTokenizer st;
    Stack<Integer> que;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        choiceSize = 6;
    }

    boolean testSettings() throws IOException {
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        if (k == 0) {
            return true;
        }
        nums = new int[k];
        visited = new int[k];
        que = new Stack<>();
        for (int i = 0; i < k; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        return false;
    }


    boolean isFull() {
        if (que.size() == choiceSize) {
            return true;
        }
        return false;
    }

    void nextNum(int start) throws IOException {
        for (int i = start; i < k; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                que.add(nums[i]);
                BT(i+1);
                que.pop();
                visited[i] = 0;
            }

        }
    }


    void BT(int start) throws IOException {
        if (isFull()) {
            String result = que.stream().map(String::valueOf).collect(Collectors.joining(" "));
            bw.write(result);
            bw.newLine();
            return;
        }
        nextNum(start);
    }


    void solve() throws IOException {
        makeSettings();
        while (true) {
            if(testSettings()) {
                break;
            };
            BT(0);
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }


    public static void main(String[] args) throws IOException {
        new 로또().solve();
    }
}
