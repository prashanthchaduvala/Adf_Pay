from rest_framework import serializers
from .models import *
from partners.models import *
from dashboard.models import *


class CountryCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryCode
        fields = '__all__'
        
class ManageNewsMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageNewsMedia
        fields = '__all__'
class ManageSEOContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageSEOContent
        fields = '__all__'

class PostVacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVacancies
        fields = '__all__'

class ResumeReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeReceipt
        fields = '__all__'

class PublishBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishBlogs
        fields = '__all__'

class ApproveCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproveComments
        fields = '__all__'

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class MobileAppAndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileAppAndroid
        fields = '__all__'

class MobileAppIOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileAppIOS
        fields = '__all__'

class TotalDownloadsAndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalDownloadsAndroid
        fields = '__all__'

class TotalDownloadsIOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalDownloadsIOS
        fields = '__all__'

class SingleDownloadAndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleDownloadAndroid
        fields = '__all__'

class SingleDownloadIOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleDownloadIOS
        fields = '__all__'

class OnlineUsersAndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineUsersAndroid
        fields = '__all__'

class OnlineUsersIOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineUsersIOS
        fields = '__all__'

class BackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backup
        fields = '__all__'

class SynchronisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synchronisation
        fields = '__all__'

class RestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restore
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ManageSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageSubscription
        fields = '__all__'

class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = '__all__'

class ApproveRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproveRate
        fields = '__all__'

class ReferallPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferallPartner
        fields = '__all__'

class PartnerPayoutStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPayoutStructure
        fields = '__all__'

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'

class ReferAndEarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferAndEarn
        fields = '__all__'

class PhoneConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneConversation
        fields = '__all__'

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class OnlineSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineSubscriber
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class RestoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restores
        fields = '__all__'


class OnlineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineUser
        fields = '__all__'


class DownloadAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadApp
        fields = '__all__'


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'
