from OffensesManager.models import DomainName
latest_question_list = DomainName.objects.all()
print(latest_question_list)
