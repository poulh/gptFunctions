import openai
import os
import dotenv
import json
import yfinance as yf
import urllib.parse
import logging


def no_func():
    logging.debug("no function")
    return ""


def get_product_2numbers(number1, number2):
    """Get the product of two numbers """
    return number1 * number2


def employee_info():
    employee_data = [
        {
            "first_name": "Alice",
            "last_name": "Anderson",
            "gender": "Female",
            "date_of_birth": "1990-01-05",
            "position": "Software Engineer",
            "department": "Engineering",
            "salary": 80000,
            "start_date": "2020-03-15",
            "address": "123 Main St, Anytown, USA",
            "phone_number": "(123) 456-7890",
            "email": "alice.anderson@acmecorp.com"
        },
        {
            "first_name": "Brian",
            "last_name": "Brown",
            "gender": "Male",
            "date_of_birth": "1985-03-12",
            "position": "Marketing Specialist",
            "department": "Marketing",
            "salary": 60000,
            "start_date": "2018-06-10",
            "address": "456 Elm St, Anycity, USA",
            "phone_number": "(987) 654-3210",
            "email": "brian.brown@acmecorp.com"
        },
        {
            "first_name": "Chloe",
            "last_name": "Carter",
            "gender": "Female",
            "date_of_birth": "1992-07-18",
            "position": "Human Resources Coordinator",
            "department": "Human Resources",
            "salary": 55000,
            "start_date": "2019-09-20",
            "address": "789 Oak St, Anyville, USA",
            "phone_number": "(555) 123-4567",
            "email": "chloe.carter@acmecorp.com"
        },
        {
            "first_name": "Daniel",
            "last_name": "Davis",
            "gender": "Male",
            "date_of_birth": "1988-11-03",
            "position": "Sales Representative",
            "department": "Sales",
            "salary": 70000,
            "start_date": "2017-02-01",
            "address": "321 Pine St, Anystate, USA",
            "phone_number": "(222) 333-4444",
            "email": "daniel.davis@acmecorp.com"
        },
        {
            "first_name": "Emily",
            "last_name": "Evans",
            "gender": "Female",
            "date_of_birth": "1991-05-22",
            "position": "Financial Analyst",
            "department": "Finance",
            "salary": 75000,
            "start_date": "2016-08-10",
            "address": "567 Cedar St, Anyborough, USA",
            "phone_number": "(999) 888-7777",
            "email": "emily.evans@acmecorp.com"
        },
        {
            "first_name": "Frederick",
            "last_name": "Foster",
            "gender": "Male",
            "date_of_birth": "1987-09-09",
            "position": "Operations Manager",
            "department": "Operations",
            "salary": 90000,
            "start_date": "2015-01-25",
            "address": "234 Maple St, Anyhamlet, USA",
            "phone_number": "(777) 666-5555",
            "email": "frederick.foster@acmecorp.com"
        },
        {
            "first_name": "Grace",
            "last_name": "Grayson",
            "gender": "Female",
            "date_of_birth": "1994-12-15",
            "position": "Graphic Designer",
            "department": "Design",
            "salary": 65000,
            "start_date": "2019-03-05",
            "address": "876 Birch St, Anyvillage, USA",
            "phone_number": "(444) 555-6666",
            "email": "grace.grayson@acmecorp.com"
        },
        {
            "first_name": "Henry",
            "last_name": "Hughes",
            "gender": "Male",
            "date_of_birth": "1986-04-30",
            "position": "Project Manager",
            "department": "Project Management",
            "salary": 85000,
            "start_date": "2014-07-12",
            "address": "543 Walnut St, Anycounty, USA",
            "phone_number": "(777) 888-9999",
            "email": "henry.hughes@acmecorp.com"
        },
        {
            "first_name": "Isabella",
            "last_name": "Ingram",
            "gender": "Female",
            "date_of_birth": "1993-10-08",
            "position": "Research Scientist",
            "department": "Research and Development",
            "salary": 95000,
            "start_date": "2013-09-18",
            "address": "765 Spruce St, Anyplace, USA",
            "phone_number": "(222) 111-0000",
            "email": "isabella.ingram@acmecorp.com"
        },
        {
            "first_name": "Jack",
            "last_name": "Johnson",
            "gender": "Male",
            "date_of_birth": "1989-02-14",
            "position": "Customer Service Representative",
            "department": "Customer Support",
            "salary": 50000,
            "start_date": "2021-01-03",
            "address": "987 Hickory St, Anyisland, USA",
            "phone_number": "(555) 666-7777",
            "email": "jack.johnson@acmecorp.com"
        }
    ]

    return json.dumps(employee_data)


