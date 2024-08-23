package 스택;

import java.io.*;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class 탑 {
    int n;
    Stack<int[]> stack, waiting;
    int[] result;
    BufferedWriter bw;
    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        stack = new Stack<>();
        waiting = new Stack<>();
        result = new int[n+1];
        int now = 1;
        while (st.hasMoreTokens()) {
            stack.push(new int[] {Integer.parseInt(st.nextToken()), now} );
            now++;
        }
    }


    void solve() throws IOException {
        makeSettings();
        while (!stack.isEmpty()) {
            if (!waiting.isEmpty()) {
                if (stack.peek()[0] > waiting.peek()[0]) {
                    while (!waiting.isEmpty() && stack.peek()[0] > waiting.peek()[0]) {
                        result[waiting.pop()[1]] = stack.size();
                    }

                }
            }
            waiting.push(stack.pop());
        }

        for (int i=1; i<=n; i++) {
            bw.write(result[i]+ " ");
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 탑().solve();
    }
}
