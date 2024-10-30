// Recursive implementation of LCS problem in java
import java.io.*;
import java.util.*;

class Main {

    // Returns length of LCS for S1[0..m-1], S2[0..n-1]
    static int lcs(String S1, String S2, int m, int n) {
        if (m == 0 || n == 0)
            return 0;
        if (S1.charAt(m - 1) == S2.charAt(n - 1))
            return 1 + lcs(S1, S2, m - 1, n - 1);
        else
            return Math.max(lcs(S1, S2, m, n - 1),
                            lcs(S1, S2, m - 1, n));
    }

    public static void main(String[] args) {
        String S1 = "AGGTAB";
        String S2 = "GXTXAYB";
        int m = S1.length();
        int n = S2.length();

        System.out.println("Length of LCS is"
                           + " " + lcs(S1, S2, m, n));
    }
}
