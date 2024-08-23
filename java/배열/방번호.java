package 배열;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class 방번호 {
    String num;
    int[] count;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        num = br.readLine();
        count = new int[10];
    }

    void run() throws IOException {
        makeSettings();
        List<String> arr = Arrays.stream(num.split("")).collect(Collectors.toList());
        int tmp;
        for (String s : arr) {
            tmp = Integer.parseInt(s) == 9 ? 6 : Integer.parseInt(s);
            count[tmp]++;
        }
        count[6] = count[6] /2 + count[6]%2;

        System.out.println(Arrays.stream(count).max().getAsInt());
    }


    public static void main(String[] args) throws IOException {
        new 방번호().run();
    }
}
