  # CMPS 6610 Problem Set 02
## Answers

**Name:** Arturo Altamirano


Place all written answers from `assignment-01.md` here for easier grading.

I have uploaded a folder (writtenSolutions) with images of my handwritten solutions, if you so prefer. - Arturo

1. **Asymptotic notation**
  1. 


  2. T(n) = 2T(n/6) + 1

     2(2T (n/36) + 1) + 1

     4(T(n/36) + 2) + 1

     **n ^ log <sub> 6 </sub> (2)**


  3. T(n) = 6T(n/4) + n

     6(6T(n/16) + n/4) + n 

     6T(n/16) + 6 (n/4) + n

     **O(n ^ log <sub> 4 </sub> (6))**


  4. T(n) = 7T(n/7) + n

     7(7T(n/49) + n/7) + n

     7T(n/49) + 7(n/7) + n

     O(n <sup> log <sub> 7 </sub> (7) </sup>)


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

  7. 

  8. T(n) = T(n - 1) + 2

      T((n - 2) + 2) + 2 

      T(n - 2) + 4

      consider that this is essentially: 

      T(n - c) + 2c

      just n plus some constant - if you ignore the constant...
      T(n + c)

      **O(n)**

  9. 

  10. 

2. **Algorithm Selection**

3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

   When prompted with random numbers, subq seems to run in 20-30% faster. This is on par with the fact that the Karatsaba algorithm reduces work from n <sup> 2 </sup> work to 1 <sup> 1.58 </sup>

   You can expect a 25% reduction in workload according to this, but also the fact that the implementation of the algorithm literally drops the operations from 4 to 3, a 25% decrease.

5. **Black Hats and White Hats**
