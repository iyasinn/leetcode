class Solution {
    public int[] dailyTemperatures(int[] t) {

        Stack<Integer> stack = new Stack<>();
        int[] sols = new int[t.length];
        for (int i = 0; i < t.length; i++){
            while (!stack.isEmpty() && t[stack.peek()] < t[i]){
                sols[stack.peek()] = i - stack.peek();
                stack.pop();
            } 
            stack.push(i);
        }

        while (!stack.isEmpty()){
            sols[stack.peek()] = 0; 
            stack.pop();
        }
        return sols;
    }
}