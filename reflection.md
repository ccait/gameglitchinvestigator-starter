# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  It asked me to guess a number between 1 to 100. But looking at the "Developer Debug Info", I noticed the hint was actually the opposite. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   50  | "go HIGHER!"      |  "go LOWER!"    | It didn't give error but it's incorrect|
|  100  | "go LOWER!"       | "go HIGHER!"    | It didn't give error but it's incorrect|
| "new game"| refresh the Developer Debug Info and start a new game| It did nothing | It didn't give error but it's incorrect|
| control + v| copy         |   Error.        | Message"Clear caches Are you sure you want to clear the app's function caches
This will remove all cached entries from functions using
@st.cache_data and @st.cache_resource."|
| switch game difficulty to "hard"| change attempts to 5| allowed 6 (0 to 5) attempts| It didn't give error but it's incorrect|
| switch game difficulty from "hard" to "easy" | should allow more attempt and new "Secret" number| didn't allow more guess| Message "Game over. Start a new game to try again."|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 ClaudeCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
"New Game" doesn't actually start a new game. AI suggested that new_game resets attempts and secret but never resets status, score, or history. After a win/loss, status is still "won"/"lost". On the rerun, the very next block sees status != "playing" and calls st.stop(), so the player is permanently stuck on "You already won." The reset is incomplete. I verified by running the game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It didn't gave incorrect example in my case.It also found new issue that I missed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I re-run the scenario manually. 
- Describe at least one test you ran (manual or using pytest)   and what it showed you about your code.
I re-run the scenario manually. First, I set difficulty "normal", then guessed the correct "secrect" at the 2nd attemp. It shows balloons and messaged "Correct!" The other bug AI fixed is the "new game" feature. After attempts are out, clicking the "new game" now refresh the attempts and the secrect number.
- Did AI help you design or understand any tests? How?
AI helped me find the bug that I didn't aware of previously, and it explained the underlying logic:  5 == '5' is False in Python and 5 > '5' raises a TypeError.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
This is the part I got stucked a lot and I still have a few questions about it. I will go to study hall and asking for help.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
The habit of starting a new chat session for every bug.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would ask AI to step-by-step debug, rather than trying to fix the whole issue all at once. It would allow me to better understand the code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
They make mistakes, too, which are harder to find because I tend to trust AI or rely on it too much.