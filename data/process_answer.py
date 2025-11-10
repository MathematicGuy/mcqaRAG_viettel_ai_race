import pandas as pd
import re

def write_answers_to_file(answers, answer_path='answer.md'):
    print('Write TASK QA')
    with open(answer_path, 'a') as f:
        f.write("\n\n### TASK QA\n")
        f.write("num_correct,answers\n")
        for answer in answers:
            print(answer)
            # Split by comma and strip spaces to count options
            options = [opt.strip() for opt in answer.split(',')]
            num_correct = len(options)
            # Format as required, quote if multiple
            if num_correct == 1:
                f.write(f"{num_correct},{answer}\n")
            else:
                f.write(f"{num_correct},\"{answer}\"\n")

# Read the CSV file
df = pd.read_csv('answers_output_qwen.csv')

# Extract and validate predicted answers using regex
predicted_answers = []
for answer in df['predicted_answer']:
    # Use regex to find only A, B, C, or D (case insensitive)
    match = re.search(r'[A-D]', str(answer).upper())
    if match:
        predicted_answers.append(match.group(0))
    else:
        # If no valid letter found, skip or use empty string
        predicted_answers.append('')

# Write to answer.md
write_answers_to_file(predicted_answers, answer_path='answer4.md')

print(f"Processed {len(predicted_answers)} answers and appended to answer.md")