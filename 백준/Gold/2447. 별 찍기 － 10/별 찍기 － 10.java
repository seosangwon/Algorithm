import java.io.*;
import java.util.Arrays;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[][] data = new String[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                data[i][j] = "*";
            }
        }

        recursion(data,0,0,n);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(data[i][j]);
            }
            sb.append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();





    }

    public static void recursion(String[][] data,int startX ,int startY , int size ) {
        if (size==1) return;

        int newSize=size/3;

        //가운데 구멍 뚫기
        for (int i = startX + newSize; i < startX + newSize * 2; i++) {
            for(int j= startY+ newSize; j< startY + newSize * 2; j++){
                data[i][j] = " ";
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if(i==1 && j==1) continue;

                recursion(data , startX+i*newSize , startY+j*newSize,newSize);

            }
        }

    }


}