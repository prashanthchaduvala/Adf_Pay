from django.urls import path
from crugapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('dashboard/', views.becomemember, name='dashboard'),
    # path('savedata/', views.savedata, name='savedata'),
    path('login/',views.login, name='login'),
    path('loginhere/',views.sucess,name='sucess'),
    path('registration/', views.register, name='registration'),
    path('indexpage/', views.completed, name='completed'),


    #Add bank details
    path('addbank/', views.addbank, name='addbank'),
    path('index/', views.index,name="index"),
    path('addnew/', views.addnew,name='addnew'),
    path('edit/<int:id>/', views.edit,name='edit'),
    # path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.destroy,name='delete'),

    # Update Profile
    path('viewregistration/',views.view_registration,name="viewregistration"),
    path('edit_register/<int:id>/', views.edit_register,name='edit_register'),
    path('delete_register/<int:id>/', views.destroy_register,name='delete_register'),


    # Suggetions
    path('suggetions/', views.suggetions, name="suggetions"),
    path('addsuggetion/', views.addsuggetion, name="addsuggetion"),
    path('addsuggetions/', views.addsuggetions, name="addsuggetions"),
    # path('edit_register/<int:id>/', views.edit_register, name='edit_register'),
    # path('delete_register/<int:id>/', views.destroy_register, name='delete_register'),


    # Feedback
    path('addfeedback/', views.addfeedback, name='addfeedback'),
    path('feedback/',views.feedback,name='feedback'),
    path('addfeedbacks/', views.addfeedbacks, name="addfeedbacks"),
    path('edit_feedback/<int:id>/', views.edit_feedback, name='edit_feedback'),
    path('delete_feedback/<int:id>/', views.destroy_feedback, name='delete_feedback'),

    # OnlineUsersAndroid
    path('adduser/', views.addusers, name='adduser'),
    path('onlineuser/', views.onlineuser, name='onlineuser'),
    path('addonlineuser/', views.addonlineuser, name="addonlineuser"),
    path('edit_onlineuser/<int:id>/', views.edit_onlineuser, name='edit_onlineuser'),
    path('delete_onlineuser/<int:id>/', views.destroy_onlineuser, name='delete_onlineuser'),

    # Downloads
    path('adddownload/', views.adddownload, name='adddownload'),
    path('download/', views.download, name='download'),
    path('adddownloads/', views.adddownloads, name="adddownloads"),
    path('edit_download/<int:id>/', views.edit_download, name='edit_download'),
    path('delete_download/<int:id>/', views.destroy_download, name='delete_download'),

    # All Reviews
    path('reviews/', views.reviews, name='reviews'),
    path('addreview/', views.addreview, name='addreview'),
    path('addreviews/',views.addreviews,name='addreviews'),
    path('edit_review/<int:id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:id>/', views.destroy_review, name='delete_review'),

    # logout user
    path('logoutuser/',views.logout_view,name='logoutuser'),

    # Cug dashboard
    path('cugdashboard/',views.cugdashboard,name='cugdashboard'),

    path('backindex/',views.backindex,name='backindex'),

    # =======================================================
    path('errorshow/',views.viewserrorshow,name='errorshow'),
    path('errorfeedback/',views.errorfeedback,name='errorfeedback'),

    # pending downloads
    path('pendingdownloads/', views.pendingdownloads, name='pendingdownloads'),


    # action button
    path('change_action/<int:objectId>/', views.change_action, name='change_action'),
    path('change_user/<int:objectId>/', views.change_user, name='change_action'),
    path('change_bank/<int:objectId>/', views.change_bank, name='change_bank'),
    path('change_review/<int:objectId>/', views.change_review, name='change_review'),
    path('change_download/<int:objectId>/', views.change_download, name='change_download'),
    path('change_online/<int:objectId>/', views.change_online, name='change_online'),

    # loginfail
    # path('loginfail/',views.loginfail,name='loginfail'),# render after logout
    # path('forgotpass/',views.forgotpass,name='forgotpass'),
    # path('getemail/',views.getemail,name='getemail'),
    # path('sucesspass/<int:id>/',views.sucesspass,name='sucesspass'),
    # path('redopass/',views.redopass,name='redopass'),

    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

    # path('userimage/',views.userimage,name='userimage'),
    # path('page/',views.PostList,name='page'),
    path("password_reset/", views.password_reset_request, name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='forgotpass/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forgotpass/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/',  auth_views.PasswordResetCompleteView.as_view(template_name='forgotpass/password_reset_complete.html'),name='password_reset_complete'),





]
