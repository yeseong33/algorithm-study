package 구현;

import java.io.*;
import java.util.*;

public class 톱니바퀴 {
    int total;
    int[] scores;
    boolean[] visited;
    List<int[]> requests;
    List<Gear> gears;
    Queue<int[]> que;

    class Gear {

        int head, tail, left, right, num, score, twelve;
        int[] body;

        public Gear(int[] body, int num, int score) {
            this.body = body;
            this.right = 2;
            this.left = 6;
            this.twelve  = 0;
            this.num = num;
            this.score = score;
            this.head = 99;
            this.tail = 99;
        }

        public int getNum() {
            return this.num;
        }

        public int getTwelve() {
            return this.twelve;
        }

        public int getHead() {
            return this.head;
        }
        public int getTail() {
            return this.tail;
        }

        public void setHead(int head) {
            this.head = head;
        }
        public void setTail(int tail) {
            this.tail = tail;
        }

        public void setLeft(int left) {
            this.left = left;
        }
        public void setRight(int right) {
            this.right = right;
        }
        public int getLeft() {
            return this.body[this.left];
        }
        public int getRight() {
            return this.body[this.right];
        }

        public void clockWise() {
            this.left -= 1;
            this.right -= 1;
            this.twelve -= 1;
            if (left == -1) {
                this.left = 7;
            }
            if (right == -1) {
                this.right = 7;
            }
            if (twelve == -1) {
                this.twelve = 7;
            }
        }
        public void counterClockWise() {
            this.left += 1;
            this.right += 1;
            this.twelve += 1;
            if (left == 8) {
                this.left =  0;
            }
            if (right == 8) {
                this.right =  0;
            }
            if (twelve == 8) {
                this.twelve =  0;
            }
        }

        public int getScore() {
            if (body[twelve] == 1) {
                return score;
            }
            return 0;
        }
    }

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        gears = new ArrayList<>();
        requests = new ArrayList<>();
        que = new LinkedList<>();
        visited = new boolean[4];

        total = 0;
        scores = new int[]{1, 2, 4, 8};
        for (int i = 0; i < 4; i++) {
            int[] body = br.readLine().chars().map(c -> c - '0').toArray();
            Gear gear = new Gear(body, i, scores[i]);
            if (i < 3) {
                gear.setHead(i+1);
            }
            if (i > 0) {
                gear.setTail(i-1);
            }
            gears.add(gear);
        }


        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] temp = new int[2];
            for (int j = 0; j < 2; j++) {
                temp[j] = Integer.parseInt(st.nextToken());
            }
            requests.add(temp);
        }

    }

    void rotation(int num, int request) {

        visited[num] = true;
        que.add(new int[] {num, request});
        while (!que.isEmpty()) {
            int[] now = que.poll();
            request = now[1];
            Gear gear = gears.get(now[0]);
            if (gear.getHead() != 99) {
                Gear head = gears.get(gear.getHead());
                if (head.getLeft() != gear.getRight() && !visited[head.getNum()]) {
                    visited[head.getNum()] = true;
                    que.add(new int[] {head.getNum(), request == 1 ? -1 :1});
                }
            }
            if (gear.getTail() != 99) {
                Gear tail = gears.get(gear.getTail());
                if (tail.getRight() != gear.getLeft() && !visited[tail.getNum()]) {
                    visited[tail.getNum()] = true;
                    que.add(new int[] {tail.getNum(), request == 1 ? -1 :1});
                }
            }


            if (request == 1) {
                gear.clockWise();
            } else {
                gear.counterClockWise();
            }
        }

    }

    void culScore() {
        for (int i = 0; i < 4; i++) {
            total += gears.get(i).getScore();
        }
    }


    void solve() throws IOException {
        makeSettings();

        for (int[] request : requests) {
            visited = new boolean[4];
            int num = request[0]-1;
            int rotate = request[1];
            rotation(num, rotate);
        }

        culScore();
        System.out.println(total);
    }


    public static void main(String[] args) throws IOException {
        new 톱니바퀴().solve();
    }
}
