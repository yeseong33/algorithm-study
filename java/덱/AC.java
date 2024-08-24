package 덱;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class AC {
    BufferedReader br;
    StringBuilder sr;
    int t, n;
    String request;
    Deque<Integer> deque;

    void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        deque = new ArrayDeque<>();
        sr = new StringBuilder();
    }

    void solve() throws IOException {
        makeSettings();
        for (int c = 0; c < t; c++) {
            boolean mode = true;
            boolean error = false;
            request = br.readLine();
            n = Integer.parseInt(br.readLine());
            StringTokenizer s = new StringTokenizer(br.readLine(), "[],");
            deque.clear();

            for(int i = 0; i < n; i++) {
                deque.add(Integer.parseInt(s.nextToken()));
            }

            for (char req : request.toCharArray()) {
                if (req == 'R') {
                    mode = !mode;
                } else {
                    if (deque.isEmpty()) {
                        sr.append("error\n");
                        error = true;
                        break;
                    }
                    if (mode) {
                        deque.removeFirst();
                    } else {
                        deque.removeLast();
                    }
                }
            }

            if (!error) {
                sr.append('[');
                if (!deque.isEmpty()) {
                    if (mode) {
                        sr.append(deque.pollFirst());
                        while (!deque.isEmpty()) {
                            sr.append(',').append(deque.pollFirst());
                        }
                    } else {
                        sr.append(deque.pollLast());
                        while (!deque.isEmpty()) {
                            sr.append(',').append(deque.pollLast());
                        }
                    }
                }
                sr.append(']').append('\n');
            }
        }
        System.out.println(sr);
    }

    public static void main(String[] args) throws IOException {
        new AC().solve();
    }
}
