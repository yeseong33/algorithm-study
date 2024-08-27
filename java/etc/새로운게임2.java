package etc;

import java.io.*;
import java.util.*;


class Node {
    int id, x, y, d;

    public Node(int id, int x, int y, int d) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.d = d;
    }
}


public class 새로운게임2 {
    int n, k, x, y, d, nx, ny, count;
    int[][] board, heads;
    int[][] dir;
    ArrayList<Node> horse;
    LinkedList<Node>[][] mBoard;
    StringTokenizer st;
    boolean isBlue, isReverse;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        board = new int[n][n];
        mBoard =  new LinkedList[n][n];
        heads = new int[n][n];
        horse = new ArrayList<>();
        dir = new int[][] {new int[]{0, 0}, new int[] {0, 1}, new int[] {0, -1}, new int[]{-1, 0}, new int[]{1, 0}};
        count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mBoard[i][j] = new LinkedList<Node>();  // LinkedList 초기화
            }
        }
        for (int i = 0; i < n; i++) {
            int[] intArray = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            board[i] = intArray;
        }

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            Node node = new Node(i+1, x-1, y-1, d);
            horse.add(node);
            heads[x-1][y-1] = i+1;
        mBoard[x-1][y-1].add(node);
        }
    }

    boolean isBlue() {
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] == 2) {
            return true;
        }
        return false;
    }

    boolean isRed() {
        if (board[nx][ny] == 1) {
            return true;
        }
        return false;
    }

    boolean play(Node node) {

        nx = node.x + dir[node.d][0];
        ny = node.y + dir[node.d][1];
        // 방향 회전
        if (isBlue()) {
            node.d = node.d == 1 || node.d == 3 ? node.d+1 : node.d-1;
            nx = node.x + dir[node.d][0];
            ny = node.y + dir[node.d][1];
            if (isBlue()) return false;
        }
        // 역 -> 역인지 기록
        // 역이면 -> pop -> Append ]
        // 정상이면 -> pop -> addfirst
//        if (isRed()) {
//            Node nowNode =  null;
//            while (nowNode != node) {
//                nowNode = mBoard[node.x][node.y].pollLast();
//                nowNode.x = nx;
//                nowNode.y = ny;
//                mBoard[nx][ny].addLast(nowNode);
//            }
//        } else {
//            Node nowNode =  null;
//            while (nowNode != node) {
//                nowNode = mBoard[node.x][node.y].pollLast();
//                nowNode.x = nx;
//                nowNode.y = ny;
//                mBoard[nx][ny].addFirst(nowNode);
//            }
//        }

        Node nowNode = null;
        LinkedList<Node> stack = new LinkedList<>();
        while (!mBoard[node.x][node.y].isEmpty()) {
            nowNode = mBoard[node.x][node.y].pollLast();
            nowNode.x = nx;
            nowNode.y = ny;
            stack.addFirst(nowNode);
            if (nowNode == node) break;
        }

        if (isRed()) {
            Collections.reverse(stack);
        }

        for (Node n : stack) {
            mBoard[nx][ny].add(n);
        }
        if (mBoard[nx][ny].size() >= 4) {
            return true;
        }

        return false;
    }



    void solve() throws IOException {
        makeSettings();

        for (int i = 0; i < 1000; i++) {
            for (Node node : horse) {
                if (play(node)) {
                    System.out.println(i+1);
                    return;
                }
            }
        }
        System.out.println("-1");
    }


    public static void main(String[] args) throws IOException {
        new 새로운게임2().solve();
    }
}
