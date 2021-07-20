from rest_framework import viewsets
from .models import *
from .serializers import *
from dashboard.models import *
from partners.models import *

class CountryCodeViewset(viewsets.ModelViewSet):
    queryset = CountryCode.objects.all()
    serializer_class = CountryCodeSerializer

class ManageNewsMediaViewset(viewsets.ModelViewSet):
    queryset = ManageNewsMedia.objects.all()
    serializer_class = ManageNewsMediaSerializer

class ManageSEOContentViewset(viewsets.ModelViewSet):
    queryset = ManageSEOContent.objects.all()
    serializer_class = ManageSEOContentSerializer

class PostVacanciesViewset(viewsets.ModelViewSet):
    queryset = PostVacancies.objects.all()
    serializer_class = PostVacanciesSerializer

class ResumeReceiptViewset(viewsets.ModelViewSet):
    queryset = ResumeReceipt.objects.all()
    serializer_class = ResumeReceiptSerializer

class PublishBlogsViewset(viewsets.ModelViewSet):
    queryset = PublishBlogs.objects.all()
    serializer_class = PublishBlogsSerializer

class ApproveCommentsViewset(viewsets.ModelViewSet):
    queryset = ApproveComments.objects.all()
    serializer_class = ApproveCommentsSerializer

class PartnersViewset(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class TestimonialsViewset(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer

class MobileAppAndroidViewset(viewsets.ModelViewSet):
    queryset = MobileAppAndroid.objects.all()
    serializer_class = MobileAppAndroidSerializer

class MobileAppIOSViewset(viewsets.ModelViewSet):
    queryset = MobileAppIOS.objects.all()
    serializer_class = MobileAppIOSSerializer

class TotalDownloadsAndroidViewset(viewsets.ModelViewSet):
    queryset = TotalDownloadsAndroid.objects.all()
    serializer_class = TotalDownloadsAndroidSerializer

class TotalDownloadsIOSViewset(viewsets.ModelViewSet):
    queryset = TotalDownloadsIOS.objects.all()
    serializer_class = TotalDownloadsIOSSerializer

class SingleDownloadAndroidViewset(viewsets.ModelViewSet):
    queryset = SingleDownloadAndroid.objects.all()
    serializer_class = SingleDownloadAndroidSerializer

class SingleDownloadIOSViewset(viewsets.ModelViewSet):
    queryset = SingleDownloadIOS.objects.all()
    serializer_class = SingleDownloadIOSSerializer

class OnlineUsersAndroidViewset(viewsets.ModelViewSet):
    queryset = OnlineUsersAndroid.objects.all()
    serializer_class = OnlineUsersAndroidSerializer

class OnlineUsersIOSViewset(viewsets.ModelViewSet):
    queryset = OnlineUsersIOS.objects.all()
    serializer_class = OnlineUsersIOSSerializer

class BackupViewset(viewsets.ModelViewSet):
    queryset = Backup.objects.all()
    serializer_class = BackupSerializer

class SynchronisationViewset(viewsets.ModelViewSet):
    queryset = Synchronisation.objects.all()
    serializer_class = SynchronisationSerializer

class RestoreViewset(viewsets.ModelViewSet):
    queryset = Restore.objects.all()
    serializer_class = RestoreSerializer

class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ReviewsViewset(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class ManageSubscriptionViewset(viewsets.ModelViewSet):
    queryset = ManageSubscription.objects.all()
    serializer_class = ManageSubscriptionSerializer

class SubscribersViewset(viewsets.ModelViewSet):
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersSerializer

class SupportViewset(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

class CommissionViewset(viewsets.ModelViewSet):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer

class ApproveRateViewset(viewsets.ModelViewSet):
    queryset = ApproveRate.objects.all()
    serializer_class = ApproveRateSerializer

class ReferallPartnerViewset(viewsets.ModelViewSet):
    queryset = ReferallPartner.objects.all()
    serializer_class = ReferallPartnerSerializer

class PartnerPayoutStructureViewset(viewsets.ModelViewSet):
    queryset = PartnerPayoutStructure.objects.all()
    serializer_class = PartnerPayoutStructureSerializer

class TransactionHistoryViewset(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

class ReferAndEarnViewset(viewsets.ModelViewSet):
    queryset = ReferAndEarn.objects.all()
    serializer_class = ReferAndEarnSerializer

class PhoneConversationViewset(viewsets.ModelViewSet):
    queryset = PhoneConversation.objects.all()
    serializer_class = PhoneConversationSerializer

class ChatBotViewset(viewsets.ModelViewSet):
    queryset = ChatBot.objects.all()
    serializer_class = ChatBotSerializer

class TicketViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class MailViewset(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer

class DiscountViewset(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class OnlineSubscriberViewset(viewsets.ModelViewSet):
    queryset = OnlineSubscriber.objects.all()
    serializer_class = OnlineSubscriberSerializer

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class RestoresViewset(viewsets.ModelViewSet):
    queryset = Restores.objects.all()
    serializer_class = RestoresSerializer

class OnlineUserViewset(viewsets.ModelViewSet):
    queryset = OnlineUser.objects.all()
    serializer_class = OnlineUserSerializer

class DownloadAppViewset(viewsets.ModelViewSet):
    queryset = DownloadApp.objects.all()
    serializer_class = DownloadAppSerializer

class DownloadViewset(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer