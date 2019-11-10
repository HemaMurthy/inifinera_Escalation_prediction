import pandas as pd

def make(problem_descriptions, feedback):
    print('hmm...')
    for problem in  problem_descriptions.iterrows():
        print(list(feedback['problem_description_id']),'*')
        problem_id= problem[1].problem_description
        if problem_id in list(feedback['problem_description_id']):
            print(problem_id,' is present in feedback table')