

// Method: main with hello world

public class minimal_example {

    // Method that returns a factorial since it receives a integer

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }


    public static void main(String[] args) { 
        System.out.println("Hello World"); 
    } 
}


// Interface for an observer

interface Observer {
    void update();
}