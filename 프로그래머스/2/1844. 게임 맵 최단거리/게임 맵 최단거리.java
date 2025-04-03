import java.util.*;

class Solution {
    public static int[] dx={1,-1,0,0};
    public static int[] dy={0,0,1,-1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        answer = bfs(maps);
        
        
        return answer;
    }
    
    public int bfs(int[][] maps){
        int n=maps.length;
        int m=maps[0].length;
        
        boolean[][] visited= new boolean[n][m];
        Queue<int[]> queue= new LinkedList<>();
        queue.add(new int[] {0,0,1});
        visited[0][0]=true;
        
        while (!queue.isEmpty()){
            int [] current= queue.poll();
            int x = current[0];
            int y = current[1];
            int value = current[2];
            //System.out.println("x= "+ x + " y= " + y + " value= " + value);
            
            // for(int[] q : queue){
            //     System.out.println(Arrays.toString(q));
            // }
            
            if (x==n-1 && y==m-1){
                return value;
            }
            
            for (int i=0; i<4; i++){
                int nx= x+dx[i];
                int ny= y+dy[i];
                
                if (0<=nx && nx <n && 0<=ny && ny<m && maps[nx][ny]==1 && visited[nx][ny]==false){
                    visited[nx][ny]=true;
                    queue.add(new int[]{nx,ny,value+1});
                }
            }
       
        }
        
        return -1;
        
        
        
        
    }
    
    
}