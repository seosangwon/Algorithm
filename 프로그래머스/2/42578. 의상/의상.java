import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String,List<String>> map = new HashMap<>();
        
        for(String[] list : clothes){
            String key = list[1];
            String value = list[0];
            
            if(map.get(key) == null){
                map.put(key, new ArrayList<>()); 
            }
            
            map.get(key).add(value);
               
        }
        
        for(Map.Entry<String, List<String>> entry : map.entrySet()){
            String key = entry.getKey();
            List<String> values = entry.getValue();
            answer*=values.size()+1;
            
        }
        
        answer-=1;
        
        return answer;
    }
}