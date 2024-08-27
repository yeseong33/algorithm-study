package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 쇠막대기 {

    String req;
    int steal, total;
    Stack<Character> que;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        req = br.readLine();
        steal = 0;
        total = 0;
        que = new Stack<>();
    }

    void slice() {
        boolean isR = false;
        for (char c : req.toCharArray()) {
            if (c == '(') {
                isR = true;
                que.add(c);
                steal += 1;
                continue;
            }
            if (!que.isEmpty() && c == ')' && que.peek() == '(') {
                if (isR) {
                    isR = false;
                    steal -= 1;
                    total += steal;
                } else {
                    total +=1;
                    steal -= 1;
                }
                que.pop();
            }
        }
        System.out.println(total);
    }

    void solve() throws IOException {
        makeSettings();
        slice();
    }


    public static void main(String[] args) throws IOException {
        new 쇠막대기().solve();

    }
}
