import requests

#Database call function
def call_database_api(input_string):
    #make required API calls
    api1_url = "https://api2.cityscope.media/experiences"
    api2_url = "https://api2.cityscope.media/articles"
    api3_url = "https://api2.cityscope.media/bytes"
    
    response1 = requests.get(api1_url, params={"query": input_string})
    response2 = requests.get(api2_url, params={"query": input_string})
    response3 = requests.get(api3_url, params={"query": input_string})
    
    # Check if the API calls have returned any data
    if response1.ok:
        data = response1.json()
        return data
    elif response2.ok:
        data = response2.json()
        return data
    elif response3.ok:
        data = response3.json()
        return data
    else:
        return None

# CHAT GPT call function
def call_chatgpt_api(input_string):
    # call chatgpt API
    chatgpt_api_url = ""
    response = requests.post(chatgpt_api_url, json={"input": input_string})
    
    if response.ok:
        data = response.json()
        return data
    else:
        return None

# Define main function
def main():
    input_string = input("Enter your query: ")
    
    # check for the query in database
    data = call_database_api(input_string)
    
    if data is None:
        # If database APIs return no data, call ChatGPT API
        data = call_chatgpt_api(input_string)
    
    if data:
        print(data)
    else:
        print("No data found")

if __name__ == "__main__":
    main()
