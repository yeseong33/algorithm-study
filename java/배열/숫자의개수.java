package 배열;

import java.io.*;

/*
 * String의 특정 인덱스의 char 값을 다시 String으로 변환
 * - String.valueOf((int) line).charAt(i) - '0'
 * - char - char 하면 유니코드로 변경후 다시 String 으로 반환하게 된다.
 *
 *
 *
 * */
public class 숫자의개수 {
    int[] num;
    int total;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        total = 1;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            total *= Integer.parseInt(line);
        }
        num = new int[10];
    }

    void run() throws IOException {
        makeSettings();
        String lines = String.valueOf(total);
        int tmp;
        for (int i = 0; i < lines.length(); i++) {
            tmp = Integer.parseInt(String.valueOf(lines.charAt(i)));
            num[tmp] += 1;
        }
        for (int value : num) {
            System.out.println(value);
        }
    }

    public static void main(String[] args) throws IOException{
        new 숫자의개수().run();

    }
}
