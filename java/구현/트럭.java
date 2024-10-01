package 구현;


import java.io.*;
import java.util.*;

public class 트럭 {

    int n, w, l, passCount, count, weight;
    Queue<Integer> bridge, stage;
    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        weight = 0;

        bridge = new LinkedList<>();
        stage = new LinkedList<>();

        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            stage.add(Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < w; i++) {
            bridge.add(0);
        }
    }

    void move() {
        int value = bridge.poll();
        weight -= value;
        if (value != 0) {
            passCount++;
        }
    }

    void intoBridge() {
        if (stage.peek() == null) return;
        if (weight + stage.peek() <= l) {
            weight += stage.peek();
            bridge.add(stage.poll());
        } else {
            bridge.add(0);
        }
    }

    void solve() throws IOException {
        makeSettings();
        while (passCount != n) {
            move();
            intoBridge();
            count++;
        }
        System.out.println(count);
    }

    public static void main(String[] args) throws IOException {
        new 트럭().solve();
    }
}
