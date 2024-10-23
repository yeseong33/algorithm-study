package DP;




import java.io.*;


public class 파도반수열 {

    int t;


    long[] requests, waves;
    BufferedWriter bw;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        t = Integer.parseInt(br.readLine());

        requests = new long[t];
        waves = new long[101];

        for (int i = 0; i < t; i++) {
            requests[i] = Integer.parseInt(br.readLine());
        }
    }


    void makeWaves() {
        waves[1] = 1L;
        waves[2] = 1L;
        waves[3] = 1L;
        for (int i = 4; i < 101; i++) {
            waves[i] = waves[i - 2] + waves[i - 3];
        }
    }

    void printResult() throws IOException {
        for (long request : requests) {
            bw.write(waves[(int) request] + "\n");
        }
        bw.flush();
        bw.close();
    }


    void solve() throws IOException {
        makeSettings();
        makeWaves();
        printResult();
    }



    public static void main(String[] args) throws IOException {
        new 파도반수열().solve();
    }
}
