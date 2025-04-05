// 모든 원소를 크기 순으로 [ , ] 정렬한다 
// 각 원소별로 제일 큰 값을 구한다 
import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        for(int[] list : sizes){
            Arrays.sort(list);   
        }
        int max1=0;
        int max2=0;
        
        for(int[] list : sizes){
            max1=Math.max(max1 , list[0]);
            max2=Math.max(max2,list[1]);
        }
        answer=max1*max2;
        
        
        return answer;
    }
}