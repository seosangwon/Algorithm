class MinHeap{
    constructor(){
        this.heap=[];
    }
    peak(){
        return this.heap[0];
    }
    size(){
        return this.heap.length;
    }
    push(value){
        this.heap.push(value);
        let index=this.heap.length-1;
        
        while(
            index > 0 &&
            this.heap[index] < this.heap[Math.floor((index-1)/2)]
        ){
            const temp= this.heap[index];
            this.heap[index]=this.heap[Math.floor((index-1)/2)];
            this.heap[Math.floor((index-1)/2)] = temp;
            index=Math.floor((index-1)/2);
            
        }
            
        }
    
    pop(){
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();
        
        const minValue = this.heap[0];
        this.heap[0]=this.heap.pop();
        let index=0;
        
        while(index *2 +1 < this.heap.length){
            let minChildIndex= (index *2 + 2 <this.heap.length && this.heap[index*2 +2] < this.heap[index*2 + 1]) ? index *2 +2 : index *2 +1;
            
            if (this.heap[index] < this.heap[minChildIndex]){
                break;
                
            }
            
            if(this.heap[index] < this.heap[minChildIndex]){
                break;
            }
            
            const temp = this.heap[index];
            this.heap[index] = this.heap[minChildIndex];
            this.heap[minChildIndex] = temp;
            index = minChildIndex;
            
            
        }
        
        return minValue;
        
    }
    
        
    }


function solution(scoville, K) {
    var answer = 0;
    var heapq= new MinHeap();
    
    for(node of scoville){
        heapq.push(node)
    }
    let count=0;
    
    if (heapq.peak() >= K){
        return 0;
    }
    
    //console.log(heapq.length)
 
    
    while(heapq.size() >= 2 && heapq.peak() < K ){ // q에 원소가 있고 더 섞어야 한다면 
        node1=heapq.pop()
        node2=heapq.pop()
        new_node=node1 + node2 * 2
        heapq.push(new_node)
        count+=1
        //console.log("실행")
        
    }
    
    if (heapq.peak()  < K){
        answer=-1
    }
    else{
        answer=count
    }
    
    
    
    
    
    return answer;
}