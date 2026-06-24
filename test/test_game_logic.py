"""
Regression tests for the two bugs fixed in app.py.

Each test targets one specific bug so that if the broken behavior is ever
reintroduced, the test will fail and point right back at the cause.
"""

import os
import sys

# Make app.py importable when running pytest from anywhere.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import check_guess, fresh_game_state


# ---------------------------------------------------------------------------
# Bug 1: On even attempts the secret was cast to str, so check_guess compared
# an int guess to a str secret. Ordering then fell into the TypeError branch
# and compared the numbers LEXICOGRAPHICALLY ("9" > "4"), producing backwards
# higher/lower hints. The fix passes the int secret every time.
# ---------------------------------------------------------------------------

def test_correct_guess_registers_as_win_bug1():
    # A right answer must win.
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"


def test_string_secret_gives_backwards_hint_root_cause_bug1():
    # With an int secret the direction is correct: 9 is below 42 -> Too Low.
    assert check_guess(9, 42)[0] == "Too Low"
    # The ROOT CAUSE we fixed: with a str secret the comparison is
    # lexicographic ("9" > "4"), so the SAME guess is wrongly reported as
    # Too High. Removing the str() cast in app.py prevents this.
    assert check_guess(9, "42")[0] == "Too High"


# ---------------------------------------------------------------------------
# Bug 2: "New Game" reset only attempts + secret, leaving status/score/history
# stale, so after a win/loss the player stayed locked out. It also used a
# hardcoded 1..100 range. The fix resets all state via fresh_game_state().
# ---------------------------------------------------------------------------

def test_new_game_resets_all_state_bug2():
    state = fresh_game_state(1, 100)
    assert state["status"] == "playing"   # was stuck on "won"/"lost"
    assert state["score"] == 0
    assert state["history"] == []
    assert state["attempts"] == 0


def test_new_game_respects_difficulty_range_bug2():
    # Was hardcoded randint(1, 100); now uses (low, high). Sample repeatedly
    # since the secret is random.
    for _ in range(100):
        secret = fresh_game_state(1, 20)["secret"]
        assert 1 <= secret <= 20
