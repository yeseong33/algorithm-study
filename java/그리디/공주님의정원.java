package 그리디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

class Flower {
    LocalDate start;
    LocalDate end;

    public Flower(LocalDate start, LocalDate end) {
        this.start = start;
        this.end = end;
    }

    public LocalDate getStart() {
        return start;
    }

    public LocalDate getEnd() {
        return end;
    }
}

public class 공주님의정원 {

    int result;
    LocalDate princeStartDate = LocalDate.of(2023, 3, 1);
    LocalDate princeEndDate = LocalDate.of(2023, 11, 30);
    List<Flower> dates;


    public static void main(String[] args) throws IOException {
        new 공주님의정원().solve();
    }

    private void solve() throws IOException {
        makeSettings();
    }

    private void makeSettings() throws IOException {

        result = 100001;

        dates = new ArrayList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        makeDate(br, n);
        dates.sort(new Comparator<Flower>() {
            @Override
            public int compare(Flower o1, Flower o2) {
                return o1.getStart().compareTo(o2.getStart());
            }
        });

        int count = 0;
        LocalDate start = princeStartDate;
        LocalDate end = princeStartDate;
        int idx = 0;
        boolean flag = true;

        while (flag && idx < n) {

            flag = false;
            LocalDate tmpStart = start;
            LocalDate tmpEnd = end;

            while (dates.get(idx).getStart().isBefore(end) || dates.get(idx).getStart().isEqual(end)) {
                tmpStart = dates.get(idx).getStart();
                if (dates.get(idx).getEnd().isAfter(tmpEnd)) {
                    tmpEnd = dates.get(idx).getEnd();
                }
                idx++;
                flag = true;
                if (idx >= n) {
                    break;
                }
            }

            count++;

            start = tmpStart;
            end = tmpEnd;

            if (end.isAfter(princeEndDate)) {
                break;
            }
        }

        if (!end.isAfter(princeEndDate)) {
            flag = false;
        }

        if (flag) {
            System.out.println(count);
        } else {
            System.out.println(0);
        }

    }


    private void makeDate(BufferedReader br, int n) throws IOException {
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            LocalDate startDate = LocalDate.of(2023, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            LocalDate endDate = LocalDate.of(2023, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            dates.add(new Flower(startDate, endDate));
        }
    }
}

