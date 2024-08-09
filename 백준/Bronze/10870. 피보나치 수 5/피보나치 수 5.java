import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());

        br.close();
        long result = p(x);
        System.out.println(result);


    }

    //피보나치 수열
    public static long p(int num) {
        if (num == 0 ) {
            return 0;
        }
        if (num == 1) {
            return 1;
        }


        return p(num - 1) + p(num - 2);
    }

}