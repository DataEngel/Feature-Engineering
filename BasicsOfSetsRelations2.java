//
You are given two sets.
Set A = {1,2,3,4,5,6}
Set B = {2,3,4,5,6,7,8}

How many elements are present in A intersection B?
Only enter the correct integer in the answering box. Do not include any extra spaces, tabs or newlines.
//

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // Define Set A
        Set<Integer> setA = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));

        // Define Set B
        Set<Integer> setB = new HashSet<>(Arrays.asList(2, 3, 4, 5, 6, 7, 8));

        // Find the intersection of sets A and B
        setA.retainAll(setB);

        // Print the size of the intersection
        System.out.print(setA.size());
    }
}
