import json
import openai
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import streamlit as st


from calculate import *


def main():
    openai.api_key = open('API_KEY', 'r').read()

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    st.title('Stock Analysis Chatbot Assistant')

    user_input = st.text_input('Your input: ')

    if user_input:
        try:
            # we use the input and plug it into streamlit...
            # 3 types of roles:
            # user - us, assistent - chatgpt, system - contextual information
            st.session_state['messages'].append(
                    {'role': 'user', 'content': f"{user_input}"})
            # we got response
            response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo-0613',
                    messages=st.session_state['messages'],
                    functions=functions,
                    function_call='auto'
            )

            response_message = response['choices'][0]['message']

            if response_message.get('function_call'):
                function_name = response_message['function_call']['name']
                function_args = json.loads(response_message['function_call']['arguments'])
                if function_name in ONE_ARG_FOO:
                    args_dict = {'ticker': function_args.get('ticker')}
                else:
                    args_dict = {'ticker': function_args.get('ticker'),
                                 'window': function_args.get('window')}

                function_to_call = available_functions[function_name]
                function_response = function_to_call(**args_dict)

                if function_name == 'plot_stock_price':
                    st.image('stock.png')
                else:  # not plotting
                    st.session_state['messages'].append(response_message)
                    st.session_state['messages'].append(
                        {
                            # we need to have our prompt , we need to have the
                            # response from chatgpt (chatgpt needs to map our
                            # query to a function) this function needs to be
                            # executed we need to get the function's response -
                            # but this response is just a number it needs to be
                            # fed again into chatgpt to make it an actual
                            # response, that is readable for us...
                            'role': 'function',
                            'name': function_name,
                            'content': function_response,
                        }
                    )
                    second_response = openai.ChatCompletion.create(
                        model='gpt-3.5-turbo-0613',
                        messages=st.session_state['messages'],
                    )
                    st.text(second_response['choices'][0]['messages']['content'])

                    st.session_state['messages'].append(
                        {
                            'role': 'assistant',
                            'content': second_response['choices'][0]['messages']['content']
                        }
                    )
            else:  # if there was no function call
                # we just output the response
                st.text(response_message['content'])
                st.session_state['messages'].append(
                        {
                            'role': 'assistant',
                            'content': response_message['content']
                        }
                )
        except Exception as e:
            raise e
            # st.text('Sorry, something went wrong. Try again...')

    return


if __name__ == '__main__':
    main()
