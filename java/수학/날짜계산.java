package 수학;

import java.io.*;
import java.util.StringTokenizer;

public class 날짜계산 {

    int e, s, m, te, ts, tm;

    public static void main(String[] args) throws IOException{
        new 날짜계산().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        findYear();
    }

    private void findYear() {
        int count = 0;
        while (true) {
            te = te % 15 + 1;
            ts = ts % 28 + 1;
            tm = tm % 19 + 1;
            count++;
            if (e == te && s == ts && m == tm) {
                break;
            }
        }
        System.out.println(count);
    }

    private void makeSettings() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        e = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        te = 0;
        ts = 0;
        tm = 0;
    }
}
