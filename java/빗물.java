import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 빗물 {
    int h, w, totalcount;
    int[][] board;
    int[] in;
    public void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        board = new int[h][w];
        in = new int[w];
        for (int i = 0; i < w; i++) {
            in[i] = Integer.parseInt(st.nextToken());
        }
        for (int j = 0; j < w; j++) {
            for (int i = h-1; i >= h-in[j]; i--) {
                board[i][j] = 1;
            }
        }
        totalcount = 0;
    }

    public void run() throws IOException {
        makeSettings();

        for (int i = 0; i < h; i++) {
            boolean countMode = false;
            int count = 0;
            for (int j = 0; j < w; j++) {
                if (board[i][j] == 1) {
                    if (countMode) {
                        totalcount += count;
                        count = 0;
                    } else {
                        countMode = true;
                    }
                } else {
                    if (countMode) {
                        count++;
                    }
                }

            }
        }
        System.out.println(totalcount);



    }


    public static void main(String[] args) throws IOException {
        new 빗물().run();
    }
}
