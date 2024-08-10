import java.io.*;
import java.util.Arrays;

public class Main {

    static int count=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] data = new String[n];

        for (int i = 0; i < n; i++) {
            data[i] = br.readLine();
            count=0; // 초기화
            System.out.println(isPar(data[i], 0, data[i].length() - 1)+" "+count);
        }


    }

    public static int isPar(String value, int l, int r) {
        count+=1;
        if (l>=r) return 1;
        else if (value.charAt(l)!=value.charAt(r)) return 0;
        else return isPar(value,l+1,r-1);


    }


}