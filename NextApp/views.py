from django.shortcuts import render
from django.http import HttpResponse
import openai
openai.api_key = "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"
def hi(request):
    return render(request,"NextApp/index.html")












def chat_view(request):
    user_input = None
    def generate_text(prompt):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        temperature=0.1)
        return response.choices[0].text
    
    if request.method == 'POST':
        user_input = request.POST.get('NextAI1', '')
        prompt =user_input
        generate_texted = generate_text(prompt)

        # Retrieve the value of 'NextAI1' from the POST data
        # Do something with the user_input, such as processing or saving to the database
        response_content = f"""<body style='background-color:#C5DFF8;font-size: 2.2em; text-align:center;><h3 style='color: black;'><pre> {generate_texted}</pre></h3></body>"""
        return HttpResponse(response_content)

    return render(request, 'NextApp/index.html')
