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

     **n ^ log <sup> 6 </sup> (2)**


  3. T(n) = 6T(n/4) + n

     6(6T(n/16) + n/4) + n 

     6T(n/16) + 6 (n/4) + n

     **O(n ^ log <sup> 4 </sup> (6))**

  4. T(n) = 7T(n/7) + n

  5. T(n) = 9T(n/4) + n ^ 2

     9(9T(n/16) + n/16 + n ^ 2)

     81T((n/16) + 9(n/16) ^ 2) + n ^ 2

     9((n/16) ^ 2)

     (9n ^ 2) / 16 < n ^ 2
     
     **O(n ^ 2)**

  6. T(n) = 4T(n/2) + n ^ 3

2. **Algorithm Selection**

3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
