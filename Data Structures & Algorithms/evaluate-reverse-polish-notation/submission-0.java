class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            if (token.equals("+")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a + b);
            } else if (token.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (token.equals("*")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a * b);
            } else if (token.equals("/")) {
                // Integer division in Java truncates toward zero by default
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                // ush Token onto the stack
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }
}