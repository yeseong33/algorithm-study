package 수학;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class 숫자카드 {

    int n, m ;
    List<Integer> numbers, cards;
    HashMap<Integer, Integer> map;
    BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        new 숫자카드().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < m; i++) {
            bw.write(map.get(cards.get(i)) + " ");
        }

        bw.flush();
        bw.close();
    }

    private void makeSettings() throws IOException {

        map = new HashMap<>();
        numbers = new ArrayList<>();
        cards = new ArrayList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int value = Integer.parseInt(st.nextToken());
            cards.add(value);
            map.put(value, 0);
        }

        for (int i = 0; i < n; i++) {
            int value = numbers.get(i);
            map.put(value, 1);
        }
    }
}
