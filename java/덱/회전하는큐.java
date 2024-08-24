package 덱;

import java.io.*;
import java.util.*;

import static java.lang.Math.min;

public class 회전하는큐 {
    int n, m, count, totalCount, size;
    int[] quest;
    Deque<Integer> deque;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        quest = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        deque = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            deque.addLast(i);
        }
        count = 0;
        totalCount = 0;
        size = 0;
    }


    int rotation(int find) {
        int value;
        int count = 0;
        for (int i = 0; i < deque.size(); i++) {
            value = deque.removeFirst();
            if (value == find) {
                return count;
            }
            count++;
            deque.addLast(value);
        }
        return -1;
    }

    void solve() throws IOException {
        makeSettings();

        for (int find : quest) {
            size = deque.size();
            count = rotation(find);
            count = min(count, size-count);
            totalCount += count;
        }
        System.out.println(totalCount);
    }


    public static void main(String[] args) throws IOException {
        new 회전하는큐().solve();
    }
}
