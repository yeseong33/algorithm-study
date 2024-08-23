package 스택;

import java.io.*;
import java.util.*;

public class 스택수열 {
    BufferedReader br;
    StringBuilder bw;
    Stack<Integer> num;
    int n, now;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new StringBuilder();
        num = new Stack<>();
        n = Integer.parseInt(br.readLine());
        now = 1;
    }

    boolean solve() throws IOException {
        makeSettings();
        int value;
        for (int i = 0; i < n; i++) {
            value = Integer.parseInt(br.readLine());
            if (value >= now) {
                while (value >= now) {
//                    bw.write("+\n");
                    bw.append("+\n");
                    num.push(now);
                    now++;
                }
                num.pop();
//                bw.write("-\n");
                bw.append("-\n");
            } else if (now > value) {
                int ti = num.pop();
                if (ti != value) {
                    System.out.println("NO");
                    return false;
                }
//                bw.write("-\n");
                bw.append("-\n");
            }
        }
        System.out.println(bw);
        return true;


    }

    public static void main(String[] args) throws IOException {
        new 스택수열().solve();

    }
}
