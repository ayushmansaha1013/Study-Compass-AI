#code for initializing nvidia api
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)



#creation of what's to be printed in main menu to user to decide what they want
def main_menu():
    print("=== 📚  Study Compass ===\n")
    print("1. Log Study Session\n")
    print("2.  Ask ai Doubt\n")
    print("3. Get Recommendation\n")
    print("4. Exit\n")

#ask ai doubt brings Meta (formerly Facebook) AI model in contact with user for their queries
def ask_ai_doubt():
    ask_user = input("Please enter the doubt:\n")
    #model gets connected for user's query to be resolved
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content":
                """
                You are Study Compass,
                a study mentor for engineering students.

                Give:
                - concise answers
                - practical study advice
                - no long essays
                """
            },
            {
                "role": "user",
                "content": ask_user
            }
        ],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024
    )
    #Ending line 
    print("\nStudy Compass:")
    print(completion.choices[0].message.content)

#defining the function to log the study session of user and then giving them advice based on that session
def giving_recommendation():

    print("\n=== Get Recommendation ===\n")

    subject = input("Subject: ")

    confidence = int(
        input("Confidence (0-10): ")
    )

    user_goal = input(
        "What's your goal? (Exam/Placement/Project/Skill Learning): "
    )

    prompt = f"""
    Subject: {subject}

    Confidence Level: {confidence}/10

    Goal: {user_goal}

    Provide:

    1. Current Assessment
    2. What to Study Next
    3. One Practical Activity
    4. One Common Mistake to Avoid

    Keep the answer concise and practical.
    """

    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content": """
                You are Study Compass, a study mentor for engineering students.

                Rules:
                - Never assume information not provided.
                - Use only the data given by the user.
                - Give concise feedback.
                - Suggest next study steps.
                - Mention strengths and weaknesses.
                - Keep response under 150 words.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024
    )

    print("\n📚 Study Compass Recommendation:\n")
    print(completion.choices[0].message.content)

    print("\nStudy Compass:")
    print(completion.choices[0].message.content)

#user enters their session duration and the subject(s) covered in it and Meta api is connected here 
def log_study_session():
    sessions = input("Enter the no. of hrs dedicated for a session: ")
    subject = input("Enter the subject(s) studied in that session: ")
    confidence = input("Enter your confidence rate in this subject between 0-10 : ")
    
    #now bringing in all the inputs of user together

    user_input =(
    f"I studied {subject} for {sessions} hours. "
    f"My confidence level is {confidence}/10. "
    f"Analyze my progress and give practical study advice."
)

    #Meta model now gets feed of whatever entered
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content":
                """
                You are Study Compass,
                a study mentor for engineering students.

                Give:
                - concise answers
                - practical study advice
                - no long essays
                """
            },
            {
                "role": "user",
                "content": user_input #sending the concatenated input to the model
            }
        ],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024
    )

    print("\nStudy Compass:")
    print(completion.choices[0].message.content)


# the main soul of the program that makes the program work
def main():
    while True:

        #Displaying the main menu to user
        main_menu()

        #User enters their choice and let's computer know about it
        choice = input("\n Choose your option to go ahead: ")

        #calling log the study session:
        if choice == "1":
            log_study_session()
        #calling ai doubt resolver
        elif choice == "2":
            ask_ai_doubt()
        #calling recommendation function
        elif choice == "3":
            giving_recommendation()
        #user decided to exit now
        elif choice == "4":
            print("bye for now!!\n")
            break
        #user selected some invalid option
        else:
            print("You have selected an invalid option!!\n")
            print("Please choose the correct one!\n")



#Starting of program
main()



