# Importing Dependencies
from chronological import read_prompt, cleaned_completion, main

# Takes in the training prompt and returns the completed response 
async def summarization_example(): 
    # Takes in a text file(summarize_for_a_2nd_grader) as the input prompt
    prompt_summarize = read_prompt('summarize_for_a_2nd_grader')    
    # Calling the completion method along with the specific GPT-3 parameters
    completion_summarize = await cleaned_completion(prompt_summarize, 
    max_tokens=100, engine="davinci", temperature=0.5, top_p=1, 
    frequency_penalty=0.2, stop=["\n\n"])
    # Return the completion response
    return completion_summarize

# Designing the end-to-end async workflow, capable of running multiple prompts 
# in parallel  
async def workflow():
    # Making async call to the summarization function
    text_summ_example = await summarization_example()
    # Printing the result in console
    print('-------------------------')
    print('Basic Example Response: {0}'.format(text_summ_example))
    print('-------------------------')
# invoke Chronology by using the main function to run the async workflow
main(workflow)