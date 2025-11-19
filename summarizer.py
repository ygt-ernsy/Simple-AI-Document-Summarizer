# 1. Import the 'ollama' library
import ollama
import sys
import argparse

def main():
    """
    Main function to run the chat client.
    """
    
    model_name = "llama3:8b"

    messages = [
        {
            'role': 'system',
            'content': "You are an expert summarization assistant. Your job is to provide a clear and concise summary of the text you are given. Focus on extracting the main ideas and key points. Start with a short introductory paragraph, followed by bullet points for the key takeaways.",
        }
    ]

    # Messages read from the file given
    parser = argparse.ArgumentParser(description="Summerizer script")
    parser.add_argument("filename", help="The path to the next file to summerize.")
    args = parser.parse_args()

    file_to_read = args.filename

    try:
        with open(file_to_read, "r") as file:
            file_content = file.read();
            print(f"Successfully read {len(file_content)} characters from {file_to_read}!")
            print("\n--- Content ---")
            print(file_content)

        try:
            user_input = file_content

            messages.append(
                {
                    'role': 'user',
                    'content': user_input,
                }
            )

            response_dictionary = ollama.chat(
                model=model_name,
                messages=messages,
                stream=False  # We want the full response at once
            )

            bot_response = response_dictionary['message']['content']

            print(bot_response)
            
            messages.append(
                {
                    'role': 'assistant',
                    'content': bot_response,
                }
            )

        except Exception as e:
            # 17. Handle errors (like if the server is not running)
            print(f"\nAn error occurred: {e}", file=sys.stderr)
            print("Please make sure the Ollama server is running ('make up') and you have pulled the model ('make pull').")

    except FileNotFoundError:
        print(f"Error: The file '{file_to_read}' was not found.")
    except Exception as e:
        print("An error occured")

    print(f"Chatting with '{model_name}'. Type 'exit' to quit.")
    

# 18. Run the main function
if __name__ == "__main__":
    main()
