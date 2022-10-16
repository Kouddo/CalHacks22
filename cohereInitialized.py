import cohere
import pandas as pd



prompt_cosmos = '''“The discovery that the Earth is a little world was made, as so many important human discoveries were, in the ancient Near East, in a time some humans call the third century B.C., in the greatest metropolis of the age, the Egyptian city of Alexandria. Here there lived a man named Eratosthenes."'''
prompt_GT = '''"Georgia Tech running backs coach Mike Daniels resigned his position, effective immediately. The team made the announcement Friday afternoon. The resignation is not believed to be performance-related, according to a person familiar with the situation. Donald Hill-Eley, who was promoted earlier this week from offensive analyst to offensive assistant and assistant special-teams coach to fill the vacancy created by Brent Key’s promotion from offensive line coach to interim head coach, will replace Daniels."'''
co = cohere.Client('JgMx33cwKF2GpRjKMh2Xc6BUen2CL1gfyfu3Zpw7', '2021-11-08')
n_generations = 5

prediction = co.generate(
    model='large',
    prompt=prompt_GT,
    return_likelihoods = 'GENERATION',
   
    max_tokens=500,
    temperature=0.7,
    num_generations=n_generations,
    k=0,
    p=0.75)

# Get list of generations
gens = []
likelihoods = []
for gen in prediction.generations:
    gens.append(gen.text)

    sum_likelihood = 0
    for t in gen.token_likelihoods:
        sum_likelihood += t.likelihood
    # Get sum of likelihoods
    likelihoods.append(sum_likelihood)

pd.options.display.max_colwidth = 200
# Create a dataframe for the generated sentences and their likelihood scores
df = pd.DataFrame({'generation':gens, 'likelihood': likelihoods})
# Drop duplicates
df = df.drop_duplicates(subset=['generation'])
# Sort by highest sum likelihood
df = df.sort_values('likelihood', ascending=False, ignore_index=True)
print("\n\n\n\n\n")
print('Candidate summaries for the sentence:')

print(df.head())
print("all done!")