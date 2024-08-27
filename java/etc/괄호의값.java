package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class 괄호의값 {
    int[] value;
    Stack<Character> stack;
    String req;
    int dep;
    Map<Character, Integer> map;
    Map<Character, Character> word;

    void makeSettings() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        req = br.readLine();
        stack = new Stack<>();
        value = new int[20];
        map = new HashMap<>();
        word = new HashMap<>();
        map.put(')', 2);
        map.put(']', 3);
        word.put('[', ']');
        word.put('(', ')');
    }


    boolean addValue(char c) {

        if (stack.isEmpty() || word.get(stack.pop()) != c ){
            return false;
        }

        dep = stack.size()+1;

        if (value[dep + 1] != 0) {
            value[dep] += value[dep+1] * map.get(c);
            value[dep+1] = 0;
        } else {
            value[dep] += map.get(c);
        }

        return true;
    }

    void cal() {
        for (char c : req.toCharArray()) {
            if (c == '(' || c == '[') {
                stack.push(c);
            } else {
                if (!addValue(c)) {
                    value[1] = 0;
                    return;
                };
            }
        }
    }


    void solve() throws IOException {
        makeSettings();
        cal();
        System.out.println(value[1]);
    }




    public static void main(String[] args) throws IOException {
        new 괄호의값().solve();
    }
}
