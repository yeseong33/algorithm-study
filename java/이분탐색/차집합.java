package 이분탐색;

import java.io.*;
import java.util.*;


public class 차집합 {

    BufferedWriter bw;
    List<Long> aSet, bSet;
    int count, a, b ;
    HashMap<Long, Integer> counting;
    Queue<Long> priorityQue;


    public static void main(String[] args) throws IOException{
        new 차집합().solve();
    }

    private void solve() throws IOException{
        makeSettings();
        compareSet();
        if (count == 0) {
            bw.write("0\n");
        } else {
            bw.write(count + "\n");
            while (!priorityQue.isEmpty()) {
                bw.write(priorityQue.poll() + " ");
            }
        }
        bw.flush();
        bw.close();
    }

    private void compareSet() throws IOException {
        for (int i = 0; i < a; i++) {
            Long value = aSet.get(i);
            if (counting.get(value) == null) {
                count++;
                priorityQue.add(value);
            }
        }
    }

    private void makeSettings() throws IOException {

        count = 0;

        aSet = new ArrayList<>();
        bSet = new ArrayList<>();

        priorityQue = new PriorityQueue<>();

        counting = new HashMap<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());


        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < a; i++) {
            Long value = Long.parseLong(st.nextToken());
            aSet.add(value);
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < b; i++) {
            Long value = Long.parseLong(st.nextToken());
            counting.put(value, 1);

        }

    }


}
