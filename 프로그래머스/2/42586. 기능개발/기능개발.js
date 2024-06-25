function solution(progresses, speeds) {
    var answer = [];
    let queue=[]
    
    for(let i=0; i<progresses.length; i++){
        queue.push([progresses[i],speeds[i]]) // 큐에 값 추가 
    }
    //console.log(queue)
    //console.log(queue[0], queue[0][0])
    
    
    while (queue.length > 0 ){ // queue가 비어질때까지 
        let count=0;
        flag = false;
        for(let i=0; i<queue.length;i++){
            queue[i][0]+=queue[i][1] // 매일 진행하기 
            }
        
        while(queue.length > 0 && queue[0][0]>=100){ // 배포하기
            queue.shift()
            count+=1
        }
        
        if (count>0){
            answer.push(count)
        }

            
        }
        
    return answer;
        
    }
    
    
    
    
    
    
    
    
