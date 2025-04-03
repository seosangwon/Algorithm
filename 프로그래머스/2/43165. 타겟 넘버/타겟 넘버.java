// 적절히 더하거나 빼기 방법 
// 1. 음수 또는 양수로 변환시킨다
// 2. 다 더한다 
// 3. 결과 값과 동일하면은 결과 값을 증가시시킨다 
import java.util.*;
class Solution {
    public static int answer=0;
    
    public int solution(int[] numbers, int target) {
        
        
        dfs(0,numbers,target,0);
        
        
        
        return answer;
    }
    
    public void dfs(int idx , int[] list , int target , int value){
        
        // 종료조건
        if (idx==list.length){
            if (value==target){
                answer+=1;
            }
            return;
        }
        
        int[] dx= {1,-1};    
        for(int i=0; i<2; i++){
            dfs(idx+1,list,target,value+dx[i]*list[idx]);        
            
        }
        
        
        
    }
    
    
    
    
}