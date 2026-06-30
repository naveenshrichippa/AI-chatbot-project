import os
from google import genai
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatHistory
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message
            )
            bot_response = response.text
        except Exception as e:
            print("Gemini API Error:", e)
            return JsonResponse({"response": "Sorry, something went wrong. Please try again."})

        ChatHistory.objects.create(
            user_message=user_message,
            bot_response=bot_response
        )
        return JsonResponse({"response": bot_response})

    return render(request, "chat.html")