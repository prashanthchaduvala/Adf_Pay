from api.models import *
from accounts.models import UserProfilesAndroid, UserProfilesIOS
from django.db.models import Count, Avg

def VacancyReport():
    post_vacancies_objects = PostVacancies.objects.all()
    total_jobs_posted = post_vacancies_objects.count()
    currently_active_posts = PostVacancies.objects.filter(action='Active').count()
    if post_vacancies_objects:
        last_posted_job = post_vacancies_objects.latest('designation').designation
        most_common_job = PostVacancies.objects.values_list('designation').annotate(model_count=Count('designation')).order_by('-model_count')[0][0]
        most_common_job_count = PostVacancies.objects.values_list('designation').annotate(model_count=Count('designation')).order_by('-model_count')[0][1]
    else:
        last_posted_job = '-'
        most_common_job = '-'
        most_common_job_count = 0
    return [total_jobs_posted, currently_active_posts, last_posted_job, most_common_job, most_common_job_count]

def ResumeReceiptReport():
    resume_receipts_objects = ResumeReceipt.objects.all()
    total_resume_count = resume_receipts_objects.count()
    if resume_receipts_objects:
        most_common_department = ResumeReceipt.objects.values_list('department').annotate(model_count=Count('department')).order_by('-model_count')[0][0]
        most_common_department_count = ResumeReceipt.objects.values_list('department').annotate(model_count=Count('department')).order_by('-model_count')[0][1]
        most_common_designation = ResumeReceipt.objects.values_list('designation').annotate(model_count=Count('designation')).order_by('-model_count')[0][0]
        most_common_designation_count = ResumeReceipt.objects.values_list('designation').annotate(model_count=Count('designation')).order_by('-model_count')[0][1]
        most_common_location = ResumeReceipt.objects.values_list('location').annotate(model_count=Count('location')).order_by('-model_count')[0][0]
        most_common_location_count = ResumeReceipt.objects.values_list('location').annotate(model_count=Count('location')).order_by('-model_count')[0][1]
    else:
        most_common_department = '-'
        most_common_department_count = 0
        most_common_designation = '-'
        most_common_designation_count = 0
        most_common_location = '-'
        most_common_location_count = 0
    return [total_resume_count, most_common_department, most_common_department_count, most_common_designation, most_common_designation_count, most_common_location, most_common_location_count]

def DownloadsReport():
    download_android_objects = SingleDownloadAndroid.objects.all()
    download_ios_objects = SingleDownloadIOS.objects.all()
    download_android_count = download_android_objects.count()
    download_ios_count = download_ios_objects.count()
    if download_android_objects:
        highest_download_android_country = SingleDownloadAndroid.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][0]
        highest_download_android_state = SingleDownloadAndroid.objects.values_list('state').annotate(model_count=Count('state')).order_by('-model_count')[0][0]
    else:
        highest_download_android_country = '-'
        highest_download_android_state = '-'
    if download_ios_objects:
        highest_download_ios_country = SingleDownloadIOS.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][0]
        highest_download_ios_state = SingleDownloadIOS.objects.values_list('state').annotate(model_count=Count('state')).order_by('-model_count')[0][0]
    else:
        highest_download_ios_country, highest_download_ios_state = '-', '-'
    return [download_android_count, highest_download_android_country, highest_download_android_state, download_ios_count, highest_download_ios_country, highest_download_ios_state]

def OnlineUsersReport():
    online_users_android = OnlineUsersAndroid.objects.all()
    online_users_ios = OnlineUsersIOS.objects.all()
    online_users_android_count = online_users_android.count()
    online_users_ios_count = online_users_ios.count()
    return [online_users_android_count, online_users_ios_count]

def UserProfilesReport():
    user_profiles_android = UserProfilesAndroid.objects.all()
    user_profiles_ios = UserProfilesIOS.objects.all()
    user_profiles_android_count = user_profiles_android.count()
    user_profiles_ios_count = user_profiles_ios.count()
    return [user_profiles_android_count, user_profiles_ios_count]

