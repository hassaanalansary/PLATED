import matplotlib.pyplot as plt
from exams.models import Exam
from subjects.models import Lesson
from curriculum.context_processors import CURRENT_SEMESTER

def avg(lst):
    """ returns the average of a list of values """
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)


def avg_score_progress(user, condition):
    """ returns the average score progress for specific purpos based on the condition  """
    solved_exams = Exam.objects.filter(student=user.student, score__isnull=False, **condition)
    scores = [exam.score_percentage for exam in solved_exams]
    return [avg(scores[:i]) for i in range(1, len(scores) + 1)]


def plot(name, data, id):
    """ plots the scores """

    name = name.replace('_', ' ').upper()

    # set the size of the img
    plt.figure(figsize=(12, 5))

    # add 0 as the first point of the data to start counting from 1
    y = [0, *data]

    plt.plot(y, '-o', color='gray', alpha=0.4, linewidth=3, markersize=7, markerfacecolor='black')

    # show point value next to the point
    for i in range(len(y)):
        plt.annotate("{:.1f}".format(y[i]), (i, y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.stairs([0, *data, 0], linewidth=3)

    plt.xlabel("Number of Exams")
    plt.ylabel("Average Score (%)")

    plt.xlim(0, len(data))
    plt.ylim(0, 100)

    plt.xticks(range(0, len(data) + 1, 1))
    plt.yticks(range(0, 101, 10))

    plt.grid()

    # color the grids
    plt.axhspan(0, 60, color='red', alpha=0.1)
    plt.axhspan(60, 80, color='yellow', alpha=0.1)
    plt.axhspan(80, 100, color='green', alpha=0.1)

    plt.title(name, fontsize=15, fontweight='bold', color='black', loc='center', pad=20)

    plt_url = f"/media/plots/{id}_{name}.jpg"

    plt.savefig(plt_url[1:], bbox_inches='tight')

    plt.close()

    return plt_url


def score_progress(user, focus: Literal["subject", "chapter"], filter):
    """ returns a list of the focus instances with a list of its scores """
    lessons = Lesson.objects.filter(grade=user.student.grade, semester=CURRENT_SEMESTER)
    # first solution
    if focus == "subject":
        xxxxx
    elif focus == "chapter":
        twqe
    elif focus == "subject":
        dsadasd
    elif focus == "subject":
        agaggd
    else:
        raise NotImplemented("Illegal focus")
        
    query = {
        'lesson': lambda: lessons.filter(**filter),
        'chapter': lambda: list(set([lesson.chapter for lesson in lessons.filter(**filter)])),
        'unit': lambda: list(set([lesson.chapter.unit for lesson in lessons.filter(**filter)])),
        'subject': lambda: list(set([lesson.chapter.unit.subject for lesson in lessons])),
    }
    from django.db import Prefetch
    focus_instances = query[focus]().prefetch_related(Prefetch('exams', queryset= Exam.objects.filter(student=user.student, score__isnull=False), to_attr= 'new_exams')))
    focus_scores = []
    for  instance in focus_instances:
        solved_exams = instance.new_exams
        scores = [exam.score_percentage for exam in solved_exams]
        focus_scores.append({
            'id': instance.id,
            'title': instance.title,
            'scores': scores
            })
    return focus_scores
