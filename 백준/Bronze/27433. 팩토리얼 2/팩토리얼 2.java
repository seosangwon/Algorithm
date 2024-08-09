import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());

        br.close();
        long result = factorial(x);
        System.out.println(result);


    }


    public static long factorial(int num) {
        if (num <= 0 ){
            return 1;
        }


        return factorial(num-1)*num;
    }

}