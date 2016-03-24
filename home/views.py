from django.template.response import TemplateResponse
from home.models import Conversation


def home_page(request):
    context = {}
    post_dict = request.POST
    print(post_dict)

    if not post_dict:
        context['answer'] = "어서오세요"
    else:
        if 'ask' in post_dict:
            ask = post_dict['ask']
            context['ask'] = ask
            answer = Conversation.objects.values(
                'answer'
            ).filter(
                ask=ask
            )
            print(answer)
            if not answer:
                context['no_answer'] = "True"

            else:
                context['answer'] = answer[0]['answer']

            if "answer_of_user" in post_dict:
                Conversation.objects.create(
                    ask=post_dict["ask_of_user"],
                    answer=post_dict["answer_of_user"]
                )
                context['no_answer'] = "False"
                context['answer'] = post_dict['answer_of_user']



    return TemplateResponse(request, 'index.html', context)