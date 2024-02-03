import zlib
import urllib
import urllib.request

url = "https://www.blueapron.com/recipes/butter-soy-glazed-chicken-with-sesame-vegetables-brown-rice"

req = urllib.request.Request(url, headers={
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    'Sec-Ch-Ua' : '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile' : '?0',
    'Sec-Fetch-Dest' : 'document',
    'Sec-Ch-Ua-Platform' : '"Windows"',
    'Sec-Fetch-Site' : 'none',
    'Sec-Fetch-User' : '?1',
    'Sec-Gpc' : '1',
    'Pragma' : 'no-cache',
    'Cache-Control' : 'no-cache',
    'Accept-Language' : 'en-US,en;q=0.6',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests' : '1',
    'Cookie' : '_session_id=ae3a20712c7662e0d6661b3321c2587b; fastly_bucket=86; __zlcmid=1K6mSqed0C3WnR3; __stripe_mid=fe47ce32-ac43-49f5-ab0b-9ed09643a395eb983b; site_tests=family_five_and_plan_flexing_holdbacks&account_zendesk_chat_testing&recipe_quickview_coming_soon&reactivation_copy&meal_reschedule&expiring_credits_modal&miss_upcoming_order&invite_granting_logic&activationButtonExperiment&recipe-quick-tag&ratings-v2-zendesk&upcomingToggleLayoutExperiment&trending-badge-test&cancellation_04_2018&one-pan-meal-badge-test&ios_enhanced_delivery_schedule&recipe-main-dish-photo&tips-from-users-button&preference_collection_test&inviteContactIntegrationExperiment&googleAutofillSignupExperiment&8608270290&specialty-tomatoes-badge-test&customer-favorite-badge-test&eds-to-new-users&launchTabExperiment&cust-fave-campaign-badge-test&30-minute-meal-badge-test&android_reportIssue&streamlinedOnboardingExperiment&inviteGoogleContactIntegrationExperiment&guestLaunchTabExperiment&sheet-pan-supper-badge-test&hands-off-cooking-badge-test&invitePromptExperiment&pushNotificationsPermissionExperiment&reportIssueExperiment&whole-30-badge-test&memberPushNotificationPermissionCopyExperiment&trial-default-meal-quantity&android_enhanced_meal_picker&quick-and-easy-badge-test&rollout_registration_refresh&merchandising_v1&welcome_series_test&invite_refresh&a_la_carte_reactivation&android_invitePrompt&cutoff_reminders_test&easy-clean-up-badge-test&great-for-grilling-badge-test&limited-quantity-badge-test&android_inviteContacts&one-pot-meal-badge-test&thanksgiving-dish-badge-test&invite_grant_badging&android_merchandising&late-cutoff-test&3ds_test&invite_grant_push_notifications&registration-refresh&checkout_refresh&ios_enhanced_meal_picker&android_upcoming_3ds&user_login_landing_location_2&discoverMerchandisingExperiment&mediterranean-diet-badge-test&16900413230&react_desktop_registration&23162200598&25565180016&25695460370&26840470099&27302740126&27272520304&27292680477&27278380761&27280230765&27453730835&27581410028&27478820744; datadome=aftdKJtwlirYP7ioHX34E9Z9OKx3wVFI8j_0cXIIcf9lNcaDU42F9IBK8K3xSYNEa4jVAcoZxoBxVFqTZkfdWKLmAWj43zq0HsyUDP8vK2ikKlJeuy_EH8mSBdokQzbJ'
    }) 

src = bytearray()

try:
    response = urllib.request.urlopen(req)
    chunk = True
    while chunk:
        chunk = response.read()
        if len(chunk) > 0:
            src.extend(zlib.decompress(chunk, 16+zlib.MAX_WBITS))
    response.close()
    
    with open("response.html", "wb") as f:
        f.write(src)

except IOError:
    print("Error retrieving page")

print("success")

#con = urllib.request.urlopen( req )
#decompressed_data=
#print(con.read())
#print(decompressed_data)