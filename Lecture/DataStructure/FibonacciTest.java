package cse2010.homework4;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import org.junit.jupiter.api.Test;

//import cse2010.homework4.solution.Fibonacci;
import static org.junit.jupiter.api.Assertions.assertEquals;

class FibonacciTest {

    @Test
    void test() {

        List<Integer> actual = IntStream.rangeClosed(0, 20)
                         .mapToObj(Fibonacci::fibIter)
                         .collect(Collectors.toList()); //mapToObj(cse2010.homework4.solution.Fibonacci::fibIter)

        List<Integer> expected = IntStream.rangeClosed(0, 20)
                                        .mapToObj(Fibonacci::fibTailRec)
                                        .collect(Collectors.toList());

        System.out.println(actual);
        System.out.println(expected);

        assertEquals(expected, actual);
    }

}