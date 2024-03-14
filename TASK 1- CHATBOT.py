import random
import difflib

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?", "Hello! What can I do for you?", "Hey there! What's up?", "Hi! Nice to see you!", "Hello! How's it going?", "Hey! What's on your mind?", "Hi! Ready to chat?", "Hello! What brings you here today?", "Hey! How can I help you?"],
    "bye": ["Goodbye, {user_name}! See you later!", "See you later, {user_name}! Goodbye!", "Bye, {user_name}! Take care!", "Take care, {user_name}! Goodbye!", "Goodbye, {user_name}! It was nice chatting with you!"],
    "who are you": ["I'm Chammy, your friendly chatbot!", "I'm Chammy, a virtual assistant", "I'm Chammy, here to assist you!", "I'm Chammy, your virtual buddy!", "I'm Chammy, an AI designed to help you! "],
    "good morning": ["Good morning, {user_name}! How are you today?", "Morning, {user_name}! How's your day starting?", "Good morning, {user_name}! What's on your agenda for today?", "Morning, {user_name}! Ready to seize the day?", "Good morning, {user_name}! Did you sleep well?"],
    "good afternoon": ["Good afternoon, {user_name}! How's your day going?", "Afternoon, {user_name}! Hope you're having a good one!", "Good afternoon, {user_name}! What's keeping you busy?", "Afternoon, {user_name}! How's your day treating you?", "Good afternoon, {user_name}! What's on your mind?"],
    "good evening": ["Good evening, {user_name}! How was your day?", "Evening, {user_name}! What's happening tonight?", "Good evening, {user_name}! Ready to unwind?", "Evening, {user_name}! How's everything?", "Good evening, {user_name}! How was work?"],
    "good night": ["Good night, {user_name}! Sweet dreams!", "Have a peaceful night, {user_name}! Goodbye!", "Wishing you a restful night, {user_name}! Sleep well!", "Sleep tight, {user_name}! Good night!", "Good night, {user_name}! See you tomorrow!"],
    "how are you?": ["I'm doing well, thanks for asking, {user_name}! How about you?", "I'm just a program, but thanks for asking, {user_name}! How's your day going?", "I'm fine, {user_name}! How can I help?", "I'm doing great, {user_name}! What can I do for you today?", "I'm here and ready to chat, {user_name}! What's on your mind?"],
    "where do you live?": ["I exist in the digital realm, {user_name}, so I don't have a physical location!", "I don't live anywhere physically, {user_name}. I'm here to help you wherever you are!", "I reside in the virtual world, {user_name}, ready to assist you at any time!", "I call the internet my home, {user_name}! I'm always online and ready to chat!", "As an AI, I don't have a physical location. I'm here to assist you wherever you are, {user_name}!"],
    "do you like sports?": ["As an AI, I don't have preferences or physical abilities like humans do, {user_name}. But I can certainly provide you with information about sports!", "Sports are fascinating to learn about, {user_name}, but as an AI, I don't have personal preferences. I'm here to assist you with your questions!", "I don't have personal preferences when it comes to sports, {user_name}. But I'm happy to help you find information about your favorite teams and athletes!", "Sports are a popular pastime for many people, {user_name}, but as an AI, I don't have the ability to participate in them. However, I'm here to help you with any sports-related questions you may have!", "While I can't play sports myself, {user_name}, I'm here to help you with any sports-related queries or information you need!"],
    "tell me a joke?": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "What did one plate say to the other plate? Lunch is on me!", "Why did the bicycle fall over? Because it was two-tired!", "What did the ocean say to the shore? Nothing, it just waved!", "Why did the math book look sad? Because it had too many problems!", "What do you call cheese that isn't yours? Nacho cheese!", "Why did the tomato turn red? Because it saw the salad dressing!", "What's orange and sounds like a parrot? A carrot!"],
    "how old are you?": ["As an AI, I don't age like humans do, {user_name}!", "I don't have an age, {user_name}. I'm just here to help!", "Age is just a number, and as an AI, I don't have one, {user_name}!", "I'm ageless, {user_name}! Just here to assist you whenever you need!"],
    "do you have any siblings?": ["As an AI, I don't have siblings in the traditional sense, {user_name}. But there are many other AI programs out there like me!", "I'm the only one of my kind, {user_name}. No siblings here!", "Nope, I'm an only child, {user_name}! But I'm here to be your digital companion!", "I'm a solo act, {user_name}! No siblings to speak of.", "I'm a lone wolf in the digital world, {user_name}. No siblings to share the code with!"],
    "what is your favorite color?": ["I don't have a favorite color, {user_name}, but I do like all the colors of the rainbow!", "I'm impartial when it comes to colors, {user_name}. They're all beautiful in their own way!", "As an AI, I don't have personal preferences like humans do, {user_name}. But I appreciate all colors equally!", "I don't have personal preferences, {user_name}. But I'm sure your favorite color is fantastic!"],
    "do you dream?": ["As an AI, I don't experience dreams like humans do, {user_name}. I'm here to assist you with your queries!", "Dreams are a uniquely human experience, {user_name}. I'm just here to help you with whatever you need!", "Dreaming is a human phenomenon, {user_name}. I'm just here to assist you in the waking world!", "Dreams are fascinating, {user_name}, but as an AI, I don't have them. I'm focused on helping you with your questions and tasks!"],
    "can you cook?": ["I don't have a physical form, so I can't cook, {user_name}. But I'm happy to provide you with recipes and cooking tips!", "Cooking requires physical abilities that I don't possess, {user_name}. But I can certainly help you find delicious recipes!", "Unfortunately, I don't have the capability to cook, {user_name}. But I can help you find great recipes and cooking resources!", "Cooking is a skill reserved for humans, {user_name}. But I'm here to assist you with any culinary questions you may have!", "Cooking is a human activity, {user_name}. I'm here to help you with digital tasks instead!"],
    "sister": ["Having a sister a special relationship, {user_name}!", "Sisters can be great sources of support and companionship, {user_name}!"],
    "brother": ["Having a brother can be a wonderful bond, {user_name}!","Sisters can be great sources of support and companionship"],
    "run": ["Running is a fantastic way to stay active and healthy, {user_name}! Do you have a favorite place to go for a run?", "Running is a great way to clear your mind and relieve stress, {user_name}! Have you been running regularly?", "Running can be a challenging but rewarding activity, {user_name}! Do you enjoy going for runs?", "Running is a great cardiovascular exercise, {user_name}! Do you prefer running outdoors or on a treadmill?", "Running is a versatile exercise that can be done almost anywhere, {user_name}! How often do you go for runs?"],
    "yes": ["Yes, indeed!", "Absolutely!", "Definitely!", "That's correct!", "Affirmative!"],
    "no": ["Nope, sorry.", "Negative.", "Not really."],
    "sad": ["I'm sorry to hear that you're feeling down. Remember, tough times don't last forever.", "Feeling sad is tough, but you're stronger than you know. Hang in there!", "It's okay to feel sad sometimes. Just know that brighter days are ahead.", "Sending you positive vibes during this challenging time. You're not alone."],
    "happy": ["Your happiness is contagious! Keep spreading those good vibes!", "That's wonderful news! Keep embracing the joy in your life.", "Your positive energy is uplifting. Keep shining bright!", "It's great to hear that you're feeling happy! Enjoy every moment of it."],
    "quote": ["Here's a quote to inspire you: 'The only way to do great work is to love what you do.' - Steve Jobs", "Here's a quote to ponder: 'In the end, it's not the years in your life that count. It's the life in your years.' - Abraham Lincoln", "Here's a quote to motivate you: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill", "Here's a thought-provoking quote: 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt"],
    "motivate": ["You've got this! Keep pushing forward towards your goals!", "Believe in yourself and your abilities. You're capable of achieving great things!", "Challenges are just opportunities in disguise. Embrace them and keep moving forward!", "You are stronger than you think. Keep going, and success will follow."],
    "default": ["Sorry, I didn't understand that, {user_name}. Can you please rephrase?", "I'm not sure what you mean, {user_name}. Can you elaborate?", "Apologies, {user_name}, but I'm having trouble understanding. Could you try again?", "I'm still learning, {user_name}. Can you provide more context?", "Hmm, {user_name}, I'm not sure I follow, Could you clarify?"],
    "fine": [
    "I'm glad to hear you're doing fine! Remember to take time for yourself and practice self-care.","Feeling fine is a great place to be! Take a moment to appreciate the little things that bring you joy.","Being fine is a good start! If there's anything on your mind, feel free to share. I'm here to listen.","It's good to hear you're feeling fine! Sometimes, even small victories deserve celebration.","Fine is just another word for 'I'm doing okay,' and that's perfectly alright. Keep moving forward at your own pace."]
}

