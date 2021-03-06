# coding: utf-8

# flake8: noqa

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from sib_api_v3_sdk.api.account_api import AccountApi
from sib_api_v3_sdk.api.attributes_api import AttributesApi
from sib_api_v3_sdk.api.contacts_api import ContactsApi
from sib_api_v3_sdk.api.email_campaigns_api import EmailCampaignsApi
from sib_api_v3_sdk.api.folders_api import FoldersApi
from sib_api_v3_sdk.api.lists_api import ListsApi
from sib_api_v3_sdk.api.process_api import ProcessApi
from sib_api_v3_sdk.api.reseller_api import ResellerApi
from sib_api_v3_sdk.api.sms_campaigns_api import SMSCampaignsApi
from sib_api_v3_sdk.api.smtp_api import SMTPApi
from sib_api_v3_sdk.api.senders_api import SendersApi
from sib_api_v3_sdk.api.transactional_sms_api import TransactionalSMSApi
from sib_api_v3_sdk.api.webhooks_api import WebhooksApi

# import ApiClient
from sib_api_v3_sdk.api_client import ApiClient
from sib_api_v3_sdk.configuration import Configuration
# import models into sdk package
from sib_api_v3_sdk.models.add_contact_to_list import AddContactToList
from sib_api_v3_sdk.models.add_credits import AddCredits
from sib_api_v3_sdk.models.create_attribute import CreateAttribute
from sib_api_v3_sdk.models.create_attribute_enumeration import CreateAttributeEnumeration
from sib_api_v3_sdk.models.create_child import CreateChild
from sib_api_v3_sdk.models.create_contact import CreateContact
from sib_api_v3_sdk.models.create_email_campaign import CreateEmailCampaign
from sib_api_v3_sdk.models.create_email_campaign_recipients import CreateEmailCampaignRecipients
from sib_api_v3_sdk.models.create_email_campaign_sender import CreateEmailCampaignSender
from sib_api_v3_sdk.models.create_list import CreateList
from sib_api_v3_sdk.models.create_model import CreateModel
from sib_api_v3_sdk.models.create_reseller import CreateReseller
from sib_api_v3_sdk.models.create_sender import CreateSender
from sib_api_v3_sdk.models.create_sender_ips import CreateSenderIps
from sib_api_v3_sdk.models.create_sender_model import CreateSenderModel
from sib_api_v3_sdk.models.create_sms_campaign import CreateSmsCampaign
from sib_api_v3_sdk.models.create_sms_campaign_recipients import CreateSmsCampaignRecipients
from sib_api_v3_sdk.models.create_smtp_email import CreateSmtpEmail
from sib_api_v3_sdk.models.create_smtp_template import CreateSmtpTemplate
from sib_api_v3_sdk.models.create_smtp_template_sender import CreateSmtpTemplateSender
from sib_api_v3_sdk.models.create_update_contact_model import CreateUpdateContactModel
from sib_api_v3_sdk.models.create_update_folder import CreateUpdateFolder
from sib_api_v3_sdk.models.create_webhook import CreateWebhook
from sib_api_v3_sdk.models.created_process_id import CreatedProcessId
from sib_api_v3_sdk.models.delete_hardbounces import DeleteHardbounces
from sib_api_v3_sdk.models.email_export_recipients import EmailExportRecipients
from sib_api_v3_sdk.models.error_model import ErrorModel
from sib_api_v3_sdk.models.get_account_marketing_automation import GetAccountMarketingAutomation
from sib_api_v3_sdk.models.get_account_plan import GetAccountPlan
from sib_api_v3_sdk.models.get_account_relay import GetAccountRelay
from sib_api_v3_sdk.models.get_account_relay_data import GetAccountRelayData
from sib_api_v3_sdk.models.get_aggregated_report import GetAggregatedReport
from sib_api_v3_sdk.models.get_attributes import GetAttributes
from sib_api_v3_sdk.models.get_attributes_attributes import GetAttributesAttributes
from sib_api_v3_sdk.models.get_attributes_enumeration import GetAttributesEnumeration
from sib_api_v3_sdk.models.get_campaign_overview import GetCampaignOverview
from sib_api_v3_sdk.models.get_campaign_recipients import GetCampaignRecipients
from sib_api_v3_sdk.models.get_campaign_stats import GetCampaignStats
from sib_api_v3_sdk.models.get_child_info_api_keys import GetChildInfoApiKeys
from sib_api_v3_sdk.models.get_child_info_api_keys_v2 import GetChildInfoApiKeysV2
from sib_api_v3_sdk.models.get_child_info_api_keys_v3 import GetChildInfoApiKeysV3
from sib_api_v3_sdk.models.get_child_info_credits import GetChildInfoCredits
from sib_api_v3_sdk.models.get_child_info_statistics import GetChildInfoStatistics
from sib_api_v3_sdk.models.get_children_list import GetChildrenList
from sib_api_v3_sdk.models.get_client import GetClient
from sib_api_v3_sdk.models.get_contact_campaign_stats import GetContactCampaignStats
from sib_api_v3_sdk.models.get_contact_campaign_stats_clicked import GetContactCampaignStatsClicked
from sib_api_v3_sdk.models.get_contact_campaign_stats_opened import GetContactCampaignStatsOpened
from sib_api_v3_sdk.models.get_contact_campaign_stats_transac_attributes import GetContactCampaignStatsTransacAttributes
from sib_api_v3_sdk.models.get_contact_campaign_stats_unsubscriptions import GetContactCampaignStatsUnsubscriptions
from sib_api_v3_sdk.models.get_contact_details import GetContactDetails
from sib_api_v3_sdk.models.get_contacts import GetContacts
from sib_api_v3_sdk.models.get_email_campaigns import GetEmailCampaigns
from sib_api_v3_sdk.models.get_email_event_report import GetEmailEventReport
from sib_api_v3_sdk.models.get_email_event_report_events import GetEmailEventReportEvents
from sib_api_v3_sdk.models.get_extended_campaign_overview_sender import GetExtendedCampaignOverviewSender
from sib_api_v3_sdk.models.get_extended_campaign_stats import GetExtendedCampaignStats
from sib_api_v3_sdk.models.get_extended_client_address import GetExtendedClientAddress
from sib_api_v3_sdk.models.get_extended_contact_details_statistics import GetExtendedContactDetailsStatistics
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_clicked import GetExtendedContactDetailsStatisticsClicked
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_links import GetExtendedContactDetailsStatisticsLinks
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_messages_sent import GetExtendedContactDetailsStatisticsMessagesSent
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_opened import GetExtendedContactDetailsStatisticsOpened
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions import GetExtendedContactDetailsStatisticsUnsubscriptions
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions_admin_unsubscription import GetExtendedContactDetailsStatisticsUnsubscriptionsAdminUnsubscription
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions_user_unsubscription import GetExtendedContactDetailsStatisticsUnsubscriptionsUserUnsubscription
from sib_api_v3_sdk.models.get_extended_list_campaign_stats import GetExtendedListCampaignStats
from sib_api_v3_sdk.models.get_folder import GetFolder
from sib_api_v3_sdk.models.get_folder_lists import GetFolderLists
from sib_api_v3_sdk.models.get_folders import GetFolders
from sib_api_v3_sdk.models.get_ip import GetIp
from sib_api_v3_sdk.models.get_ip_from_sender import GetIpFromSender
from sib_api_v3_sdk.models.get_ips import GetIps
from sib_api_v3_sdk.models.get_ips_from_sender import GetIpsFromSender
from sib_api_v3_sdk.models.get_list import GetList
from sib_api_v3_sdk.models.get_lists import GetLists
from sib_api_v3_sdk.models.get_process import GetProcess
from sib_api_v3_sdk.models.get_processes import GetProcesses
from sib_api_v3_sdk.models.get_reports import GetReports
from sib_api_v3_sdk.models.get_reports_reports import GetReportsReports
from sib_api_v3_sdk.models.get_senders_list import GetSendersList
from sib_api_v3_sdk.models.get_senders_list_ips import GetSendersListIps
from sib_api_v3_sdk.models.get_senders_list_senders import GetSendersListSenders
from sib_api_v3_sdk.models.get_sms_campaign_overview import GetSmsCampaignOverview
from sib_api_v3_sdk.models.get_sms_campaign_stats import GetSmsCampaignStats
from sib_api_v3_sdk.models.get_sms_campaigns import GetSmsCampaigns
from sib_api_v3_sdk.models.get_sms_event_report import GetSmsEventReport
from sib_api_v3_sdk.models.get_sms_event_report_events import GetSmsEventReportEvents
from sib_api_v3_sdk.models.get_smtp_template_overview import GetSmtpTemplateOverview
from sib_api_v3_sdk.models.get_smtp_template_overview_sender import GetSmtpTemplateOverviewSender
from sib_api_v3_sdk.models.get_smtp_templates import GetSmtpTemplates
from sib_api_v3_sdk.models.get_stats_by_domain import GetStatsByDomain
from sib_api_v3_sdk.models.get_transac_aggregated_sms_report import GetTransacAggregatedSmsReport
from sib_api_v3_sdk.models.get_transac_sms_report import GetTransacSmsReport
from sib_api_v3_sdk.models.get_transac_sms_report_reports import GetTransacSmsReportReports
from sib_api_v3_sdk.models.get_webhook import GetWebhook
from sib_api_v3_sdk.models.get_webhooks import GetWebhooks
from sib_api_v3_sdk.models.manage_ip import ManageIp
from sib_api_v3_sdk.models.post_contact_info import PostContactInfo
from sib_api_v3_sdk.models.post_contact_info_contacts import PostContactInfoContacts
from sib_api_v3_sdk.models.post_send_failed import PostSendFailed
from sib_api_v3_sdk.models.post_send_sms_test_failed import PostSendSmsTestFailed
from sib_api_v3_sdk.models.remaining_credit_model import RemainingCreditModel
from sib_api_v3_sdk.models.remaining_credit_model_child import RemainingCreditModelChild
from sib_api_v3_sdk.models.remaining_credit_model_reseller import RemainingCreditModelReseller
from sib_api_v3_sdk.models.remove_contact_from_list import RemoveContactFromList
from sib_api_v3_sdk.models.remove_credits import RemoveCredits
from sib_api_v3_sdk.models.request_contact_export import RequestContactExport
from sib_api_v3_sdk.models.request_contact_import import RequestContactImport
from sib_api_v3_sdk.models.request_contact_import_new_list import RequestContactImportNewList
from sib_api_v3_sdk.models.request_sms_recipient_export import RequestSmsRecipientExport
from sib_api_v3_sdk.models.send_email import SendEmail
from sib_api_v3_sdk.models.send_email_attachment import SendEmailAttachment
from sib_api_v3_sdk.models.send_report import SendReport
from sib_api_v3_sdk.models.send_report_email import SendReportEmail
from sib_api_v3_sdk.models.send_sms import SendSms
from sib_api_v3_sdk.models.send_smtp_email import SendSmtpEmail
from sib_api_v3_sdk.models.send_smtp_email_attachment import SendSmtpEmailAttachment
from sib_api_v3_sdk.models.send_smtp_email_bcc import SendSmtpEmailBcc
from sib_api_v3_sdk.models.send_smtp_email_cc import SendSmtpEmailCc
from sib_api_v3_sdk.models.send_smtp_email_reply_to import SendSmtpEmailReplyTo
from sib_api_v3_sdk.models.send_smtp_email_sender import SendSmtpEmailSender
from sib_api_v3_sdk.models.send_smtp_email_to import SendSmtpEmailTo
from sib_api_v3_sdk.models.send_template_email import SendTemplateEmail
from sib_api_v3_sdk.models.send_test_email import SendTestEmail
from sib_api_v3_sdk.models.send_test_sms import SendTestSms
from sib_api_v3_sdk.models.send_transac_sms import SendTransacSms
from sib_api_v3_sdk.models.update_attribute import UpdateAttribute
from sib_api_v3_sdk.models.update_attribute_enumeration import UpdateAttributeEnumeration
from sib_api_v3_sdk.models.update_campaign_status import UpdateCampaignStatus
from sib_api_v3_sdk.models.update_child import UpdateChild
from sib_api_v3_sdk.models.update_contact import UpdateContact
from sib_api_v3_sdk.models.update_email_campaign import UpdateEmailCampaign
from sib_api_v3_sdk.models.update_email_campaign_recipients import UpdateEmailCampaignRecipients
from sib_api_v3_sdk.models.update_email_campaign_sender import UpdateEmailCampaignSender
from sib_api_v3_sdk.models.update_list import UpdateList
from sib_api_v3_sdk.models.update_sender import UpdateSender
from sib_api_v3_sdk.models.update_sms_campaign import UpdateSmsCampaign
from sib_api_v3_sdk.models.update_smtp_template import UpdateSmtpTemplate
from sib_api_v3_sdk.models.update_smtp_template_sender import UpdateSmtpTemplateSender
from sib_api_v3_sdk.models.update_webhook import UpdateWebhook
from sib_api_v3_sdk.models.get_child_info import GetChildInfo
from sib_api_v3_sdk.models.get_extended_campaign_overview import GetExtendedCampaignOverview
from sib_api_v3_sdk.models.get_extended_client import GetExtendedClient
from sib_api_v3_sdk.models.get_extended_contact_details import GetExtendedContactDetails
from sib_api_v3_sdk.models.get_extended_list import GetExtendedList
from sib_api_v3_sdk.models.get_sms_campaign import GetSmsCampaign
from sib_api_v3_sdk.models.get_account import GetAccount
from sib_api_v3_sdk.models.get_email_campaign import GetEmailCampaign
