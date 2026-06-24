# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience
- [x] Describe the game's purpose.
User guess a secret number, get "higher/lower" hints, and try to win before running out of attempts.
- [x] Detail which bugs you found.
More bugs in reflection.md
1. Hints were incorrect.
2. Change difficulty didn't update the game.
3. "New Game" didn't refresh the game.
- [x] Explain what fixes you applied.
1. Guessing the correct number on even attempt, like 2, 4, 6 are no longer rejected.
2. "New Game" reset the score, history, and status.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and open the app.
2. User select a difficulty in the sidebar to set the number range.
3. User Type a guess and click "Submit Guess".
4. User read the hint: "Go HIGHER!" or "Go LOWER!", which is opposite right now.
5. Guess the right number to win and see user's score.
6. User can click "New Game" to reset everything and play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0 -- /Users/t.c./Desktop/2026/gameglitchinvestigator-starter/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/t.c./Desktop/2026/gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 4 items

test/test_game_logic.py::test_correct_guess_registers_as_win_bug1 PASSED [ 25%]
test/test_game_logic.py::test_string_secret_gives_backwards_hint_root_cause_bug1 PASSED [ 50%]
test/test_game_logic.py::test_new_game_resets_all_state_bug2 PASSED      [ 75%]
test/test_game_logic.py::test_new_game_respects_difficulty_range_bug2 PASSED [100%]

============================== 4 passed in 0.82s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
