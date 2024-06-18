
import time

def typing_master():
    print()
    text = "The quick brown fox jumps over the lazy dog."
    print()
    print("Type the following text:")
    print(text)
   
    input("Press Enter when you're ready to start...")
   
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()

    accuracy = sum(1 for a, b in zip(text, typed_text) if a == b) / len(text) * 100
    time_taken = end_time - start_time

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print()

    continue_typing = input("Do you want to continue? (yes/no): ")

    if continue_typing.lower() == "yes":
        typing_master()
    else:
        print("Thanks for using the Typing Master!")

# Start the typing master game
typing_master()
