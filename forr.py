# Import libraries
import aima.utils
import aima.logic

# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []

    # Add first-order logic clauses (rules and fact)
    personality_types = ['Alpha', 'Beta', 'Sigma', 'Omega', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Theta', 'Iota']
    rules = [
        'HasTrait(x, Extraversion) & Not(HasTrait(x, Neuroticism)) & HasTrait(x, Conscientiousness) & HasTrait(x, Openness) & Not(HasTrait(x, Agreeableness)) ==> Alpha(x)',
        'Not(HasTrait(x, Extraversion)) & HasTrait(x, Agreeableness) & HasTrait(x, Neuroticism) & Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) ==> Beta(x)',
        'HasTrait(x, Openness) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Neuroticism)) ==> Sigma(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Neuroticism) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Agreeableness)) ==> Omega(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & Not(HasTrait(x, Extraversion)) & HasTrait(x, Agreeableness) & Not(HasTrait(x, Neuroticism)) ==> Gamma(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & HasTrait(x, Extraversion) & HasTrait(x, Agreeableness) & Not(HasTrait(x, Neuroticism)) ==> Delta(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Neuroticism)) ==> Epsilon(x)',
        'HasTrait(x, Openness) & Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Extraversion) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Neuroticism)) ==> Zeta(x)',
        'HasTrait(x, Agreeableness) & HasTrait(x, Extraversion) & Not(HasTrait(x, Neuroticism)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Openness)) ==> Theta(x)',
        'HasTrait(x, Conscientiousness) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Neuroticism)) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Openness)) ==> Iota(x)',
        'Not(HasTrait(x, Extraversion)) & HasTrait(x, Neuroticism) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Openness)) & HasTrait(x, Agreeableness) ==> Alpha(x)',
        'HasTrait(x, Extraversion) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Neuroticism)) & HasTrait(x, Openness) & HasTrait(x, Conscientiousness) ==> Beta(x)',
        'Not(HasTrait(x, Openness)) & HasTrait(x, Agreeableness) & HasTrait(x, Conscientiousness) & HasTrait(x, Extraversion) & HasTrait(x, Neuroticism) ==> Sigma(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & Not(HasTrait(x, Neuroticism)) & HasTrait(x, Extraversion) & HasTrait(x, Agreeableness) ==> Omega(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Extraversion) & Not(HasTrait(x, Agreeableness)) & HasTrait(x, Neuroticism) ==> Gamma(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Agreeableness)) & HasTrait(x, Neuroticism) ==> Delta(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & HasTrait(x, Extraversion) & HasTrait(x, Agreeableness) & HasTrait(x, Neuroticism) ==> Epsilon(x)',
        'Not(HasTrait(x, Openness)) & HasTrait(x, Conscientiousness) & Not(HasTrait(x, Extraversion)) & HasTrait(x, Agreeableness) & HasTrait(x, Neuroticism) ==> Zeta(x)',
        'Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Extraversion)) & HasTrait(x, Neuroticism) & HasTrait(x, Conscientiousness) & HasTrait(x, Openness) ==> Theta(x)',
        'Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Extraversion) & HasTrait(x, Neuroticism) & HasTrait(x, Agreeableness) & HasTrait(x, Openness) ==> Iota(x)'
    ]
     # Add indirect questions
    indirect_questions = [
        'LikesReading(x) ==> HasTrait(x, Openness)',
        'LikesNewExperiences(x) ==> HasTrait(x, Openness)',
        'IsOrganized(x) ==> HasTrait(x, Conscientiousness)',
        'IsCareful(x) ==> HasTrait(x, Conscientiousness)',
        'IsSocial(x) ==> HasTrait(x, Extraversion)',
        'LikesParties(x) ==> HasTrait(x, Extraversion)',
        'IsSympathetic(x) ==> HasTrait(x, Agreeableness)',
        'LikesHelpingOthers(x) ==> HasTrait(x, Agreeableness)',
        'GetsNervous(x) ==> HasTrait(x, Neuroticism)',
        'WorriesALot(x) ==> HasTrait(x, Neuroticism)',
        'Not(LikesReading(x)) ==> Not(HasTrait(x, Openness))',
        'Not(LikesNewExperiences(x)) ==> Not(HasTrait(x, Openness))',
        'Not(IsOrganized(x)) ==> Not(HasTrait(x, Conscientiousness))',
        'Not(IsCareful(x)) ==> Not(HasTrait(x, Conscientiousness))',
        'Not(IsSocial(x)) ==> Not(HasTrait(x, Extraversion))',
        'Not(LikesParties(x)) ==> Not(HasTrait(x, Extraversion))',
        'Not(IsSympathetic(x)) ==> Not(HasTrait(x, Agreeableness))',
        'Not(LikesHelpingOthers(x)) ==> Not(HasTrait(x, Agreeableness))',
        'Not(GetsNervous(x)) ==> Not(HasTrait(x, Neuroticism))',
        'Not(WorriesALot(x)) ==> Not(HasTrait(x, Neuroticism))'
    ]
    questions = [
        'Do you like reading?',
        'Do you like new experiences?',
        'Are you organized?',
        'Are you careful?',
        'Are you social?',
        'Do you like parties?',
        'Are you sympathetic?',
        'Do you like helping others?',
        'Do you get nervous?',
        'Do you worry a lot?'
    ]

    
    for rule in rules + indirect_questions:
        clauses.append(aima.utils.expr(rule))

    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)

    # Ask the user indirect questions and add their responses to the knowledge base
    user = input("What's your name? ")
    for i, question in enumerate(questions):
        answer = input(question + ' (yes/no) ')
        if answer.lower() == 'yes':
            KB.tell(aima.utils.expr(indirect_questions[i].split('==>')[0].replace('x', user)))
        elif answer.lower() == 'no':
            # Add the negation of the trait to the knowledge base
            trait = indirect_questions[i].split('==>')[1].split(',')[1].strip()
            KB.tell(aima.utils.expr(f'Not({trait}({user}))'))
    
    # Get information from the knowledge base with ask
    for personality in personality_types:
        answer = aima.logic.fol_fc_ask(KB, aima.utils.expr(f'{personality}({user})'))
        print(f'Is {user} a {personality}?')
        for k in KB.clauses:
            print(k)
        print('True' if list(answer) else 'False')
# Tell python to run main method
if __name__ == "__main__":
    main()