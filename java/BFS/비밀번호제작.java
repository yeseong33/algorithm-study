package BFS;
//1. 가장 큰 값의 2진법 길이 수 구하기
//2. nC(안전수)
//3. 높은거부터 시작 -> 이에 해당하는 값과 모든 num 비교 -> N
//4. 방문처리 ->
//5. 방문 끝났는지 확인 -> N
//    7. 여기서 값이 도출됨
//6. 끝나지 않으면 -> 안전수 작게 만들기

import java.io.*;
import java.util.*;

public class 비밀번호제작 {
    int n, m, value, now, ans;
    Queue<Integer> que;
    int [] visited;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        que = new LinkedList<>();
        visited = new int[n+1];
        Arrays.fill(visited, -1);
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            value = Integer.parseInt(st.nextToken());
            que.add(value);
            visited[value] = 0;
        }
    }


    int BFS() {

        while (!que.isEmpty()) {
            now = que.poll();

            for (int i = 0; i < 20; i++) {
                int next = now ^(1<<i);
                if (n < next || visited[next] != -1) continue;
                visited[next] = visited[now] + 1;
                que.add(next);
                ans = Math.max(ans, visited[next]);
            }
        }

        return ans;
    }



    void solve() throws IOException {
        makeSettings();
        System.out.print(BFS());
    }


    public static void main(String[] args) throws IOException {
        new 비밀번호제작().solve();
    }
}
