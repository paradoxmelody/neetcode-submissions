class MedianFinder {
public:
    //Max heap to store smaller half of numbers
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap; //Min heap that stores larger half of the numbers

    MedianFinder() {   
    }
    
    void addNum(int num) {
        //add the number to the maxHeap
        maxHeap.push(num);

        //move the top element of maxHeap to minHeap
        minHeap.push(maxHeap.top());
        maxHeap.pop();

        //If the minHeap has more elements, balance the heaps
        if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
        
    }
    
    double findMedian() {
        if(maxHeap.size() > minHeap.size())

           return maxHeap.top(); // if max heap has more elements then median is at the top of the maxHeap
        return (maxHeap.top() + minHeap.top()) / 2.0; //otherwise average the tops of both heaps to get the median
        
    }
};