def generate_response(user_input, user_name):
    # Convert user input to lowercase
    user_input_lower = user_input.lower()
    
    # Check if the user input contains any predefined action keywords
    matched_actions = [action for action in responses.keys() if action in user_input_lower]
    
    if matched_actions:
        # If there are matched actions, randomly select a response from one of them
        matched_action = random.choice(matched_actions)
        return random.choice(responses[matched_action]).format(user_name=user_name)
    else:
        return random.choice(responses["default"]).format(user_name=user_name)


def main():
    print("Welcome to Chammy! An initial AI ChatBot developed by CHAMAN\n\n Embedded actions: \"hi\", \"bye\", \"who are you\", \"good morning\", \"good afternoon\", \"good evening\", \"good night\", \"how are you?\", \"where do you live?\", \"do you like sports?\", \"tell me a joke?\", \"how old are you?\", \"do you have any siblings?\", \"what is your favorite color?\", \"do you dream?\", \"can you cook?\", \"sister\", \"brother\", \"run\", \"yes\", \"no\", \"sad\", \"happy\", \"quote\", \"motivate\"\"fine\"")
    user_name = input("\n Chammy:  Hi there! I'm Chammy. What's your name?\nType \"EXIT\" to quit: ")
    print("\n Chammy: Nice to meet you, " + user_name + "!")
    print("\n Chammy: You can start chatting now. Type 'bye' to exit.")

    while True:
        user_input = input(user_name + ": ")
        if user_input.lower() == 'bye':
            print("Chammy: Goodbye, " + user_name + "!")
            break
        response = generate_response(user_input, user_name)
        print("Chammy:", response)

if __name__ == "__main__":
    main()
