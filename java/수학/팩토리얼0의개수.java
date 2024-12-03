package 수학;

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class 팩토리얼0의개수 {

    int n;

    public static void main(String[] args) throws IOException {
        new 팩토리얼0의개수().solve();
    }

    private void solve() throws IOException{
        makeSettings();

        String value = fac();
        int count = countZero(value);
        System.out.println(count);

    }

    private int countZero(String value) {
        int count = 0;
        for (int i = value.length() - 1; i >= 0; i--) {
            if (value.charAt(i) == '0') {
                count++;
            } else {
                break;
            }
        }
        return count;
    }

    private String fac() {
        BigInteger value = BigInteger.valueOf(1);
        for (int i = 1; i < n + 1; i++) {
            value = value.multiply(BigInteger.valueOf(i));
        }
        return String.valueOf(value);
    }

    private void makeSettings() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

    }
}
