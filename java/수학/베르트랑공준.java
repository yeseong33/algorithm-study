package 수학;

import javax.swing.text.Style;
import java.io.*;


public class 베르트랑공준 {

    BufferedReader br;
    BufferedWriter bw;
    int n;
    boolean[] numbers;

    public static void main(String[] args) throws IOException {
        new 베르트랑공준().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        makeSosu();

        while (true) {
            n = getN();
            if (n == 0) break;
            bw.write(count() + "\n");
        }

        bw.flush();
        bw.close();

    }

    private int count() {
        int count = 0;
        for (int i = n+1; i < 2 * n + 1; i++) {
            if (i < 2) continue;
            if (!numbers[i]) {
                count++;
            }
        }
        return count;
    }


    private void makeSosu() {
        numbers = new boolean[123456 * 2 +1];

        for (int i = 2; i < Math.sqrt(123456 * 2)+1; i++) {
            int j = 2;
            while (i * j <= 123456 * 2) {
                int value = i * j;
                if (!numbers[value]) {
                    numbers[value] = true;
                }
                j++;
            }
        }
    }

    private int getN() throws IOException{
        return Integer.parseInt(br.readLine());
    }

    private void makeSettings() {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
    }
}
