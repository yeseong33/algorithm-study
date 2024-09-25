package 백트레킹;

import java.io.*;
import java.util.*;

public class 계란으로계란치기 {

    int n, maxBroke;
    int[] weight, life;
    boolean[] visited;
    StringTokenizer st;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        weight = new int[n];
        life = new int[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            life[i] = Integer.parseInt(st.nextToken());
            weight[i] = Integer.parseInt(st.nextToken());
        }
        maxBroke = 0;
    }

    int isBroke(int egg) {
        if (life[egg] <= 0) {
            return 1;
        }
        return 0;
    }

    void nextEgg(int count, int now) {
        for (int i = 0; i < n; i++) {
            if (life[i] <= 0 || i == now) continue;

            life[i] -= weight[now];
            life[now] -= weight[i];
            BT(count+isBroke(i)+isBroke(now), now+1);
            life[i] += weight[now];
            life[now] += weight[i];

        }
    }

    boolean isEnd(int now) {
        // 1. 다음에 잡을 계란이 없을때
        //   - 내손의 계란이 깨져있을 경우  => 다음 모든 계란이 꺠져있음
        //   - 내손의 계란이 안깨져 있을 경우  => 다음 모든 계란이 깨져있음
        //   - 마지막 계란일 경우 => 다음 계란이 없
        if (now == n) {
            return true;
        }
        for (int i = 0; i < n; i++) {
            if (life[i] > 0 && i != now) {
                return false;
            }
        }
        return true;
    }

    void BT(int count, int now) {
        if (isEnd(now)) {
            if (count > maxBroke) {
                maxBroke = count;
            }
            return;
        }

        if (life[now] <= 0) {
            BT(count, now+1);
            return;
        }
        nextEgg(count, now);
    }


    void solve() throws IOException {
        makeSettings();
        BT(0, 0);
        System.out.println(maxBroke);
    }

    public static void main(String[] args) throws IOException {
        new 계란으로계란치기().solve();
    }
}
