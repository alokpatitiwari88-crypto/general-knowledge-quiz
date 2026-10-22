# The General Knowledge Quiz

A terminal-based trivia game built with Python. Test your general knowledge across multiple categories with randomized, non-repeating questions, defensive input normalization, and real-time score tracking.

---

## Features

- **Curated Question Pool**: Draws from a pool of diverse general knowledge questions (geography, science, arts, history, and nature).
- **Non-Repeating Questions**: Questions are sampled without replacement so you never see the same question repeated within a game or across consecutive rounds.
- **Robust Input Normalization**: Defensively cleans answers with `.strip()` and `.lower()` so accidental spacing and case variations (e.g., `  PaRiS  ` or `MARS`) are graded accurately.
- **Immediate Feedback**: Gives instant confirmation for correct answers (+1 point) and reveals the correct answer upon incorrect inputs.
- **Performance Summary & Scoring**: Displays your final score out of 3 along with custom feedback tailored to your performance tier.
- **Replay Support**: Offers a continuous play option to start new rounds seamlessly.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.

### How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/alokpatitiwari88-crypto/general-knowledge-quiz.git
   cd general-knowledge-quiz
   ```

2. Run the game in your terminal:
   ```bash
   python quiz.py
   ```
   *(or `py quiz.py` on Windows)*

---

## Gameplay Preview

```text
=============================================
         THE GENERAL KNOWLEDGE QUIZ         
=============================================
Answer the 3 questions below:

Question 1: What is the capital of France?
Your answer: paris
Correct! Excellent job! (+1 point)

Question 2: Which planet is known as the Red Planet?
Your answer: Mars
Correct! Excellent job! (+1 point)

Question 3: What is the largest ocean on Earth?
Your answer: pacific ocean
Correct! Excellent job! (+1 point)

=============================================
Quiz Complete! Your Final Score: 3/3
Feedback: Outstanding! You got a perfect score!
=============================================

Would you like to play another round? (yes/no):
```

---

## Project Structure

```text
general-knowledge-quiz/
├── quiz.py         # Main game logic and question bank
├── README.md       # Project documentation
└── .gitignore      # Git ignore rules
```

---

## License

This project is open source and available under the [MIT License](LICENSE).
