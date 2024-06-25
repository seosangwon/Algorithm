function solution(nums) {
    var answer = 0;
    hash_map=new Map()
    
    for(num of nums){
        if ( !(num in hash_map)) { // 없으면은 key값 추가 
            hash_map[num]=true
            
        }
        
    } 
    len_=(Object.keys(hash_map).length)
    
    if (len_ > Object.keys(nums).length /2 ){
        answer=Object.values(nums).length /2
    }
    else
        answer=len_
    
    
    
    
    
    
    
    
    
    
    return answer;
}