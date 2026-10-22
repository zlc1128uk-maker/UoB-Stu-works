---
type: study
module: "[[PROG]]"
week: 3
topic: Pseudocode and flowcharts
tags: [study/prog]
---

# PROG Week 03 — Pseudocode and flowcharts

Teaching week 5–9 Oct 2026. Mon 5 Oct 16:00–18:00 and Thu 8 Oct 09:00–11:00, rooms 4.32 and 4.33. Syed Murad, group 2.

Two decks: pseudocode, then flowcharts.

## Know this

Pseudocode is structured English for an algorithm. "Pseudo" is from Greek *psevdes*, false, so it is not a real language and it has no strict syntax. The point is to write the logic without Java or Python syntax getting in the way. The same algorithm is shown once as Python and once as Java, with the same output.

There is no single standard notation. Keywords the slides use:

| Keyword | Job |
| --- | --- |
| START / END, or BEGIN / STOP | Start and finish |
| INPUT, ACCEPT | A user types something |
| OUTPUT, DISPLAY, PRINT | Something appears |
| SET | Give a variable a value. Example: `SET Counter TO 0` |
| IF, THEN, ELSE, ENDIF | A choice |
| FOR, TO, DO, ENDFOR | A counting loop |
| WHILE, ENDWHILE | A loop that tests the condition at the start |
| REPEAT, UNTIL | A loop that tests the condition at the end |
| RETURN | |

AND is true only when both conditions are true. OR is true when either condition is true.

## Method

**Sum of two numbers**, in the notation of the slide:

```
begin
numeric nNum1, nNum2, nSum
display "ENTER THE FIRST NUMBER : "
accept nNum1
display "ENTER THE SECOND NUMBER : "
accept nNum2
compute nSum = nNum1 + nNum2
```

**Flowchart.** A diagram of the same steps. Symbols on the slides:

- Start and end of the algorithm
- A process
- A sub-process
- A decision
- Input or output
- A connector, when the arrow cannot stay unbroken
- The arrow itself, which is the order of the steps

Three structures. Sequence is statement 1, then 2, then 3. Selection is a condition with a Yes branch and a No branch. Repetition is a condition with a loop back.

Example: read a birth year, set age to the current year minus that year, display the age. Second example: read an age, and if it is over 18 print "You are allowed to buy", otherwise print "You are NOT allowed to buy".

The in-class task is a flowchart that reads two numbers, adds them, and displays the sum, then the same thing as pseudocode.

## Originals

- `IFP Foundations of Computer Programming - Week 3.pdf`
- `IFP Foundations of Computer Programming - Week 3 p2.pdf`

In Archive/Course Content/PROG/Week 03.
