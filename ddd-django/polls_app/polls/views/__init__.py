from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)

    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_show_vote_results_use_case()
    try:
        results = use_case.execute(question_id)
    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)
    else:
        return render(request, "polls/results.html", results)


def vote(request, question_id):
    assert isinstance(question_id, int)

    use_case = build_vote_use_case()
    try:
        choice_id = int(request.POST["choice"])
        use_case.execute(question_id, choice_id)
    except (KeyError, ChoiceDoesNotExist) as e:

        question = e.args[0]
        error_message = e.args[1]

        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": error_message
            },
        )
    except QuestionDoesNotExist as e:
        error_message = e.args[0]
        raise Http404(error_message)
    else:
        return HttpResponseRedirect(
            reverse("polls:results", args=(question_id,))
        )
