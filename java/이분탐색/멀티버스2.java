package 이분탐색;

import java.io.*;
import java.util.*;

public class 멀티버스2 {

    int n, m, count;
    List<Integer> universes;
    List<List<int[]>> universes2;

    public static void main(String[] args) throws IOException {
        new 멀티버스2().solve();
    }

    void solve() throws IOException {
        makeSettings();
        findMultiVerse();
        System.out.println(count);
    }

    private void findMultiVerse() {
        for (int i = 0; i < n; i++) {
            int universe1 = universes.get(i);
            for (int j = i + 1; j < n; j++) {
                int universe2 = universes.get(j);
                if (isMulti(universe1, universe2, i, j)) count++;
            }
        }
    }

    private boolean isMulti(int universe1, int universe2, int i, int j) {
        if (universe1 == universe2) {
            return universes.get(i).equals(universes.get(j));
        }
        return false;
    }

    private void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        count = 0;

        universes = new ArrayList<>();
        universes2 = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<int[]> tmp = new ArrayList<>();
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                tmp.add(new int[]{Integer.parseInt(st.nextToken()), j});
            }
            tmp.sort(Comparator.comparingInt((int[] a) -> a[0])
                    .thenComparingInt(a -> a[1]));

            universes.add(calculateHash(tmp));
            universes2.add(tmp);
        }

    }

    private int calculateHash(List<int[]> universe) {
        int[] rank = new int[universe.size()];
        int currentRank = 0;

        for (int i = 0; i < universe.size(); i++) {
            if (i > 0 && universe.get(i)[0] == universe.get(i - 1)[0]) {
                rank[universe.get(i)[1]] = currentRank;
            } else {
                rank[universe.get(i)[1]] = ++currentRank;
            }
        }

        return Arrays.hashCode(rank);
    }


}
