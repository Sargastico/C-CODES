import java.util.HashMap;
import java.util.Map;

import static jdk.nashorn.internal.objects.Global.print;

class main {

    public static void main(String[] args){

        Fibonacci fibonacci = new Fibonacci();
        System.out.println(fibonacci.fibo(36));
    }
}

class Fibonacci {
    
    private final Map<Integer,Long> fiboMemory;
    
    public Fibonacci(){
        fiboMemory = new HashMap<Integer, Long>();
        fiboMemory.put(0, 0L);
        fiboMemory.put(1,1L);
    }
    
    public long fibo(int indice){
    
        return (fiboMemory.computeIfAbsent(indice, k -> fibo(k-1) + fibo(k-2) ));
    
    }
}
