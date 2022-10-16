import cohere


co = cohere.Client('JgMx33cwKF2GpRjKMh2Xc6BUen2CL1gfyfu3Zpw7', '2021-11-08')
prediction = co.generate(
            prompt="Ben Shapiro is going to the mars because",
            model='large',
            max_tokens=20)

print('prediction: {}'.format(prediction.generations[0].text))