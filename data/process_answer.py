import pandas as pd
import re

def write_answers_to_file(answers, answer_path='answer.md'):
    print('Write TASK QA')
    with open(answer_path, 'a') as f:
        f.write("\n\n### TASK QA\n")
        f.write("num_correct,answers\n")
        for answer in answers:
            # Split by comma and strip spaces to count options
            num_correct = [opt.strip() for opt in answer.split(',')]
            print(len(num_correct), answer)
            # Format as required, quote if multiple
            if len(num_correct) == 1:
                f.write(f"{len(num_correct)},{answer.replace('"', ' ')}\n")
            else:
                f.write(f"{len(num_correct)},\"{answer}\"\n")

# Read the CSV file
df = pd.read_csv('answers_mcq_qwen4-2.csv')
qdf = pd.read_csv('question.csv')

# Extract and validate predicted answers using regex
predicted_answers = []
nan_time = 0
resp_time = 0
for answer in df['predicted_answer']:
    # Use regex to find only A, B, C, or D (case insensitive)
    # match = re.search(r'[A-D]', str(answer).upper())

    # predicted_answers.append(str(answer))

    if type(answer) is not str:
        predicted_answers.append(f'C')
        nan_time+=1
    elif answer:
        predicted_answers.append(answer)
        resp_time+=1
    # if answer == 'Ca' or answer == 'nan' or answer == 'NaN':
    #     predicted_answers.append('nan')


# Write to answer.md

if len(predicted_answers) < (281):
        predicted_answers.append('C')

print('question lenght:', len(qdf['Question']))
print(predicted_answers)
print(f"Total non-string answers: {nan_time}, Total string answers: {resp_time}", f"Nan to Resp Ratio: {nan_time/(nan_time+resp_time)} - {resp_time/(nan_time+resp_time)}")
write_answers_to_file(predicted_answers, answer_path='answer.md')
print(f"Processed {len(predicted_answers)} answers and appended to answer.md")