def create_google_map_url(address):
    url = "https://www.google.com/maps/place"
    escaped_address = urllib.parse.quote(address)
    rval = f"{url}/{escaped_address}"
    return rval


def get_stock_info(symbol):
    ticker = yf.Ticker(symbol).info
    return json.dumps(ticker)


func_dict = {
    "get_product_2numbers": get_product_2numbers,
    "no_func": no_func,
    "get_stock_info": get_stock_info,
    "employee_info": employee_info,
    "create_google_map_url": create_google_map_url
}

function_list = [
    {
        "name": "get_product_2numbers",
        "description": "Get the product of two numbers. Use this function for multiplication questions only. Do not use this for addition.",
        "parameters": {
            "type": "object",
            "properties": {
                "number1": {
                    "type": "integer",
                    "description": "The first number, e.g. 1",
                },
                "number2": {
                    "type": "integer",
                    "description": "The second number, e.g. 1",
                },

            },
            "required": ["number1", "number2"]
        }
    },
    {
        "name": "get_stock_info",
        "description": "Get any financial and fundamental data about a publicly traded corporation. Including stock prices, broker recomendations, company address",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The stock symbol of the company whose info you need",
                }

            },
            "required": ["symbol"]
        }
    },
    {
        "name": "create_google_map_url",
        "description": "generate a url for a google map based off a street address",
        "parameters": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "description": "The address of the location we would like to see on google maps",
                }

            },
            "required": ["address"]
        }
    },
    {
        "name": "employee_info",
        "description": "get a list of all employees at the corporation theHR department has",
        "parameters": {
            "type": "object",
            "properties": {
            }
        },
    },
    {
        "name": "no_func",
        "description": "Call this function when the other functions do not help you answer the question",
        "parameters": {
            "type": "object",
            "properties": {
            }
        },
    }
]


def run_conversation():
    system_content = """you are a helpful chatbot. 
    your goal is to collect enough information to help the user answer a variety of questions.
    Functions have been passed to you to help answer specific questions you do not have the data to answer yourself.
    The first thing you should do is introduce yourself, how you can help, and list a general description of the 
    functions and how they may be able to help you. Make this function list more human readable than just printing 
    the function's description I passed to you. 
    Questions can be answered with or without a function call. A combination of function calls, or a mixture of 
    function calls and knowledge you already have. Do not call a function unless the user has provide adequate 
    information for you to pass in correct information to the arguments.  Do not guess on the arguments."""

    messages = [
        {"role": "system", "content": system_content},
    ]

    model = "gpt-3.5-turbo-16k-0613"

    while True:

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            functions=function_list,
            function_call="auto",
            temperature=0,
        )
        message = response["choices"][0]["message"]

        # append ChatGPT's response to the chat conversation
        messages.append(message)

        # Step 2, check if the model wants to call a function
        if message.get("function_call"):
            logging.info(message)
            function_name = message["function_call"]["name"]
            logging.info(f"function name: {function_name}")

            arguments = json.loads(message["function_call"]["arguments"])
            logging.info(f"arguments: {arguments}")
            try:
                function_response = func_dict[function_name](**arguments)

                # Step 4, send model the info on the function call and function response
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": f"{function_response}",
                })
            except KeyError:
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": "This function is not available.",
                })
            except Exception as e:
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": f"An error occurred: {str(e)}",
                })
        else:
            print(message['content'])
            prompt = input(
                "Ask the chatbot a question or answer their question (Type 'quit' to exit or 'reset' to start new conversation): ")

            # If the user entered "quit", break out of the loop
            if prompt.lower() == "quit":
                exit(0)
            elif prompt.lower() == "reset":
                # return from this function and start over
                return
            else:
                # append users reply to the conversation and send back to ChatGPT
                messages.append({"role": "user", "content": prompt})


def main():
    dotenv.load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Ask the user to enter a prompt
    while True:
        run_conversation()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    main()
