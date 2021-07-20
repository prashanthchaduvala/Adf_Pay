from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class TermsAndConditionsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TermsAndConditions
        fields = ('content',)

class TermsOfUseForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TermsOfUse
        fields = ('content',)

class FairPracticeCodeForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FairPracticeCode
        fields = ('content',)

class PrivacyPolicyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = PrivacyPolicy
        fields = ('content',)

class DisclaimerForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Disclaimer
        fields = ('content',)

class GrievanceAddressMechanismForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = GrievanceAddressMechanism
        fields = ('content',)

class FaqForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Faq
        fields = ('content',)

class LifeAtAdfpayForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TermsAndConditions
        fields = ('content',)

class ManageNewsMediaForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = ManageNewsMedia
        fields = ('content',)

class PublishBlogsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = PublishBlogs
        fields = ('content',)