def BackupReport():
    backup_objects = Backup.objects.all()
    backup_objects_count = backup_objects.count()
    if backup_objects:
        backup_most_common_user = Backup.objects.values_list('name').annotate(model_count=Count('name')).order_by('-model_count')[0][0]
        backup_most_common_user_count = Backup.objects.values_list('name').annotate(model_count=Count('name')).order_by('-model_count')[0][1]
        backup_most_common_country = Backup.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][0]
        backup_most_common_country_count = Backup.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][1]
    else:
        backup_most_common_user = '-'
        backup_most_common_user_count = 0
        backup_most_common_country = '-'
        backup_most_common_country_count = 0
    return [backup_objects_count, backup_most_common_country, backup_most_common_country_count, backup_most_common_user, backup_most_common_user_count]

def RestoreReport():
    restore_objects = Restore.objects.all()
    restore_objects_count = restore_objects.count()
    if restore_objects:
        restore_most_common_user = Restore.objects.values_list('name').annotate(model_count=Count('name')).order_by('-model_count')[0][0]
        restore_most_common_user_count = Restore.objects.values_list('name').annotate(model_count=Count('name')).order_by('-model_count')[0][1]
        restore_most_common_country = Restore.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][0]
        restore_most_common_country_count = Restore.objects.values_list('country').annotate(model_count=Count('country')).order_by('-model_count')[0][1]
    else:
        restore_most_common_user = '-'
        restore_most_common_user_count = 0
        restore_most_common_country = '-'
        restore_most_common_country_count = 0
    return [restore_objects_count, restore_most_common_country, restore_most_common_country_count, restore_most_common_user, restore_most_common_user_count]

def FeedbackReport():
    feedback_objects = Feedback.objects.all()
    feedback_count = feedback_objects.count()
    unanswered_feedback_count = Feedback.objects.filter(company_response='').count()
    answered_feedback_count = feedback_count - unanswered_feedback_count
    return [feedback_count, answered_feedback_count, unanswered_feedback_count]

def ReviewsReport():
    reviews_objects = Reviews.objects.all()
    reviews_count = reviews_objects.count()
    unanswered_reviews_count = Reviews.objects.filter(company_response='').count()
    answered_reviews_count = reviews_count - unanswered_reviews_count
    if reviews_objects:
        average_review_rating = reviews_objects.aggregate(Avg('review_rating'))['review_rating__avg']
    else:
        average_review_rating = 0
    return [reviews_count, answered_reviews_count, unanswered_reviews_count, average_review_rating]

def SubscriptionReport():
    subscribers_objects = Subscribers.objects.all()
    subscribers_count = subscribers_objects.count()
    if subscribers_objects:
        most_common_profile_type = Subscribers.objects.values_list('profile_type').annotate(model_count=Count('profile_type')).order_by('-model_count')[0][0]
        most_common_profile_type_count = Subscribers.objects.values_list('profile_type').annotate(model_count=Count('profile_type')).order_by('-model_count')[0][1]
        most_common_subscription_type = Subscribers.objects.values_list('subscription_type').annotate(model_count=Count('subscription_type')).order_by('-model_count')[0][0]
        most_common_subscription_type_count = Subscribers.objects.values_list('subscription_type').annotate(model_count=Count('subscription_type')).order_by('-model_count')[0][1]
        most_common_collection_method = Subscribers.objects.values_list('collection_method').annotate(model_count=Count('collection_method')).order_by('-model_count')[0][0]
        most_common_collection_method_count = Subscribers.objects.values_list('collection_method').annotate(model_count=Count('collection_method')).order_by('-model_count')[0][1]
    else:
        most_common_profile_type = '-'
        most_common_profile_type_count = 0
        most_common_subscription_type = '-'
        most_common_subscription_type_count = 0
        most_common_collection_method = '-'
        most_common_collection_method_count = 0
    return [subscribers_count, most_common_collection_method, most_common_collection_method_count, most_common_profile_type, most_common_profile_type_count, most_common_subscription_type, most_common_subscription_type_count]
