from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http.response import JsonResponse
from django.template import loader
from django.urls import reverse

from polls_app.polls.factories import (
    build_show_vote_results_use_case,
    build_show_vote_detail_use_case,
    build_show_vote_index_use_case,

    build_vote_use_case,
)
from polls_app.polls.exceptions import (
    ChoiceDoesNotExist, QuestionDoesNotExist
)


def json_index(request):
    use_case = build_show_vote_index_use_case()

    context = use_case.execute()

    return JsonResponse(
        data={
            'context': dir(context)
        },
        status=200
    )


def json_detail(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_show_vote_detail_use_case()
    try:
        question = use_case.execute(question_id)
    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)

    return JsonResponse(
        data={
            "question": str(question)
        },
        status=200
    )


def json_results(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_show_vote_results_use_case()
    try:
        results = use_case.execute(question_id)
    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)
    else:
        return JsonResponse(
            data={
                "question": str(results)
            },
            status=200
        )


def json_vote(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_vote_use_case()
    try:
        choice_id = int(request.POST["choice"])
        use_case.execute(question_id, choice_id)
    except (KeyError, ChoiceDoesNotExist) as e:

        question = e.args[0]
        error_message = e.args[1]

        return JsonResponse(
            data={
                "question_id": str(question),
                "error_message": error_message
            },
            status=200
        )

    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)
    else:
        return HttpResponseRedirect(
            reverse("polls:results", args=(question_id,))
        )
        return JsonResponse(
            data={
                "question_id": str(question_id),
            },
            status=200
        )

