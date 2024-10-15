

import java.io.*;
import java.util.*;

public class 접두사 {
    List<String> words;

    int n, count;
    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        words = new ArrayList<>();
        count = n;

        for (int i = 0; i < n; i++) {
            String value = br.readLine();
            words.add(value);
        }
        words.sort((s1, s2) -> Integer.compare(s1.length(), s2.length()));
    }

    void solve() throws IOException {
        makeSettings();

        for (int ii = 0; ii < n; ii++) {
            String value = words.get(ii);
            for (int jj = ii+1; jj < n; jj++) {
                String value2 = words.get(jj);
                boolean isSub = false;
                for (int i = 0; i < value.length(); i++) {
                    if (value.charAt(i) != value2.charAt(i)) {
                        isSub = true;
                        break;
                    }
                }
                if (!isSub) {
                    count--;
                    break;
                }
            }

        }

        System.out.println(count);

    }



    public static void main(String[] args) throws IOException {
        new 접두사().solve();
    }
}
