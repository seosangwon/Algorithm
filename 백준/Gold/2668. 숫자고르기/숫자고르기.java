import java.io.*;
import java.security.KeyStore;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {

    static List<Integer> result = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] graph = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            int v = Integer.parseInt(br.readLine());
            graph[i] = v;
        }

        boolean[] visited = new boolean[n + 1];

        for (int node = 1; node < n + 1; node++) {
            if (! visited[node]) {
                List<Integer> cycle = new ArrayList<>(); // cycle 초기화
                dfs(node, cycle, visited, graph);
            }
        }

        Collections.sort(result);
        System.out.println(result.size());
        for (int i=0; i<result.size();i++) System.out.println(result.get(i));



    }

    public static void dfs(int node , List<Integer> cycle , boolean[] visited , int[] graph) {
        visited[node]= true; // 방문처리
        int next_node = graph[node];
        cycle.add(node);

        if (visited[next_node]) {
            if (cycle.contains(next_node)) { // 만약 next_node가 이미 cycle 안에 있다면은
                // cycle 리스트내에서 next_node의 index를 알아내야함
                int idx_start = cycle.indexOf(next_node);
                for (int i = idx_start; i < cycle.size(); i++) {
                    result.add(cycle.get(i));
                }
            }
        } else {
            dfs(next_node , cycle , visited , graph);
        }

    }


}