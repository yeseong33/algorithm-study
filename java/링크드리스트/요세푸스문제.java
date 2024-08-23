package 링크드리스트;

import java.io.*;
import java.util.*;

public class 요세푸스문제 {
    int n, k, num;
    LinkedList<Integer> list;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        list = new LinkedList<>();
        for (int i = 1; i < n+1; i++) {
            list.add(i);
        }
        for (int i = 0; i < k-1; i++) {
            list.add(list.removeFirst());
        }
    }

    void solve() throws IOException {
        makeSettings();
        System.out.print("<");
        while (list.size() > 1) {
            System.out.print(list.removeFirst() + ", ");
            for (int i = 0; i < k-1; i++) {
                list.add(list.removeFirst());
            }
        }
        System.out.print(list.poll() + ">");


    }

    public static void main(String[] args) throws IOException {
        new 요세푸스문제().solve();
    }
}
