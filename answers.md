  # CMPS 6610 Problem Set 02
## Answers

**Name:** Arturo Altamirano

Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
  1. 


  2. T(n) = 2T(n/6) + 1

     2(2T (n/36) + 1) + 1

     4(T(n/36) + 2) + 1

     **n <sup> log <sub> 6 </sub> (2)</sup>**


  3. T(n) = 6T(n/4) + n

     6(6T(n/16) + n/4) + n 

     6T(n/16) + 6 (n/4) + n

     **O(n ^ <sup> log <sub> 4 </sub> (6))</sup>**


  4. T(n) = 7T(n/7) + n

     7(7T(n/49) + n/7) + n

     7T(n/49) + 7(n/7) + n

     **O(n <sup> log <sub> 7 </sub> (7) </sup>)**


  5. T(n) = 9T(n/4) + n ^ 2

     9(9T(n/16) + n/16 + n ^ 2)

     81T((n/16) + 9(n/16) ^ 2) + n ^ 2

     9((n/16) ^ 2)

     (9n ^ 2) / 16 < n ^ 2

     **O (n <sup> 2 </sup>)** 
     

  6. T(n) = 4T(n/2) + n ^ 3

      4( (4T (n/8) + (n/2) ^ 3) + n ^ 3)

      64T ( (n/8) + 4 (n <sup> 3 </sup> / 8) + n <sup> 3 </sup>)

      n <sup> log <sub> 2 </sub> (4) </sup>

      **O (n <sup> 2 </sup>)**

  7. SOLUTION NEEDED

  8. T(n) = T(n - 1) + 2

      T((n - 2) + 2) + 2 

      T(n - 2) + 4

      consider that this is essentially: 

      T(n - c) + 2c

      just n plus some constant - if you ignore the constant...
      T(n + c)

      **O(n)**

  9. SOLUTION NEEDED

  10. T(n) = T(sqrt(N) + 1)

      T(1/4 root(N) + 2) 

      continues to unroll into 1/8 root N, 1/16 root N etc...

      so we can say that at a certain point it becomes n <sup> 1/2<sup>k</sup>
      </sup>

      1/2<sup>k</sup> log n = n 

      2<sup>k</sup> = Θ(log n)

      k = Θ(log log n)

2. **Algorithm Selection**

   Algorithm A: 2w(n/5) + n<sup> 2 </sup>
   Work - n <sup> 2 </sup>
   Span - n <sup> 2 </sup> (quadratic time?)

   2w(n/5) + n <sup> 2 </sup>

   2(2w(n/25) + (n/5)) + n <sup> 2 </sup>

   4w(n/25) + 2(n/25 <sup> 2 </sup>) + n <sup> 2 </sup>

   root dominated so use: 

   2(n <sup> 2 </sup> / 25)

   **2n <sup> 2 </sup> / 25 < n <sup> 2 </sup>**

   Algorithm B: w(n - 1) + (log n)
   Work - n log n
   Span - log n

   w(n - 1) + log n

   w(n - 2) + (log n)<sup> 2 </sup>

   w(n - k) + (log n)<sup> 2 </sup>

   remove constants k

   **O(n * log n)**

   Algorithm C: w(n/3) + w(2n/3) + n <sup> 1.1 </sup>
   Work - n <sup> 2 </sup>
   Span - n <sup> 1.1 </sup>

   w(w(n/9) + n/3) + w(w 2n/9) + 2n/3 + n <sup> 1.1 </sup>

   w(n/9) + (n/3) <sup>1.1</sup> + w(2n/3)<sup> 2 </sup> + n <sup>1.1 </sup>

   **O(w(2n/9) <sup> 2 </sup> < n <sup>2</sup>)**


3. **More Algorithm Selection** 

   Algorithm A: 5w(n/2) + n
      Work - n <sup> log <sub> 4 </sub> <sup> 5 </sup> </sup>
      Span - n (linear time)

      work calculation: 

      5w(n/2) + n 

      5(5w(n/4) + n/2) + n

      5w(n/4) + 5(n/2) + n 

      leaf dominated, so we use n <sup> log <sub> b </sub> (a)

      **O(n <sup> log <sub> 4 </sub> <sup> 5 </sup> </sup>)**

   Algorithm B: 2w(n-1) + c
      Work - n
      Span - c (some constant)

      2(2w(n - 2) + c)

      4w(n - 3) + 2(n - 1) + c

      leaf dominated, so use

   Algorithm C:
      Work - n <sup> 2 </sup>
      Span - n <sup> 2 </sup>

      work calculation: 9w(n/3) + n <sup> 2 </sup>
      9w(n/3) + O(n <sup> 2 </sup>)

      9(9w(n/9) + 9(n/9)<sup> 2 </sup> + n <sup> 2 </sup>)

      81w(n/9) + 9(n/9) + n <sup> 2 </sup>

      9(n <sup> 2 </sup> / 9) < n <sup> 2 </sup>

      **O(n <sup> 2 </sup>)**

4. **Integer Multiplication Timing Results**

   When prompted with random numbers, subq seems to run in 20-30% faster. This is on par with the fact that the Karatsaba algorithm reduces work from n <sup> 2 </sup> work to 1 <sup> 1.58 </sup>

   You can expect a 25% reduction in workload according to this, but also the fact that the implementation of the algorithm literally drops the operations from 4 to 3, a 25% decrease.

5. **Black Hats and White Hats**

   5a: More than n/2 are black hats 

   Intuition: If a majority of our participants are assumed to be adversarial, then no pair from the class can be trusted, since we know they are more likely to be black hats than white. 

   5b: Finding a single white hat 

   Intuition: This can be characterized as a search/span problem. Just sequentially going through the search space until we satisfy a condition.

   5c: 
