package 스택;

import java.io.*;
import java.util.*;

public class 제로 {
    int k, total;
    Stack<Integer> stack;
    BufferedReader br;

    void makeSettings() throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        stack = new Stack<>();
        total = 0;
    }

    void solve() throws IOException {
        makeSettings();
        int value;
        for (int i = 0; i < k; i++) {
            value = Integer.parseInt(br.readLine());
            if (value == 0) {
                stack.pop();
            } else {
                stack.push(value);
            }
        }

        for (int s : stack) {
            total += s;
        }
        System.out.println(total);
    }


    public static void main(String[] args) throws IOException {
        new 제로().solve();
    }
}
