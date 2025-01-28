[![wakatime](https://wakatime.com/badge/user/49489c61-f548-4cec-982d-e443f9ca894f/project/c3b064e5-0ac8-43b6-8d37-b92d2e09c75a.svg)](https://wakatime.com/badge/user/49489c61-f548-4cec-982d-e443f9ca894f/project/c3b064e5-0ac8-43b6-8d37-b92d2e09c75a)

# Simple Quiz CLI Application

A command-line quiz application that asks multiple-choice questions and provides feedback on the user's answers. The quiz questions are loaded from a JSON file.

## Features

    ✅ Load multiple-choice questions from `questions.json`
    ✅ Ask questions one by one
    ✅ Accept user input and provide feedback
    ✅ Track and display the final score

## Requirements

- Python 3.x

## Installation

1. Clone the repository or copy the script.
2. Ensure Python 3 is installed.

## Usage

Run the script using:

```bash
python main.py
```

### Expected JSON Structure

The `questions.json` file should be structured as follows:

```json
[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "JavaScript", "C++", "Ruby"],
        "answer": "JavaScript"
    }
]
```

## Example

```
Question 1: What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Lisbon
Enter your choice: 3
✅ Correct!

Your final score: 1/1
```

## License

This project is open-source and available for use and modification.

## Contributions

Feel free to submit issues and pull requests to improve the project!

## Contact

For any questions or feedback, please feel free to [email me](mailto:goldendevuz@gmail.com).