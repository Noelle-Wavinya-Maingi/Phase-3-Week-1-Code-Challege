# Phase 3 Week 1 (Toy Problems)

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Challenges

### Challenge 1: Convert 12-hour time to 24-hour time
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

By convention, noon is 12:00 pm, and midnight is 12:00 am.

To run the solution, execute the provided Python script "Challenge_One.py". The script prompts the user to enter the time in 12-hour format (e.g., "8:30:23am" or "8:30:23pm") and then outputs the corresponding time in 24-hour format.


### Challenge 2: Two numbers are positive
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

#### Examples:
(2, 4, -3) == True

(-4, 6, 8) == True

(4, -6, 9) == True

(-4, 6, 0) == False

(4, 6, 10) == False

(-14, -3, -4) == False

To run the solution, execute the Python script "Challenge_Two.py". The script prompts the user to enter three integers and then outputs whether the condition is satisfied or not.

### Challenge Three: Consonant Value
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

#### Examples;
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

To run the solution, execute the Python script "Challenge_Three.py". The script prompts the user to enter a string and then calculates and outputs the highest value of consonant substrings.


### Project setup
Ensure that you have Python3 installed on your machine to run the solutions

1. Clone this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the repository.

4. Choose the challenge you want to run:
    - For Challenge 1:  Run:```sh python3 Challenge_One.py ```

     - For Challenge 2:  Run ```sh python3 Challenge_Two.py ```

      - For Challenge 3:  Run ```sh python3 Challenge_Three.py ```

5. Follow the prompts and input the required values.

6. The solution will execute and display the results based on the provided input.

### Author
The author of the code challenge solution is Noelle Maingi.

### Licence
 [LICENCE](LICENCE)
