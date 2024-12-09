package 수학;

import java.io.*;
import java.math.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class GCD합 {

    BufferedReader br;
    BufferedWriter bw;
    int t;
    BigInteger total;
    List<BigInteger> numbers;

    public static void main(String[] args) throws IOException {
        new GCD합().solve();
    }

    private void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < t; i++) {
            roundSettings();
            gcdSum();
            bw.write(total + "\n");
        }

        bw.flush();
        bw.close();
    }

    private void roundSettings() throws IOException {
        total = BigInteger.valueOf(0);
        numbers = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            numbers.add(BigInteger.valueOf(Long.parseLong(st.nextToken())));
        }
    }

    private void gcdSum() {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i+1 ; j < numbers.size(); j++) {
                total = total.add(numbers.get(i).gcd(numbers.get(j)));
            }
        }
    }

    private void makeSettings() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        t = Integer.parseInt(br.readLine());
    }


}
