while True:
    # Print something
    original_text = input("Enter text to edit (or type 'exit' to end): ")
    
    # Check if the user wants to exit the loop
    if original_text.lower() == 'exit':
        break

    # Edit the text (you can replace this with your own editing logic)
    edited_text = original_text.upper()

    # Print the edited text
    print("Edited text:", edited_text)
