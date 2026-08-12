# 24.Create a python program that recognizes dialog acts in a given dialog or conversation.

sentence = input("Enter a sentence: ").lower()
if sentence.endswith("?"):
    print("Dialog Act: Question")
elif sentence.startswith(("please", "kindly")):
    print("Dialog Act: Request")
elif any(word in sentence for word in ["hello", "hi", "good morning"]):
    print("Dialog Act: Greeting")
elif any(word in sentence for word in ["thanks", "thank you"]):
    print("Dialog Act: Thanking")
else:
    print("Dialog Act: Statement")