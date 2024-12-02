package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class 가장큰정사각형 {

    int max;
    List<List<Integer>> dp;
    List<List<Integer>> board;

    public static void main(String[] args) throws IOException {
        new 가장큰정사각형().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        square();
        findMaxSquare();
        System.out.println(max * max);
    }

    private void findMaxSquare() {
        dp.forEach(line -> {
            line.forEach(value -> {
                max = Math.max(max, value);
            });
        });
    }

    private void square() {
        IntStream.range(0, board.size())
                .forEach(i -> {
                    IntStream.range(0, board.get(i).size())
                            .forEach(j -> {
                                if (board.get(i).get(j) == 1) {
                                    if (i == 0 || j == 0) {
                                        dp.get(i).set(j, 1);
                                    } else {
                                        int tmp = Math.min(dp.get(i-1).get(j-1), dp.get(i).get(j - 1));
                                        tmp = Math.min(tmp, dp.get(i-1).get(j));
                                        dp.get(i).set(j, tmp + 1);
                                    }
                                }
                            });
                });
    }


    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        max = 0;

        dp = new ArrayList<>();
        board = new ArrayList<>();

        IntStream.range(0, n)
                .forEach(i -> {
                    board.add(new ArrayList<>());
                    dp.add(new ArrayList<>());
                });

        IntStream.range(0, n)
                .forEach(i -> {
                    try {
                        String value = br.readLine();
                        value.chars()
                                .forEach(c -> {
                                    board.get(i).add(c - '0');
                                    dp.get(i).add(0);
                                });
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                });
    }
}


//4 4
//0100
//0111
//1111
//0011

//4 4
//1111
//0111
//1110
//0010