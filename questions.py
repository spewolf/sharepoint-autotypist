# questions.py contains questions for specific form elements

def askSuccess():
    print('''
        1. No success to report
        2. Academic achievement (exam, GPA)
        3. Attends programs (hall or campus)
        4. Found a Job
        5. Friend group on floor
        6. Has met with faculty/advisor
        7. Has used campus resources
        8. Identified major at BGSU
        9. Intramural team
        10. Joined a student organization
        11. Positive personal experience (specify in notes)
        12. Positive roommate relationship
        13. Regularly attends class
    ''')
    success = input('Success?\n>> ')
    return 0 if not success else int(success) - 1

def askChallenge():
    print('''
        1. No challenge to report
        2. Conduct Issue
        3. Death/Illness in family
        4. Family issues
        5. Financial Issues
        6. Goes home frequently
        7. Medical/Injury
        8. Not attending class
        9. Not on floor frequently
        10. Relationship challenge
        11. roommate issue
        12. Struggling academically
        13. Student of concern
        14. Thinking of transferring
    ''')
    challenge = input('Challenge?\n>> ')
    return 0 if not challenge else int(challenge) - 1

def askFlag():
    print('''
        1. Unlikely
        2. Likely
    ''')
    returning = input('Returning?\n>> ')
    return 1 if not returning else int(returning) - 1

challengeQuestions = [
    'None',
    'Academic Performance',
    'Advising/Registration',
    'Financial Challenge',
    'Thinking of leaving university/transferring'
]
def askChallengeQuestion():
    for i in range(len(resources)):
        print('{0}. {1}'.format(i + 1, resources[i]))
    challenge = input('Challenge Question?\n>> ')
    return 0 if not challenge else int(challenge) - 1

resources = [
    'None',
    'Academic Advisor',
    'BGSU Police',
    'Bursars Office',
    'Campus Activities',
    'Campus Operations',
    'Carreer Center',
    'Counceling Center',
    'Dean of Students Office',
    'Falcon Health Center',
    'Financial Aid',
    'FSRC Guide',
    'Hall Director',
    'Learning Commons',
    'Multicultural Affairs',
    'Office of residence life',
    'Other',
    'Personal Advice',
    'Professor',
    'Student Contact',
    'Student Employment',
    'Title IX Coordinator',
]

def askResource():
    for i in range(len(resources)):
        print('{0}. {1}'.format(i + 1, resources[i]))
    resource = input('Resource?\n>> ')
    return 0 if not resource else int(resource) - 1

def askAdvice():
    return input('Personal Advice/Experience?\n>> ')

def askNotes():
    return input('Notes?\n>> ')
