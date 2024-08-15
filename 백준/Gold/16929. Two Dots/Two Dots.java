import java.io.*;
import java.security.KeyStore;
import java.util.Arrays;


public class Main {

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        char[][] data = new char[n][m];

        for (int i = 0; i < n; i++) {
            String inputLine = br.readLine();

            for (int j = 0; j < m; j++) {
                data[i][j] = inputLine.charAt(j);
            }

        }

        boolean[][] visited = new boolean[n][m]; // boolean 배열은 초기화 하지 않으면 자동으로 false 이다

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(i, j, i, j, 1, data[i][j], n, m, visited, data)) {
                    System.out.println("Yes");
                    System.exit(0);

                }
            }
        }
        System.out.println("No");


    }

    public static boolean dfs(int s_x, int s_y, int x, int y, int depth, char alpha, int n, int m, boolean[][] visited, char[][] data) {

        if (s_x == x && s_y == y && depth >= 4) return true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && data[nx][ny] == alpha) {
                visited[nx][ny] = true;
                if (dfs(s_x, s_y, nx, ny, depth + 1, alpha, n, m, visited, data)) return true;
                visited[nx][ny] = false;
            }


        }
        return false;


    }


}