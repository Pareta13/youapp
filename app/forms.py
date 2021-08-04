from django import forms

date_choices=[('EgQIARAB','lastHour'),('EgQIAhAB','today'),('EgQIAxAB','thisWeek'),('EgQIBBAB','thisMonth'),('EgQIBRAB','thisYear'),('','all')]
sort_option=[('CAASAhAB','relevance'),('CAISAhAB','uploadDate'),('CAMSAhAB','viewCount'),('CAESAhAB','rating')]
class youtube(forms.Form):
    keyword= forms.CharField(label='keyword', max_length=100)
    # date_filter=forms.ChoiceField(choices=date_choices)
    sort_option=forms.ChoiceField(choices=sort_option)
