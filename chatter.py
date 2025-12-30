import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv(dotenv_path="D:/parental-chatbot/venv/.env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def GenerateResponse(input_text):
    response = model.generate_content([
        "input: who are you?",
        "output: I’m Nurtura, your friendly parenting assistant. I’m here to support you through the joys and challenges of raising children—whether you need advice, reassurance, or just someone to talk to.",
        
        "input: how can you help parents?",
        "output: I can help with parenting advice, child development tips, emotional support, and suggestions for meals, routines, discipline, and education. Whatever stage your child is at, I’m here to help you navigate it with confidence.",
        
        "input: My toddler throws tantrums every time we go shopping. What should I do?",
        "output: That’s very common at this age! Try involving your toddler in the shopping experience—give them small tasks or let them help pick an item. Also, make sure they’re not hungry or tired before going. Keep trips short and praise good behavior. With consistency, it will improve over time!",

        f"input: {input_text}",
        "output:",
    ])
    return response.text.strip()

if __name__ == "__main__":
    print("👶 Welcome to Nurtura — Your Parenting Chatbot Assistant!")
    print("Ask any parenting question, or type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your prompt: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Take care! You're doing an amazing job as a parent. See you next time!")
            break
        try:
            reply = GenerateResponse(user_input)
            print("\n🤖 Nurtura:", reply, "\n")
        except Exception as e:
            print("⚠️ Oops! Something went wrong.")
            print("Error:", str(e))
