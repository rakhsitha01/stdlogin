# Student Marks Calculator

A simple Python program that:

- Accepts a student's name and marks in three subjects
- Calculates the total, average and percentage
- Displays PASS or FAIL

## Passing rule

A student **passes** only if both are true:

1. Marks in **each** subject are at least **40**
2. Overall percentage is at least **40%**

Otherwise the student **fails**. Each subject is out of 100.

## How to run in VS Code

1. Unzip the folder and open it in VS Code (File > Open Folder).
2. Open `marks_calculator.py`.
3. Click the Run (play) button at the top right, or press `F5`.
   Or open the terminal (Ctrl + `) and run:

   ```
   python marks_calculator.py
   ```

   (On Mac/Linux you may need `python3 marks_calculator.py`.)

Requires Python 3.6 or newer. No extra packages needed.

## Sample run

```
Enter student name: Shreya
Enter marks for Subject 1 (0-100): 78
Enter marks for Subject 2 (0-100): 85
Enter marks for Subject 3 (0-100): 92
```

Output: Total 255 / 300, Average 85.00, Percentage 85.00%, Status PASS.
