import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for(int s : scoville){
            q.add(s);
        }
        while(q.size()>=2){
            int s1 = q.poll();
            if(s1 >=K){
                break;
            }
            
            int s2=q.poll();
            int new_s= s1+s2*2;
            
            q.add(new_s);
            answer+=1;
            
        }
        
        if(q.peek() != null && q.peek() < K){
            return -1;
        }
        
        
        
        
        
        return answer;
    }
}