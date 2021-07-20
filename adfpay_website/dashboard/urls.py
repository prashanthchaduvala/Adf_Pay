from django.urls import path
from .import views

urlpatterns = [
    path('',views.admindashboard, name='admindashboard'),

    # permissions
    path('menu_permission_list/', views.menu_permission_list, name='menu_permission_list'),
    path('sub_menu_permission_list/', views.sub_menu_permission_list, name='sub_menu_permission_list'),
    path('create_perission_name/',views.create_perission_name, name='create_perission_name'),
    path('edit_perission_name/<int:id>', views.edit_perission_name, name='edit_perission_name'),
    path('change_action/<str:objectType>/<int:objectId>/', views.change_action, name='change_action'),

    path('android/',views.android, name='android'),
    path('add_android/',views.add_android, name='add_android'),
    path('edit_android/<str:id>/', views.edit_android, name='edit_android'),
    path('delete_android/<str:id>/', views.delete_android, name='delete_android'),
    path('android_change_action/<str:objectId>/<str:state>/', views.android_change_action, name='android_change_action'),

    path('ios/',views.ios, name='ios'),
    path('add_ios/',views.add_ios, name='add_ios'),
    path('edit_ios/<str:id>/', views.edit_ios, name='edit_ios'),
    path('delete_ios/<str:id>/', views.delete_ios, name='delete_ios'),
    path('ios_change_action/<str:objectId>/<str:state>/', views.ios_change_action, name='ios_change_action'),


    path('download/',views.downloads, name='downloads'),

    path('download_app/',views.download_app, name='download_app'),
    path('download_app_change_action/<int:objectId>/<str:state>/', views.download_app_change_action, name='download_app_change_action'),
    
    path('user_profile/',views.user_profile, name='user_profile'),
    path('user_profile_change_action/<int:objectId>/<str:state>/', views.user_profile_change_action, name='user_profile_change_action'),
    path('delete_user_profile/<int:id>/', views.delete_user_profile, name='delete_user_profile'),

    # start
    path('online_user/',views.online_user, name='online_user'),
    
    path('restores/',views.restores, name='restores'),
    path('restores_change_action/<int:objectId>/<str:state>/', views.restores_change_action, name='restores_change_action'),
    path('delete_restores/<int:id>/', views.delete_restores, name='delete_restores'),


    path('subscription/',views.subscription, name='subscription'),
    path('add_subscription/',views.add_subscription, name='add_subscription'),
    path('edit_subscription/<str:id>/', views.edit_subscription, name='edit_subscription'),
    path('delete_subscription/<str:id>/', views.delete_subscription, name='delete_subscription'),
    path('subscription_change_action/<str:objectId>/<str:state>/', views.subscription_change_action, name='subscription_change_action'),

    path('online_subscriber/',views.online_subscriber, name='online_subscriber'),
    path('online_subscriber_change_action/<int:objectId>/<str:state>/', views.online_subscriber_change_action, name='online_subscriber_change_action'),
    path('delete_online_subscriber/<int:id>/', views.delete_online_subscriber, name='delete_online_subscriber'),

    path('subscription_payment/',views.subscription_payment, name='subscription_payment'),
    path('new_review/',views.new_review, name='new_review'),
    path('allocated_review/',views.allocated_review, name='allocated_review'),
    path('review_reply_received/',views.review_reply_received, name='review_reply_received'),
    path('review_reply_responded/',views.review_reply_responded, name='review_reply_responded'),
    path('review_pending/',views.review_pending, name='review_pending'),
    path('review_all/',views.review_all, name='review_all'),


    path('new_feedback/',views.new_feedback, name='new_feedback'),
    path('allocated_feedback/',views.allocated_feedback, name='allocated_feedback'),
    path('feedback_reply_received/',views.feedback_reply_received, name='feedback_reply_received'),
    path('feedback_reply_responded/',views.feedback_reply_responded, name='feedback_reply_responded'),
    path('feedback_pending/',views.feedback_pending, name='feedback_pending'),
    path('all_feedback/',views.all_feedback, name='all_feedback'),

    path('new_inovative_idea/',views.new_inovative_idea, name='new_inovative_idea'),
    path('inovative_idea_allocated/',views.inovative_idea_allocated, name='inovative_idea_allocated'),
    path('inovative_idea_reply_received/',views.inovative_idea_reply_received, name='inovative_idea_reply_received'),
    path('inovative_idea_reply_responded/',views.inovative_idea_reply_responded, name='inovative_idea_reply_responded'),
    path('inovative_idea_implemented/',views.inovative_idea_implemented, name='inovative_idea_implemented'),
    path('inovative_idea_pending/',views.inovative_idea_pending, name='inovative_idea_pending'),
    path('inovative_idea_all/',views.inovative_idea_all, name='inovative_idea_all'),


    path('coupon_listing/',views.coupon_listing, name='coupon_listing'),
    path('coupon_expired/',views.coupon_expired, name='coupon_expired'),
    path('coupon_available/', views.coupon_available, name='coupon_available'),
    path('coupon_utilisation/', views.coupon_utilization, name='coupon_utilization'),
    path('coupon_generate/', views.coupon_generate, name='coupon_generate'),
    # path('coupons_generate/', views.coupons_generate, name='coupons_generate'),

    #pra
    path('pendingreg/', views.pendingreg, name='pendingreg'),
    path('decline_reg/', views.declinereg, name='decline_reg'),
    path('view_approve/', views.view_approve, name='view_approve'),

    path('approve/', views.approve_user, name='approve'),
    path('decline_user/', views.decline_user, name='decline'),

    #priya
    path('all_mails/', views.all_mails, name='all_mails'),
    path('mail_generate/',views.mail_generate, name='mail_generate'),
    path('mail_expired/', views.mail_expired, name='mail_expired'),
    path('new_mail_received/', views.new_mail_received, name='new_mail_received'),
    path('mail_forwarded/', views.mail_forwarded, name='mail_forwaded'),
    path('mail_resolved/', views.mail_resolved, name='mail_resolved'),
    path('mail_esclated/', views.mail_esclated, name='mail_esclated'),
    path('mail_pending/', views.mail_pending, name='mail_pending'),

    path('ticket_generate/', views.ticket_generate, name='ticket_generate'),
    path('new_tickets/', views.new_tickets, name='new_tickets'),
    path('ticket_forwarded/', views.ticket_forwarded, name='ticket_forwaded'),
    path('ticket_resolved/', views.ticket_resolved, name='ticket_resolved'),
    path('ticket_esclated/', views.ticket_esclated, name='ticket_esclated'),
    path('ticket_pending/', views.ticket_pending, name='ticket_pending'),
    path('ticket_expired/', views.ticket_expired, name='ticket_expired'),
    path('all_tickets/', views.all_tickets, name='all_tickets'),

    path('chatbot_generate/', views.chatbot_generate, name='chatbot_generate'),
    path('all_request/', views.all_request, name='all_request'),
    path('request_pending/', views.request_pending, name='request_pending'),
    path('request_esclated/', views.request_esclated, name='request_esclated'),
    path('request_resolved/', views.request_resolved, name='request_resolved'),
    path('request_forwarded/', views.request_forwarded, name='request_forwarded'),
    path('request_expired/', views.request_expired, name='request_expired'),
    path('calls_generate/', views.calls_generate, name='calls_generate'),
    path('new_request_received/', views.new_request_received, name='new_request_received'),

    path('new_call_received/', views.new_call_received, name='new_call_received'),
    path('new_call_forwarded/', views.new_call_forwarded, name='new_call_forwarded'),
    path('call_resolved/', views.call_resolved, name='call_resolved'),
    path('call_esclated/', views.call_esclated, name='call_esclated'),
    path('call_pending/', views.call_pending, name='call_pending'),
    path('call_all/', views.call_all, name='call_all'),

    # refer n earn
    path('incentive_structure/',views.incentive_structure, name='incentive_structure'),
    path('incentive_utilised/', views.incentive_utilised, name='incentive_utilised'),
    path('incentive_paid/', views.incentive_paid, name='incentive_paid'),
    path('incentive_outstanding/', views.incentive_outstanding, name='incentive_outstanding'),

    # community member
    path('banking_application_received/', views.become_application_received, name='banking_application_received'),
    path('banking_application_approved/', views.banking_application_approved, name='banking_application_approved'),
    path('banking_active_members/', views.banking_active_members, name='banking_active_members'),
    path('banking_members_performance/', views.banking_members_performance, name='banking_members_performance'),
    # path('banking_members_payout_structure/', views.banking_members_payout_structure, name='banking_members_payout_structure'),
    path('banking_invoice_generated/', views.banking_invoice_generated, name='banking_invoice_generated'),
    path('banking_invoice_approval/', views.banking_invoice_approval, name='banking_invoice_approval'),
    path('banking_invoice_payment_status/', views.banking_invoice_payment_status, name='banking_invoice_payment_status'),

    # services
    path('service_listing/', views.service_listing, name='service_listing'),
    path('service_utilisation/', views.service_utilisation, name='service_utilisation'),
    path('service_charge_reciept/', views.service_charge_reciept, name='service_charge_reciept'),
    path('service_charge_outstand/', views.service_charge_outstanding, name='service_charge_outstand'),
    path('service_charge/', views.service_charge_structure, name='service_charge'),

#Transaction History
    path('transaction_initiated/', views.transaction_initiated, name="transaction_initiated"),
    path('transaction_completed/', views.transaction_completed, name="transaction_completed"),
    path('transaction_failed/', views.transaction_failed, name="transaction_failed"),
    path('transaction_pending/', views.transaction_pending, name="transaction_pending"),

# referal partner
    path('pendingreg/', views.pendingreg, name='pendingreg'),
    path('decline_reg/', views.declinereg, name='decline_reg'),
    path('view_approve/', views.view_approve, name='view_approve'),

    path('approve/', views.approve_user, name='approve'),
    path('decline_user/', views.decline_user, name='decline'),

    path('partner_structure/',views.partner_structure,name='partner_structure'),
    path('partner_save/',views.partner_save,name='partner_save'),
    path('active_patner/',views.active_user,name='active_patner'),

    path('member_perfomance/',views.member_perfomance,name='member_perfomance'),

    path('invoice_generate/',views.invoice_generate,name='invoice_generate'),


    path('invoice_approval/',views.invoice_approval,name='invoice_approval'),

    path('invoice_payment/',views.invoice_payment,name='invoice_payment'),

    # community
    path('approve_become/', views.approve_member, name='approve_become'),








]