package 스택활용;

import java.io.*;
import java.util.*;

public class 좋은단어 {
    BufferedWriter bw;
    BufferedReader br;
    int n, count;
    String word;
    Stack<Character> stack;


    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        stack = new Stack<>();
    }

    boolean isGoodWord() {
        for (char w : word.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == w) {
                stack.pop();
            } else {
                stack.add(w);
            }
        }
        return stack.isEmpty();
    }

    void solve() throws IOException {
        makeSettings();
        for (int i = 0; i < n; i++) {
            word = br.readLine();
            if (isGoodWord()) {
                count++;
            }
            stack.clear();
        }
        System.out.println(count);
    }


    public static void main(String[] args) throws IOException {
        new 좋은단어().solve();
    }
}
