package 그리디;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 멀티탭스케줄링 {

    int n, count;
    List<Integer> devices, outlet;

    public static void main(String[] args) throws IOException {
        new 멀티탭스케줄링().solve();
    }

    private void solve() throws IOException {
        makeSettings();
        multi();
        System.out.println(count);
    }

    private void multi() {

        for (int i = 0; i < devices.size(); i++) {

            if (outlet.contains(devices.get(i))) continue;

            if (outlet.size() == n) {
                isFull(i, devices.get(i));
            } else {
                isNotFull(devices.get(i));
            }
        }


    }

    private void isFull(int now, int value) {

        int removeIdx = -1;
        int lastIdx = -1;

        for (int i = 0; i < outlet.size(); i++) {
            int device = outlet.get(i);
            boolean found = false;

            for (int j = now+1; j < devices.size(); j++) {
                if (devices.get(j) == device) {
                    found = true;
                    if (j > lastIdx) {
                        lastIdx = j;
                        removeIdx = i;
                    }
                    break;
                }
            }

            if (!found) {
                removeIdx = i;
                break;
            }
        }

        outlet.remove(removeIdx);
        outlet.add(value);
        count++;
    }

    private void isNotFull(int value) {
        outlet.add(value);
    }

    private void makeSettings() throws IOException {

        devices = new ArrayList<>();
        outlet = new ArrayList<>();
        count = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            devices.add(Integer.parseInt(st.nextToken()));
        }
    }

}


