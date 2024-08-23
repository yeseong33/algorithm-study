package 링크드리스트;

import java.util.*;
import java.io.*;


public class 키로거 {
    int c;
    Queue<String> requests;
    Deque<Character> front, back;
    String request;
    char[] chars;
    BufferedWriter bw;


    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        c = Integer.parseInt(br.readLine());
        requests = new LinkedList<>();
        for (int i = 0; i < c; i++) {
            requests.add(br.readLine());
        }
        front = new ArrayDeque<>();
        back = new ArrayDeque<>();
    }

    void makeString() throws IOException {
        for (char c : chars) {
            if (c ==  '<') {
                if (back.isEmpty()) continue;
                front.addFirst(back.removeLast());
            } else if (c ==  '>') {
                if(front.isEmpty()) continue;
                back.addLast(front.removeFirst());
            } else if (c ==  '-') {
                if (back.isEmpty()) continue;
                back.removeLast();
            } else {
                back.addLast(c);
            }
        }
        for (Character character : back) bw.write(character);

        while (!front.isEmpty()) bw.write(front.removeFirst());
        bw.write("\n");
        front = new ArrayDeque<>();
        back = new ArrayDeque<>();
    }

    void solve() throws IOException {
        makeSettings();
        while (!requests.isEmpty()){
            request = requests.poll();
            chars = request.toCharArray();
            makeString();
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        new 키로거().solve();
    }
}
