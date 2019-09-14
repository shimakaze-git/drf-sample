from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

# Create your views here.

from .models import Choice, Question


# from rest_framework.views import APIView

from .factories import (
    build_show_vote_results_use_case,
    build_show_vote_detail_use_case,
    build_show_vote_index_use_case,
)


def index(request):
    use_case = build_show_vote_index_use_case()

    context = use_case.execute()
    template = loader.get_template("polls/index.html")

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_show_vote_detail_use_case()
    try:
        question = use_case.execute(question_id)

        if not question:
            raise Http404("Question does not exist")
    except Exception:
        raise Http404

    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    use_case = build_show_vote_results_use_case()
    try:
        results = use_case.execute(question_id)
    except Exception as e:
        print("e", e)
        raise Http404
    else:
        return render(request, "polls/results.html", results)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(dir(question.choice_set))

    # print(question.choice_set.values())
    # print(question.choice_set.values_list())

    try:
        # print("question.choice_set", question.choice_set)
        # print("request.POST['choice']", request.POST["choice"])
        # print(dir(question))

        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        print("selected_choice", selected_choice)
        print(type(selected_choice))

        selected_choice = question.choice_set.filter(pk=20)
        print("selected_choice []", selected_choice)

        print(not selected_choice)

    except (KeyError, Choice.DoesNotExist):
        # request.POST['choice'] は KeyError を送出
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        # selected_choice.votes += 1
        # selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# class CreateUserView(APIView):
#     def post(self, request):
#         # validate input
#         user_dto, errors = CreateUserSerializer().load(request.data)
#         if errors:
#             return Response(errors, status=status.HTTP_400_BAD_REQUEST)

#         # call usecase
#         use_case = build_create_user_use_case()
#         try:
#             user = use_case.execute(user_dto)

#         # handle exceptions
#         except (UsernameAlreadyExistsError) as e:
#             return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except permissionsInsuficientException as e:
#             return Response(str(e), status=status.HTTP_403_FORBIDDEN)

#         # return serialised data
#         else:
#             return Response(
#                 UserSerializer().dump(user).data,
#                 status=status.HTTP_201_CREATED
#             )
