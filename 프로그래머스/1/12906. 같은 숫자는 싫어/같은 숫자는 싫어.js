function solution(arr)
{
    var answer = [];
    
    if(! arr){
        return answer
    }
    
    let prev=arr[0]
    answer.push(prev)
    
    for (let i=1; i<arr.length; i++){
        if (prev===arr[i]){ //같으면은 pass
            continue
        }
        else{ // 다르면은 prev 갱신 , answer에 추가 
            answer.push(arr[i])
            prev=arr[i]
        }
    }
    
    
    
    return answer;
}